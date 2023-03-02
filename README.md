Тестовое задание на позицию Python Developer

Инструкция по установке и запуску проекта:
1. Скопировать адрес репозитория: https://github.com/DaryaKhatsuk/PythonDeveloper_ProductLab.git
2. Запустить Terminal c консолью Command Prompt(cmd)
3. Клонировать проект с помощью: git clone https://github.com/DaryaKhatsuk/PythonDeveloper_ProductLab.git
4. Использовать в команду pip install -r requirements.txt для загрузки импортов из файла requirements.txt
5. Часть №1 задания реализована в файле 
[user_links.py](https://github.com/DaryaKhatsuk/PythonDeveloper_ProductLab/blob/master/user_links.py). 
Для его запуска откройте данный файл и нажмите сочетание клавиш Shift + F10.
6. Для запуска части №2 задания нужно:
   1. Перейти в папку с проектом: cd ParsingWildberries
   2. В файле 
   [settings.py](https://github.com/DaryaKhatsuk/PythonDeveloper_ProductLab/blob/master/ParsingWildberries/ParsingWildberries/settings.py), 
   подключите актуальные DATABASES. В проекте подключен PostgreSQL
   3. В терминале проведите и зарегистрируйте миграции при помощи: 
   
   python manage.py makemigrations 
   
   python manage.py migrate
   4. Создайте суперпользователя командой: python manage.py createsuperuser. Действие в данном случае не обязательно.
   5. В файле 
   [details_parsing.py](https://github.com/DaryaKhatsuk/PythonDeveloper_ProductLab/blob/master/ParsingWildberries/details_app/details_parsing.py)
   для парсинга используется браузер Chrome, убедитесь что он установлен на вашем устройстве, а в строке service указан 
   актуальный путь к файлу chromedriver.exe для Chrome версии 110.0.5481.77. Если ваша версия отличается, скачайте нужную на [sites.google.com](https://sites.google.com/chromium.org/driver/)
   
   При желании использовать другой браузер используйте geckodriver.exe 
   находящийся в той-же директории, но предварительно запустите файл 7z2201-x64.exe вручную. При выборе этого способа 
   могут потребоваться и другие изменения которые я могла не учесть.
   
   Так же вы можете изменить время для загрузки страницы в строках 21, 22 и 24, если это позволяет скорость вашей сети интернет. 

   6. Запустите сервер командой в терминале: python manage.py runserver. Перейдя адресу http://127.0.0.1:8000/ следуйте указаниям 
   при вводе данных. Согласно условию задания "Из полученных данных необходимо сделать PyDantic объект.", его вывод 
   будет в вашем терминале после завершения работы программы, в противном случае вы увидите ошибку в браузере.
