# Import the necessary module
import joblib 

# Load the pre-trained model
model = joblib.load('penguin_classifier.pkl')

# Print the type of the loaded model
print(f"Loaded model type: {type(model)}")