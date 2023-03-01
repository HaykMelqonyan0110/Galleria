from django.test import TestCase
from django.urls import reverse
from .models import Category, Subcategory, Product


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Men')

    def test_category_name(self):
        self.assertEqual(str(self.category), 'Men')


class SubcategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Men')
        self.subcategory = Subcategory.objects.create(name='Shirts', category=self.category)

    def test_subcategory_name(self):
        self.assertEqual(str(self.subcategory), 'Shirts')


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Men')
        self.subcategory = Subcategory.objects.create(name='Shirts', category=self.category)
        self.product = Product.objects.create(name='T-Shirt', description='A simple T-Shirt', price='9.99',
                                              subcategory=self.subcategory)

    def test_product_name(self):
        self.assertEqual(str(self.product), 'T-Shirt')


class HomeViewTest(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


class CategoryDetailViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Men')

    def test_category_detail_view_status_code(self):
        url = reverse('category_detail', kwargs={'pk': self.category.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_detail_view_template(self):
        url = reverse('category_detail', kwargs={'pk': self.category.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'category_detail.html')


class SubcategoryDetailViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Men')
        self.subcategory = Subcategory.objects.create(name='Shirts', category=self.category)

    def test_subcategory_detail_view_status_code(self):
        url = reverse('subcategory_detail', kwargs={'pk': self.subcategory.pk})
        response = self.client.get


