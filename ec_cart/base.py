import json
import threading
from typing import Tuple, Dict, Any

import requests


class ActiveResource(object):
    timeout = 60
    _api_path = ''
    service_endpoint = ''
    _thread_local = None

    class Meta:
        model = None

    @classmethod
    def find(cls, id_=None, **kwargs) -> Any:
        """Core method for finding resources.

        Args:
            id_: A specific resource to retrieve.
            kwargs: any keyword arguments for query.

        Returns:
            An Meta model object.
        """
        if id_:
            kwargs['id'] = str(id_)

        return cls.__get(cls, **kwargs)

    def __path_connect(self, **kwargs) -> Tuple[str, Dict[str, Any]]:
        if 'id' in kwargs:
            _id = kwargs.pop('id')
            self._api_path = self._api_path.replace('${id}', _id)
        else:
            self._api_path = self._api_path.replace('${id}', '')
        return self.service_endpoint + str(self._api_path), kwargs

    @staticmethod
    def __get(cls, **kwargs) -> Any:
        try:
            path_connect, kwargs = cls.__path_connect(cls, **kwargs)
            response = requests.get(
                url=path_connect,
                headers=cls._thread_local._headers,
                timeout=cls.timeout,
                params=kwargs
            )
            response_content = json.loads(response.content)
            if response.ok:
                data = cls.__build_response(cls, response_content.get('data'))
                return data
            else:
                return response_content.get('message')
        except Exception as e:
            raise e

    @staticmethod
    def __build_response(cls, data) -> Any:
        if cls.Meta.model is None:
            return data
        try:
            if isinstance(data, (dict,)):
                return cls.Meta.model.parse_obj(data)
            elif isinstance(data, (list, tuple)):
                return [cls.Meta.model.parse_obj(d) for d in data]
            else:
                return data
        except Exception:
            return data


class ReInterfaceResource(ActiveResource):
    api_key = None
    service_code = None
    system_code = None
    ec_url = None
    access_token = None
    _thread_local = threading.local()

    old_headers = {
        "User-Agent": "PostmanRuntime/7.29.0"
    }
    headers = {}

    _url = None

    @classmethod
    def activate_service(cls, service):
        """ active session service function
        :param service:
        """
        cls.api_key = service.api_key
        cls.service_code = service.service_code
        cls.service_endpoint = service.endpoint + service.version.path
        cls.system_code = service.system_code
        cls.ec_url = service.ec_url
        cls.access_token = service.access_token
        cls._thread_local._system_code = service.system_code
        cls._thread_local._ec_url = service.ec_url
        cls._thread_local._access_token = service.access_token
        cls.headers = cls.old_headers
        cls._thread_local._headers = cls.headers
        cls._thread_local._headers.update({
            'x-api-key': cls.api_key,
            'system-code': cls._thread_local._system_code,
            'service-code': cls.service_code,
        })

        if cls._thread_local._access_token:
            cls._thread_local._headers.update({
                'Authorization': f'Bearer {cls._thread_local._access_token}',
            })

    @classmethod
    def clear_service(cls):
        cls.system_code = None
        cls._ec_url = None
        cls.access_token = None
        cls.headers = cls.old_headers
        cls._thread_local._system_code = None
        cls._thread_local._ec_url = None
        cls._thread_local._headers = {}
        cls._thread_local._access_token = None
