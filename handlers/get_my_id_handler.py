from aiogram.types import Message
from aiogram.dispatcher.dispatcher import FSMContext

from utils.functions.get_bot_and_db import get_bot_and_db
from states_handlers.states import BotStates


async def get_my_id_handler(message: Message, state: FSMContext):
    bot, db = get_bot_and_db()
    tg_id = message.from_user.id

    await bot.send_message(
        chat_id=tg_id,
        text="Ваш ID, отправьте его админу для получения прав"
    )

    await bot.send_message(
        chat_id=tg_id,
        text=f"<pre>{tg_id}</pre>",
        parse_mode="html"
    )

