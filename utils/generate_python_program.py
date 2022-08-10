
from tabnanny import filename_only


def generate():
    for num in row_num:
        filename = f"{filename_head}_{num:08d}.py"
        dataset_filename = f"{filename_head}_{num}.csv"
        full_path = destination_dir + filename
        f = open(full_path, "w") 
        f.write(
"""
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

df = pandas.read_csv('data/activity/%s')

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
""" % (dataset_filename))
        f.close()


destination_dir = "programs/activity/v2_nb/code_pg_1col/"
filename_head = "pg_1col"
row_num = [10,20,50,75,100,250,500,750,1000,2500,5000,7500,
            10_000,25_000,50_000,75_000,100_000,250_000,500_000,750_000,
            1000_000,1250_000,1500_000,1750_000,2000_000]
generate()
