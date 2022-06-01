SC_SHOPIFY = 'SHOPIFY'
SC_EC_CUBE = 'EC_CUBE'


class ServiceCode:
    SHOPIFY = SC_SHOPIFY
    EC_CUBE = SC_EC_CUBE

    def __list__(self):
        return [self.SHOPIFY, self.EC_CUBE]
