from django.test import TestCase
from django.shortcuts import reverse
from .views import home_page
# from django.core.urlresolvers import reverse, reverse_lazy, resolve 
from django.urls import resolve


class ViewTestcase(TestCase):

    def test_home_page(self):
        res = resolve(reverse('home'))
        response = self.client.get(reverse('home')) 
        self.assertEqual(response.status_code,200)
        # self.assertEqual(response.content,b'this is my home')
        self.assertEqual(res.func,home_page)  

   


