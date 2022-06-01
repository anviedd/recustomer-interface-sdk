from ec_cart.base import ReInterfaceResource
from ec_cart.models.Order import OrderModel
from ec_cart.resources.base import BaseResourceObject


class Order(ReInterfaceResource, BaseResourceObject):
    _api_path = "/orders/${id}"

    class Meta:
        model = OrderModel
