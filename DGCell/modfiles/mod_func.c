#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _hDG_reg();
extern void _im_reg();
extern void _kdrDG_reg();
extern void _leakDG_reg();
extern void _nap_reg();
extern void _natDG_reg();

void modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," hDG.mod");
fprintf(stderr," im.mod");
fprintf(stderr," kdrDG.mod");
fprintf(stderr," leakDG.mod");
fprintf(stderr," nap.mod");
fprintf(stderr," natDG.mod");
fprintf(stderr, "\n");
    }
_hDG_reg();
_im_reg();
_kdrDG_reg();
_leakDG_reg();
_nap_reg();
_natDG_reg();
}
