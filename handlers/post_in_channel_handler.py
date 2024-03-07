from aiogram.types import Message
from aiogram.dispatcher.dispatcher import FSMContext

from states_handlers.states import BotStates

from utils.functions.get_bot_and_db import get_bot_and_db


async def post_in_channel_handler(message: Message, state: FSMContext):
    bot, db = get_bot_and_db()
    tg_id = message.from_user.id
    admins = db.get_admins()

    if tg_id in admins:
        await bot.send_message(
            chat_id=tg_id,
            text="Отправьте пост в этот чат и я отправлю его в канал с кнопкой, ведущей к боту"
        )

        await BotStates.post_in_channel.set()

