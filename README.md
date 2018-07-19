Порядок установки и запуска
1. Установить virtualenv
2. Перейти в консоли в папку с проектом
3. Создать виртуальное окружение командой `virtualenv --no-site-packages -p python venv`
4. В PyCharm (Settings -> Interpretator) выбрать созданное виртуальное окружение (нужно будет указать путь к самому
интерпретатору, он находится в `.\venv\bin\python`)
5.Активировать его: `venv\Scripts\activate`
6. Установить пакеты из requirements.txt: `pip install -r requirements.txt`
7. Запускаем скрипт: `python main.py -f text.txt`. text.txt -- текстовый файл, который скрипт будет обрабатывать.
Сохраняться данные будут в data.csv
