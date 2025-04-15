# 📝 TaskManager API

**TaskManager** — это сервис для управления задачами, позволяющий добавлять, просматривать, редактировать, удалять и фильтровать задачи. На данный момент проект находится на стадии разработки.

---

## 🚀 Технологии

- ⚙️ **Python**, **FastAPI**
- 🗄 **PostgreSQL** + **SQLAlchemy (async)**
- 🧪 **Alembic** (миграции)
- 📐 **Pydantic** (валидация данных)
- 🐳 **Docker** для контейнеризации
- 🔄 Автоматические миграции при запуске приложения

---

## 📚 Функциональность

- ✅ Создание, чтение, обновление и удаление задач (CRUD)
- 🔍 Фильтрация задач по различным параметрам
- 🧱 Слоистая архитектура: **Repository** → **Service** → **API**
- 🛠 Работа с асинхронной базой данных через SQLAlchemy и PostgreSQL

---

## ⚙️ Установка и запуск

### 1. Клонировать репозиторий:

```bash
git clone https://github.com/your-username/taskmanager-api.git

```
### 2. Запуск с помощью docker-file:
```bash
# Собрать и запустить контейнеры
docker-compose up --build

# Приложение доступно по адресу:
# http://localhost:80
```
### 3. Запсук локально без докера:
```bash
# 1. Клонируем репозиторий
git clone https://github.com/vladikhub/TasksAPI.git

# 2. Устанавливаем зависимости
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt

# 3. Применяем миграции
alembic upgrade head

# 4. Запуск проекта
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

