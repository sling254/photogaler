from django.test import TestCase
from gallery.views import *
from .models import  Image,Location,Category

# Create your tests here.


# Create your tests here.

class PhotoTestClass(TestCase):
    # Set up Method
    def setUp(self):

        self.category = Category(category_name="City")
        self.category.save_category()

        self.location = Location(location_name="Nairobi")
        self.location.save_location()

        self.image = Image(name='City Image', description='Nice city city',location=self.location, category=self.category)
        self.image.save()

    def test_instance(self):
            self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        self.image.delete_image()
        self.category.delete_category()
        self.location.delete_location()

    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)
