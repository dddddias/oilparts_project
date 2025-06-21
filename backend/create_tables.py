# create_tables.py
from db.session import engine
from db.base import Base

# Импорт моделей для регистрации в metadata
import models.unit_type
import models.assembly_node
import models.manufacturer
import models.part
import models.order
import models.order_item
import models.hotzone



if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("✅ Все таблицы успешно созданы в БД")

