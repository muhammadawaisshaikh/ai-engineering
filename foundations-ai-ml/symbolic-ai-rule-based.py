# Sample rule-based filtering logic (Symbolic AI)
def filter_products(products, entities):
    """
    Filter products based on symbolic rules extracted from user query.
    
    Args:
        products: List of product dictionaries
        entities: Dictionary containing extracted entities (category, max_price, etc.)
    
    Returns:
        List of products that match all the symbolic rules
    """
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

# Example extracted entities from user query
extracted_entities = {
    "category": "headphones",
    "max_price": 300,
    "feature_required": "noise-canceling"
}

# Applying symbolic rules
recommended = filter_products(product_list, extracted_entities)
print("Products matching symbolic rules:")
for product in recommended:
    print(f"- {product['name']}: ${product['price']}")

# Demonstrate symbolic reasoning
print(f"\nSymbolic rules applied:")
print(f"- Category must be: {extracted_entities['category']}")
print(f"- Must have feature: {extracted_entities['feature_required']}")
print(f"- Price must be <= ${extracted_entities['max_price']}")
print(f"- Must be in stock: True")
