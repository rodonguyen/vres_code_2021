import pandas, numpy
from sklearn import linear_model
import get_metrics

# prediction_row = int(sys.argv[1])

prediction_file = open('count_result/predict_trace_mnist.csv', 'w')
prediction_file.write('actual,prediction')

df_original = pandas.read_csv('data/trace/mnist.csv')

df = df_original.copy()
x = numpy.array(df.loc[:,'images']).reshape(-1,1)
y1 = numpy.array(df.loc[:,'pop'])
y2 = numpy.array(df.loc[:,'shrink'])
y3 = numpy.array(df.loc[:,'grow'])

# Train a completely new model
regression = linear_model.LinearRegression().fit(x, y2)
pred = numpy.round( regression.predict(numpy.array([26, 97, 150, 373, 642, 1234, 4101, 4880]).reshape(-1, 1)) )
actual = pandas.read_csv('count_result/mnist_prediction.csv')['actual_shrink']
print(get_metrics.RMSE(pred, actual))

# print(regression.coef_, regression.intercept_)
# output: [0.00043282] 24877.819753842254
pandas.DataFrame(pred).to_csv('count_result/mnist_prediction_000.csv', index=False)