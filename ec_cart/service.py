import os
from ec_cart import constants
from ec_cart.api_version import ApiVersion
import ec_cart
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

        ec_cart.ReInterfaceResource.activate_service(self)

    @property
    def endpoint(self):
        return f"{self.protocol}://{self.endpoint_domain}"

    def __prepare_url(self):
        url_o = urlparse(self.endpoint_domain)
        self.protocol = url_o.scheme
        self.endpoint_domain = url_o.netloc
