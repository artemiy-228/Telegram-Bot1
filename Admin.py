from aiogram.filters import Filter
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message


class Admin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in [1041134324, 839399041, 1053774198]

class Form(StatesGroup):
    message = State()
    image = State()
