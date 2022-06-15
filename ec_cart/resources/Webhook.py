from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.Webhook import WebhookModel


class Webhook(ActiveResource):
    _api_path = "/webhooks/${id}"

    class Meta:
        model = WebhookModel

    def create(self, id_=None, **kwargs):
        if id_:
            kwargs['id'] = str(id_)

        return self._post(**kwargs)

    def delete(self, id_=None, **kwargs):
        if not id_ and 'id' not in kwargs:
            raise exceptions.WebhookIdNotFoundError
        elif 'id' in kwargs and not kwargs['id']:
            raise exceptions.WebhookIdNotFoundError

        if id_:
            kwargs['id'] = str(id_)

        return super(Webhook, self).delete(id_=None, **kwargs)
