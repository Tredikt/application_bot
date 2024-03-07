from utils.functions.get_bot_and_db import get_bot_and_db
from blanks.bot_texts import used_age_request
from blanks.bot_markup import used_age_keyboard
from states_handlers.states import BotStates


async def model_request_handler(message, state):
    chat = message.chat.id
    text = message.text
    bot, db = get_bot_and_db()

    async with state.proxy() as data:
        data["model"] = text

    await bot.send_message(
        chat_id=chat,
        text=used_age_request,
        reply_markup=used_age_keyboard,
        parse_mode="html"
    )

    await BotStates.used_age_request.set()