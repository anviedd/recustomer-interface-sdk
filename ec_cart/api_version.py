import re


class InvalidVersionError(Exception):
    pass


class VersionNotFoundError(Exception):
    pass


class ApiVersion(object):
    versions = {}

    @classmethod
    def coerce_to_version(cls, version):
        try:
            return cls.versions[version]
        except KeyError:
            raise VersionNotFoundError

    @classmethod
    def define_version(cls, version):
        cls.versions[version.name] = version
        return version

    @classmethod
    def default_versions(cls):
        cls.define_version(Release("v1"))

    @classmethod
    def clear_defined_versions(cls):
        cls.versions = {}

    @property
    def name(self):
        return self._name

    @property
    def path(self):
        return self._path


class Release(ApiVersion):
    FORMAT = re.compile(r"^v\d{1,2}$")
    API_PREFIX = "/api"

    def __init__(self, version_number):
        if not self.FORMAT.match(version_number):
            raise InvalidVersionError
        self._path = f"{self.API_PREFIX}/{version_number}/interface"
        self._name = version_number

    @property
    def stable(self):
        return True


ApiVersion.default_versions()
