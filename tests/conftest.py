import pytest
from rest_framework.test import APIClient
from model_bakery import baker

@pytest.fixture()
def client():
    return APIClient()

# фикстура из model_bakery для Course
@pytest.fixture()
def course_factory():
    def factory(**kwargs):
        return baker.make('Course', **kwargs)
    return factory

# фикстура из model_bakery для Student
@pytest.fixture()
def student_factory():
    def factory(**kwargs):
        return baker.make('Student', **kwargs)
    return factory