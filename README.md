# Тестирование Django-приложения

## Описание

Есть бекенд простого приложения с курсами и списком студентов. Вся логика для бекенда уже есть в заготовке, но совершенно нет тестов.

## Что сделано:

Тесты для текущей логики приложения.

Заведены фикстуры:

- для api-client'а
- для фабрики курсов
- для фабрики студентов

В качестве библиотеки для фабрик используется `model_bakery` (https://github.com/model-bakers/model_bakery).

Добавлены следующие тест-кейсы:

- проверка получения 1го курса (retrieve-логика)
  - создаем курс через фабрику
  - строим урл и делаем запрос через тестовый клиент
  - проверяем, что вернулся именно тот курс, который запрашивали
- проверка получения списка курсов (list-логика)
  - аналогично – сначала вызываем фабрики, затем делаем запрос и проверяем результат
- проверка фильтрации списка курсов по `id`
  - создаем курсы через фабрику, передать id одного курса в фильтр, проверить результат запроса с фильтром
- проверка фильтрации списка курсов по `name`
- тест успешного создания курса
  - здесь фабрика не нужна, готовим JSON-данные и создаем курс
- тест успешного обновления курса
  - сначала через фабрику создаем, потом обновляем JSON-данными
- тест успешного удаления курса

Все тесты явно проверяют код возврата.

Запуск тестов делается через команду:

```
$ pytest
```

Перед началом работы убедитесь, что все зависимости установлены (dev-зависимости указаны в `requirements-dev.txt`) и тесты успешно запускаются. Вы должны увидеть:

```
$ pytest
======== test session starts =====

...
collected 1 item

tests/students/test_courses_api.py F                                                                                                                                          [100%]

====== FAILURES ====
_____ test_example ____

    def test_example():
>       assert False, "Just test example"
E       AssertionError: Just test example
E       assert False

tests/students/test_courses_api.py:2: AssertionError
=== short test summary info ===
FAILED tests/students/test_courses_api.py::test_example - AssertionError: Just test example
===== 1 failed in 0.21s =====
```

## Документация

pytest: https://docs.pytest.org/en/stable/

pytest-django: https://pytest-django.readthedocs.io/en/latest/

тестирование DRF: https://www.django-rest-framework.org/api-guide/testing/
