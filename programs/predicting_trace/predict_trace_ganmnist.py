import pandas, numpy
from sklearn import linear_model
import get_metrics

# prediction_row = int(sys.argv[1])

# prediction_file = open('count_result/predict_trace_mnist.csv', 'w')
# prediction_file.write('actual,prediction')


df = pandas.read_csv(f"count_result/gan_mnist/available_ganmnist.csv")
actual_trace = pandas.read_csv(f"count_result/gan_mnist/actual_ganmnist.csv")
prediction = pandas.DataFrame()

row_num = [26, 97, 150, 373, 642, 1234, 4880, 7601, 7899, 11890, 26090, 33333, 53011]

x = numpy.array(df.loc[:,'images']).reshape(-1,1)
y1 = numpy.array(df.loc[:,'pop'])
y2 = numpy.array(df.loc[:,'push'])
y3 = numpy.array(df.loc[:,'shrink'])
y4 = numpy.array(df.loc[:,'grow'])

# Train a completely new model
regression = linear_model.LinearRegression().fit(x, y1)
pred = regression.predict(numpy.array(row_num).reshape(-1, 1)) 
actual = actual_trace['pop']
prediction['pred_pop'] = pred
print(get_metrics.RMSE(pred, actual))

# Train a completely new model
regression = linear_model.LinearRegression().fit(x, y2)
# pred = numpy.round( regression.predict(numpy.array(row_rum).reshape(-1, 1)) )
pred = regression.predict(numpy.array(row_num).reshape(-1, 1)) 
actual = actual_trace['push']
prediction['pred_push'] = pred
print(get_metrics.RMSE(pred, actual))

# Train a completely new model
regression = linear_model.LinearRegression().fit(x, y4)
pred = regression.predict(numpy.array(row_num).reshape(-1, 1)) 
actual = actual_trace['grow']
prediction['pred_grow'] = pred
print(get_metrics.RMSE(pred, actual))

# Train a completely new model
regression = linear_model.LinearRegression().fit(x, y3)
pred = regression.predict(numpy.array(row_num).reshape(-1, 1)) 
actual = actual_trace['shrink']
prediction['pred_shrink'] = pred
print(get_metrics.RMSE(pred, actual))



# print(regression.coef_, regression.intercept_)
# output: [0.00043282] 24877.819753842254
prediction.to_csv(f"count_result/gan_mnist/prediction_ganmnist.csv", index=False)