#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _imOLM_reg(void);
extern void _kaproxOLM_reg(void);
extern void _kdrca1OLM_reg(void);
extern void _leakinterOLM_reg(void);
extern void _napOLM_reg(void);
extern void _natOLM_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," modfiles//imOLM.mod");
    fprintf(stderr," modfiles//kaproxOLM.mod");
    fprintf(stderr," modfiles//kdrca1OLM.mod");
    fprintf(stderr," modfiles//leakinterOLM.mod");
    fprintf(stderr," modfiles//napOLM.mod");
    fprintf(stderr," modfiles//natOLM.mod");
    fprintf(stderr, "\n");
  }
  _imOLM_reg();
  _kaproxOLM_reg();
  _kdrca1OLM_reg();
  _leakinterOLM_reg();
  _napOLM_reg();
  _natOLM_reg();
}
