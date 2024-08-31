from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from service_1c.statuses import statuses
from service_1c.tamplates import (
    MessageTemplate,
    flyers_template
)


router = APIRouter()


@router.post("/user_orders/")
async def get_user_order(telefon: str) -> JSONResponse:
    data = []
    orders = await statuses.order_response(telefon=telefon)
    for order in orders:
        message = MessageTemplate(order=order).message()
        data.append(message)
    return JSONResponse(
        content={
            "status": "ok",
            "data": f"{data}"
        }
    )


@router.post("/user_flyers/")
async def get_user_flyers(telefon: str) -> JSONResponse:
    flyer = await statuses.flyer_response(telefon=telefon)
    message = flyers_template(flyer=flyer)
    return JSONResponse(
        content={
            "status": "ok",
            "data": f"{message}"
        }
    )
