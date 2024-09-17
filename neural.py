import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score

# Load the dataset
data = pd.read_csv('/Users/patron/Desktop/UM DSAI/Project/09-CodeSecondPhase/target/classes/com/example/umproject/MergedDataSet.csv')

# Preprocessing
encoder = OneHotEncoder(sparse_output=False)
categorical_features = data[['Suruna Value', 'Hurni Level', 'Volta']]
categorical_encoded = encoder.fit_transform(categorical_features)
numerical_features = data[['Lal Count', 'Ratios']].apply(pd.to_numeric, errors='coerce')
X = np.hstack((categorical_encoded, numerical_features))

# Identify the target column (first column with 'NG' values)
ng_columns = [col for col in data.columns if data[col].apply(lambda x: isinstance(x, str) and 'NG' in x).any() and not data[col].eq('NG').all()]

for target_column in ng_columns:
    y = pd.to_numeric(data[target_column].replace('NG', np.nan), errors='coerce')

    # Splitting data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train_filtered = X_train[~y_train.isna()]
    y_train_filtered = y_train[~y_train.isna()]
    X_test_filtered = X_test[~y_test.isna()]
    y_test_filtered = y_test[~y_test.isna()]

    # Standardize numerical features
    scaler = StandardScaler()
    X_train_filtered[:, -2:] = scaler.fit_transform(X_train_filtered[:, -2:])
    X_test_filtered[:, -2:] = scaler.transform(X_test_filtered[:, -2:])

    # Build the neural network model
    model = keras.Sequential([
        keras.layers.Dense(128, activation='relu', input_dim=X_train_filtered.shape[1]),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(1)  # Output layer with 1 neuron for regression
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_squared_error'])

    # Train the model
    model.fit(X_train_filtered, y_train_filtered, epochs=100, batch_size=32, verbose=0)

    # Evaluate the model on the test set
    y_pred_filtered = model.predict(X_test_filtered)
    mse_filtered = mean_squared_error(y_test_filtered, y_pred_filtered)
    r2_score_filtered = r2_score(y_test_filtered, y_pred_filtered)

    # Calculate accuracy scores using cross-validation
    scores = cross_val_score(model, X_train_filtered, y_train_filtered, cv=5, scoring='neg_mean_squared_error')
    mse_cv = -scores.mean()

    # Print the evaluation metrics
    print(f"Column: {target_column}")
    print(f"Mean Squared Error on Test Set: {mse_filtered:.2f}")
    print(f"R-squared on Test Set: {r2_score_filtered:.2f}")
    print(f"Mean Squared Error (Cross-validation): {mse_cv:.2f}")

    # Optionally, save the trained model
    model.save(f'/Users/patron/Desktop/decision tree/model_{target_column}.h5')

# Output the original and predicted columns
for target_column in ng_columns:
    print(data[[target_column, 'Predicted_' + target_column]])