# tools/crypto_tool.py

from agents import tool

@tool
async def get_crypto_rate(symbol: str) -> str:
    """Get crypto rate for a given coin."""
    # Fake static response
    return f"The current rate of {symbol.upper()} is 70,000 USD"
