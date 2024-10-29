
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart
from create_bot import bot
from keyboards import client_kb as kb

router = Router()
goods_list = ['Телевізор', 'Телефон', 'Приставка']


class Order(StatesGroup):
    goods = State()
    quantity = State()
    address = State()


@router.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await bot.send_message(
        message.chat.id,
        text='Вітаємо! 👋🏽'
             '\n\nВиберіть товар, який ви хочете замовити'
             '\nТисніть на одну з кнопок 👇🏽',
        reply_markup=kb.ikb_client_main_menu(goods_list).as_markup()
    )


@router.callback_query(lambda callback: callback.data and callback.data.startswith("good_"))
async def handle_good_callback(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    good_name = callback.data.split("_", 1)[1]
    await state.update_data(good_name=good_name)
    await state.set_state(Order.quantity)
    await bot.send_message(callback.message.chat.id,
                           text=f"Ви обрали товар: {good_name}"
                                f"\nБудь ласка, введіть кількість товару, яку ви хочете замовити:")

@router.message(Order.quantity)
async def handle_quantity(message: types.Message, state: FSMContext):
    quantity = message.text
    await state.update_data(quantity=quantity)

    # Перехід до стану address
    await state.set_state(Order.address)
    await bot.send_message(message.chat.id,
                           text=f"Ви ввели кількість товару: {quantity}"
                                f"\nБудь ласка, введіть адресу доставки:")


@router.message(Order.address)
async def handle_address(message: types.Message, state: FSMContext):
    address = message.text
    data = await state.get_data()
    good_name = data.get("good_name")
    quantity = data.get("quantity")

    await bot.send_message(message.chat.id,
                           text=f"Ви ввели адресу доставки: {address}"
                                f"\n\nВаше замовлення:"
                                f"\nТовар: {good_name}"
                                f"\nКількість: {quantity}"
                                f"\nАдреса доставки: {address}",
                           reply_markup=kb.back_to_main_menu().as_markup())

@router.callback_query(lambda callback: callback.data == 'back_to_main_menu')
async def back_to_main_menu(callback: types.CallbackQuery):
    await callback.message.delete()
    await command_start_handler(callback.message)
