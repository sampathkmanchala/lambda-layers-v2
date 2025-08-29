from faker import Faker

def handler(event,context):
 from boltons.iterutils import chunked
 print(list(chunked(range(10), 3)))
 print("I am in third function")
 fake = Faker()
 fake_address = fake.street_address()
 return fake_address
