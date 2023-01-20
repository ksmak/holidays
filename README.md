# holidays

Установка приложения на Windows

1. Установить python  в папку C:\Python
2. Установить компоненты IIS, CGI
3. Скопировать папку с приложениями на локальный диск в папку C:\sites\holiday
4. Открыть командную строку от имени администратора
5. Запустить pip install -r requirements.txt
6. Запустить команду:  wfastcgi-enable
7. Открыть диспетчер служб IIS перейти в Параметры FastCGI
8. Добавить приложение с данными параметрами:
   Полный путь: C:\Python\python.exe
   Аргументы: C:\Python\Lib\site-packages\wfastcgi.py
   Переменные среды (список):

   имя: WSGI_HANDLERWSGI_HANDLER	значение: django.core.wsgi.get_wsgi_application()django.core.wsgi.get_wsgi_application()

   имя: PYTHONPATHPYTHONPATH значение: C:\sites\holidays

   имя: DJANGO_SETTINGS_MODULE значение: settings.base
9. В диспечере служб IIS также добавить сайт указав имя и полный путь к папке приложения, порт указать 8000
10. Создать правило для порта 8000 в брандмауэере windows
