#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _CaBK_reg(void);
extern void _Cagk_BC_reg(void);
extern void _IA_OLM_reg(void);
extern void _Ih_OLM_reg(void);
extern void _LcaMig_reg(void);
extern void _LcaMigCA3_reg(void);
extern void _Lca_BC_reg(void);
extern void _Lca_OLM_reg(void);
extern void _bg2pyr_reg(void);
extern void _bg2pyr2_reg(void);
extern void _bgka_reg(void);
extern void _bgkaCA3_reg(void);
extern void _borgkaCA3_reg(void);
extern void _borgka_BC_reg(void);
extern void _cal2_reg(void);
extern void _capool_reg(void);
extern void _catCA3_reg(void);
extern void _cat_OLM_reg(void);
extern void _ccanl_reg(void);
extern void _ccanlCA3_reg(void);
extern void _ccanl_BC_reg(void);
extern void _ccanl_OLM_reg(void);
extern void _cell_im_reg(void);
extern void _cell_lca_reg(void);
extern void _cell_nca_reg(void);
extern void _exp2syn_stsp_reg(void);
extern void _gskch_reg(void);
extern void _gskchCA3_reg(void);
extern void _gskch_BC_reg(void);
extern void _h_reg(void);
extern void _hCA3_reg(void);
extern void _hDG_reg(void);
extern void _ichan2_reg(void);
extern void _ichan2CA3_reg(void);
extern void _ichan2_BC_reg(void);
extern void _ichan2_OLM_reg(void);
extern void _inter2emo_reg(void);
extern void _izh_reg(void);
extern void _kaproxOLM_reg(void);
extern void _kdrBC_reg(void);
extern void _kdrCA3_reg(void);
extern void _kdrDG_reg(void);
extern void _kdrca1OLM_reg(void);
extern void _leakBC_reg(void);
extern void _leakCA3_reg(void);
extern void _leakDG_reg(void);
extern void _leakinterOLM_reg(void);
extern void _mossy_reg(void);
extern void _nap_reg(void);
extern void _natBC_reg(void);
extern void _natCA3_reg(void);
extern void _natDG_reg(void);
extern void _natOLM_reg(void);
extern void _nca_reg(void);
extern void _ncaCA3_reg(void);
extern void _nca_BC_reg(void);
extern void _pyr2emo_reg(void);
extern void _pyr2pyr_reg(void);
extern void _sahp_reg(void);
extern void _sahp_OLM_reg(void);
extern void _synapse_inter2pyr_reg(void);
extern void _vecevent_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," modfiles//CaBK.mod");
    fprintf(stderr," modfiles//Cagk_BC.mod");
    fprintf(stderr," modfiles//IA_OLM.mod");
    fprintf(stderr," modfiles//Ih_OLM.mod");
    fprintf(stderr," modfiles//LcaMig.mod");
    fprintf(stderr," modfiles//LcaMigCA3.mod");
    fprintf(stderr," modfiles//Lca_BC.mod");
    fprintf(stderr," modfiles//Lca_OLM.mod");
    fprintf(stderr," modfiles//bg2pyr.mod");
    fprintf(stderr," modfiles//bg2pyr2.mod");
    fprintf(stderr," modfiles//bgka.mod");
    fprintf(stderr," modfiles//bgkaCA3.mod");
    fprintf(stderr," modfiles//borgkaCA3.mod");
    fprintf(stderr," modfiles//borgka_BC.mod");
    fprintf(stderr," modfiles//cal2.mod");
    fprintf(stderr," modfiles//capool.mod");
    fprintf(stderr," modfiles//catCA3.mod");
    fprintf(stderr," modfiles//cat_OLM.mod");
    fprintf(stderr," modfiles//ccanl.mod");
    fprintf(stderr," modfiles//ccanlCA3.mod");
    fprintf(stderr," modfiles//ccanl_BC.mod");
    fprintf(stderr," modfiles//ccanl_OLM.mod");
    fprintf(stderr," modfiles//cell_im.mod");
    fprintf(stderr," modfiles//cell_lca.mod");
    fprintf(stderr," modfiles//cell_nca.mod");
    fprintf(stderr," modfiles//exp2syn_stsp.mod");
    fprintf(stderr," modfiles//gskch.mod");
    fprintf(stderr," modfiles//gskchCA3.mod");
    fprintf(stderr," modfiles//gskch_BC.mod");
    fprintf(stderr," modfiles//h.mod");
    fprintf(stderr," modfiles//hCA3.mod");
    fprintf(stderr," modfiles//hDG.mod");
    fprintf(stderr," modfiles//ichan2.mod");
    fprintf(stderr," modfiles//ichan2CA3.mod");
    fprintf(stderr," modfiles//ichan2_BC.mod");
    fprintf(stderr," modfiles//ichan2_OLM.mod");
    fprintf(stderr," modfiles//inter2emo.mod");
    fprintf(stderr," modfiles//izh.mod");
    fprintf(stderr," modfiles//kaproxOLM.mod");
    fprintf(stderr," modfiles//kdrBC.mod");
    fprintf(stderr," modfiles//kdrCA3.mod");
    fprintf(stderr," modfiles//kdrDG.mod");
    fprintf(stderr," modfiles//kdrca1OLM.mod");
    fprintf(stderr," modfiles//leakBC.mod");
    fprintf(stderr," modfiles//leakCA3.mod");
    fprintf(stderr," modfiles//leakDG.mod");
    fprintf(stderr," modfiles//leakinterOLM.mod");
    fprintf(stderr," modfiles//mossy.mod");
    fprintf(stderr," modfiles//nap.mod");
    fprintf(stderr," modfiles//natBC.mod");
    fprintf(stderr," modfiles//natCA3.mod");
    fprintf(stderr," modfiles//natDG.mod");
    fprintf(stderr," modfiles//natOLM.mod");
    fprintf(stderr," modfiles//nca.mod");
    fprintf(stderr," modfiles//ncaCA3.mod");
    fprintf(stderr," modfiles//nca_BC.mod");
    fprintf(stderr," modfiles//pyr2emo.mod");
    fprintf(stderr," modfiles//pyr2pyr.mod");
    fprintf(stderr," modfiles//sahp.mod");
    fprintf(stderr," modfiles//sahp_OLM.mod");
    fprintf(stderr," modfiles//synapse_inter2pyr.mod");
    fprintf(stderr," modfiles//vecevent.mod");
    fprintf(stderr, "\n");
  }
  _CaBK_reg();
  _Cagk_BC_reg();
  _IA_OLM_reg();
  _Ih_OLM_reg();
  _LcaMig_reg();
  _LcaMigCA3_reg();
  _Lca_BC_reg();
  _Lca_OLM_reg();
  _bg2pyr_reg();
  _bg2pyr2_reg();
  _bgka_reg();
  _bgkaCA3_reg();
  _borgkaCA3_reg();
  _borgka_BC_reg();
  _cal2_reg();
  _capool_reg();
  _catCA3_reg();
  _cat_OLM_reg();
  _ccanl_reg();
  _ccanlCA3_reg();
  _ccanl_BC_reg();
  _ccanl_OLM_reg();
  _cell_im_reg();
  _cell_lca_reg();
  _cell_nca_reg();
  _exp2syn_stsp_reg();
  _gskch_reg();
  _gskchCA3_reg();
  _gskch_BC_reg();
  _h_reg();
  _hCA3_reg();
  _hDG_reg();
  _ichan2_reg();
  _ichan2CA3_reg();
  _ichan2_BC_reg();
  _ichan2_OLM_reg();
  _inter2emo_reg();
  _izh_reg();
  _kaproxOLM_reg();
  _kdrBC_reg();
  _kdrCA3_reg();
  _kdrDG_reg();
  _kdrca1OLM_reg();
  _leakBC_reg();
  _leakCA3_reg();
  _leakDG_reg();
  _leakinterOLM_reg();
  _mossy_reg();
  _nap_reg();
  _natBC_reg();
  _natCA3_reg();
  _natDG_reg();
  _natOLM_reg();
  _nca_reg();
  _ncaCA3_reg();
  _nca_BC_reg();
  _pyr2emo_reg();
  _pyr2pyr_reg();
  _sahp_reg();
  _sahp_OLM_reg();
  _synapse_inter2pyr_reg();
  _vecevent_reg();
}
