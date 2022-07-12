import copy
import inspect
import os
import sys
from urllib.parse import urlparse

from ec_cart.api_version import ApiVersion
from ec_cart import exceptions


class Service:
    class SessionVariables:
        system_code = None
        ec_url = None
        access_token = None
        api_versions = os.environ.get('INTERFACE_API_KEY')
        api_key = os.environ.get('INTERFACE_API_KEY')
        request_service_code = os.environ.get('INTERFACE_REQUEST_SERVICE_CODE')
        protocol = "https"
        endpoint_domain = os.environ.get('INTERFACE_ENDPOINT')
        service_endpoint = ''
        headers = {
            "User-Agent": "PostmanRuntime/7.29.0"
        }

    _session = SessionVariables
    Order = None
    Product = None
    Variant = None
    ProductVariant = None
    ScriptTag = None
    Image = None
    Webhook = None
    OrderTransaction = None
    OrderCancel = None
    OrderRefund = None
    Inventory = None
    Shop = None
    IneligibleData = None
    OrderEditBegin = None
    OrderEditLineQuantity = None
    OrderEditCommit = None
    Subscription = None

    def __init__(
            self,
            system_code=None,
            ec_url=None,
            access_token=None,
            api_versions=os.environ.get('INTERFACE_API_VERSION'),
            api_key=os.environ.get('INTERFACE_API_KEY'),
            request_service_code=os.environ.get('INTERFACE_REQUEST_SERVICE_CODE'),
    ):

        if not system_code:
            raise exceptions.SystemCodeNotFoundError

        if not ec_url:
            raise exceptions.EcUrlNotFoundError

        if not access_token:
            raise exceptions.AccessTokenNotFoundError

        if not api_versions:
            raise exceptions.VersionNotFoundError

        if not api_key:
            raise exceptions.ApiKeyNotFoundError

        if not request_service_code:
            raise exceptions.RequestServiceCodeNotFoundError

        self._session.system_code = system_code
        self._session.ec_url = ec_url
        self._session.access_token = access_token
        self._session.api_versions = ApiVersion(api_versions)
        self._session.api_key = api_key
        self._session.request_service_code = request_service_code

        self.__prepare_url()

        self.set_header()

        self._create_resource()

    @property
    def endpoint(self):
        return f"{self._session.protocol}://{self._session.endpoint_domain}"

    def __prepare_url(self):
        self._session.endpoint_domain = os.environ.get('INTERFACE_ENDPOINT')
        self._session.service_endpoint = os.environ.get('INTERFACE_ENDPOINT')

    def _create_resource(self):
        for name, obj in inspect.getmembers(sys.modules['ec_cart.resources']):
            if inspect.isclass(obj):
                new_object = obj(
                    headers=self.get_headers(),
                    service_endpoint=self.get_service_endpoint()
                )
                setattr(self, obj.__name__, new_object)

    def set_header(self):
        self._session.headers.update({
            'x-api-key': self._session.api_key,
            'ec-url': self._session.ec_url,
            'system-code': self._session.system_code,
            'service-code': self._session.request_service_code,
            'Authorization': f'Bearer {self._session.access_token}'
        })

    def get_headers(self):
        return self._session.headers

    def get_service_endpoint(self):
        return self._session.service_endpoint + self._session.api_versions.path_to_version
