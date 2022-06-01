class BaseResourceObject(object):
    class Meta:
        model = None

    def __init__(self):
        assert self.Meta.model is not None
