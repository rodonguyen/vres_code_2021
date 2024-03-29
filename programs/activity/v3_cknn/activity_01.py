import pandas
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
N_NEIGHBORS = 5
WEIGHTS = 'uniform'

df = pandas.read_csv('data/activity/pa_10.csv')
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

# Train
X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(
                                        X, Y, test_size=0.2, random_state=RANDOM_STATE)
cknn = sklearn.neighbors.KNeighborsClassifier(n_neighbors=N_NEIGHBORS, weights=WEIGHTS)
cknn.fit(X_train, Y_train)

# Evaluate
pred = cknn.predict(X_test)
print('Test Set Performance: ' + str(sum(pred == Y_test)/len(Y_test)))


function_end()
############################################