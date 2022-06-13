import json
from typing import Tuple, Dict, Any

import requests
import six

from ec_cart import exceptions


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

        return self._get(**kwargs)

    def delete(self, id_=None, **kwargs):
        if not id_:
            if 'id' not in kwargs:
                raise exceptions.ParamIdNotFoundError
            elif not kwargs['id']:
                raise exceptions.ParamIdNotFoundError
        else:
            kwargs['id'] = str(id_)

        return self._delete(**kwargs)

    def __path_connect(self, **kwargs) -> Tuple[str, Dict[str, Any]]:
        _api_path = self._api_path
        if 'id' in kwargs:
            _id = kwargs.pop('id')
        else:
            _id = ''
        if '${id}' in _api_path:
            _api_path = _api_path.replace('${id}', str(_id))
        else:
            _api_path = _api_path + str(_id)
        return self.service_endpoint + str(_api_path), kwargs

    def _get(self, **kwargs) -> Any:
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

    def _post(self, **kwargs):
        try:
            path_connect, kwargs = self.__path_connect(**kwargs)
            self.headers.update({"Content-Type": "application/json"})
            response = requests.post(
                url=path_connect,
                headers=self.headers,
                timeout=self.timeout,
                data=json.dumps(kwargs)
            )
            response_content = json.loads(response.content)
            if response.ok:
                return self.__build_response(self, response_content)
            else:
                return response_content
        except Exception as e:
            raise e

    def _delete(self, **kwargs):
        try:
            path_connect, kwargs = self.__path_connect(**kwargs)
            response = requests.delete(
                url=path_connect,
                headers=self.headers,
                timeout=self.timeout
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
        if content is None:
            return {
                'data': content
            }
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
