from adapter.object_adapter.vendor import Vendor
from adapter.object_adapter.vendor_adapter import VendorAdapter

MOCKVENDORS = (
    VendorAdapter(Vendor('Dough Factory', 1, 'Semolina Court')),
    VendorAdapter(Vendor('Farm Produce', 14, 'Country Rd.')),
    VendorAdapter(Vendor('Cocoa World', 53, 'Tropical Blvd.'))
)