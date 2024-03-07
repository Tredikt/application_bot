from utils.functions.get_bot_and_db import get_bot_and_db
from blanks.bot_texts import brand_request
from blanks.bot_markup import markups_brands_list
from states_handlers.states import BotStates


async def contact_request_handler(message, state):
    chat = message.chat.id
    tg_id = message.from_user.id
    username = message.from_user.username
    contact = message.contact.phone_number
    bot, db = get_bot_and_db()

    contact = str(contact)
    if contact[0] == "8":
        contact = contact.replace("8", "7", 1)

    elif contact[0] == "+":
        contact = contact.replace("+7", "7", 1)

    async with state.proxy() as data:
        name = data["name"]

    db.add_user(
        tg_id=tg_id,
        phone=contact,
        name=name,
        username=username
    )

    await bot.send_message(
        chat_id=chat,
        text=brand_request,
        reply_markup=markups_brands_list[0],
        parse_mode="html"
    )
    await BotStates.brand_request.set()

