from data_utils import create_sample_data, create_rating_matrix
from similarity import calculate_user_similarity
from display import display_header, display_data, display_all_recommendations

def main():
    """Main function that orchestrates the recommendation system"""
    
    # Display header
    display_header()
    
    # Create and display data
    data = create_sample_data()
    display_data(data)
    
    # Create rating matrix and calculate similarities
    rating_matrix = create_rating_matrix(data)
    user_similarity_df = calculate_user_similarity(rating_matrix)
    
    # Display recommendations for all users
    display_all_recommendations(data, rating_matrix, user_similarity_df)

if __name__ == "__main__":
    main()