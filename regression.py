import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import json

def tree_to_json(decision_tree, feature_names=None):
    from sklearn.tree import _tree

    tree_ = decision_tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    def recurse(node, depth):
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            left = recurse(tree_.children_left[node], depth + 1)
            right = recurse(tree_.children_right[node], depth + 1)
            return {"name": name, "threshold": threshold, "left": left, "right": right}
        else:
            return {"value": tree_.value[node].tolist()}

    return recurse(0, 1)

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

    # Building the model
    regressor = DecisionTreeRegressor(random_state=42)
    regressor.fit(X_train_filtered, y_train_filtered)
    
    # Evaluating the model
    y_pred_filtered = regressor.predict(X_test_filtered)
    mse_filtered = mean_squared_error(y_test_filtered, y_pred_filtered)
    r2_score_filtered = r2_score(y_test_filtered, y_pred_filtered)

    # Calculate accuracy scores using cross-validation
    scores = cross_val_score(regressor, X_train_filtered, y_train_filtered, cv=5)

    # Print the evaluation metrics
    print(f"Column: {target_column}")
    print(f"Mean Squared Error: {mse_filtered:.2f}")
    print(f"R-squared: {r2_score_filtered:.2f}")
    print(f"Accuracy: {scores.mean():.2f} (+/- {scores.std() * 2:.2f})")

    # Predicting the entire column with 'NG' values
    data['Predicted_' + target_column] = regressor.predict(X)

    # Convert the trained model to JSON
    tree_json = tree_to_json(regressor, feature_names=encoder.get_feature_names_out().tolist() + ['Lal Count', 'Ratios'])

    # Save the JSON to a file
    with open(f'/Users/patron/Desktop/decision tree/Json/decision_tree_{target_column}.json', 'w') as f: 
        json.dump(tree_json, f, indent=4)

    # Optionally, save each tree as an image
    plt.figure(figsize=(20, 10))
    plot_tree(regressor, filled=True, feature_names=encoder.get_feature_names_out().tolist() + ['Lal Count', 'Ratios'])
    plt.savefig(f'/Users/patron/Desktop/decision tree/decision_tree_{target_column}.pdf', format='pdf', bbox_inches='tight')
    plt.close()

# Output the original and predicted columns
for target_column in ng_columns:
    print(data[[target_column, 'Predicted_' + target_column]])