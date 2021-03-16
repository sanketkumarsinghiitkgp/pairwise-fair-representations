# -*- coding: utf-8 -*-
"""
Created on Apr 20 22:50:11 2020

@author: Harshvardhan
"""

import numpy as np
import numpy.linalg as linalg


class optimizer:
    def __init__(self, D, Wx, Wf, gamma = 1.0 , x_input , protected_index):
        """
        Initializes the model.
        :param D:       Hyperparameter representing the number of final dimensions.
        :param Wx:     The adjacency matrix of k-nearest neighbour graph over input space X
        :param Wf:     The adjacency matrix of the pairwise fairness graph G associated to the problem.
        :param gamma:   Hyperparam controlling the influence of Wf.
        :param protected_index : s according to the paper
        """
        self.D = D
        self.Wf = Wf
        self.Wx = Wx
        self.gamma = gamma
        self.pidx = protected_index
        
    
    def formlaplacian(self,mat):
        csum = np.sum(mat,axis=0,dtype=float)
        d = np.diag(csum)
        return d-mat
    
    def create_z(self):
        
        Lx=formlaplacian(self.Wx)        
        Lf=formlaplacian(self.Wf)
        gamma = self.gamma
        L=gamma*Lf+(1-gamma)*Lx
        
        xt=np.transpose(self.x)
        mat=np.dot(xt,np.dot(L,x))
        
        eigenValues, eigenVectors = linalg.eig(mat)
        eigenValues = np.real(eigenValues)
        top_eigen_indices = np.argpartition(eigenValues, self.D)[:self.D]

        V=eigenVectors[0:,top_eigen_indices]
        z=np.dot(V.transpose(),xt)
        z = np.transpose(z)
        z = np.append(z,np.resize(x[:][self.pidx],(x.shape[0],1)),axis=1)
        return z

    