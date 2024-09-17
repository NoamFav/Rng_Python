from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt
from sklearn import tree
import pandas as pd
from typing import Union
import numpy as np



def preprocess_features(dataframe):
    processed_df = dataframe.copy()

    # Replace 'nulp' with NaN or appropriate numeric value
    processed_df.replace('nulp', np.nan, inplace=True)

    # Handle NaN values (either fill them or drop them)
    # Example: processed_df.fillna(method='ffill', inplace=True)

    # Identify and transform categorical columns
    categorical_cols = processed_df.select_dtypes(include=['object']).columns

    for col in categorical_cols:
        if len(processed_df[col].unique()) <= 2:
            le = LabelEncoder()
            processed_df[col] = le.fit_transform(processed_df[col])
        else:
            processed_df = pd.get_dummies(processed_df, columns=[col], prefix=[col])
    
    return processed_df

def load_and_preprocess_data(info_file_path: str, grades_file_path: str) -> pd.DataFrame:
    student_info_df = pd.read_csv(info_file_path)
    current_grades_df = pd.read_csv(grades_file_path)
    current_grades_df.reset_index(inplace=True)
    current_grades_df.rename(columns={'index': 'StudentNumber'}, inplace=True)
    for col in current_grades_df.columns:
        if col != 'StudentNumber':
            current_grades_df[col] = pd.to_numeric(current_grades_df[col], errors='coerce')
    merged_df = pd.merge(student_info_df, current_grades_df, on='StudentNumber', how='inner')
    return merged_df

# Analyze Score Difference by Property
def analyze_score_difference_by_property(course: str, property: str, dataframe: pd.DataFrame) -> Union[pd.DataFrame, str]:
    if course not in dataframe.columns or property not in dataframe.columns:
        return "Invalid course or property specified."
    grouped = dataframe.groupby(property)[course].agg(['mean', 'std']).reset_index()
    grouped.columns = [property, f'{course}_mean', f'{course}_std']
    return grouped

# Analyze Score Difference by Previous Course
def analyze_score_difference_by_previous_course(course1: str, course2: str, dataframe: pd.DataFrame) -> Union[pd.DataFrame, str]:
    if course1 not in dataframe.columns or course2 not in dataframe.columns:
        return "Invalid courses specified."
    grouped = dataframe.groupby(course1)[course2].agg(['mean', 'std']).reset_index()
    grouped.columns = [f'{course1}_score', f'{course2}_mean', f'{course2}_std']
    return grouped

# Find Best Property for Course
def find_best_property_for_course(course: str, dataframe: pd.DataFrame) -> Union[str, dict]:
    if course not in dataframe.columns:
        return "Invalid course specified."
    properties = dataframe.columns.difference(dataframe.columns[5:]).difference(['StudentNumber'])
    best_property = None
    max_variance_reduction = 0
    subgroup_stats = None
    for prop in properties:
        grouped = dataframe.groupby(prop)[course].agg(['mean', 'var', 'count']).reset_index()
        total_count = grouped['count'].sum()
        weighted_variance = (grouped['var'] * grouped['count'] / total_count).sum()
        overall_variance = dataframe[course].var()
        variance_reduction = overall_variance - weighted_variance
        if variance_reduction > max_variance_reduction:
            best_property = prop
            max_variance_reduction = variance_reduction
            subgroup_stats = grouped
    return {
        'best_property': best_property,
        'variance_reduction': max_variance_reduction,
        'subgroup_statistics': subgroup_stats
    }

# Predict Student Performance
def predict_student_performance(student_properties: dict, course: str, dataframe: pd.DataFrame) -> Union[str, float]:
    best_property_info = find_best_property_for_course(course, dataframe)
    best_property = best_property_info['best_property']
    subgroup_stats = best_property_info['subgroup_statistics']
    student_property_value = student_properties.get(best_property)
    if student_property_value is None:
        return f"Missing value for property {best_property}."
    predicted_score = subgroup_stats.loc[subgroup_stats[best_property] == student_property_value, 'mean'].values
    if len(predicted_score) == 0:
        return dataframe[course].mean()
    return predicted_score[0]

def analyze_all_courses(dataframe: pd.DataFrame):
    # Iterate over all courses in the dataframe (excluding non-course columns)
    for course in dataframe.columns[5:]:
        print(f"Analysis for Course: {course}")
        
        # Find best property for the course
        best_property_info = find_best_property_for_course(course, dataframe)
        best_property = best_property_info['best_property']
        variance_reduction = best_property_info['variance_reduction']
        subgroup_stats = best_property_info['subgroup_statistics']
        
        print(f"Best Property: {best_property}")
        print(f"Variance Reduction: {variance_reduction}")
        print("Subgroup Statistics:")
        print(subgroup_stats)
        print("\n" + "="*50 + "\n")

def impute_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    imputed_data = data.copy()

    # Iterate over rows and columns
    for idx, row in imputed_data.iterrows():
        for col in imputed_data.columns:
            # Check if the value is missing (you might need to adjust this check)
            if pd.isnull(row[col]):
                # Use other columns as student properties (excluding the current column with missing value)
                student_properties = row.drop(col).to_dict()
                # Predict missing value and replace it
                predicted_value = predict_student_performance(student_properties, col, imputed_data)
                # Handle the case where predicted_value is a string error message
                if not isinstance(predicted_value, str):
                    imputed_data.at[idx, col] = predicted_value
    return imputed_data


if __name__ == "__main__":
    # Load and preprocess data
    info_file_path = '/Users/patron/Desktop/UM DSAI/Project/09-CodeSecondPhase/src/main/resources/com/example/umproject/StudentInfo.csv'
    grades_file_path = '/Users/patron/Desktop/UM DSAI/Project/09-CodeSecondPhase/src/main/resources/com/example/umproject/CurrentGrades.csv'
    data = load_and_preprocess_data(info_file_path, grades_file_path)
    
    # Impute missing values
    completed_data = impute_missing_values(data)

    # Additional preprocessing
    processed_data = preprocess_features(completed_data)

    # Select features and target for the decision tree model
    # Assuming the target variable is named 'Target' and is the last column
    X = completed_data.iloc[:, :-1]  # Features
    y = completed_data.iloc[:, -1]   # Target

    # Split the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the decision tree model
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    # Predict and evaluate the model
    y_pred = clf.predict(X_test)
    print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
    print(classification_report(y_test, y_pred))

    # Plot the decision tree
    plt.figure(figsize=(20, 10))
    tree.plot_tree(clf, filled=True)
    plt.show()