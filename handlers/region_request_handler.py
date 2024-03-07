from utils.functions.get_bot_and_db import get_bot_and_db
from blanks.bot_markup import back_to_channel_keyboard
from blanks.bot_texts import end_message
from config import group_id


async def region_request_handler(call, state):
    tg_id = call["from"]["id"]
    chat = call.message.chat.id
    bot, db = get_bot_and_db()
    callback = call.data

    if callback.isdigit():
        inline_list = call.message.reply_markup.inline_keyboard

        for elem in inline_list:
            if elem[0].callback_data == callback:
                async with state.proxy() as data:
                    brand = data["brand"]
                    model = data["model"]
                    used_age = data["used_age"]
                    mileage = data["mileage"]
                    region = elem[0].text

                name, phone, username = db.get_user_data(tg_id=tg_id)

                await bot.send_message(
                    chat_id=group_id,
                    text="<pre>Новая заявка по расчёту стоимости.</pre>\n"
                         f"Имя: {name}\n"
                         f"Телефон: +{phone}\n"
                         f"Username: {username}\n\n"
                         f"Марка автомобиля: {brand}.\n"
                         f"Модель автомобиля: {model}.\n"
                         f"Возраст автомобиля: {used_age}.\n"
                         f"Пробег автомобиля: {mileage}.\n"
                         f"Регион филиала: {region}.",
                    parse_mode="html"
                )

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
                        text=end_message,
                        parse_mode="html",
                        reply_markup=back_to_channel_keyboard
                    )

                await state.finish()