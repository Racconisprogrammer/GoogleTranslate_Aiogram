from aiogram import types
from loader import dp, bot
from deep_translator import GoogleTranslator
from keyboards.inline.languages import buttons, button
from states.tarjimon import Translator
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from keyboards.default.languages import TranslateButton



def translateGoogle(input, output, text):
    result = GoogleTranslator(source=input, target=output).translate(text)
    return result

@dp.message_handler(commands='tarjima', state=None)
async def start(message: types.Message):
    await message.answer("Qaysi tilda ma'lumot kiritasiz", reply_markup=buttons)


    await Translator.inp.set()

@dp.callback_query_handler(Text(startswith='👍'), state=Translator.inp)
async def second(call: types.CallbackQuery, state:FSMContext):
    data = call.data
    await state.update_data({
        'inp':data[1:]
    })

    await call.message.delete()
    await call.message.answer("Ma'lumot qaysi tilda chiqishini tanlang", reply_markup=button)
    await Translator.next()

    @dp.callback_query_handler(Text(startswith='cancel'), state=Translator.inp)
    async def cancel(call: types.CallbackQuery, state:FSMContext):
        await call.answer(cache_time=60)
        await call.message.delete()
        await call.message.answer(f"Buyruq bekor qilindi!❌")
        await call.message.answer(f"Tarjima boti ishlashi uchun /tarjima so'zini kiriting")
        await state.finish()

    @dp.callback_query_handler(Text(startswith='👍'), state=Translator.out)
    async def third(call: types.CallbackQuery, state: FSMContext):
        await call.answer(cache_time=60)
        data = call.data
        await state.update_data({
            'out': data[1:]
        })

        await call.message.delete()
        await call.message.answer("Matnni kiriting")
        await Translator.next()

    @dp.callback_query_handler(Text(equals='back'), state=Translator.out)
    async def back(call: types.CallbackQuery, state:FSMContext):
        await call.answer(cache_time=60)
        await call.message.delete()
        await call.message.answer("Ma'lumot qaysi tilda chiqishini tanlang", reply_markup=buttons)
        await Translator.inp.set()

    @dp.message_handler(content_types='text', state=Translator.text)
    async def textInTranslate(message: types.Message, state:FSMContext):
        text = message.text
        await state.update_data({
            'text': text
        })

        data = await state.get_data()
        result = translateGoogle(data['inp'], data['out'], data['text'])
        await message.answer(f"<b>Sizning tarjimangiz:</b>\n"
                             f"<i>{result}</i>")
        await state.finish()