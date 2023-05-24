#First we import all relevant libraries
import pandas as pd
import os
#We want to find our current working directory so that we can help our computer to find the downloaded data sets
print(os.getcwd())

#Now we want to merger the advanced and game stats for every season together
#We use a for loop to be able to do the merging for every season
#Then we save the 42 data sets
for year in range(1,43):
    df_game=pd.read_csv("data/PGD_"+str(year)+".csv",sep=";")
    df_advanced=pd.read_csv("data/AD_"+str(year)+".csv",sep=";",skiprows=1)
    df_merge=pd.merge(df_game,df_advanced,how="outer",on="Team")
    df_merge.to_csv("data/sports_"+str(year)+".csv", index=False)

#We read the first merged data set
df=pd.read_csv("data/sports_1.csv")
print(df.head())

#Now we append all other 41 datasets to the first using a for loop
for year in range(2,43):
    df_2=pd.read_csv("data/sports_"+str(year)+".csv")
    df=df.append(df_2)

#We save the final data set as data_uncleaned
df.to_csv("data_uncleaned.csv", index=False)
