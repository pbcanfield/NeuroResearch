#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _hOLM_reg();
extern void _imOLM_reg();
extern void _kdrca1OLM_reg();
extern void _leakinterOLM_reg();
extern void _napOLM_reg();
extern void _natOLM_reg();

void modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," hOLM.mod");
fprintf(stderr," imOLM.mod");
fprintf(stderr," kdrca1OLM.mod");
fprintf(stderr," leakinterOLM.mod");
fprintf(stderr," napOLM.mod");
fprintf(stderr," natOLM.mod");
fprintf(stderr, "\n");
    }
_hOLM_reg();
_imOLM_reg();
_kdrca1OLM_reg();
_leakinterOLM_reg();
_napOLM_reg();
_natOLM_reg();
}
