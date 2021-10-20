import pytest
from django.urls import reverse

from students.models import Course

# проверка получения 1го курса
from tests.conftest import course_factory


@pytest.mark.django_db
def test_get_first_curses(client, course_factory):
    course_factory(_quantity=12)
    course_first =Course.objects.first()
    url = reverse('courses-detail', args=(course_first.id, ))
    response =client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == course_first.id
    assert response.data['name'] == course_first.name


# проверка получения списка курсов
@pytest.mark.django_db
def test_get_list_curses(client, course_factory):
    course_factory(_quantity=12)
    url = reverse('courses-list')
    response =client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 12

# проверка фильтрации списка курсов по id
@pytest.mark.django_db
def test_get_course_filter_id(client, course_factory):
    course_factory(_quantity=5)
    course_list = Course.objects.all()
    url = reverse("courses-list")
    response = client.get(url)
    assert response.status_code == 200
    assert response.data[3].get('id') == course_list[3].id


# проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_get_course_filter_name(client, course_factory):
    course_factory(_quantity=5)
    course_list = Course.objects.all()
    url = reverse("courses-list")
    response = client.get(url)
    assert response.status_code == 200
    assert response.data[3].get('name') == course_list[3].name

# тест успешного создания курса
@pytest.mark.django_db
def test_create_course(client):
    url = reverse("courses-list")
    data = {'name': 'IZO',
            'stundents': []}
    response = client.post(url, data)
    assert response.status_code == 201

# тест успешного обновления курса
@pytest.mark.django_db
def test_update_course(client, course_factory):
    course_factory(_quantity=5)
    course_up = Course.objects.first()
    url = reverse("courses-detail", args=(course_up.id, ))
    data_update = {'name': 'maths'}
    response = client.patch(url, data_update)
    assert response.status_code == 200

# тест успешного удаления  курса
@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course_factory(_quantity=5)
    course_up = Course.objects.first()
    url = reverse("courses-detail", args=(course_up.id, ))
    data_update = {'name': 'maths'}
    response = client.delete(url, data_update)
    assert response.status_code == 204