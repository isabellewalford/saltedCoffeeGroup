from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from sustainability.models import PlantOfTheDay

ADD_PLANT_OF_THE_DAY = 'add_plant_of_the_day'

plant_of_the_day_permission = Permission.objects.filter(codename=ADD_PLANT_OF_THE_DAY).first()
content_type = ContentType.objects.get_for_model(PlantOfTheDay)

if not plant_of_the_day_permission:
    plant_of_the_day_permission = Permission.objects.create(
        codename=ADD_PLANT_OF_THE_DAY,
        name='Can add plant of the day',
        content_type=content_type
    )
