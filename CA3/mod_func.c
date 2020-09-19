#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _bkkca_reg();
extern void _ca_reg();
extern void _cadyn_reg();
extern void _cal2_reg();
extern void _capool_reg();
extern void _hCA3_reg();
extern void _im_reg();
extern void _kca_reg();
extern void _kdrCA3_reg();
extern void _leakCA3_reg();
extern void _nap_reg();
extern void _natCA3_reg();
extern void _pyr2pyr_reg();
extern void _sahp_reg();
extern void _synapse_inter2pyr_reg();

void modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," bkkca.mod");
fprintf(stderr," ca.mod");
fprintf(stderr," cadyn.mod");
fprintf(stderr," cal2.mod");
fprintf(stderr," capool.mod");
fprintf(stderr," hCA3.mod");
fprintf(stderr," im.mod");
fprintf(stderr," kca.mod");
fprintf(stderr," kdrCA3.mod");
fprintf(stderr," leakCA3.mod");
fprintf(stderr," nap.mod");
fprintf(stderr," natCA3.mod");
fprintf(stderr," pyr2pyr.mod");
fprintf(stderr," sahp.mod");
fprintf(stderr," synapse_inter2pyr.mod");
fprintf(stderr, "\n");
    }
_bkkca_reg();
_ca_reg();
_cadyn_reg();
_cal2_reg();
_capool_reg();
_hCA3_reg();
_im_reg();
_kca_reg();
_kdrCA3_reg();
_leakCA3_reg();
_nap_reg();
_natCA3_reg();
_pyr2pyr_reg();
_sahp_reg();
_synapse_inter2pyr_reg();
}
