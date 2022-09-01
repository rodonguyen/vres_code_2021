

def generate(program_content):
    for col_num in col_nums:
        for row_num in row_nums:
            filename = f"{filename_head}_{col_num}col_{row_num:08d}.py"
            dataset_filename = f"{filename_head}_{col_num}col_{row_num}.csv"
            full_path = destination_dir + filename
            f = open(full_path, "w") 
            f.write(program_content % (dataset_filename))
        f.close()


destination_dir = "programs/weather/code_test/"
filename_head = 'w_Float2DigitsTemp' # w_IntegerX100Temp # w_Float2DigitsTemp
# row_nums = [10,20,50,75,100,250,500,750,1000,2500,5000,7500,
#             10_000,25_000,50_000,75_000,100_000,250_000,500_000,750_000,
#             1000_000,1250_000,1500_000,1750_000,2000_000]
row_nums = [i*(10**power) for power in range(1, 5) 
                for i in range(1, 10)] + [100_000]
# row_nums = (1234,2300,15151,22000,43000,48000,74000,82820,94444)
col_nums = (2,)


program_activity_content = \
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
"""
program_weather_content = \
"""
import pandas
import sklearn
import sklearn.model_selection
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

def function_start():
    print('---')

def function_end():
    print('---')

############################################
function_start()
RANDOM_STATE = 10

df = pandas.read_csv('data/weather/%s')

# Split data
X = df.iloc[:,:-1]
Y = df.iloc[:,-1]

# Train
X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(
                                    X, Y, test_size=0.2, random_state=RANDOM_STATE)
regression = linear_model.LinearRegression()
regression.fit(X_train, Y_train)

# Evaluate
pred = regression.predict(X_test)
print('Test Set RMSE: ' + str(mean_squared_error(Y_test, pred)))

function_end()
############################################
"""

generate(program_weather_content)
