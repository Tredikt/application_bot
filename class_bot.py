from aiogram import Bot, Dispatcher, executor
from utils.db_api.database import DataBase

from aiogram.types import Message, ContentTypes
from aiogram.dispatcher.dispatcher import FSMContext

from states_handlers.states import BotStates

from blanks.bot_texts import brand_request, name_request
from blanks.bot_markup import markups_brands_list

from handlers.name_request_handler import name_request_handler
from handlers.contant_request_handler import contact_request_handler
from handlers.model_request_handler import model_request_handler
from handlers.mileage_request_handler import mileage_request_handler
from handlers.used_age_request_handler import used_age_request_handler
from handlers.region_request_handler import region_request_handler
from handlers.brands_request_handler import brand_request_handler
from handlers.add_admin_handler import add_admin_handler
from handlers.add_admin_state import add_admin_state
from handlers.post_in_channel_handler import post_in_channel_handler
from handlers.post_in_channel_state import post_in_channel_state
from handlers.get_my_id_handler import get_my_id_handler


class MyBot:
    def __init__(self, bot: Bot, dp: Dispatcher, db: DataBase):
        self.bot = bot
        self.dp = dp
        self.db = db

    async def start_handler(self, message: Message, state: FSMContext):
        chat = message.chat.id
        tg_id = message.from_user.id
        username = message.from_user.username

        users = self.db.get_users_ids()

        if tg_id in users:
            await BotStates.brand_request.set()
            await self.bot.send_message(
                chat_id=chat,
                text=brand_request,
                reply_markup=markups_brands_list[0],
                parse_mode="html"
            )

        else:
            await BotStates.name_request.set()
            await self.bot.send_message(
                chat_id=chat,
                text=name_request,
                parse_mode="html"
            )

    async def text_handler(self, message: Message, state: FSMContext):
        tg_id = message.from_user.id
        m_id = message.message_id
        chat_type = message.chat.type

        # print(message)

    def register_handlers(self):
        self.dp.register_message_handler(callback=self.start_handler, commands=["start"], state="*")
        self.dp.register_message_handler(callback=get_my_id_handler, commands=["get_my_id"], state="*")

        self.dp.register_message_handler(callback=name_request_handler, content_types=["text"], state=BotStates.name_request)
        self.dp.register_message_handler(callback=contact_request_handler, content_types=["contact"], state=BotStates.contact_request)
        self.dp.register_message_handler(callback=model_request_handler, content_types=["text"], state=BotStates.model_request)
        self.dp.register_message_handler(callback=mileage_request_handler, content_types=["text"], state=BotStates.mileage_request)

        self.dp.register_callback_query_handler(callback=brand_request_handler, state=BotStates.brand_request)
        self.dp.register_callback_query_handler(callback=region_request_handler, state=BotStates.region_request)
        self.dp.register_callback_query_handler(callback=used_age_request_handler, state=BotStates.used_age_request)

        self.dp.register_message_handler(callback=add_admin_handler, commands=["add_admin"], state="*")
        self.dp.register_message_handler(callback=add_admin_state, content_types=["text"], state=BotStates.add_admin)

        self.dp.register_message_handler(callback=post_in_channel_handler, commands=["post_in_channel", "post_to_channel"], state="*")
        self.dp.register_message_handler(callback=post_in_channel_state, content_types=ContentTypes.ANY, state=BotStates.post_in_channel)

        self.dp.register_message_handler(callback=self.text_handler, state="*", content_types=["text"])

    def run(self):
        self.register_handlers()
        executor.start_polling(dispatcher=self.dp, skip_updates=True)