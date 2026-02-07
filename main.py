import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

BOT_TOKEN = "8544285722:AAEM2I7UEL42O2w0-yXC3uDsLhhLElI4Vms"

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

ans_message = """<b>Введите числа в одном из форматов:</b>

<code>[цена 1] [цена 2]</code>
<code>[цена 1] [цена 2] [кол-во монет]</code>

<i>* разделитель может быть [ . ] или [ , ]</i>"""

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(ans_message)

@dp.message()
async def spread_calculator(message: Message):
    try:
        parts = message.text.strip().split()

        if len(parts) == 2:
            price1 = float(parts[0].strip().replace(',', '.'))
            price2 = float(parts[1].strip().replace(',', '.'))

            spread_percent = abs(price1 - price2) / min(price1, price2) * 100

            await message.reply(
                f"➡️ <b>Спред:</b> <code>{spread_percent:.2f}%</code>"
            )

        elif len(parts) == 3:
            price1 = float(parts[0].strip().replace(',', '.'))
            price2 = float(parts[1].strip().replace(',', '.'))
            coins = float(parts[2].strip().replace(',', '.'))

            spread_percent = abs(price1 - price2) / min(price1, price2) * 100

            profit_usd = abs(price1 - price2) * coins

            await message.reply(
                f"➡️ <b>Спред:</b> <code>{spread_percent:.2f}%</code>\n\n"
                f"💸 <b>Макс. прибыль:</b> <code>{profit_usd:.2f}$</code>"
            )

        else:
            await message.reply("🔴 " + ans_message)

    except ValueError:
        await message.reply("🔴 " + ans_message)
    except Exception as e:
        await message.reply("🔴 " + ans_message)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
