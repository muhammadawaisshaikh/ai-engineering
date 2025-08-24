import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def calculate_user_similarity(rating_matrix):
    user_similarity = cosine_similarity(rating_matrix)
    
    user_similarity_df = pd.DataFrame(
        user_similarity, 
        index=rating_matrix.index, 
        columns=rating_matrix.index
    )
    
    return user_similarity_df

def get_similar_users(user_id, user_similarity_df, n_similar=2):
    if user_id not in user_similarity_df.index:
        return pd.Series()
    
    # Get similarity scores for the user, sort by similarity, exclude self
    user_similarities = user_similarity_df[user_id].sort_values(ascending=False)
    similar_users = user_similarities[user_similarities.index != user_id]
    
    return similar_users.head(n_similar)
