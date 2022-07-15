import pandas
import numpy
import sklearn
import sklearn.model_selection
import sklearn.neighbors

def function_start():
    print('---')

def function_end():
    print('---')

############################################
function_start()

RANDOM_STATE = 10
N_NEIGHBORS = 10
WEIGHTS = 'uniform'

cancer = pandas.read_csv('data/classification/wdbc.data')
X = cancer.iloc[:, 2:].to_numpy()
cancer.iloc[:, 1] = cancer.iloc[:, 1].astype("category")
Y = cancer.iloc[:, 1].cat.codes.to_numpy()
mu = numpy.mean(X, 0)
sigma = numpy.std(X, 0)
X = (X - mu) / sigma


X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(
                                    X, Y, test_size=0.6, random_state=RANDOM_STATE)
cknn = sklearn.neighbors.KNeighborsClassifier(n_neighbors=N_NEIGHBORS, weights=WEIGHTS)
cknn.fit(X_train, Y_train)

def eval_model(model, X_test, Y_test):
    pred = model.predict(X_test)
    print('Test Set Performance: ' + str(sum(pred == Y_test)/len(Y_test)))

eval_model(cknn, X_test, Y_test)

function_end()
############################################
