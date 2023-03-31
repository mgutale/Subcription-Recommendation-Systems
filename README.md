# Subscription Recommendation System

This code implements a recommendation system that recommends subscription types to users based on their NPS scores and the NPS scores of similar users. It uses a pivot table and cosine similarity to calculate user similarity and generate recommendations.

## Use Case
This recommendation system can be applied to a variety of business problems, such as:

Recommending new subscription types to existing customers to increase their satisfaction and loyalty
Identifying customers who are at risk of churning and recommending subscription types that may increase their likelihood of staying
Personalising the subscription types offered to new customers based on their characteristics and preferences

## Dependencies
    Python 3.x
    Flask
    pandas
    scikit-learn

## How to Use
1. Clone the repository or download the code files.
2. Install the dependencies using the command above.
3. Place your data in a CSV file named data.csv and put it in a subdirectory named dataset. The CSV file should have the following columns:
    Member ID: The unique identifier for each user
    Subscription Type: The subscription type that the user has subscribed to
    NPS Score: The NPS score for the user's subscription
4. Run the Flask app by executing the following command in your terminal:
    python app.py
5. Send a POST request to the /recommend endpoint with the following JSON payload:
    {
    "user_id": <user_id>
    }
where <user_id> is the ID of the user for whom you want to generate recommendations.
6. The app will return a JSON response with the following structure:
    {
    "user_id": <user_id>,
    "recommendations": [
        {
            "subscription_type": <subscription_type>,
            "nps_score": <nps_score>
        },
        ...
    ]
}
where each object in the recommendations array represents a recommended subscription type and its corresponding NPS score. The recommendations are sorted in descending order of NPS score.

## How to Interpret the Result
The recommendations are sorted in descending order of NPS score, so the first recommendation in the list is the one with the highest NPS score. The NPS score indicates how likely the user is to recommend the subscription type to others, so a higher NPS score indicates higher satisfaction and loyalty. The user can be recommended multiple subscription types, depending on how many similar users have subscribed to those types and how high their NPS scores are.


## How to use it
1. Clone the repository
2. Install the required dependencies: pip install flask pandas scikit-learn
3. Prepare your dataset in CSV format with the following columns:
    user_id: unique identifier for each user
    product_id: unique identifier for each product
    rating: the user's rating for the product (typically on a scale of 1-5)
4. Train the model by running the train.py script with the following arguments:
    -d or --data: path to your CSV dataset
    -m or --model: path to save the trained model
    -n or --num_recommendations: number of recommendations to generate per user (default is 10)

    Example usage: python main.py -d data.csv -m model.pkl -n 5

5. Run the Flask server by running the server.py script.
6. Send a POST request to the server endpoint http://localhost:5000/recommend with a JSON payload containing the user_id for which you  want to generate recommendations:
    import requests

    response = requests.post('http://localhost:5000/recommend', json={'user_id': 123})
    print(response.json())

This will return a JSON response containing a list of recommended products and their corresponding scores/ratings.

## Interpreting the result
The recommendation system generates a list of recommended products and their corresponding scores/ratings. The list is sorted in descending order based on the scores, so the first item in the list is the highest-rated recommended product. The score/rating represents the system's confidence in the recommendation and can be interpreted as a probability or confidence level. A higher score/rating indicates a more confident recommendation.