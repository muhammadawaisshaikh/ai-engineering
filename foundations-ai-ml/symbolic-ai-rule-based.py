# Sample rule-based filtering logic (Symbolic AI)
def filter_products(products, entities):
    return [
        p for p in products
        if p["category"] == entities["category"]
        and "noise-canceling" in p["features"]
        and p["price"] <= entities["max_price"]
        and p["in_stock"] is True  # Symbolic rule
    ]

# Example product list
product_list = [
    {"name": "BrandX Headphones", "category": "headphones", "features": ["noise-canceling"], "price": 250, "in_stock": True},
    {"name": "BrandY Headphones", "category": "headphones", "features": ["wireless"], "price": 280, "in_stock": True},
    {"name": "BrandZ Headphones", "category": "headphones", "features": ["noise-canceling"], "price": 320, "in_stock": False},
]

# Applying symbolic rules
recommended = filter_products(product_list, extracted_entities)
print(recommended)
