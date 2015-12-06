"""
        SPAM FILTER USING NAIVE BAYES AND SVM ANALYSIS
"""

from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
import numpy as np

class parser(object):
    
    s = {}
    def __init__(self,path,total_mails):
        self.total_mails = total_mails
        self.labels_train=[]
        self.features_train = []
        self.path =  path
        self.dataset = open("train.txt","r")
       
        for i in range(0,self.total_mails):
            mail = self.dataset.readline().split()
            for i in range(2,len(mail)):
                self.s[mail[i]] = 1
                
    def resetMail(self):
        for key in self.s:
            self.s[key] = 0
            
    def generateList(self):
        result  = []
        for key in self.s:
            result.append(self.s[key])
        return result 
 
    def update_tables(self):
        self.dataset.close()
        self.dataset = open(self.path,"r")
        for i in range(self.total_mails):
            mail = self.dataset.readline().split()
            self.resetMail()
            j = 1
            while j<len(mail):
                if(j==1):
                    if(mail[j]=='spam'):
                        self.labels_train.append(1)
                    else:
                        self.labels_train.append(0)
                else:
                    self.s[mail[j]] = int(mail[j+1])
                    j = j + 1
                j = j  + 1
            self.features_train.append(self.generateList())
        self.dataset.close()
        
        

           
train = parser("train.txt",8000)
train.update_tables()

clf = GaussianNB()
clf.fit(np.array(train.features_train),np.array(train.labels_train))

test = parser("test.txt",1000)
test.update_tables()


predictions = []
results = []
for i in range(700):
    predictions.append(clf.predict(np.array(test.features_train[i])))
    results.append(train.labels_train[i])
    
    
accuracy = accuracy_score(results,predictions,True)
print accuracy*100





