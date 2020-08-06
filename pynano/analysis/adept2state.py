import sys
import math
import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
from lmfit import minimize, Parameters, Parameter, report_errors, Minimizer

def threadList(l1, l2):
    """ thread two lists    """
    try:
        return list(map( lambda x,y : (x,y), l1, l2 ))
    except KeyboardInterrupt:
        raise

def eventEndIndex(dat, mu, sigma):
    try:
        return ([ d for d in dat if d[0] < (mu-2*sigma) ][-1][1]+1)
    except IndexError:
        return -1

def eventStartIndex(dat, mu, sigma):
    try:
        return ([ d for d in dat if d[0] < (mu-2.75*sigma) ][0][1]+1)
    except IndexError:
        return -1

def heaviside(x):
    out=np.array(x)

    out[out==0]=0.5
    out[out<0]=0
    out[out>0]=1
    return out

def stepResponseFunc(t, tau1, tau2, mu1, mu2, a, b):
    try:
        t1=(np.exp((mu1-t)/tau1)-1)*heaviside(t-mu1)
        t2=(1-np.exp((mu2-t)/tau2))*heaviside(t-mu2)

        # Either t1, t2 or both could contain NaN due to fixed precision arithmetic errors.
        # In this case, we can set those values to zero.
        t1[np.isnan(t1)]=0
        t2[np.isnan(t2)]=0

        return a*( t1+t2 ) + b
    except:
        raise


def objfunc(params, t, data):
    try:
        tau1 = params['tau1'].value
        tau2 = params['tau2'].value
        mu1 = params['mu1'].value
        mu2 = params['mu2'].value
        a = params['a'].value
        b = params['b'].value

        model = stepResponseFunc(t, tau1, tau2, mu1, mu2, a, b)

        return model - data
    except KeyboardInterrupt:
        raise



def fit_adept2(data,dt,i0,i0sig,estart,eend):
    fitTol=1e-7
    fitIters=50000
    linkRCConst=True
    varyBlockedCurrent=True
    tauVal=dt
    dataPolarity=float(np.sign(np.mean(data)))
    edat=dataPolarity*np.asarray( data,  dtype='float64' )
    estart  = eventStartIndex( threadList( edat, list(range(0,len(edat))) ), i0, i0sig ) - 1
    eend    = eventEndIndex( threadList( edat, list(range(0,len(edat))) ), i0, i0sig ) - 2
    np.seterr(invalid='ignore', over='ignore', under='ignore')
    blockedCurrent=min(edat)
    ts = np.array([ t*dt for t in range(0,len(edat)) ], dtype='float64')
    params=Parameters()
    params.add('mu1', value=estart * dt)
    params.add('mu2', value=eend * dt)
    params.add('a', value=(i0-blockedCurrent), vary=varyBlockedCurrent)
    params.add('b', value = i0)
    params.add('tau1', value = tauVal)
    if linkRCConst:
        params.add('tau2', value = tauVal, expr='tau1')
    else:
        params.add('tau2', value = tauVal)

    optfit=Minimizer(objfunc, params, fcn_args=(ts,edat,))
    optfit.prepare_fit()
    result=optfit.leastsq(xtol=fitTol,ftol=fitTol,max_nfev=fitIters)
    mdOpenChCurrent     = result.params['b'].value 
    mdBlockedCurrent    = result.params['b'].value - result.params['a'].value
    mdEventStart        = result.params['mu1'].value 
    mdEventEnd          = result.params['mu2'].value
    mdRCConst1          = result.params['tau1'].value
    mdRCConst2          = result.params['tau2'].value
    #mdAbsEventStart     = mdEventStart + self.absDataStartIndex * dt
    #mdBlockDepth        = self.mdBlockedCurrent/self.mdOpenChCurrent
    mdResTime           = mdEventEnd - mdEventStart                  
    #mdRedChiSq          = result.chisqr/( np.var(result.residual) * (len(self.eventData) - result.nvarys -1) )
    tau1 = result.params['tau1'].value
    tau2 = result.params['tau2'].value
    mu1 = result.params['mu1'].value
    mu2 = result.params['mu2'].value
    a = result.params['a'].value
    b = result.params['b'].value
    s2=stepResponseFunc(ts,tau1,tau2,mu1,mu2,a,b)
    return [mdOpenChCurrent,mdBlockedCurrent,mdEventStart,mdEventEnd,mdRCConst1,mdRCConst2,mdResTime],s2


if __name__ == '__main__':
    pass