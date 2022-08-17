import pandas as pd
from sklearn import linear_model
import sys
import warnings
warnings.filterwarnings('ignore')

# prediction_row = int(sys.argv[1])

prediction_file = open('count_result/predict_trace_pa.csv', 'w')
prediction_file.write('actual,prediction')

df_original = pd.read_csv('count_result/vpython_trace_activity_pa_withRowColNum.csv')

for prediction_row in range(len(df_original)):
    # Create train data without the row being predicted
    df = df_original.drop(prediction_row, axis=0)
    x = df.iloc[:,:-1]
    y = df.iloc[:,-1]

    # Train a completely new model
    regression = linear_model.LinearRegression()
    regression.fit(x, y)

    # Record prediction
    print('Predicting:', df_original.iloc[prediction_row,:2])
    print(f"{df_original.loc[prediction_row,'pop_in_A']},{int(regression.predict([df_original.iloc[prediction_row,:2]])[0])}\n")
    prediction_file.write(f"\n{df_original.loc[prediction_row,'pop_in_A']},{int(regression.predict([df_original.iloc[prediction_row,:2]])[0])}")

prediction_file.close()