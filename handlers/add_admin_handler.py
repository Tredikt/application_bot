from aiogram.types import Message
from aiogram.dispatcher.dispatcher import FSMContext

from utils.functions.get_bot_and_db import get_bot_and_db
from states_handlers.states import BotStates


async def add_admin_handler(message: Message, state: FSMContext):
    bot, db = get_bot_and_db()
    tg_id = message.from_user.id
    admins = db.get_admins()

    if tg_id in admins:
        await bot.send_message(
            chat_id=tg_id,
            text="Отправьте tg_id пользователя, которому хотите выдать права админа, "
                 "для этого ему необходимо прописать в бота"
                 "/get_my_id и прислать ответ бота вам"
        )

        await BotStates.add_admin.set()
