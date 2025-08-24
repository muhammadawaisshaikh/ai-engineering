from data_utils import get_user_products, get_product_name
from similarity import get_similar_users

def get_recommendations(user_id, data, rating_matrix, user_similarity_df):
    similar_users = get_similar_users(user_id, user_similarity_df, n_similar=2)
    
    if similar_users.empty:
        return []
    
    # Get products already rated by the user
    user_products = get_user_products(user_id, rating_matrix)
    recommendations = []
    
    # Collect recommendations from similar users
    for similar_user, similarity in similar_users.items():
        if similarity > 0:
            similar_user_products = get_user_products(similar_user, rating_matrix)
            new_products = similar_user_products - user_products
            
            for product_id in new_products:
                product_name = get_product_name(product_id, data)
                recommendations.append((product_name, similarity))
    
    # Return top 2 recommendations
    return recommendations[:2]
