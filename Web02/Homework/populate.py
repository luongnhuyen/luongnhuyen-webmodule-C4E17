from Models.service import Service
from random import randint, choice
from faker import Faker
import mlab

mlab.connect()

fake = Faker()

# print(fake.address())
for i in range(50):
    print("Saving service", i+ 1, "...")
    service = Service(name=fake.name(),
                        gender=randint(0,1),
                        email=fake.email(),
                        phone=fake.phone_number(),
                        job=fake.job(),
                        company=fake.company(),
                        address=fake.address(),
                        contacted=randint(0,1))

    service.save()
