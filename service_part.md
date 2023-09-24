# Service

[![linting and testing](https://github.com/kapkaevandrey/test_task_for_dom_rf/actions/workflows/ci.yaml/badge.svg)](https://github.com/kapkaevandrey/test_task_for_dom_rf/actions/workflows/ci.yaml)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
___________________________________________________

### *Описание проекта*

Сервис обработки данных о кадастровых номерах

> ***Козьма́ Петро́вич Прутко́в***
>> Самый отдалённый пункт земного шара к чему-нибудь да близок, а самый близкий от чего-нибудь да отдалён.
________________________________________

## Навигация:

### [Работа с зависимостями](#dependencies)

### [Настройка переменных окружения](#envs)

### [Запуск приложения](#run)

```shell
sudo docker-compose --env-file .env -f infrastructure/docker-compose.local.yaml up --build
```

________________________________________

### Использование Poetry для управления зависимостями<a name="dependencies"></a>

Если poetry не установлен, то просто следуйте официальной __[инструкции](https://python-poetry.org/docs/)__

- для Linux, macOS, Windows (WSL)

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

- Windows (Powershell)

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

Что бы в дальнейшем poetry создавал виртуальное окружение прямо в директории с проектом выполните:

```shell
poetry config virtualenvs.in-project true
```

Посмотреть полный список настроек:

```shell
poetry config --list
```

Следующая команда создаст виртуальное окружение и установит все зависимости из файла __pyproject.toml__ (выполнять в
директории проекта)

```shell
poetry install
```

Если работа с poetry вам не нравится, вы можете воспользоваться стандартным файлом [requirements.txt](requirements.txt).

### Настройка переменных окружения<a name="branches"></a>

Для настройки переменных окружения перед запуском проекта создайте файл `.env` в директории проекта.  
Скопируйте содержимое файла `.env.example` в файл `.env`

________________________________________

### Запуск приложения<a name="run"></a>

Скопируйте репозиторий и перейдите в директорию с проектом:

```shell
git clone https://github.com/kapkaevandrey/test_task_for_dom_rf.git
cd test_task_for_dom_rf
```

Заполните файл `.env`

```shell
cp .env.example .env 
```

Для локальной разработки запустите:

```shell
sudo docker-compose --env-file .env -f infrastructure/docker-compose.local.yaml up --build
uvicron app.main:app --reload
```

**_Примечание:_** при локальном запуске, когда часть сервисов работает в контейнере, а основное приложение запущено
локально убедитесь, что в переменных окружения - `ENVIRONMENT` установлено значение `ENVIRONMENT=localhost`.
Это связано с тем, что Redis развёрнут в контейнере для нашего сервиса на хосте 127.0.0.1 или **localhost**.
Также при установке `ENVIRONMENT=localhost` некторые внешние сервисы будут заменены фейковыми классами.

Чтобы развернуть сервис в режиме тестирования или Продакшн:
Установите переменной `ENVIRONMENT` значение `TEST` или `PROD` соответственно расположите рядом в docker-compose файлом, файл `.env`.
```shell
sudo docker-compose --env-file .env -f infrastrucure/docker-compose.yaml up
```
