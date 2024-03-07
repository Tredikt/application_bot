from utils.functions.get_bot_and_db import get_bot_and_db
from blanks.bot_examinations import examination_symbols
from blanks.bot_texts import contact_request, decline_name
from blanks.bot_markup import get_contact_markup
from states_handlers.states import BotStates


async def name_request_handler(message, state):
    chat = message.chat.id
    text = message.text
    bot, db = get_bot_and_db()

    for symbol in text:
        if symbol.lower() not in examination_symbols:
            await bot.send_message(
                chat_id=chat,
                text=decline_name
            )
            break
    else:
        async with state.proxy() as data:
            data["name"] = text

        await bot.send_message(
            chat_id=chat,
            text=contact_request,
            reply_markup=get_contact_markup,
            parse_mode="html"
        )

        await BotStates.contact_request.set()