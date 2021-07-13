from django.test import TestCase

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack
# Create your tests here.

class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="liyan", email="liyan@gmail.com", password="123456"
        )

        self.snack = Snack.objects.create(
            title="salad", description="so tasty", purchaser=self.user,
        )

    def test_string(self):
        self.assertEqual(str(self.snack), "salad")

    def test_snack_content(self):
        self.assertEqual(self.snack.title, "salad")
        self.assertEqual(self.snack.description, 'so tasty')
        self.assertEqual(f"{self.snack.purchaser}", "liyan")

    def test_list(self):
        url= reverse('snack_list')
        self.assertTemplateUsed(self.client.get(url), 'snack_list.html')
        expected=200
        self.assertEqual(expected,self.client.get(url).status_code)

    def test_details(self):
        response= self.client.get(
            reverse('snack_detail',args='1') ,
            {'name':'salad', 
             
            'description':'so tasty',
            'purchaser':self.user 
            },
        )
        expected=200
        self.assertEqual(response.status_code, expected)

    def test_create(self):
        expected=200
        response= self.client.get(
            reverse('create_snack') ,
            {'name':'salad', 
             
            'description':'so tasty',
            'purchaser':self.user 
            },
        )
        self.assertEqual(response.status_code, expected)


    def test_update(self):
        expected=200
        response= self.client.get(
            reverse('update',args='1') ,
            {'name':'salad', 
             
            'description':'so tasty',
            'purchaser':self.user 
            },
        )
        self.assertEqual(response.status_code, expected)

    def test_delete_page(self):
        expected=200
        response= self.client.get(
            reverse('delete',args='1') ,
            {'name':'salad', 
             
            'description':'so tasty',
            'purchaser':self.user 
            },
        )
        self.assertEqual(response.status_code, expected)



