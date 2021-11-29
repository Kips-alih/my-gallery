from django.test import TestCase
from .models import Image,category

# Create your tests here.
# Testing Save Method
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.image=Image( title= 'Nature', description ='Our work to conserve biodiversity focuses on Key Biodiversity Areas.', image ='a6rncpjr5ptr0zuealce',category='nature',location='Kenya')

    # Creating a new category and saving it
        self.new_category = category(name = 'Nature')
        self.new_category.save()

        self.image.category.add(self.new_category)
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

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

    