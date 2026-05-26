import numpy as np
class Linear_Regression():
    #initiating the parameters(learning rate and no.of iterations)
    def __init__(self,learning_rate,no_of_iterations):
        self.learning_rate=learning_rate
        self.no_of_iterations=no_of_iterations
    def fit(self,x,y):
        #m=no.of datapoints, n=no.of features
        self.m,self.n= x.shape
        #initiating the weight and bias of the model
        self.w=np.zeros(self.n)
        self.b=0
        self.x=x
        self.y=y
        #implementing gradient descent
        for i in range(self.no_of_iterations):
            self.update_weights()
    def update_weights(self):
        y_prediction=self.predict(self.x)
        #calculate the gradient
        dw=-(2*(self.x.T).dot(self.y-y_prediction))/self.m
        db=-2*np.sum(self.y-y_prediction)/self.m
        #based on the dw and db, we update the weights and bias
        self.w=self.w-self.learning_rate*dw
        self.b=self.b-self.learning_rate*db
        y_prediction=self.predict(self.x)
    def predict(self,x):
        #when we give the X value.i.e, the experience value, the model predicts the corresponding salary value based the current learning
        return x.dot(self.w)+self.b
    