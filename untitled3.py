from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import numpy as np

class data_loader(object):
    def __init__(self,path):
        self.features = []
        self.labels = []
        
        file = open(path,"r")  
        samples = 958 
    
        
        for j in range(samples):
            state = file.readline().split(',')
            #print state
            temp = []
            for i in state:
                if(i=='x'):
                    temp.append(2)
                elif(i=='o'):
                    temp.append(1)
                elif(i=='b'):
                    temp.append(0)
                else:
                    if(i[0]=='n'):
                        self.labels.append(0)
                    else:
                        self.labels.append(1)
                    break;
            self.features.append(temp)
    def train(self):
        #clf = SVC(kernel = "rbf")
        clf = GaussianNB()
        clf.fit(np.array(self.features),np.array(self.labels))
        return clf
        
class tictactoe(object):
    def __init__(self,clf):
        self.state = [0,0,0,0,0,0,0,0,0]
        self.clf = clf
        
    def next_move(self):
        next_state = []
        for i in range(9):
            if(i==0):
                next_state = self.state
                next_state[i] = 2
                out = self.clf.predict(next_state)
                if(out==1):
                    break
        return next_state
    
    def winner(self):
        
        for i in range(3):
            flag = True
            for j in range(1,3):
                if(self.state[i*3 + j]==self.state[i*3] and self.state[i*3]!=0):
                    continue
                else:
                    flag = False
            if(flag==True):
                return self.state[i*3]
        
        for j in range(3):
            flag = True
            for i in range(1,3):
                if(self.state[i*3 + j]==self.state[i*3] and self.state[i*3]!=0):
                    continue
                else:
                    flag = False
            if(flag==True):
                return self.state[j*3]
        
        if(self.state[0]==self.state[4] and self.state[4]==self.state[8] and self.state[0]!=0):
            return self.state[0]
        if(self.state[2]==self.state[4] and self.state[4]==self.state[6] and self.state[2]!=0):
            return self.state[2]
            
        return 0
        
    def reset(self):
        self.state = [0,0,0,0,0,0,0,0,0]
    
    def print_state(self):
        for i in range(3):
            print ""
            for j in range(3):
                print self.state[i*3+j] + "|"
        
    def play_game(self):
        
        move = 0
        while(True):
            x = self.winner() 
            if(x!=0):
                return x    
            if(move==0):
                self.state = self.next_move()
            else:
                inp = raw_input().split()
                x = int(inp[0])
                y = int(inp[1])
                x = x-1
                y = y-1
                self.state[x*3 + y] = 1 
                
            move = move^1
        print ""
        self.print_state()
                
    
    
"""
    MAIN PROGRAM BEGINS
"""

load_data = data_loader("tictactoe.txt")
clf = load_data.train()

new_game = tictactoe(clf)
new_game.reset()
winner = new_game.play_game()


print "Player " + str(winner) + " is the winner."

     