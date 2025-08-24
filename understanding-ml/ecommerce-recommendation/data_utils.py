import pandas as pd

def create_sample_data():
    """Create simple sample data for the recommendation system"""
    data = {
        'user_id': [1, 1, 2, 2, 3, 3],
        'product_id': [101, 102, 101, 103, 102, 103],
        'rating': [5, 4, 4, 5, 3, 4],
        'product_name': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse', 'Keyboard']
    }
    return pd.DataFrame(data)

def create_rating_matrix(data):
    """Convert data to user-product rating matrix"""
    rating_matrix = data.pivot_table(
        index='user_id', 
        columns='product_id', 
        values='rating'
    ).fillna(0)
    return rating_matrix

def get_user_products(user_id, rating_matrix):
    """Get products rated by a specific user"""
    if user_id in rating_matrix.index:
        user_ratings = rating_matrix.loc[user_id]
        return set(user_ratings[user_ratings > 0].index)
    return set()

def get_product_name(product_id, data):
    """Get product name by product ID"""
    product_info = data[data['product_id'] == product_id]
    if not product_info.empty:
        return product_info['product_name'].iloc[0]
    return f"Product_{product_id}"
