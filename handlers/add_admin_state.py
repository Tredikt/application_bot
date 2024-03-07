from aiogram.types import Message
from aiogram.dispatcher.dispatcher import FSMContext

from utils.functions.get_bot_and_db import get_bot_and_db
from states_handlers.states import BotStates


async def add_admin_state(message: Message, state: FSMContext):
    bot, db = get_bot_and_db()
    tg_id = message.from_user.id
    text = message.text

    if text.isdigit():
        db.add_admin(tg_id=text)

        await bot.send_message(
            chat_id=tg_id,
            text="Права админа успешно выданы"
        )

        await state.finish()

    else:
        await bot.send_message(
            chat_id=tg_id,
            text="ID должно быть целым числом"
        )
