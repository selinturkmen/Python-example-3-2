
def calc_mean(X):

    mean= sum(X)/len(X)
    return mean 
        

def calc_stdev(X):

    Xdeviation=0
    for y in X:
     y = (y - calc_mean(X))**2
     Xdeviation = Xdeviation + y
    
    Xdeviation = (Xdeviation/ (len(X) -1)) **(1/2)
    return Xdeviation 


def calc_cov(X, Y):

    covariance = 0
    for x in range(len(X)) and range(len(Y)):
        x = (X[x]- calc_mean(X)) * (Y[x]- calc_mean(Y))
        covariance = covariance +x
    covariance = covariance / (len(Y) -1)
        
    return covariance


def calc_pearson(X, Y):

    pearson = calc_cov(X, Y)/ (calc_stdev(X)* calc_stdev(Y))
    
    return pearson 


def main():
    print(calc_pearson([1.5, 3.2, 0.8], [1.9, 4.5, 6.0]))

  
       
    

    
################################################################ 
