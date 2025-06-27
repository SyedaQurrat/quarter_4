import chainlit as cl
import requests

BINANCE_URL = "https://api.binance.com/api/v3/ticker/price"

# Function to fetch top 10 prices
def fetch_top_10_prices():
    try:
        response = requests.get(BINANCE_URL)
        response.raise_for_status()
        data = response.json()
        return data[:10]
    except requests.exceptions.RequestException as e:
        return f"❌ Error: {e}"

# Function to fetch specific coin price
def fetch_coin_price(symbol):
    try:
        url = f"{BINANCE_URL}?symbol={symbol.upper()}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"{symbol.upper()} Price: {data['price']} USDT"
        else:
            return "❌ Invalid coin symbol or not available on Binance."
    except requests.exceptions.RequestException as e:
        return f"❌ Error: {e}"
@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Welcome to the **Crypto Price Agent**!").send() 
    
# Chainlit entry point
@cl.on_message
async def main(message: cl.Message):
    user_input = message.content.strip()

    if user_input.lower() == "top 10":
        top_prices = fetch_top_10_prices()
        if isinstance(top_prices, str):
            await cl.Message(content=top_prices).send()
        else:
            msg = "🔝 **Top 10 Crypto Coin Prices on Binance:**\n\n"
            for coin in top_prices:
                msg += f"- {coin['symbol']}: {coin['price']} USDT\n"
            await cl.Message(content=msg).send()
    else:
        price = fetch_coin_price(user_input)
        await cl.Message(content=price).send()







