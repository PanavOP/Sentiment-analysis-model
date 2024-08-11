import pandas as pd 
from textblob import TextBlob as tb
#importing pandas and Textblob libraries

file1 = pd.read_csv('telecom_reviews_dataset.csv')
#importing data set of 200 telecom reviews 

n = len(file1)
#Calculating number of rows in dataset

accuracy = 0
positive = []
negative = []
neutral = []
positivec = 0 
negativec= 0
neutralc = 0
#Classifaction every review 

for i in range(n):
    str = file1.iloc[i,0]
    Review = file1.iloc[i,1]
    #Retrieving original values from our dataset
    
    a = str.split(" ")
    #Tokenization (NLTK is not properly working otherwise we can use work_tokenize function to do the same task)
    
    pol = 0
    for j in a:
        blob = tb(j)
        value = blob.sentiment.polarity
        pol = pol+value
    finalpol = pol/len(a)
    #Calculating average polarity of every word in review 
    
    if finalpol>0:
        our = 'Positive'
        positivec=positivec+1
        positive.append(str)
    elif finalpol<0:
        our = 'Negative'
        negativec=negativec+1
        negative.append(str)
        
    else:
        our = 'Neutral'
        neutralc = neutralc+1
        neutral.append(str)
    #Classification of every review based on the polarity values and inserting them into arrays
    
    if our==Review:
        accuracy=accuracy+1
    #Calculating how much correct review we have compared to original data set
    
accuracy = accuracy/n*100
#Calculating final accuracy of Model 


print("Total Positive Reviews: " , positivec)
print("******************************************************")
print("All positive reviews: ",positive)
print("******************************************************")
print("******************************************************")
print("Total Negative Reviews: " , negativec)
print("******************************************************")
print("All negative reviews",negative)
print("******************************************************")
print("******************************************************")
print("Total Neutral Reviews: " , neutralc)
print("******************************************************")
print("All neutral reviews",neutral)
print("******************************************************")
print("******************************************************")
print("Model Accuracy: " ,accuracy,"%")

#Printing all the final Values