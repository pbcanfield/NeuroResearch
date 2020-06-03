: passive leak current

NEURON {
	SUFFIX leak_WB
	NONSPECIFIC_CURRENT il
	RANGE il, el, glbar
}

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)
}

PARAMETER {
	glbar = 0.0001 (siemens/cm2) < 0, 1e9 >
	el = -65.0 (mV)
}

ASSIGNED {
	v (mV)
	il (mA/cm2)
}

BREAKPOINT { 
	il = glbar*(v - el)
}
