from mongoengine import *

#design database
#create collection
class Service(Document):
    name = StringField()
    gender = IntField()
    email = StringField()
    phone = StringField()
    job = StringField()
    company = StringField()
    address = StringField()
    contacted = IntField()
