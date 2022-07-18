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


RANDOM_STATE = 40
N_NEIGHBORS = 10
WEIGHTS = 'uniform'

redwine_binary = pandas.read_csv('data/classification/redwine-multiclass.csv')
X = redwine_binary.drop('quality', axis=1)
Y = redwine_binary['quality']
X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.4) #, random_state=RANDOM_STATE)
mu = numpy.mean(X_train)
sigma = numpy.std(X_train)
X_train = (X_train - mu) / sigma
X_test = (X_test - mu) / sigma

X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(
                                    X, Y, test_size=0.4, random_state=RANDOM_STATE)
cknn = sklearn.neighbors.KNeighborsClassifier(n_neighbors=N_NEIGHBORS, weights=WEIGHTS)
cknn.fit(X_train, Y_train)


def eval_model(model, X_test, Y_test):
    pred = model.predict(X_test)
    print('Test Set Performance: ' + str(sum(pred == Y_test)/len(Y_test)))
eval_model(cknn, X_test, Y_test)


function_end()
############################################
