from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

menu = InlineKeyboardMarkup()

back_to_channel_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton(
        text="Вернуться в канал",
        url="t.me/zakazfresh"
    )
)

get_contact_markup = ReplyKeyboardMarkup(resize_keyboard=True)
get_contact_markup.add(
    KeyboardButton(text="Отправить номер телефона 📱", request_contact=True)
)


used_age_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton(
        text="меньше 3-х лет",
        callback_data="<3"
    )
).add(
    InlineKeyboardButton(
        text="3-5 лет",
        callback_data="3-5"
    )
).add(
    InlineKeyboardButton(
        text="5-7 лет",
        callback_data="5-7"
    )
).add(
    InlineKeyboardButton(
        text="больше 7-ми лет",
        callback_data=">7"
    )
)

region_keyboard = InlineKeyboardMarkup(row_width=1)
region_keyboard.add(InlineKeyboardButton(text="Москва", callback_data="1"))
region_keyboard.add(InlineKeyboardButton(text="Воронеж", callback_data="2"))
region_keyboard.add(InlineKeyboardButton(text="Ростов-на-Дону", callback_data="3"))
region_keyboard.add(InlineKeyboardButton(text="Краснодар", callback_data="4"))
region_keyboard.add(InlineKeyboardButton(text="Волгоград", callback_data="5"))
region_keyboard.add(InlineKeyboardButton(text="Минеральные Воды", callback_data="6"))
region_keyboard.add(InlineKeyboardButton(text="Тюмень", callback_data="7"))
region_keyboard.add(InlineKeyboardButton(text="Оренбург", callback_data="8"))
region_keyboard.add(InlineKeyboardButton(text="Ставрополь", callback_data="9"))
region_keyboard.add(InlineKeyboardButton(text="Сургут", callback_data="10"))
region_keyboard.add(InlineKeyboardButton(text="Сочи", callback_data="11"))
region_keyboard.add(InlineKeyboardButton(text="Тверь", callback_data="12"))

with open("brands.txt", "r", encoding="UTF-8") as file:
    brands_list = file.read().split("\n")
    markups_brands_list = []
    brands_keyboard = InlineKeyboardMarkup()
    count = 1
    markup_count = 0
    for elem in brands_list:
        try:
            code, brands = elem.split("@")
        except Exception:
            pass
        if count == 10:
            if markup_count == 0:
                brands_keyboard.add(
                    InlineKeyboardButton(text="⏩", callback_data="next_page_brand1")
                )

            elif markup_count == 8:
                brands_keyboard.add(
                    InlineKeyboardButton(text="⏪", callback_data="prev_page_brand7")
                )

            else:
                brands_keyboard.add(
                    InlineKeyboardButton(text="⏪", callback_data=f"prev_page_brand{markup_count - 1}"),
                    InlineKeyboardButton(text="⏩", callback_data=f"next_page_brand{markup_count + 1}"),
                )

            markups_brands_list.append(brands_keyboard)
            brands_keyboard = InlineKeyboardMarkup()
            count = 0
            markup_count += 1

        brands_keyboard.add(
            InlineKeyboardButton(text=brands, callback_data=code)
        )
        count += 1


to_bot_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton(
        text="Рассчитать стоимость авто",
        url="https://t.me/zakazautofresh_bot"
    )
)