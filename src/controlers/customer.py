from fastapi import APIRouter


router = APIRouter()


@router.get("/customer")
async def get_all(customer_id: int):
    return {"message": "This endpoint will return a list of <customer>s."}


@router.get("/customer/{customer_id}")
async def get_one(customer_id: int):
    return {"message": "This endpoint will return <customer> info."}


@router.post("/customer")
async def create():
    return {"message": "This endpoint will create a <customer>."}


@router.put("/customer/{customer_id}")
async def update(customer_id: int):
    return {"message": "This endpoint will update a <customer> info."}


@router.delete("/customer/{customer_id}")
async def delete(customer_id: int):
    return {"message": "This endpoint will delete a <customer>."}
