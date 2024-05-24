from typing import List

from fastapi import APIRouter, Depends

from src.apps.employees import models
from src.apps.employees.dependencies import valid_business_trip_id
from src.apps.employees.schemas.business_trip import BusinessTrip, CreateBusinessTrip
from src.apps.employees.transformers.business_trip import BusinessTripTransformer
from src.core.database.session_manager import db_manager
from src.utils.handlers import api_handler
from src.utils.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.transformer import transform

router: APIRouter = APIRouter(
    prefix="/business_trips",
    tags=["business_trips"],
)


@router.get(path="", response_model=List[BusinessTrip])
@api_handler
async def get_business_trips():
    """Returns the list of business trips."""

    business_trips: List[models.BusinessTrip] = await SqlAlchemyRepository(db_manager.get_session,
                                                                           model=models.BusinessTrip).get_multi(
        unique=True)
    return transform(business_trips, BusinessTripTransformer().include(["employee"]))


@router.get(path="/{business_trip_id}")
@api_handler
async def get_business_trip(business_trip: BusinessTrip = Depends(valid_business_trip_id)):
    """Returns the business trip with the given id."""

    return transform(business_trip, BusinessTripTransformer().include(["employee"]))


@router.post(path="", response_model=BusinessTrip)
@api_handler
async def create_business_trip(data: CreateBusinessTrip):
    """Returns created with the given data business trip."""

    business_trip: models.BusinessTrip = await SqlAlchemyRepository(db_manager.get_session,
                                                                    model=models.BusinessTrip).create(data)
    return transform(business_trip, BusinessTripTransformer())