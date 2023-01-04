from adapter.object_adapter.customer import Customer
from adapter.object_adapter.customer_adapter import CustomerAdapter

MOCKCUSTOMERS = (
    CustomerAdapter(Customer('Pizza Love', '33 Pepperoni Lane')),
    CustomerAdapter(Customer('Happy and Green', '25 Kale St.')),
    CustomerAdapter(Customer('Sweet Tooth', '42 Chocolate Ave.'))
)