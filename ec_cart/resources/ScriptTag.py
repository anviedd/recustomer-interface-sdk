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
        if not id_ and 'id' not in kwargs:
            raise exceptions.ScriptTagIdNotFoundError
        elif 'id' in kwargs and not kwargs['id']:
            raise exceptions.ScriptTagIdNotFoundError

        if id_:
            kwargs['id'] = str(id_)

        return super(ScriptTag, self).delete(id_=None, **kwargs)
