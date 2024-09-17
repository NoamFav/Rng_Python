import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from sklearn.tree import export_graphviz
import graphviz

# Load the provided CSV files
current_grades_path = '/Users/patron/Desktop/UM DSAI/Project/09-CodeSecondPhase/src/main/resources/com/example/umproject/CurrentGrades.csv'
bug_free_graduate_grades_path = '/Users/patron/Desktop/UM DSAI/Project/09-CodeSecondPhase/src/main/resources/com/example/umproject/bugFreeGraduateGrades.csv'

current_grades = pd.read_csv(current_grades_path)
bug_free_graduate_grades = pd.read_csv(bug_free_graduate_grades_path)

# Preprocessing the data in CurrentGrades.csv
current_grades.replace('NG', -1, inplace=True)
current_grades.fillna(-1, inplace=True)
current_grades = current_grades.apply(pd.to_numeric)

# Preparing the training data from bugFreeGraduateGrades.csv
X_train = bug_free_graduate_grades.drop('StudentID', axis=1)
y_train = bug_free_graduate_grades.drop('StudentID', axis=1)

# Preparing the data to be predicted from CurrentGrades.csv
X_to_predict = current_grades.drop('StudentID', axis=1)

# Training the Random Forest model
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Predicting the grades
predicted_grades = rf.predict(X_to_predict)

# Replacing -1 in the original dataframe with the predicted values
for i, column in enumerate(current_grades.columns):
    if column != 'StudentID':
        current_grades[column] = np.where(current_grades[column] == -1, predicted_grades[:, i-1], current_grades[column])

# Correcting the inadvertent replacement of 'StudentID'
current_grades['StudentID'] = current_grades.index

# Save the updated dataframe to a new CSV file
updated_grades_path = '/Users/patron/Downloads/UpdatedCurrentGrades.csv'
current_grades.to_csv(updated_grades_path, index=False)

for single_tree in rf.estimators_: 

    # Exporting the decision tree to a dot file
    dot_file = export_graphviz(single_tree, out_file=None, 
                           feature_names=X_train.columns,  
                           filled=True, rounded=True,  
                           special_characters=True)

    # Generating a graph from the dot file
    graph = graphviz.Source(dot_file)
    tree_file_path = f"/Users/patron/Downloads/decision_tree_{i}"  # Replace with the correct path
    graph.format = 'png'
    graph.render(tree_file_path)
