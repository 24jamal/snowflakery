from faker import Faker

fake = Faker('ta_IN')

for i in range(10):
    print("Name:", fake.name())
    print("First Name:", fake.first_name())
    print("Last Name:", fake.last_name())
    print("Address:", fake.address())
    print("City:", fake.city())
    print("State:", fake.state())
    print("Phone:", fake.phone_number())
    print("-" * 50)