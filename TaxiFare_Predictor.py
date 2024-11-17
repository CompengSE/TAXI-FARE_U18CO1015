import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib

# load the dataset
TFare = pd.read_csv('NYCTFares.csv')

# split the dataset into features and target variables
x = TFare[["pickup_longitude", "pickup_latitude", "dropoff_longitude", "dropoff_latitude", "passenger_count"]]
y = TFare["fare_amount"]

# split the data into train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# data preparation
standardize = StandardScaler()
x_train_std = standardize.fit_transform(x_train)
x_test_std = standardize.transform(x_test)

# Ridge regression
ridge_regul = Ridge(alpha=0.1)
ridge_regul.fit(x_train_std, y_train)
predict_ridge = ridge_regul.predict(x_test_std)
mse_ridge = mean_squared_error(predict_ridge, y_test)
r2_ridge = r2_score(y_test, predict_ridge)

# Random Forest Regression
random = RandomForestRegressor(n_estimators=100)
random.fit(x_train_std, y_train)
rand_predict = random.predict(x_test_std)
mse_rand = mean_squared_error(rand_predict, y_test)
r2_rand = r2_score(y_test, rand_predict)

#Save the trained model
joblib.dump(random, 'random_forest_model.pkl')

print("Model saved as 'random_forest_model.pkl'")