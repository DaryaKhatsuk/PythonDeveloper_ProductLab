Тестовое задание на позицию Python Developer

Инструкция по установке и запуску проекта:
1. Скопировать адрес репозитория: https://github.com/DaryaKhatsuk/PythonDeveloper_ProductLab.git
2. Запустить Terminal c консолью Command Prompt(cmd)
3. Клонировать проект с помощью: 
git clone https://github.com/DaryaKhatsuk/PythonDeveloper_ProductLab.git
4. Использовать в команду pip install -r requirements.txt для загрузки импортов из файла requirements.txt
5. Часть №1 задания реализована в файле 
[user_links.py](https://github.com/DaryaKhatsuk/PythonDeveloper_ProductLab/blob/master/user_links.py). 
Для его запуска откройте данный файл и нажмите сочетание клавиш Shift + F10.
6. Для запуска части №2 задания нужно:
   1. Перейти в папку с проектом: cd ParsingWildberries
   2. В файле settings.py, убедитесь что у вас подключены актуальные DATABASES. 
   В проекте подключен PostgreSQL.
   3. В терминале проведите и зарегистрируйте миграции при помощи: 
   
   python manage.py makemigrations 
   
   python manage.py migrate
   4. Создайте суперпользователя командой: python manage.py createsuperuser
   5. Запустите сервер командой: python manage.py runserver
   6. 

Часть №2
1. Изначально необходимо отследить трафик с www.wildberries.ru и найти HTTP
запрос, который в JSON формате присылает данные о бренде и название
артикула. Пример страницы товара:
https://www.wildberries.ru/catalog/73512949/detail.aspx
2. Далее необходимо реализовать API принимающее файл формата xlsx с
артикулами (артикулы должны вводиться построчно в первой колонке) или
один артикул (не в файле, а исключительно одно значение). В API должно быть
два инпута: файл или одно значение, передаваться должно что-то одно.
3. API должно асинхронно взаимодействовать с найденным HTTP запросом в
первом пункте и получать данные о карточке товара. Из полученных данных
необходимо сделать PyDantic объект.
4. Успешным результатом работы API является возврат данных о бренде и
названии артикула в JSON формате. Пример: информация об одном артикуле -
{"article": 123, "brand": "brand", "title": "Title"}; артикулы из файла - [{"article": 1,
"brand": "Brand1", "title": "Title1"}, {"article": 2, "brand": "Brand2", "title": "Title2"}]

