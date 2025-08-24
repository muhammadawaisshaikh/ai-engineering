def display_header():
    """Display the system header"""
    print("Simple Ecommerce Recommendation System")
    print("=" * 40)

def display_data(data):
    """Display the sample data"""
    print("Sample data:")
    print(data)
    print()

def display_user_recommendations(user_id, recommendations):
    """Display recommendations for a specific user"""
    print(f"User {user_id} recommendations:")
    
    if recommendations:
        for product_name, similarity in recommendations:
            print(f"  - {product_name} (similarity: {similarity:.2f})")
    else:
        print("  No recommendations available")
    print()

def display_all_recommendations(data, rating_matrix, user_similarity_df):
    """Display recommendations for all users"""
    from recommendations import get_recommendations
    
    for user_id in data['user_id'].unique():
        recommendations = get_recommendations(user_id, data, rating_matrix, user_similarity_df)
        display_user_recommendations(user_id, recommendations)
