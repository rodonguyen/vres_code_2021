import pandas, numpy
from sklearn import linear_model
import sys
import warnings
import get_metrics
warnings.filterwarnings('ignore')

# prediction_row = int(sys.argv[1])

prediction_file = open('count_result/predict_trace_pa.csv', 'w')
prediction_file.write('actual,prediction')

df_original = pandas.read_csv('data/trace/weather.csv')

df = df_original.copy()
x = df.iloc[:,:-1]
y = df.iloc[:,-1]

# Train a completely new model
regression = linear_model.LinearRegression()
regression.fit(x, y)

pred = regression.predict(numpy.array([1234,2300,15151,22000,43000,48000,74000,82820,94444]).reshape(-1, 1))
# pandas.DataFrame(pred).to_csv('count_result/weather_prediction.csv', index=False)

actual = pandas.read_csv('count_result/weather_prediction.csv')['actual']

print(get_metrics.RMSE(pred, actual))

# print(regression.coef_, regression.intercept_)
# output: [0.00043282] 24877.819753842254