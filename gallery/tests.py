from django.test import TestCase
from .models import Image, Location,category

# Create your tests here.
# Testing Save Method
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.image=Image( title= 'Nature', description ='Our work to conserve biodiversity focuses on Key Biodiversity Areas.', image ='http://image.com/image.jpg',category=category.objects.create(name="nature"),location=Location.objects.create(name='Kenya'))


    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))   

    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def tearDown(self):
        Image.objects.all().delete()
        category.objects.all().delete()

#Category test cases
class categoryTestCase(TestCase):

    def setUp(self):
        category.objects.create(name="Category_test")

    def test_category_name(self):
        Category = category.objects.get(name="Category_test")
        self.assertEqual(Category.name, "Category_test")

    def test_category_str(self):
        Category = category.objects.get(name="Category_test")
        self.assertEqual(str(Category), "Category_test")

    