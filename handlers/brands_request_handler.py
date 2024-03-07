from utils.functions.get_bot_and_db import get_bot_and_db
from blanks.bot_markup import markups_brands_list
from blanks.bot_texts import model_request
from states_handlers.states import BotStates


async def brand_request_handler(call, state):
    chat = call.message.chat.id
    bot, db = get_bot_and_db()
    callback = call.data

    if callback[:9] == "next_page":
        await bot.edit_message_reply_markup(
            chat_id=chat,
            message_id=call.message.message_id,
            reply_markup=markups_brands_list[int(callback[15:])]
        )

    elif callback[:9] == "prev_page":
        await bot.edit_message_reply_markup(
            chat_id=chat,
            message_id=call.message.message_id,
            reply_markup=markups_brands_list[int(callback[15:])]
        )

    elif callback.isdigit():
        inline_list = call.message.reply_markup.inline_keyboard

        for elem in inline_list:
            if elem[0].callback_data == callback:
                async with state.proxy() as data:
                    data["brand"] = elem[0].text

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
                    text=model_request,
                    parse_mode="html"
                )

                await BotStates.model_request.set()