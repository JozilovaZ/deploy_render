from data import config
from aiogram import types
from aiogram.filters import Filter


class IsAdmin(Filter):
    async def __call__(self, message: types.Message) -> bool:
        return str(message.from_user.id) in config.ADMINS