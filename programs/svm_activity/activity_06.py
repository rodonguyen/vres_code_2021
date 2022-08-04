import pandas
import numpy
import sklearn
import sklearn.model_selection
import sklearn.svm

def function_start():
    print('---')

def function_end():
    print('---')

############################################
function_start()
RANDOM_STATE = 10
KERNEL = 'rbf'
GAMMA = 0.1
MAX_ITER = -1


df = pandas.read_csv('data/activity/pa_1000000.csv')
# Transform strings to integers
label_encoder = sklearn.preprocessing.LabelEncoder()
label_encoder.fit(df.loc[:,'User'])
df.loc[:,'User'] = label_encoder.transform(df.loc[:,'User'])
label_encoder = sklearn.preprocessing.LabelEncoder()
label_encoder.fit(df.loc[:,'Model'])
df.loc[:,'Model'] = label_encoder.transform(df.loc[:,'Model'])
label_encoder = sklearn.preprocessing.LabelEncoder()
label_encoder.fit(df.loc[:,'Device'])
df.loc[:,'Device'] = label_encoder.transform(df.loc[:,'Device'])
label_encoder = sklearn.preprocessing.LabelEncoder()
label_encoder.fit(df.loc[:,'gt'])
df.loc[:,'gt'] = label_encoder.transform(df.loc[:,'gt'])

# Split data
X = df.drop(columns=['Index','Arrival_Time','Creation_Time', 'gt'], axis=1)
Y = df['gt']
X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(
                                    X, Y, test_size=0.4, random_state=RANDOM_STATE)

# Standardise
# mu = numpy.mean(X_train.loc[:,'x':'z'], axis=1)
# sigma = numpy.std(X_train.loc[:,'x':'z'])
# X_train.loc[:,'x':'z'] = (X_train.loc[:,'x':'z'] - mu) / sigma
# X_test.loc[:,'x':'z'] = (X_test.loc[:,'x':'z'] - mu) / sigma

# Train
X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(
                                    X, Y, test_size=0.2, random_state=RANDOM_STATE)
svm = sklearn.svm.SVC(C=1, gamma=GAMMA, kernel=KERNEL,  max_iter=MAX_ITER)
svm.fit(X_train, Y_train)


# Evaluate
pred = svm.predict(X_test)
print('Test Set Performance: ' + str(sum(pred == Y_test)/len(Y_test)))


function_end()
############################################