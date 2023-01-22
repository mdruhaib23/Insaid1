# feature importances
importances = clf.feature_importances_

# sort feature importances
sorted_index = np.argsort(importances)[::-1]

# display feature importances
for i in sorted_index:
    print(f"{data.columns[i]}: {importances[i]}")
