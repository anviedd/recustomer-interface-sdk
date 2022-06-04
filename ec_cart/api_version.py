import re

from ec_cart.exceptions import InvalidVersionError


class ApiVersion(object):
    FORMAT = re.compile(r"^v\d{1,2}$")
    API_PREFIX = "/api"
    path_to_version = ''

    def __init__(self, version_number):
        if not self.FORMAT.match(version_number):
            raise InvalidVersionError
        self.path_to_version = f"{self.API_PREFIX}/{version_number}/interface"
