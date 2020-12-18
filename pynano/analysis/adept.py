
import sys
import math
import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
from lmfit import minimize, Parameters, Parameter, report_errors, Minimizer

def heaviside(x):
    out=np.array(x)

    out[out==0]=0.5
    out[out<0]=0
    out[out>0]=1
    return out

def multiStateFunc(t, tau, mu, a, b, n):
    try:
        func=b
        for i in range(n):
            t1=(1-np.exp((mu[i]-t)/tau[i]))

            # For long events, t1 could contain NaN due to fixed precision arithmetic errors.
            # In this case, we can set those values to zero.
            t1[np.isnan(t1)]=0
            
            func += a[i]*heaviside(t-mu[i])*t1

        return func
    except:
        raise

def objfunc2(params, t, data, initguess):
    """ model parameters for multistate blockade """
    try:
        nStates=len(initguess)
        b = params['b'].value
        tau = [params['tau'+str(i)].value for i in range(nStates)]
        a=[params['a'+str(i)].value for i in range(nStates)]
        mu=[params['mu'+str(i)].value for i in range(nStates)]

        model = multiStateFunc(t, tau, mu, a, b, nStates)
        return model - data
    except KeyboardInterrupt:
        raise
     

def _cusumInitGuess(self, edat):
    cusumSettings={}
    cusumSettings["MinThreshold"]=0.1
    cusumSettings["MaxThreshold"]=100.
    cusumSettings["StepSize"]=self.StepSize
    cusumSettings["MinLength"]=self.MinStateLength

        # print cusumSettings

    cusumObj=cusum.cusumPlus(
                edat,
                edat, 
                self.Fs,
                eventstart=self.eStartEstimate,                     # event start point
                eventend=self.eEndEstimate,                         # event end point
                baselinestats=[ self.baseMean, self.baseSD, self.baseSlope ],
                algosettingsdict=cusumSettings.copy(),
                savets=False,
                absdatidx=self.absDataStartIndex,
                datafilehnd=None
            )
    cusumObj.processEvent()

    if cusumObj.mdProcessingStatus != "normal":
            # raise InvalidEvent
        self.rejectEvent(cusumObj.mdProcessingStatus+"_init")
    else:
        return list(zip(cusumObj.mdCurrentStep, cusumObj.mdEventDelay))

def fit_adept(edat,dt, initguess,baseMean):
    ts = np.array([ t*dt for t in range(0,len(edat)) ], dtype='float64')
    np.seterr(invalid='ignore', over='ignore', under='ignore')
    ts = np.array([ t*dt for t in range(0,len(edat)) ], dtype='float64')
    nStates=len(initguess)
    initRCConst=dt*5.
    params=Parameters()
    for i in range(0, len(initguess)):
        params.add('a'+str(i), value=initguess[i][0])
        params.add('mu'+str(i), value=initguess[i][1])
        if self.LinkRCConst:
            if i==0:
                params.add('tau'+str(i), value=initRCConst)
            else:
                params.add('tau'+str(i), value=initRCConst, expr='tau0')
        else:
            params.add('tau'+str(i), value=initRCConst)
        params.add('b', value=self.baseMean )
        igdict=params.valuesdict()
        optfit=Minimizer(self._objfunc, params, fcn_args=(ts,edat,))
        optfit.prepare_fit()
        result=optfit.leastsq(xtol=self.FitTol,ftol=self.FitTol,maxfev=self.FitIters)
        if result.success:
            tt=[init[0] for init, final in zip(list(igdict.items()), list((result.params.valuesdict()).items())) if init==final]
            if len(tt) > 0:
                flagEvent('wInitGuessUnchanged')
            recordevent(result,fs,nStates)

def recordevent(optfit,fs,nStates):
    dt=1000/fs
    try:
        if nStates<2:
            ptint('eInvalidStates')
        elif optfit.params['mu0'].value < 0.0 or optfit.params['mu'+str(nStates-1)].value < 0.0:
            print('eInvalidResTime')
        # The start of the event is set past the length of the data
        elif optfit.params['mu'+str(nStates-1)].value > (1000./fs)*(len(eventData)-1):
            self.rejectEvent('eInvalidStartTime')
        else:
            self.mdOpenChCurrent    = optfit.params['b'].value 
            self.mdCurrentStep      = [ optfit.params['a'+str(i)].value for i in range(self.nStates) ]
            
            self.mdNStates          = self.nStates

            self.mdBlockDepth       = np.cumsum( self.mdCurrentStep[:-1] )/self.mdOpenChCurrent + 1

            self.mdEventDelay       = [ optfit.params['mu'+str(i)].value for i in range(self.nStates) ]

            self.mdStateResTime     = np.diff(self.mdEventDelay)

            self.mdEventStart       = optfit.params['mu0'].value
            self.mdEventEnd         = optfit.params['mu'+str(self.nStates-1)].value
            self.mdRCConst          = [ optfit.params['tau'+str(i)].value for i in range(self.nStates) ]

            self.mdResTime          = self.mdEventEnd - self.mdEventStart

            self.mdAbsEventStart    = self.mdEventStart + self.absDataStartIndex * dt
            
            self.mdRedChiSq         = sum(np.array(optfit.residual)**2/self.baseSD**2)/optfit.nfree
                
            if math.isnan(self.mdRedChiSq):
                # print "wInvalidRedChiSq"
                self.flagEvent('wInvalidRedChiSq')  

            if ((np.array(self.mdBlockDepth)<0).all() or (np.array(self.mdBlockDepth)>1).all()):
                self.rejectEvent('eInvalidBlockDepth')
            if (np.array(self.mdStateResTime)<0).all():
                self.rejectEvent('eNegativeEventDelay')
            elif (np.array(self.mdRCConst)<0).all():
                self.rejectEvent('eInvalidRCConst')

    except:
        self.rejectEvent('eInvalidEvent')