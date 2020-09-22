from sklearn import tree
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = ['Orange', 'Orange',  'Apple', 'Apple']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print clf.predict([[145,1]])