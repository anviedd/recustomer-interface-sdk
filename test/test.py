import os
import time

os.environ.setdefault('INTERFACE_ENDPOINT', 'http://0.0.0.0:9009')
os.environ.setdefault('INTERFACE_API_KEY', 'bb6da2c308ef736a6902ad4552e4dfdd')
os.environ.setdefault('INTERFACE_REQUEST_SERVICE_CODE', 'tracking')
os.environ.setdefault('INTERFACE_API_VERSION', 'v1')

import ec_cart as EcCart

service = EcCart.Service(
    system_code='SHOPIFY', ec_url='release2903v1.myshopify.com',
    access_token='InNocGF0X2NmODE5NGFlODBlY2NkOWVlODg4Zjc3YmE0MjM4YWYyIg:1nfY1f:WTzjCM8lOt-V2HHGUyDaTQQM9HpNIUCgzAaVCuVaC28'
)

variant = service.ScriptTag.delete(id=12)
print(variant)
