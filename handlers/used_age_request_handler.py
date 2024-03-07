from utils.functions.get_bot_and_db import get_bot_and_db
from blanks.bot_texts import mileage_request
from states_handlers.states import BotStates


async def used_age_request_handler(call, state):
    chat = call.message.chat.id
    bot, db = get_bot_and_db()
    callback = call.data

    inline_list = call.message.reply_markup.inline_keyboard

    for elem in inline_list:
        if elem[0].callback_data == callback:
            async with state.proxy() as data:
                data["used_age"] = elem[0].text

            await bot.delete_message(
                chat_id=chat,
                message_id=call.message.message_id
            )

            await bot.send_message(
                chat_id=chat,
                text=f"💬: <i>{elem[0].text}</i>",
                parse_mode="html"
            )

            await bot.send_message(
                chat_id=chat,
                text=mileage_request,
                parse_mode="html"
            )

            await BotStates.mileage_request.set()