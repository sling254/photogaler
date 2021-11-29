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

    def test_get_all_image(self):
        images = Image.get_all_Images()
        self.assertTrue(len(images)>0)

    def test_get_image_id(self):
        images= Image.get_image_id(self.image.id)
        self.assertTrue(len(images) == 1)

    def test_search_photos_by_category(self):
        images = Image.search_photos_by_category('City')
        self.assertTrue(len(images)>0)
    
    def test_update(self):
        category = Category.get_category_id(self.category.id)
        category.update_category('horse riding')
        category = Category.get_category_id(self.category.id)
        self.assertTrue(category.category_name == 'horse riding')

   

class CategoryTestClass(TestCase):
# Set up Method
    def setUp(self):
        self.category = Category(category_name="hike")
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.category.save_category()
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def test_update(self):
        category = Category.get_category_id(self.category.id)
        category.update_category('coding')
        category = Category.get_category_id(self.category.id)
        self.assertTrue(category.category_name == 'coding')
    
class LocationTestCLass(TestCase):
    #Set up Method
    def setUp(self):
        self.location = Location(location_name="Home")
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.location.save_location()
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def test_update(self):
        location = Location.get_location_id(self.location.id)
        location.update_location('Nyeri')
        location = Location.get_location_id(self.location.id)
        self.assertTrue(location.location_name == 'Nyeri')