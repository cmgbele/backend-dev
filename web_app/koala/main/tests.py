from django.test import TestCase
from django.shortcuts import reverse
from .views import home_page, contact_us
# from django.core.urlresolvers import reverse, reverse_lazy, resolve 
from django.urls import resolve


class ViewTestcase(TestCase):

    def test_home_page(self):
        res = resolve(reverse('home'))
        response = self.client.get(reverse('home')) 
        self.assertEqual(response.status_code,200)
        self.assertContains(response.content,b'WELCOME TO THECHRIS STORE') 
        self.assertTemplateUsed(response,'home.html')
        self.assertTemplateUsed(response,'base.html')
        self.assertEqual(res.func,home_page)  
        self.assertContains(response, 'ecommerce.css')


    def test_contact_page(self):
        res = resolve(reverse('contact'))
        response = self.client.get(reverse('contact')) 
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response,"LinkedIn") 
        self.assertContains(response.content,b'this is my home')
        self.assertTemplateUsed(response,'contact.html')
        self.assertTemplateUsed(response,'base.html') 
        self.assertEqual(res.func, contact_us)  
        self.assertContains(response, 'ecommerce.css') 



   


