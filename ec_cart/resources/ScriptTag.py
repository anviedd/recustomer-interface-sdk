from ec_cart.base import ActiveResource
from ec_cart.models.ScriptTag import ScriptTagModel


class ScriptTag(ActiveResource):
    _api_path = "/script-tags/${id}"

    class Meta:
        model = ScriptTagModel

    def create(self, id_=None, **kwargs):
        if id_:
            kwargs['id'] = str(id_)

        return self._post(**kwargs)
