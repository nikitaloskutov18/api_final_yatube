# api_final
Описание:
Проект api_yatube - это API социальной сети yatube.
Проект Api Ytube - это соцеальная сеть С помощью api_yatube можно запрашивать данные о постах, группах, комментариях, а также создавать новые.

Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/VadimVolkovsky/api_final_yatube.git
cd api_final_yatube
Cоздать и активировать виртуальное окружение:

python3 -m venv venv(MacOS)
python -m venv venv(Windows)
source venv/bin/activate
Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip(MacOS)
python -m pip install --upgrade pip(Windows)
pip install -r requirements.txt
Выполнить миграции:

python3 manage.py migrate(MacOS)
python manage.py migrate(Windows)
Запустить проект:

python3 manage.py runserver(MacOS)
python manage.py runserver(Windows)
