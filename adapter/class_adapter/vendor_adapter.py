from adapter.class_adapter.vendor import Vendor


class VendorAdapter(Vendor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def address(self):
        return f'{self._number} {self._street}'

