# Oil & Gas Parts API

REST-сервис для работы с каталогом нефтегазовых запчастей и заказами.

## Требования

- Python 3.10+
- PostgreSQL
- Docker & Docker-Compose (опционально)

## Быстрый старт (локально без Docker)

```bash
git clone <repo-url>
cd oilparts_project
python -m venv venv
# Windows:
venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt

# Создать базу (если не создана):
python init_db.py

# Создать таблицы
python create_tables.py

# Запустить сервер
uvicorn main:app --reload
```

При использовании Docker можно запустить `docker-compose` из каталога `infra`

### Hotzones API

Маршруты для работы с горячими зонами на схеме:

- `POST /hotzones/` — создать зону.
- `GET /hotzones/` — список всех зон.
- `GET /hotzones/drawing/{drawing_id}` — зоны для указанной схемы.
- `GET /hotzones/{hz_id}` — получить зону по ID.
- `PUT /hotzones/{hz_id}` — обновить зону.
- `DELETE /hotzones/{hz_id}` — удалить зону.