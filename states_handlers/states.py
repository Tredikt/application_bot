from aiogram.dispatcher.filters.state import StatesGroup, State


class BotStates(StatesGroup):
    name_request = State()
    contact_request = State()
    brand_request = State()
    model_request = State()
    used_age_request = State()
    region_request = State()
    mileage_request = State()

    post_in_channel = State()
    add_admin = State()