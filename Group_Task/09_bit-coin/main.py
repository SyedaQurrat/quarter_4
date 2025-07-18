# import chainlit as cl
# import requests

# BINANCE_URL = "https://api.binance.com/api/v3/ticker/price"

# # Function to fetch top 10 prices
# def fetch_top_10_prices():
#     try:
#         response = requests.get(BINANCE_URL)
#         response.raise_for_status()
#         data = response.json()
#         return data[:10]
#     except requests.exceptions.RequestException as e:
#         return f"❌ Error: {e}"

# # Function to fetch specific coin price
# def fetch_coin_price(symbol):
#     try:
#         url = f"{BINANCE_URL}?symbol={symbol.upper()}"
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = response.json()
#             return f"{symbol.upper()} Price: {data['price']} USDT"
#         else:
#             return "❌ Invalid coin symbol or not available on Binance."
#     except requests.exceptions.RequestException as e:
#         return f"❌ Error: {e}"
# @cl.on_chat_start
# async def start():
#     await cl.Message(content="👋 Welcome to the **Crypto Price Agent**!").send() 
    
# # Chainlit entry point
# @cl.on_message
# async def main(message: cl.Message):
#     user_input = message.content.strip()

#     if user_input.lower() == "top 10":
#         top_prices = fetch_top_10_prices()
#         if isinstance(top_prices, str):
#             await cl.Message(content=top_prices).send()
#         else:
#             msg = "🔝 **Top 10 Crypto Coin Prices on Binance:**\n\n"
#             for coin in top_prices:
#                 msg += f"- {coin['symbol']}: {coin['price']} USDT\n"
#             await cl.Message(content=msg).send()
#     else:
#         price = fetch_coin_price(user_input)
#         await cl.Message(content=price).send()






# import os
# import requests
# import chainlit as cl
# from dotenv import load_dotenv
# from openai_agents import OpenAIAgent, Tool

# load_dotenv()

# # 🔑 API setup
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

# # 🎯 Tool: Get crypto price
# def get_price(symbol: str) -> dict:
#     url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
#     res = requests.get(url)
#     if res.status_code == 200:
#         data = res.json()
#         return {"symbol": data["symbol"], "price": data["price"]}
#     else:
#         return {"error": "Invalid symbol"}

# price_tool = Tool(
#     name="get_price",
#     func=get_price,
#     description="Get crypto price by symbol (like BTCUSDT, ETHUSDT)"
# )

# # 🤖 Custom Gemini Client with OpenAI SDK-style
# class GeminiClient:
#     def __init__(self, api_key, base_url):
#         self.api_key = api_key
#         self.base_url = base_url

#     def chat_completion(self, messages, model="gemini-1.5-flash"):
#         headers = {
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {self.api_key}"
#         }
#         body = {
#             "contents": [
#                 {"role": m["role"], "parts": [{"text": m["content"]}]}
#                 for m in messages
#             ]
#         }
#         res = requests.post(self.base_url, headers=headers, json=body)
#         res.raise_for_status()
#         return {
#             "choices": [{
#                 "message": {
#                     "role": "assistant",
#                     "content": res.json()["candidates"][0]["content"]["parts"][0]["text"]
#                 }
#             }]
#         }

# # 🎬 Chainlit start point
# @cl.on_chat_start
# async def start_chat():
#     await cl.Message("👋 Welcome! Ask me about any crypto price like `BTCUSDT`, `ETHUSDT`, etc.").send()

# # 📩 On message
# @cl.on_message
# async def handle_message(message: cl.Message):
#     client = GeminiClient(api_key=GEMINI_API_KEY, base_url=BASE_URL)
#     agent = OpenAIAgent(
#         name="GeminiAgent",
#         model=client,
#         tools=[price_tool]
#     )

#     result = agent.run(message.content)
#     await cl.Message(content=result).send()
