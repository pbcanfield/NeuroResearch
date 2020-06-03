TITLE Potasium C type current for RD Traub, J Neurophysiol 89:909-921, 2003

COMMENT

	Implemented by Maciej Lazarewicz 2003 (mlazarew@seas.upenn.edu)

ENDCOMMENT

INDEPENDENT { t FROM 0 TO 1 WITH 1 (ms) }

UNITS { 
	(mV) = (millivolt) 
	(mA) = (milliamp) 
}
 
NEURON { 
	SUFFIX kc
	USEION k READ ek WRITE ik
	USEION ca READ cai
	RANGE  gbar, ik,minf, slope, vhalf
}

PARAMETER { 
	gbar = 0.0 	(mho/cm2)
	v ek 		(mV)  
	cai		(1)
	slope = 6
	vhalf = -19
} 

ASSIGNED { 
	ik 		(mA/cm2) 
	alpha beta	(/ms)
	minf 		(1)
	mtau 		(ms) 
}
 
STATE {
	m
}

BREAKPOINT { 
	SOLVE states METHOD cnexp
	if( 0.004 * cai < 1 ) {
		ik = gbar * m * 0.004 * cai * ( v - ek ) 
	}else{
		ik = gbar * m * ( v - ek ) 
	}
}
 
INITIAL { 
	settables(v) 
	m = minf
	m = 0
}
 
DERIVATIVE states { 
	settables(v) 
	m' = ( minf - m ) / mtau 
}

UNITSOFF 

PROCEDURE settables(v) { 
	:TABLE alpha, beta FROM -120 TO 40 WITH 641
	TABLE minf, mtau,alpha, beta FROM -120 TO 40 WITH 641
	if (v>-67.5){
		minf  = 1 / ( 1 + exp( ( - v + vhalf ) / slope ) )
	}else{
		minf = 0
	}
	if( v < -10.0 ) {
		alpha = 2 / 37.95 * ( exp( ( v + 50 ) / 11 - ( v + 53.5 ) / 27 ) )

		: Note that there is typo in the paper - missing minus sign in the front of 'v'
		beta  = 2 * exp( ( - v - 53.5 ) / 27 ) - alpha
	}else{
		alpha = 2 * exp( ( - v - 53.5 ) / 27 )
		beta  = 0
	}

	mtau = 1/(alpha+beta)
}

UNITSON