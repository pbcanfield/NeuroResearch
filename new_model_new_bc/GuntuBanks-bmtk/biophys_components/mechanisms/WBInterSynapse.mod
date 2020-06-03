NEURON {
	POINT_PROCESS WBInterSynapse
	NONSPECIFIC_CURRENT i_syn
	RANGE initW
	RANGE Cdur_syn, AlphaTmax_syn, Beta_syn, Erev_syn, gbar_syn, W_syn, on_syn, g_syn, i_syn
	RANGE pregid,postgid
}

UNITS {
	(mV) = (millivolt)
    (mA) = (milliamp)
	(uS) = (microsiemens)
}

PARAMETER {
	initW = 10

	Cdur_syn = 1 (ms)
	AlphaTmax_syn = .08 (/ms)
	Beta_syn = 0.1 (/ms)
	Erev_syn = -75. (mV)
	gbar_syn = 1e-4(uS)

}

ASSIGNED {
	v (mV)

	i_syn (mA)
	g_syn (uS)
	on_syn
	W_syn

	t0 (ms)
	
	pregid
	postgid
}

STATE { r_syn r_ampa Capoolcon }

INITIAL {
	on_syn = 0
	r_syn = 0
	W_syn = initW
	
	t0 = -1

}

BREAKPOINT {
	SOLVE release METHOD cnexp
}

DERIVATIVE release {
	if (t0>0) {
		if (t-t0 < Cdur_syn) {
			on_syn = 1
		} else {
			on_syn = 0
		}
		
	}
	r_syn' = AlphaTmax_syn*on_syn*(1-r_syn)-Beta_syn*r_syn

	g_syn = gbar_syn*r_syn
	i_syn = W_syn*g_syn*(v - Erev_syn)

}

NET_RECEIVE(dummy_weight) {
	t0 = t
}

