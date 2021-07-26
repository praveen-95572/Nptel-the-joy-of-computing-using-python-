import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')

file='data_file.xlsx'
xl=pd.ExcelFile(file)  #Read from excel(pandas lib feat.)
dfs=xl.parse(xl.sheet_names[0])    #parsing the excel sheet to data frame
dfs=list[dfs['Timeline']]          # removes the blank row from data frame
print(dfs)
sid=SentimentIntensityAnalyzer()
str1="UTC+05:30"              #if date find then skips that info.

for data in dfs:
     a=data.find(str1)
     if a==-1:
          ss=sid.polarity_scores(data)
          print(data)
          for k in ss:
               print(k,ss[k])
