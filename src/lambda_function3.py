from faker import Faker

def handler(event,context):
 print("I am in third function")
 fake = Faker()
 fake_address = fake.street_address()
 return fake_address
