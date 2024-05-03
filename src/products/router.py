import time

from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.datebase import get_async_session
from src.products.models import Product
from src.products.schemas import ProductSchema

router = APIRouter(
    prefix='/products',
    tags=["Products"]
)


@router.post('/add_product')
async def add_product(product: ProductSchema, session: AsyncSession = Depends(get_async_session)):
    try:
        query = insert(Product).values(**product.dict())
        result = await session.execute(query)
        await session.commit()
        return {
            'status': 'success',
            'data': None,
            'details': None
        }
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'data': None,
            'details':  type(ex).__name__
        })


@router.get('/all_products')
async def all_products(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Product)
        result = await session.execute(query)
        return {
            'status': 'success',
            'data': result.scalars().all(),
            'details': None
        }
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'data': None,
            'details': type(ex).__name__
        })


@router.get("/long_oper")
@cache(expire=60)
async def index():
    time.sleep(2)
    return {'status': 'success'}
