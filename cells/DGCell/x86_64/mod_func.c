#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _hDG_reg(void);
extern void _imDG_reg(void);
extern void _kdrDG_reg(void);
extern void _leakDG_reg(void);
extern void _napDG_reg(void);
extern void _natDG_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," modfiles//hDG.mod");
    fprintf(stderr," modfiles//imDG.mod");
    fprintf(stderr," modfiles//kdrDG.mod");
    fprintf(stderr," modfiles//leakDG.mod");
    fprintf(stderr," modfiles//napDG.mod");
    fprintf(stderr," modfiles//natDG.mod");
    fprintf(stderr, "\n");
  }
  _hDG_reg();
  _imDG_reg();
  _kdrDG_reg();
  _leakDG_reg();
  _napDG_reg();
  _natDG_reg();
}
