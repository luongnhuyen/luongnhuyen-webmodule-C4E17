from Models.service import Service
import mlab

mlab.connect()

all_service= Service.objects(contacted='true')

all_service= Service.objects(contacted='false')

for index, service in enumerate(all_service):
    print(service['name'])
    if index == 9:
        break
