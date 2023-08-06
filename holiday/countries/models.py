from django.db import models
from django.utils import timezone

class Destination(models.Model):
    country = models.CharField(max_length=64)
    username = models.CharField(max_length=64)

    city = models.ManyToManyField('City')
    fromDate = models.DateField()
    toDate = models.DateField()
    entry = models.CharField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
    
        return f"{self.id}: Visited {self.country} from {self.fromDate} to {self.toDate}"

class City(models.Model):
    name=models.CharField(max_length=64)

    def __str__(self):
        return self.name

def upload_to_photo(instance, filename):
    
    return f'photos/{instance.destination.username}/{filename}'

class Photo(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to=upload_to_photo)


class MapImage(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='map_image')
    image_data = models.TextField() 


