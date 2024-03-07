from utils.functions.get_bot_and_db import get_bot_and_db
from blanks.bot_texts import region_request
from blanks.bot_markup import region_keyboard
from states_handlers.states import BotStates


async def mileage_request_handler(message, state):
    chat = message.chat.id
    text = message.text
    bot, db = get_bot_and_db()

    if text.isdigit():
        async with state.proxy() as data:
            data["mileage"] = text

        await bot.send_message(
            chat_id=chat,
            text=region_request,
            parse_mode="html",
            reply_markup=region_keyboard
        )

        await BotStates.region_request.set()

    else:
        await bot.send_message(
            chat_id=chat,
            text="Пробег должен быть целым числом, попробуйте снова"
        )