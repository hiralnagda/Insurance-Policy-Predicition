
# Feature Extraction with RFE
import pandas
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
# load data
url = "finaldataagent1.csv"
names = ['no_of_kids','Maratial_Status','Gender','education','income_tax_payer','Income','smoking_alcohol','weight','Height','Preexisting Disease','Regularity','Age','Term','Total sum assured','total_premium','Plan']
dataframe = pandas.read_csv(url, names=names)
array = dataframe.values
X = array[:,0:15]
Y = array[:,15]
model = LogisticRegression()
rfe = RFE(model,10)#10 is no of features
fit = rfe.fit(X, Y)
print(names)
print( fit.n_features_)
c=0
for i in fit.ranking_:
    if i==1:
        print(names[c])
    c=c+1

print (fit.support_) #mask
print( fit.ranking_)
