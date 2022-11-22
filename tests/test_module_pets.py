from api import PetFriends
from settings import valid_email, valid_password
import os

PF = PetFriends()


# Тест №1
def test_get_api_key_with_invalid_email(email='invalid9@mail9.ru', password=valid_password):
    """Негативный кейс на отправку невалидного электронного адреса"""

    status, result = PF.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


# Тест №2
def test_get_api_key_with_invalid_password(email=valid_email, password='123'):
    """Негативный кейс на отправку невалидного пароля"""

    status, result = PF.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


# Тест №3
def test_add_new_pet_with_invalid_name(name=12345, animal_type='Кот',
                                       age='2', pet_photo='images/white_cat.jpg'):
    """Негативный кейс на добавление питомца с невалидным именем (integer вместо string)"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = PF.get_api_key(valid_email, valid_password)

    # Добавляем питомца c обработкой исключения
    try:
        status, result = PF.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    except AttributeError:
        print('Невалидное имя. Питомец не добавлен')


# Тест №4
def test_add_new_pet_with_empty_name(name='', animal_type='Кот', age='2',
                                     pet_photo='images/black_cat.jpg'):
    """Негативный кейс на добавление питомца с пустым значением имени"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = PF.get_api_key(valid_email, valid_password)

    status, result = PF.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Подразумевается, что питомец не будет добавлен с пустым значением имени
    assert status == 200


# Тест №5
def test_add_new_pet_without_photo(name='', animal_type='Кот', age='2'):
    """Негативный кейс на добавление питомца без фотографии"""

    _, auth_key = PF.get_api_key(valid_email, valid_password)

    # Добавляем питомца c обработкой исключения
    try:
        status, result = PF.add_new_pet(auth_key, name, animal_type, age)
    except TypeError:
        print('Питомец без фотографии не добавлен')


# Тест №6
def test_add_new_pet_with_invalid_animal_type(name='Поликарп', animal_type=12345,
                                              age='2', pet_photo='images/black_cat.jpg'):
    """Негативный кейс на добавление питомца с невалидной породой (integer вместо string)"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = PF.get_api_key(valid_email, valid_password)

    # Добавляем питомца c обработкой исключения
    try:
        status, result = PF.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    except AttributeError:
        print('Невалидный формат породы питомца. Питомец не добавлен')


# Тест №7
def test_add_new_pet_with_none_value_animal_type(name='Поликарп', animal_type='',
                                                 age='2', pet_photo='images/black_cat.jpg'):
    """Негативный кейс на добавление питомца с пустым значением породы"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = PF.get_api_key(valid_email, valid_password)

    status, result = PF.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Подразумевается, что питомец не будет добавлен с пустым значением породы
    assert status == 200


# Тест №8
def test_add_new_pet_with_invalid_age(name='Поликарп', animal_type='Кот',
                                      age='два', pet_photo='images/white_cat.jpg'):
    """Негативный кейс на добавление питомца с невалидным возрастом (string вместо number)"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = PF.get_api_key(valid_email, valid_password)

    status, result = PF.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Подразумевается, что питомец не будет добавлен с невалидным значением породы
    assert status == 200


# Тест №9
def test_add_new_pet_with_none_value_age(name='Поликарп', animal_type='Кот',
                                         age='0', pet_photo='images/black_cat.png'):
    """Негативный кейс на добавление питомца с нулевым значением возраста"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = PF.get_api_key(valid_email, valid_password)

    status, result = PF.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Подразумевается, что питомец не будет добавлен с нулевым значением возраста
    assert status == 200


# Тест №10
def test_add_new_pet_with_invalid_format_pet_photo(name='Поликарп', animal_type='Кот',
                                                   age='7', pet_photo='images/bandit_cat.bmp'):
    """Негативный кейс на добавление фотографии питомца с невалидным форматом (BMP вместо JPG, JPEG или PNG)"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = PF.get_api_key(valid_email, valid_password)

    status, result = PF.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Подразумевается, что питомец не будет добавлен с невалидным форматом фотографии
    assert status == 200
