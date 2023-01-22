from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix

# split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data.drop("fraud", axis=1), data["fraud"], test_size=0.2, random_state=42)

# train the model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# evaluate the model
y_pred = clf.predict(X_test)
print("Precision: ", precision_score(y_test, y_pred))
print("Recall: ", recall_score(y_test, y_pred))
print("F1 Score: ", f1_score(y_test, y_pred))
print("Confusion Matrix: ", confusion_matrix(y_test, y_pred))
