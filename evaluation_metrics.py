# -*- coding: utf-8 -*-
"""
Created on Apr 22 23:09:11 2020

@author: Harshvardhan
"""

class measures:
    def __init__(self, Wx, Wf, y_truth , y_pred):
        """
        Initializes the evaluation criterias.
        :param Wx:     The adjacency matrix of k-nearest neighbour graph over input space X
        :param Wf:     The adjacency matrix of the pairwise fairness graph G associated to the problem.
        :param y_truth: Truth Labels Array
        :param y_pred: Predictions Array
        """
        self.Wf = Wf
        self.Wx = Wx
        self.y_truth = y_truth
        self.preds = y_pred
        
    
    def consistency(W,Y):
        n = W.shape[0]
        m = W.shape[1]
        denom = np.sum(W)
        outer_sum = 0
        inner_sum = 0
        for i in range(n):
            for j in range(m):
                if i != j:
                    inner_sum+=np.abs(Y[i]-Y[j])*W[i][j]
        outer_sum = 1-inner_sum*1.0/denom
        return outer_sum
    
    # race is 1 for African-American, 0 otherwise
    def positive_prediction_rate(self,race,racearr): 
        cnt = 0
        pos = 0
        for i in range(len(self.preds)):
            if racearr[i]==race:
                cnt+=1
                pos+=self.preds[i]
        return pos*1.0/cnt
    
    def error_rates(self,race,racearr):
        cnt=0
        errors=0
        for i in range(len(self.preds)):
            if racearr[i]==race:
                cnt+=1
                errors+= int(self.preds[i]!= self.y_truth[i])
        return errors*1.0/cnt
    
    
    def fpr(self,race,racearr):
        fp = 0
        tn = 0
        for i in range(len(self.preds)):
            if (racearr[i]==race):
                if(self.preds[i]==self.y_truth[i] and self.preds[i]==0):
                    tn+=1
                elif self.preds[i]!=self.y_truth[i] and self.preds[i]==1:
                    fp+=1
        return fp*1.0/(fp+tn)
    
    def fnr(self,race,racearr):
        fn = 0
        tp = 0
        for i in range(len(self.preds)):
            if (racearr[i]==race):
                if(self.preds[i]==self.y_truth[i] and self.preds[i]==1):
                    tp+=1
                elif self.preds[i]!=self.y_truth[i] and self.preds[i]==0:
                    fn+=1
        return fn*1.0/(fn+tp)
    
