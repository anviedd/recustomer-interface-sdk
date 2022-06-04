import json
from typing import Tuple, Dict, Any

import requests
import six


class ActiveResource(object):
    timeout = 60
    _api_path = ''
    service_endpoint = ''
    headers = {
        "User-Agent": "PostmanRuntime/7.29.0"
    }

    def __init__(self, **kwargs):
        for k, v in six.iteritems(kwargs):
            setattr(self, k, v)
        assert self.Meta.model is not None

    class Meta:
        model = None

    def find(self, id_=None, **kwargs) -> Any:
        """Core method for finding resources.

        Args:
            id_: A specific resource to retrieve.
            kwargs: any keyword arguments for query.

        Returns:
            An Meta model object.
        """
        if id_:
            kwargs['id'] = str(id_)

        return self.__get(**kwargs)

    def __path_connect(self, **kwargs) -> Tuple[str, Dict[str, Any]]:
        if 'id' in kwargs:
            _id = kwargs.pop('id')
            self._api_path = self._api_path.replace('${id}', str(_id))
        else:
            self._api_path = self._api_path.replace('${id}', '')
        return self.service_endpoint + str(self._api_path), kwargs

    def __get(self, **kwargs) -> Any:
        try:
            path_connect, kwargs = self.__path_connect(**kwargs)
            response = requests.get(
                url=path_connect,
                headers=self.headers,
                timeout=self.timeout,
                params=kwargs
            )
            response_content = json.loads(response.content)
            if response.ok:
                return self.__build_response(self, response_content)
            else:
                return response_content
        except Exception as e:
            raise e

    @staticmethod
    def __build_response(cls, content) -> Any:
        data = content.get('data')
        if cls.Meta.model is None:
            return data
        try:
            if isinstance(data, (dict,)):
                content['data'] = cls.Meta.model.parse_obj(data)
            elif isinstance(data, (list, tuple)):
                content['data'] = [cls.Meta.model.parse_obj(d) for d in data]
            return content
        except Exception:
            return content
