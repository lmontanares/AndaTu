from rest_framework.test import APIClient


def test():
    factory = APIClient()
    request = factory.post('/notes/', {'title': 'new idea'})
