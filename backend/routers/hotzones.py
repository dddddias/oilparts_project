# backend/routers/hotzones.py

from fastapi import APIRouter, HTTPException


router = APIRouter(
    prefix="/hotzones",
    tags=["hotzones"],
)


# GET /hotzones/  — возвращает список (пока пусть будет пустой)
@router.get("/", response_model=list)
async def list_hotzones():
    return []


# GET /hotzones/{hotzone_id} — возвращает одну «зону» по ID
@router.get("/{hotzone_id}", response_model=dict)
async def get_hotzone(hotzone_id: int):
    # здесь можно добавить логику работы с БД
    # пока просто заглушка:
    if hotzone_id < 1:
        raise HTTPException(status_code=404, detail="Hotzone not found")
    return {"id": hotzone_id}
