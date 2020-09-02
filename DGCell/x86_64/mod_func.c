#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _hDG_reg(void);
extern void _kdrca1DG_reg(void);
extern void _leakDG_reg(void);
extern void _natDG_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," modfiles//hDG.mod");
    fprintf(stderr," modfiles//kdrca1DG.mod");
    fprintf(stderr," modfiles//leakDG.mod");
    fprintf(stderr," modfiles//natDG.mod");
    fprintf(stderr, "\n");
  }
  _hDG_reg();
  _kdrca1DG_reg();
  _leakDG_reg();
  _natDG_reg();
}
