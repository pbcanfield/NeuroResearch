#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _k_reg(void);
extern void _leak_reg(void);
extern void _na_reg(void);
extern void _VVClamp_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," modfiles//k.mod");
    fprintf(stderr," modfiles//leak.mod");
    fprintf(stderr," modfiles//na.mod");
    fprintf(stderr," modfiles//VVClamp.mod");
    fprintf(stderr, "\n");
  }
  _k_reg();
  _leak_reg();
  _na_reg();
  _VVClamp_reg();
}
