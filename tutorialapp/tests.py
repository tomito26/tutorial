from django.test import TestCase
from .models import Tutorial
from rest_framework.test import APITestCase,APIClient
from rest_framework.views import status
from .serializers import TutorialSerializer
from django.urls import reverse

# Create your tests here.

class BaseViewTest(APITestCase):
    client = APIClient()
    
    @staticmethod
    def create_tutorial(title='',description='',image='',content='',author='',published='',created_on='',updated_on=''):
        if title != ""  and  description != ""  and image != "" and content != "" and author != "" and published != "" and created_on != "" and updated_on !="":
            Tutorial.objects.create(title=title,description=description,image=image,content=content, author=author,published=published,created_on=created_on,updated_on=updated_on)

    def setUp(self):
        """
        add test data
        """
        self.create_tutorial('how to install django','This a tutorial on how to install django','http://wuhrhs.jpeg','First install virtual env then activate it','cynthia',True,'Friday 12th march 2020','monday 17 march 2020')
        

class GetAllTutorialTest(BaseViewTest):
    def test_get_all_tutorials(self):
        '''
        This test ensures that all tutorials added in the setup method exist when we make a get request to the tutorial/ endpoint
        '''
        # hit the API endpoint
        
        response = self.client.get(
            reverse('tutorial-all',kwargs={'version':'v1'})
        )
        # fetch the data from db
        expected = Tutorial.objects.all()
        serialized = TutorialSerializer(expected,many=True)
        self.assertEqual(response.data,serialized.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        