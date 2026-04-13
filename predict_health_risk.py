import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

## load data set
df = pd.read_excel('DQN1 Dataset.xlsx', sheet_name='Data')

##Input features array
feature_columns = [
'pm2.5', 'no2', 'co2', 'humidity', 'temp', 'pressure', 'windgust', 'visibility', 'uvindex'
]
target_column = 'healthRiskScore'

x = df[feature_columns]
y = df[target_column]

## handle NULL values
x = x.fillna(x.mean())

##training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    x,y,test_size=0.2, random_state=42
)

##Train Forest Regressor
model= RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

## Test set predictions
y_pred = model.predict(x_test)

##evaluation
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"R-squared (R^2): {r2:.4f}")