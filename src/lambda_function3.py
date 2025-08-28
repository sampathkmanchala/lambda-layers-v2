from faker import Faker

def handler(event,context):
 fake = Faker()
 fake_address = fake.street_address()
 return fake_address
