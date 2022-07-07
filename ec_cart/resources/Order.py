from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.Order import OrderModel


class Order(ActiveResource):
    _api_path = "/orders/${id}"

    class Meta:
        model = OrderModel

    def update(self, id_=None, **kwargs):
        if id_:
            kwargs['id'] = str(id_)

        return self._put(**kwargs)

    def delete(self, id_=None, **kwargs):
        raise exceptions.MethodNotAllowedError
