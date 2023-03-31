import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the dataset into a Pandas DataFrame
data = pd.read_csv('dataset/data.csv')

# Create a pivot table to calculate user similarity
pivot_table = pd.pivot_table(data, values='NPS Score', index='Member ID', columns='Subscription Type')
pivot_table = pivot_table.fillna(0)
user_similarity = cosine_similarity(pivot_table)

# Define the recommendation function
def recommend_subscriptions(user_id, pivot_table, user_similarity):
    user_index = np.where(pivot_table.index == user_id)[0][0]
    similar_users = user_similarity[user_index]
    sorted_similar_users = np.argsort(-similar_users)
    user_subscription_types = pivot_table.iloc[user_index]
    recommendations = []
    for i in range(len(sorted_similar_users)):
        similar_user_index = sorted_similar_users[i]
        similar_user_subscription_types = pivot_table.iloc[similar_user_index]
        for subscription_type, nps_score in similar_user_subscription_types.iteritems():
            if nps_score > 0 and user_subscription_types[subscription_type] == 0:
                recommendations.append((subscription_type, nps_score))
    sorted_recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)
    return sorted_recommendations

# Define the Flask endpoint for recommending subscriptions
@app.route('/recommend', methods=['POST'])
def recommend():
    # Get the user ID from the request data
    user_id = int(request.json['user_id'])
    # Call the recommendation function
    recommendations = recommend_subscriptions(user_id, pivot_table, user_similarity)
    # Return the recommendations as a JSON response
    response = {'user_id': user_id, 'recommendations': recommendations}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False)
