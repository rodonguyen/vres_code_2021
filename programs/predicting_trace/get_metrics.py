from sklearn.metrics import mean_squared_error
import math

def RMSE(pred, actual):
  MSE = mean_squared_error(actual, pred)
  RMSE = math.sqrt(MSE)
  return RMSE
