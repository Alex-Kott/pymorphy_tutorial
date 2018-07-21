#Порядок установки и запуска
1. Установить virtualenv
2. Перейти в консоли в папку с проектом `cd path/to/project`
3. Создать виртуальное окружение командой `virtualenv --no-site-packages -p python venv`
    Активировать его: если в стандартной виндовой консоли, то `venv\Scripts\activate`, если в git shell, то `source venv/bin/activate`
4. В PyCharm (Settings -> Interpretator) выбрать созданное виртуальное окружение (нужно будет указать путь к самому
интерпретатору, он находится в `.\venv\bin\python`) (это не обязательно, просто чтобы PyCharm ошибки не подсвечивал)
5. Установить пакеты из requirements.txt: `pip install -r requirements.txt`
6. Запускаем скрипт: `python main.py -f text.txt`. text.txt -- текстовый файл, который скрипт будет обрабатывать.
Сохраняться данные будут в data.csv

Полезное
- Кодировку исходного файла можно указать с помощью аргумента `--source-encoding`, например, `--source-encoding windows-1251`
- Кодировку результирующего файла можно указать с помощью аргумента `--dest-encoding`, например, `--dest-encoding utf-8`
- По умолчанию используется utf-8.