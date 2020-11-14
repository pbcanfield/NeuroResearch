#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _OLM_IA_reg(void);
extern void _OLM_Ih_reg(void);
extern void _OLM_Lca_reg(void);
extern void _OLM_cat_reg(void);
extern void _OLM_ccanl_reg(void);
extern void _OLM_ichan2_reg(void);
extern void _OLM_sahp_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," modfiles//OLM_IA.mod");
    fprintf(stderr," modfiles//OLM_Ih.mod");
    fprintf(stderr," modfiles//OLM_Lca.mod");
    fprintf(stderr," modfiles//OLM_cat.mod");
    fprintf(stderr," modfiles//OLM_ccanl.mod");
    fprintf(stderr," modfiles//OLM_ichan2.mod");
    fprintf(stderr," modfiles//OLM_sahp.mod");
    fprintf(stderr, "\n");
  }
  _OLM_IA_reg();
  _OLM_Ih_reg();
  _OLM_Lca_reg();
  _OLM_cat_reg();
  _OLM_ccanl_reg();
  _OLM_ichan2_reg();
  _OLM_sahp_reg();
}
