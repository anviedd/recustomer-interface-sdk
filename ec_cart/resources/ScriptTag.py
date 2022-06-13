from ec_cart import exceptions
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

    def delete(self, id_=None, **kwargs):
        if not id_ or 'id' not in kwargs or not kwargs['id']:
            raise exceptions.ScriptTagIdNotFoundError
        return super(ScriptTag, self).delete(id_=None, **kwargs)
