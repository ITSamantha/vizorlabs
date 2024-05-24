import datetime
from typing import Optional

from src.core.schemas.base import BaseSchemaModel, BaseResponseSchemaModel


class CreateBusinessTrip(BaseSchemaModel):
    employee_id: int

    start_date: datetime.date
    end_date: datetime.date

    purpose: str

    destination: str


class UpdateBusinessTrip(BaseSchemaModel):
    pass


class BusinessTrip(BaseResponseSchemaModel):
    id: int

    start_date: datetime.date
    end_date: datetime.date

    purpose: str
    destination: str

    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: Optional[datetime.datetime]