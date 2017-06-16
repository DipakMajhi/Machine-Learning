from sklearn import datasets, metrics
from sklearn.linear_model import LinearRegression

housing_data = datasets.load_boston()

clf = LinearRegression()

X_train = clf.fit(housing_data.data, housing_data.target)
predictions = clf.predict(housing_data.data)

score = metrics.r2_score(housing_data.target, predictions)

print(score)
