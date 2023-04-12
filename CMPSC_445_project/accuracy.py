import pandas as pd
df=pd.read_csv('testset6.csv')
accuracy=0
for i in range(0,43000):

    if df['chosen_class'].loc[i]!=df['actual_class'].loc[i]:
        #accuracy+=1
        print('Index ' + str(i))
        print(df['total_sales_price'].loc[i])
        print(df['chosen_class'].loc[i])
        print(df['actual_class'].loc[i])

    #print('Accuracy'+str(accuracy/(i+1)))
