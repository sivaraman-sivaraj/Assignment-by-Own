import os 
import shutil
import numpy as np 
import scipy as sp
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy import integrate
from symfit import parameters, variables, sin, cos, Fit
################################################
### Result Directory 
path = os.getcwd()+"\\Result" 
try:
    os.mkdir(path) 
except FileExistsError:
    shutil.rmtree(path=path) 
    os.mkdir(path)
################################################
############ sample Data Creation ##############
################################################
### User should define the training data points here 
class Data_Creation(object):
    def __init__(self,name = path):
        self.periodic = 2*np.pi 
        self.custom   = 100 # say it as in time domain
        self.path     = name

    def two_sine_wave(self):
        X  = np.linspace(0,2*np.pi,1000)
        Y0 = np.sin(X)
        Y1 = np.sin(2*np.pi*0.3*X)
        Y2 = np.cos(2*np.pi*1.5*X)
        Y = Y0 + Y1 +Y2
        return X,Y,Y0,Y1,Y2
    
    def Visualize(self,X,Y,Y0,Y1,Y2):
        plt.figure(figsize=(9,6))
        plt.plot(X,Y,color="teal",linewidth=2.0,label="Training Trajectory (Y = Y0 + Y1)") 
        plt.plot(X,Y0,color="crimson",linewidth=2.0,linestyle="--",label="Y0",alpha=0.5) 
        plt.plot(X,Y1,color="navy",linewidth=2.0,linestyle="dashdot",label="Y1",alpha=0.5)
        plt.plot(X,Y2,color="coral",linewidth=2.0,linestyle="dashdot",label="Y2",alpha=0.5)
        plt.legend(loc="best")
        plt.grid()
        plt.xlabel("Time (in seconds)") 
        plt.ylabel("Amplitude")
        plt.title("Training Data") 
        plt.savefig(self.path+"\\Training_Data.jpg",dpi=420)
        plt.show() 

Data          = Data_Creation()
X,Y,y0,y1,y2  = Data.two_sine_wave()
Data.Visualize(X,Y,y0,y1,y2) 
###########################################################
############### Fourier Series Encoding ###################
###########################################################
class Fourier_Series(object):
    def __init__(self, X,Y,Order = 3,name=path,periodic = 2*np.pi):
        self.No_Std_Coeff = 10 
        self.periodic  = periodic
        self.X         = X 
        self.Y         = Y
        self.A0        = []
        self.An        = []
        self.Bn        = [] 
        self.dir       = name
        self.order     = Order 

    def fourier_series(x, f, n=0):
        """
        Returns a symbolic fourier series of order `n`.

        n: Order of the fourier series.
        x: Independent variable
        f: Frequency of the fourier series
        """
        # Make the parameter objects for all the terms
        a0, *cos_a = parameters(','.join(['a{}'.format(i) for i in range(0, n + 1)]))
        sin_b = parameters(','.join(['b{}'.format(i) for i in range(1, n + 1)]))
        # Construct the series
        series = a0 + sum(ai * cos(i * f * x) + bi * sin(i * f * x)
                        for i, (ai, bi) in enumerate(zip(cos_a, sin_b), start=1))
        return series
    
    def show_fourier_series(self,n):
        """ Fourier series will be returned in the form of dictionary"""
        x, y       = variables('x, y')
        w,         = parameters('w')
        f          = w
        # Make the parameter objects for all the terms
        a0, *cos_a = parameters(','.join(['a{}'.format(i) for i in range(0, n + 1)]))
        sin_b      = parameters(','.join(['b{}'.format(i) for i in range(1, n + 1)]))
        # Construct the series
        series = a0 + sum(ai * cos(i *f* x) + bi * sin(i *f* x)
                        for i, (ai, bi) in enumerate(zip(cos_a, sin_b), start=1))
        
        model_dict = {y: series} 
        print("The Fourier Series Equation",model_dict) 
        return model_dict 
    
    def Fit_the_model(self):
        """ Based on the training data, It will fit the curve by symfit function for Fourier Coefficients"""
        x, y             = variables('x, y')
        model_dict       = self.show_fourier_series(self.order)
        fit              = Fit(model_dict, x=self.X, y=self.Y) 
        fit_result       = fit.execute() 
        # print(fit_result) 
        self.Y_pred      = fit.model(x=self.X, **fit_result.params).y
        Model_parameters = fit_result.params
        #######################################
        ### saving the coefficients 
        Model_Coeffs_Names  = [ele for ele in Model_parameters.keys()]
        Model_Coeffs_values = [ele for ele in Model_parameters.values()]
        Coeff_dict          = dict()
        for i in range(len(Model_Coeffs_Names)):
            Coeff_dict[Model_Coeffs_Names[i]] = [Model_Coeffs_values[i]]
        Coeff_dict_pd       = pd.DataFrame.from_dict(Coeff_dict)
        Coeff_dict_pd.to_csv(self.dir+"\\Model_Coefficients.csv", index=False)
        return self.Y_pred
    
    def Values_Custom_Range(self,X_custom):
        """ Feed your custom time span here"""
        x, y             = variables('x, y')
        model_dict       = self.show_fourier_series(self.order)
        fit              = Fit(model_dict, x=self.X, y=self.Y) 
        fit_result       = fit.execute() 
        # print(fit_result) 
        self.Y_pred      = fit.model(x=X_custom, **fit_result.params).y 
        return self.Y_pred


##################################################
################## Execution #####################
##################################################
FS = Fourier_Series(X,Y,Order=12)
Y_pred = FS.Fit_the_model() 

plt.figure(figsize=(9,6))
plt.plot(X,Y_pred,color="teal",linewidth=2.0,label="Predicted") 
plt.plot(X,Y,color="coral",linestyle="--",linewidth=2.0,label="Actual")
plt.title("Fourier Series Result Comparison") 
plt.xlabel("Periodic time span (one cycle)")
plt.ylabel("Amplitude")
plt.axhline(y=0,color="k")
plt.axvline(x=0,color="k")
plt.axvline(x=X[-1],color="k")
plt.legend(loc="best")
plt.grid()
plt.savefig(path+"\\Result_Comparison.jpg",dpi=420)
plt.show() 

SS = np.linspace(0,4*np.pi,2000) 
YY = FS.Values_Custom_Range(SS)

plt.plot(YY)
plt.show()
##################################################
##################################################