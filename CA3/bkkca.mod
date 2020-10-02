:BKKCA 


NEURON {
	SUFFIX bkkca
	USEION k READ ek WRITE ik
	USEION cas READ casi VALENCE 2 
	RANGE G, g, ainf, binf, vao1seg, vao2seg, Vao1, Vao2, sao1, sao2
	RANGE i
}

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)
}

PARAMETER {
	g = 0.002 :0.012 (siemens/cm2) <0,1e9>

	f = 0.08 :0.08    :(mV/uM)
	
	koa = 0.4 :0.4  (1/msec)
	kob = 0.2 :0.2 (1/msec)
	kCa = 0.36  (1/msec)
	
	Vao1 = -5 :-5   (mV)
	Vao2 = -5 :-5 (mV)
	
	sao1 = -15 :-15   :-23 (mV)
	sao2 = -9 :-9    :-5 (mV)
	
	c1 = 0.0001  :3.2  : 2.5  :(uM)
	c2 =  14  :(uM)
	c3 =  15  :(uM)

	vao1seg = -999
	vao2seg = -999
}

	:g = 0.002  :0.012 (siemens/cm2) <0,1e9>
ASSIGNED {
	v (mV)
	casi
	ek (mV)
	i
	:g := 0.002  :0.012 (siemens/cm2) <0,1e9>
	ik (mA/cm2)
	G (siemens/cm2)
	ainf
	binf
}

STATE {
	a b
}

BREAKPOINT {
	SOLVE states METHOD cnexp
	G = g*a*b
	i = G*(v-ek)
	ik = i
}

INITIAL {
	a = ainf
	b = binf
}

DERIVATIVE states {
	rate(v,casi)
	segment(v)
	a' = (ainf-a)*koa
	b' = (binf-b)*kob
}

PROCEDURE rate(v(mV),ca) {
	ainf = 1/(1+exp((v-Vao1+f*ca)/sao1))*1/(1+exp((v-Vao2+f*ca)/sao2))*(ca/(c1+ca))
	binf = c2/(c3+ca)
}

: Segmentation functions

PROCEDURE segment(v){
	if (v < vao1seg){
		ainf = 0
	}
	if (v < vao2seg){
		ainf = 0
	}
}
