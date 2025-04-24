import joblib
from google.colab import files

# Save the model and scaler to disk
joblib.dump(model, "model/logistic_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")