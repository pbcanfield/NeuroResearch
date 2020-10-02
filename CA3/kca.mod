:  ca-dependent potassium current

NEURON {
	SUFFIX kca
	USEION k READ ek WRITE ik
	USEION ca READ cai
    RANGE g, gbar, ik
	RANGE cinf, cinfvhalf, cinfk, cseg
}

UNITS {
        (mM) = (milli/liter)
	(mA) = (milliamp)
	(mV) = (millivolt)
}

PARAMETER {
	gbar (siemens/cm2)
	cinfvhalf = 28.3 (mV)
	cinfk = 12.6
	cseg = -999 (mV)
}

ASSIGNED {
	v (mV)
	ek (mV)
	ik (mA/cm2)
	cinf 
	ctau (ms)
	g (siemens/cm2)
	cai (mM)
}

STATE {
	c
}


BREAKPOINT {
	SOLVE states METHOD cnexp
	g = gbar*c*c*c*c       
	ik = g*(v-ek)
}


INITIAL {
	rate(v,cai)
	segment(v)
	c = cinf
}

DERIVATIVE states {
        rate(v,cai)
	c' = (cinf-c)/ctau
}
PROCEDURE rate(v (mV), cai (mM)) {
	UNITSOFF
	:activation based on internal concentration of capool
	cinf = ((cai)/(cai + 0.003))*((1.0)/(1+ (exp (-(v+cinfvhalf)/(cinfk)))))        
	ctau = ((180.6)-(150.2)/(1+(exp (-(v+46)/(22.7))))) 
	UNITSON		
}

PROCEDURE segment(v){
	if (v < cseg){
		cinf = 0
	}
}
