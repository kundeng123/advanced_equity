from math import *
from scipy.stats import norm


def price_european_option_call(r,T,vol,ForwardPrice, strike):
    volSqrtT = vol * sqrt(T)
    #print(volSqrtT)
    #volSqrtT = 0.153271649
    logMoneyness = log(ForwardPrice/strike)
    #d1 = ln(F/K) + 0.5 * vol^2 * T
    d1 = (logMoneyness + 0.5 * vol * vol * T)/volSqrtT
    d2 = d1 - volSqrtT
    #print(d2)
    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)

    #print ( Nd1)
    #print(Nd2)
    return exp(-r * T) * (ForwardPrice * Nd1 - strike * Nd2)

def price_european_option_put(r,T,vol,ForwardPrice, strike):
    volSqrtT = vol * sqrt(T)
    #print(volSqrtT)
    #volSqrtT = 0.153271649
    logMoneyness = log(ForwardPrice/strike)
    #d1 = ln(F/K) + 0.5 * vol^2 * T
    d1 = (logMoneyness + 0.5 * vol * vol * T)/volSqrtT
    d2 = d1 - volSqrtT
    #print(d2)
    Nd1 = norm.cdf(-d1)
    Nd2 = norm.cdf(-d2)

    #print ( Nd1)
    #print(Nd2)
    return exp(-r * T) * (-ForwardPrice * Nd1 + strike * Nd2)


print("euro call ", price_european_option_call(0,0.54247,0.2081017,1931.32,1950))
print("euro put ", price_european_option_put(0,0.54247,0.2550,1931.32,1750))