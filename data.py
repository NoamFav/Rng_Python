from sklearn.model_selection import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree


file_path = '/Users/patron/Book2.csv'
data = pd.read_csv(file_path, delimiter=';')

for col in ['mass', 'width', 'height', 'color_score']:
    data[col] = data[col].astype(str).str.replace(',', '.').astype(float)

X = data[['mass', 'width', 'height', 'color_score']]
y = data['fruit_subtype']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
scores = cross_val_score(clf, X, y, cv=5)

y_pred = clf.predict(X_test)

print(classification_report(y_test, y_pred))
print(f"Accuracy: {scores.mean():.2f} (+/- {scores.std() * 2:.2f})")


plt.figure(figsize=(10,10))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=clf.classes_, rounded=True)
plt.show()
