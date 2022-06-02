import os
from contextlib import contextmanager

from ec_cart import constants
from ec_cart.api_version import ApiVersion
import six
from urllib.parse import urlparse


class ValidationException(Exception):
    pass


class Service(object):
    system_code = None
    ec_url = None
    api_key = os.environ.get('INTERFACE_API_KEY')
    service_code = os.environ.get('INTERFACE_SERVICE_CODE')
    version = os.environ.get('INTERFACE_API_VERSION')
    protocol = "https"
    endpoint_domain = os.environ.get('INTERFACE_ENDPOINT')

    def __init__(self, system_code, ec_url=None, access_token=None, version='v1'):
        """ Init Session Service
        :param system_code: Third-party system identifiers. Ex: SHOPIFY
        :param ec_url: User site can be a shop, a carrier,...
        :param access_token: Token used for user authentication.
        :param version: Interface API version. Ex: v1. Default: v1
        """
        assert self.api_key != '' 'api_key is not empty'
        assert system_code in constants.ServiceCode().__list__()
        assert self.endpoint_domain != '' 'INTERFACE_ENDPOINT is not empty'
        self.__prepare_url()
        self.system_code = system_code
        self.ec_url = ec_url
        self.access_token = access_token
        self.version = ApiVersion.coerce_to_version(version)
        return

    @staticmethod
    @contextmanager
    def temp(system_code, ec_url, access_token):
        import ec_cart
        original_system_code = ec_cart.ReInterfaceResource.system_code
        original_ec_url = ec_cart.ReInterfaceResource.ec_url
        original_access_token = ec_cart.ReInterfaceResource.access_token
        original_service = None
        if original_system_code is not None:
            original_service = ec_cart.Service(original_system_code, original_ec_url, original_access_token)

        service = Service(system_code, ec_url, access_token)
        ec_cart.ReInterfaceResource.activate_service(service)
        yield
        if original_system_code is not None and original_service:
            ec_cart.ReInterfaceResource.activate_service(original_service)

    @property
    def endpoint(self):
        return f"{self.protocol}://{self.endpoint_domain}"

    def __prepare_url(self):
        url_o = urlparse(self.endpoint_domain)
        self.protocol = url_o.scheme
        self.endpoint_domain = url_o.netloc
