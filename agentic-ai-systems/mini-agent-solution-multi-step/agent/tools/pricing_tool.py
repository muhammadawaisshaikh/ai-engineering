from agent.config import PRICE_DATA


def query_pricing_tool(product):
    if not product:
        return {"ok": False, "error": "No product provided"}

    payload = PRICE_DATA.get(product.lower())
    if not payload:
        return {"ok": False, "error": f"No price data found for '{product}'"}

    return {"ok": True, "data": payload}
