#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _kdrca1_reg(void);
extern void _leakBC_reg(void);
extern void _nat_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," modfiles//kdrca1.mod");
    fprintf(stderr," modfiles//leakBC.mod");
    fprintf(stderr," modfiles//nat.mod");
    fprintf(stderr, "\n");
  }
  _kdrca1_reg();
  _leakBC_reg();
  _nat_reg();
}
