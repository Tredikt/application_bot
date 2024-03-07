from aiogram.types import Message
from aiogram.dispatcher.dispatcher import FSMContext

from utils.functions.get_bot_and_db import get_bot_and_db
from config import channel_id

from blanks.bot_markup import to_bot_keyboard


async def post_in_channel_state(message: Message, state: FSMContext):
    bot, db = get_bot_and_db()
    tg_id = message.from_user.id
    m_id = message.message_id

    await bot.copy_message(
        chat_id=channel_id,
        from_chat_id=tg_id,
        message_id=m_id,
        reply_markup=to_bot_keyboard
    )

    await bot.send_message(
        chat_id=tg_id,
        text="Сообщение успешно было отправлено в канал"
    )

    await state.finish()

