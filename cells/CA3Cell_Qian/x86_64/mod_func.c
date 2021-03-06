#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _Gfluct_new_exc_reg(void);
extern void _Gfluct_new_inh_reg(void);
extern void _imCA3_reg(void);
extern void _kdrCA3_reg(void);
extern void _leakCA3_reg(void);
extern void _napCA3_reg(void);
extern void _natCA3_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," modfiles//Gfluct_new_exc.mod");
    fprintf(stderr," modfiles//Gfluct_new_inh.mod");
    fprintf(stderr," modfiles//imCA3.mod");
    fprintf(stderr," modfiles//kdrCA3.mod");
    fprintf(stderr," modfiles//leakCA3.mod");
    fprintf(stderr," modfiles//napCA3.mod");
    fprintf(stderr," modfiles//natCA3.mod");
    fprintf(stderr, "\n");
  }
  _Gfluct_new_exc_reg();
  _Gfluct_new_inh_reg();
  _imCA3_reg();
  _kdrCA3_reg();
  _leakCA3_reg();
  _napCA3_reg();
  _natCA3_reg();
}
