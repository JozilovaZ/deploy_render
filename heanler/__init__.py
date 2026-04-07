from aiogram import Router
from .users import ur

def set_up()->Router:
    main_router=Router()
    main_router.include_router(ur)

    return main_router

