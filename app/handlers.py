from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
import app.keyboard as kb
import app.models as md
from Admin import Admin, Form

router = Router()
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()


@router.message(F.text == '/start')
async def cmd_start(message: Message) -> None:
    await md.create_user(message.from_user.id, False)
    await message.answer("Добро пожаловать в наш магазин Башмакоф!", reply_markup=kb.main)


@router.message(F.text == '/my_id')
async def cmd_start(message: Message) -> None:
    await message.answer(f"Ваш id: {message.from_user.id}")


@router.message(F.text == 'О нас')
async def cmd_start(message: Message) -> None:
    await message.answer(text)
    await message.answer_photo(
        photo='https://sun9-49.userapi.com/impg/PYk5NmRIqql0v_lqRAtCjKDw3Z4xgPvwoP25zg/icwHBndSL44.jpg?size=500x600&quality=95&sign=459dc0138c6b5304a3e3c143da4d53e4&type=album',
        caption='P.S. Мужчина с рекламы не продается')


@router.message(F.text == 'Подписаться на рассылку')
async def sub(message: Message) -> None:
    answer = await md.subscribe(message.from_user.id)
    await message.answer(answer)


@router.message(F.text == 'Отписаться от рассылки')
async def unsub(message: Message) -> None:
    answer = await md.unsubscribe(message.from_user.id)
    await message.answer(answer)


@router.message(F.text == 'Контакты')
async def contacts_share(message: Message) -> None:
    await message.answer("Контакты для связи с нами")
    await message.answer("По вопросам покупки обращаться только сюда❗❗❗")
    await message.answer("Помимо покупок, вы можете насладиться живыми башмаками на нашем YouTube канале.",
                         reply_markup=kb.socials)


@router.message(F.text == 'Вильдан')
async def cmd_send_image(message: Message):
    await message.answer_photo(photo='https://risovach.ru/upload/2019/01/mem/negr-gey_197875192_orig_.jpg',
                               caption='Вильдан')


@router.message(Admin(), F.text == '/рассылка')
async def distribution(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.message)
    await message.answer(
        "Введите текст рассылки: ",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Form.message)
async def process_name(message: Message, state: FSMContext) -> None:
    subs = await md.get_subscribers()
    photo = message.photo[-1].file_id
    TOKEN = "6470249858:AAHYrl78pTSaDv-pUIpcpNZUhqMba867YYg"
    bot = Bot(token=TOKEN)
    try:
        for sub in subs:
            await bot.send_message(sub, message.caption)
            await bot.send_photo(sub, photo)
    finally:
        del subs
        await bot.session.close()
        await state.clear()


@router.message()
async def unknown_command(message: Message) -> None:
    await message.reply(f"I don't understand you!")
