# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Здесь мы подключаем все ваши роутеры
from routers.unit_types     import router as unit_types_router
from routers.assembly_nodes import router as nodes_router
from routers.manufacturers  import router as manu_router
from routers.parts          import router as parts_router
from routers.orders         import router as orders_router

app = FastAPI(
    title="Oil & Gas Parts API",
    description="API для каталога запчастей и оформления заказов",
    version="1.0.0",
)

# ─────────────── CORS ───────────────────
# Позволяет фронтенду на localhost:3000 обращаться к нашему API
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       
    allow_credentials=True,
    allow_methods=["*"],         
    allow_headers=["*"],         
)
# ─────────────────────────────────────────

@app.get("/", tags=["health"])
async def health_check():
    """
    Здоровье приложения. 
    Нужно для проверки, что сервер поднят и отвечает.
    """
    return {"message": "API работает!"}


# ─────────────── Роутеры ─────────────────
# Каждый из этих роутеров должен быть правильно определён в папке backend/routers
app.include_router(unit_types_router,   prefix="/unit_types",      tags=["unit_types"])
app.include_router(nodes_router,        prefix="/assembly_nodes",  tags=["assembly_nodes"])
app.include_router(manu_router,         prefix="/manufacturers",    tags=["manufacturers"])
app.include_router(parts_router,        prefix="/parts",            tags=["parts"])
app.include_router(orders_router,       prefix="/orders",           tags=["orders"])
# ─────────────────────────────────────────


from routers.hotzones import router as hotzones_router

app.include_router(
    hotzones_router,
    prefix="/hotzones",
    tags=["hotzones"],
)

app.include_router(unit_types_router,   prefix="/unit_types",     tags=["unit_types"])
app.include_router(nodes_router,        prefix="/assembly_nodes", tags=["assembly_nodes"])
app.include_router(manu_router,         prefix="/manufacturers",  tags=["manufacturers"])
app.include_router(parts_router,        prefix="/parts",          tags=["parts"])
app.include_router(orders_router,       prefix="/orders",         tags=["orders"])
app.include_router(hotzones_router,     prefix="/hotzones",       tags=["hotzones"])


