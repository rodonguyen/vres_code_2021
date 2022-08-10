
import pandas
import sklearn
import sklearn.model_selection
from sklearn.naive_bayes import GaussianNB


def function_start():
    print('---')

def function_end():
    print('---')

############################################
function_start()
RANDOM_STATE = 10

df = pandas.read_csv('data/activity/pg_4col_50.csv')

# Split data
X = df.iloc[:,:-1]
Y = df.iloc[:,-1]

# Train
X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(
                                    X, Y, test_size=0.2, random_state=RANDOM_STATE)
gnb = GaussianNB()
gnb.fit(X_train, Y_train)

# Evaluate
pred = gnb.predict(X_test)
print('Test Set Performance: ' + str(sum(pred == Y_test)/len(Y_test)))


function_end()
############################################
