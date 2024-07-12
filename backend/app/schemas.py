from pydantic import BaseModel
from datetime import datetime
from typing import Optional



# Todoアイテムを作成する際に使用するスキーマ
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None



class Todo(BaseModel):
    id: int 
    title: str
    description: Optional[str] = None
    completed: bool 
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True   # ORMモデルとの互換性を持たせる


# Todoアイテムを更新する際に使用するスキーマ
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[str] =None
