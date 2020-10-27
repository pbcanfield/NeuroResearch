TITLE nat
: Na current 
: from Jeff M.
:  ---------- modified -------M.Migliore may97

NEURON {
	SUFFIX natCA3
	USEION na READ ena WRITE ina
	:RANGE  , i :, ar2
	RANGE gbar, gna, i, minf, hinf, mtau, htau : , qinf, thinf
}

PARAMETER {
	
	gbar = 0.010   	(mho/cm2)	
								
	tha  =  -30	(mV)		: v 1/2 for act	
	qa   = 7.2	(mV)		: act slope (4.5)		
	Ra   = 0.4	(/ms)		: open (v)		
	Rb   = 0.124 	(/ms)		: close (v)		

	thi1  = -45	(mV)		: v 1/2 for inact 	
	thi2  = -45 	(mV)		: v 1/2 for inact 	
	qd   = 1.5	(mV)	        : inact tau slope
	qg   = 1.5      (mV)
	mmin=0.02	
	hmin=0.5			
	q10=2
	Rg   = 0.01 	(/ms)		: inact recov (v) 	
	Rd   = .03 	(/ms)		: inact (v)	
	qq   = 10        (mV)
	tq   = -55      (mV)

	thinf  = -50 	(mV)		: inact inf slope	
	qinf  = 4 	(mV)		: inact inf slope 

    ar2=1		(1)		: 1=no inact., 0=max inact.
	ena		(mV)            : must be explicitly def. in hoc
	celsius
	v 		(mV)
}


UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)
	(pS) = (picosiemens)
	(um) = (micron)
} 

ASSIGNED {
	ina 		(mA/cm2)
	i    		(mA/cm2)
	gna		(mho/cm2)
	minf 		hinf 		
	mtau (ms)	htau (ms) 	
	tha1	
}
 

STATE { m h}

BREAKPOINT {
        SOLVE states METHOD cnexp
        gna = gbar*m*m*m*h
	ina = gna * (v - ena)
	i = ina
} 

INITIAL {
	trates(v,ar2)
	m=minf  
	h=hinf
}


LOCAL mexp, hexp

DERIVATIVE states {   
        trates(v,ar2)      
        m' = (minf-m)/mtau
        h' = (hinf-h)/htau
}

PROCEDURE trates(vm,a2) {  
        LOCAL  a, b, qt
		qt = 1.6245
		tha1 = tha 
	a = trap0(vm,tha1,Ra,qa)
	b = trap0(-vm,-tha1,Rb,qa)
	mtau = 1/(a+b)/qt
        if (mtau<mmin) {mtau=mmin}
	if (v < -52.5 ) {			:-57.5 :-52.5
	minf = 0
	} else{
	minf  = 1 / ( 1 + exp( ( - v - 35.5) / 7.2 ) ) :35.5
	}
	a = trap0(vm,thi1,Rd,qd)
	b = trap0(-vm,-thi2,Rg,qg)
	htau =  1/(a+b)/qt
        if (htau<hmin) {htau=hmin}
	hinf  = 1 / ( 1 + exp( ( v + 40 ) / 4 ) ) :40
}

FUNCTION trap0(v,th,a,q) {
	if (fabs(v-th) > 1e-6) {
	        trap0 = a * (v - th) / (1 - exp(-(v - th)/q))
	} else {
	        trap0 = a * q
 	}
}	
