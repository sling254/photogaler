from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length=20)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, name):
        self.location_name = name
        self.save()

    @classmethod
    def get_location_id(cls, id):
        location_id = Location.objects.get(pk = id)
        return location_id

    def __str__(self):
        return self.location_name
    
class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, name):
        self.category_name = name
        self.save()

    @classmethod
    def get_category_id(cls, id):
        category_id = Category.objects.get(pk = id)
        return category_id

    def __str__(self):
        return self.category_name
    
class Image(models.Model):    
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField()
    posted_at = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id ,name,description, location, category):
        update = cls.objects.filter(id = id).update(name = name,description = description,location = location,category = category)
        return update

    @classmethod
    def get_all_Image(cls):
        Image = cls.objects.all()
        return Image

    @classmethod
    def get_image_id(cls,id):
        image_id = cls.objects.filter(id= id).all()
        return image_id

    @classmethod
    def filter_photo_by_location(cls,location):
        images = Image.objects.filter(location__location_name__icontains=location)
        return images

    @classmethod
    def search_photos_by_category(cls,category):
        images = Image.objects.filter(category__category_name__icontains=category)
        return images



    def __str__(self):
        return self.name
