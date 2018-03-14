"""

Attention  : fichier autogénéré.
Ne pas l'éditer à la main.
Pour l'éditer, utiliser parseur

"""

# Standard Libraries
from collections import namedtuple

ProcApi = namedtuple('ProcApi', 'name input_type genre')

thesoapi = {
    'get_cip':
        ProcApi(name='get_cip', input_type=['int6'], genre='char'),
    'get_frm':
        ProcApi(name='get_frm', input_type=['int6'], genre='char'),
    'get_voie':
        ProcApi(name='get_voie', input_type=['int6'], genre='char'),
    'is_atu':
        ProcApi(name='is_atu', input_type=['int6'], genre='char'),
    'is_retro':
        ProcApi(name='is_retro', input_type=['int6'], genre='char'),
    'is_t2a':
        ProcApi(name='is_t2a', input_type=['int6'], genre='char'),
    'get_cons':
        ProcApi(name='get_cons', input_type=['str13'], genre='char'),
    'is_hormono':
        ProcApi(name='is_hormono', input_type=['int6'], genre='char'),
    'get_the_gen_equiv':
        ProcApi(name='get_the_gen_equiv', input_type=['int', 'int'], genre='cursor'),
    'get_the_spe_details':
        ProcApi(name='get_the_spe_details', input_type=['str', 'int'], genre='cursor'),
    'get_the_cim10':
        ProcApi(name='get_the_cim10', input_type=['int'], genre='cursor'),
    'get_the_cipemg_id':
        ProcApi(name='get_the_cipemg_id', input_type=['int', 'str'], genre='cursor'),
    'get_the_incompat_fiche':
        ProcApi(name='get_the_incompat_fiche', input_type=['int'], genre='cursor'),
    'get_the_inter':
        ProcApi(name='get_the_inter', input_type=['str', 'int'], genre='cursor'),
    'get_the_conservation_spe':
        ProcApi(name='get_the_conservation_spe', input_type=['str'], genre='cursor'),
    'get_the_inter_sacinter_sac':
        ProcApi(name='get_the_inter_sacinter_sac', input_type=['str', 'str'], genre='cursor'),
    'get_the_cim10_by_code':
        ProcApi(name='get_the_cim10_by_code', input_type=['str'], genre='cursor'),
    'get_the_spe_by_ind_ucd':
        ProcApi(name='get_the_spe_by_ind_ucd', input_type=['str'], genre='cursor'),
    'get_the_spe_by_ind_ucdind':
        ProcApi(name='get_the_spe_by_ind_ucdind', input_type=['str'], genre='cursor'),
    'get_the_cipemg_text_sp':
        ProcApi(name='get_the_cipemg_text_sp', input_type=['int', 'str'], genre='cursor'),
    'get_the_hyper_code_by_name':
        ProcApi(name='get_the_hyper_code_by_name', input_type=['str'], genre='cursor'),
    'get_the_spe_same_cls':
        ProcApi(name='get_the_spe_same_cls', input_type=['int', 'int'], genre='cursor'),
    'get_the_code_cim10':
        ProcApi(name='get_the_code_cim10', input_type=['str'], genre='cursor'),
    'get_the_smr_asmr_spe':
        ProcApi(name='get_the_smr_asmr_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_smr_asmr_gsp':
        ProcApi(name='get_the_smr_asmr_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_produit_stup':
        ProcApi(name='get_the_produit_stup', input_type=['str', 'int'], genre='cursor'),
    'get_the_produit_stup_gsp':
        ProcApi(name='get_the_produit_stup_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_produit_dop':
        ProcApi(name='get_the_produit_dop', input_type=['str', 'int'], genre='cursor'),
    'get_the_produit_dop_gsp':
        ProcApi(name='get_the_produit_dop_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_reserve_hosp':
        ProcApi(name='get_the_reserve_hosp', input_type=['str', 'int'], genre='cursor'),
    'get_the_reserve_hosp_gsp':
        ProcApi(name='get_the_reserve_hosp_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_prescr_rest':
        ProcApi(name='get_the_prescr_rest', input_type=['str', 'int'], genre='cursor'),
    'get_the_prescr_rest_gsp':
        ProcApi(name='get_the_prescr_rest_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_delivr_rest':
        ProcApi(name='get_the_delivr_rest', input_type=['str', 'int'], genre='cursor'),
    'get_the_delivr_rest_gsp':
        ProcApi(name='get_the_delivr_rest_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_gen_ref':
        ProcApi(name='get_the_gen_ref', input_type=['str', 'int'], genre='cursor'),
    'get_the_spe_dsp':
        ProcApi(name='get_the_spe_dsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_gsp_dsp':
        ProcApi(name='get_the_gsp_dsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_prix':
        ProcApi(name='get_the_prix', input_type=['str', 'int'], genre='cursor'),
    'get_the_atu':
        ProcApi(name='get_the_atu', input_type=['str', 'int'], genre='cursor'),
    'get_the_atu_gsp':
        ProcApi(name='get_the_atu_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_vigi_conduct':
        ProcApi(name='get_the_vigi_conduct', input_type=['str', 'int'], genre='cursor'),
    'get_the_vigi_conduct_gsp':
        ProcApi(name='get_the_vigi_conduct_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_atc_ddd_v2':
        ProcApi(name='get_the_atc_ddd_v2', input_type=['str', 'int'], genre='cursor'),
    'get_the_atc_ddd_gsp_v2':
        ProcApi(name='get_the_atc_ddd_gsp_v2', input_type=['str', 'int'], genre='cursor'),
    'get_the_solute':
        ProcApi(name='get_the_solute', input_type=['str', 'int'], genre='cursor'),
    'get_the_solute_gsp':
        ProcApi(name='get_the_solute_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_virtuel':
        ProcApi(name='get_the_virtuel', input_type=['str', 'int'], genre='cursor'),
    'get_the_forme_spe_v2':
        ProcApi(name='get_the_forme_spe_v2', input_type=['str', 'int'], genre='cursor'),
    'get_the_forme_gsp':
        ProcApi(name='get_the_forme_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_compo_spe':
        ProcApi(name='get_the_compo_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_compo_gsp':
        ProcApi(name='get_the_compo_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_compo_synth_spe':
        ProcApi(name='get_the_compo_synth_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_compo_synth_gsp':
        ProcApi(name='get_the_compo_synth_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_effet_notoire_spe':
        ProcApi(name='get_the_effet_notoire_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_effet_notoire_gsp':
        ProcApi(name='get_the_effet_notoire_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_fic_info_thera':
        ProcApi(name='get_the_fic_info_thera', input_type=['str'], genre='cursor'),
    'get_the_fic_info_thera_gsp':
        ProcApi(name='get_the_fic_info_thera_gsp', input_type=['str'], genre='cursor'),
    'get_the_ter_cipemg_age':
        ProcApi(name='get_the_ter_cipemg_age', input_type=['str', 'int', 'int'], genre='cursor'),
    'get_the_ter_cipemg_age_gsp':
        ProcApi(
            name='get_the_ter_cipemg_age_gsp', input_type=['str', 'int', 'int'], genre='cursor'),
    'get_the_ter_cipemg_pds':
        ProcApi(name='get_the_ter_cipemg_pds', input_type=['str', 'int', 'int'], genre='cursor'),
    'get_the_ter_cipemg_pds_gsp':
        ProcApi(
            name='get_the_ter_cipemg_pds_gsp', input_type=['str', 'int', 'int'], genre='cursor'),
    'get_the_ter_cipemg_clr':
        ProcApi(name='get_the_ter_cipemg_clr', input_type=['str', 'int', 'int'], genre='cursor'),
    'get_the_ter_cipemg_clr_gsp':
        ProcApi(
            name='get_the_ter_cipemg_clr_gsp', input_type=['str', 'int', 'int'], genre='cursor'),
    'get_the_ter_cipemg_surf':
        ProcApi(name='get_the_ter_cipemg_surf', input_type=['str', 'int', 'int'], genre='cursor'),
    'get_the_ter_cipemg_sur_gsp':
        ProcApi(
            name='get_the_ter_cipemg_sur_gsp', input_type=['str', 'int', 'int'], genre='cursor'),
    'get_the_proc_spe':
        ProcApi(name='get_the_proc_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_proc_gsp':
        ProcApi(name='get_the_proc_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_proc_spev2':
        ProcApi(name='get_the_proc_spev2', input_type=['str', 'int', 'int'], genre='cursor'),
    'get_the_proc_gspv2':
        ProcApi(name='get_the_proc_gspv2', input_type=['str', 'int', 'int'], genre='cursor'),
    'get_the_sexe_spe':
        ProcApi(name='get_the_sexe_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_sexe_gsp':
        ProcApi(name='get_the_sexe_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_ter_cipemg_gr':
        ProcApi(name='get_the_ter_cipemg_gr', input_type=['str', 'int', 'int'], genre='cursor'),
    'get_the_ter_cipemg_gr_gsp':
        ProcApi(name='get_the_ter_cipemg_gr_gsp', input_type=['str', 'int', 'int'], genre='cursor'),
    'get_the_ter_cipemg_al':
        ProcApi(name='get_the_ter_cipemg_al', input_type=['str', 'int'], genre='cursor'),
    'get_the_ter_cipemg_al_gsp':
        ProcApi(name='get_the_ter_cipemg_al_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_spe_to_hyper':
        ProcApi(name='get_the_spe_to_hyper', input_type=['str'], genre='cursor'),
    'get_the_gsp_to_hyper':
        ProcApi(name='get_the_gsp_to_hyper', input_type=['str'], genre='cursor'),
    'get_the_gsp_to_hyper_sac':
        ProcApi(name='get_the_gsp_to_hyper_sac', input_type=['str'], genre='cursor'),
    'get_the_hyper_to_spe':
        ProcApi(name='get_the_hyper_to_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_indic_spe':
        ProcApi(name='get_the_indic_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_indic_gsp':
        ProcApi(name='get_the_indic_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_cipe_spe_cim10':
        ProcApi(name='get_the_cipe_spe_cim10', input_type=['str', 'int'], genre='cursor'),
    'get_the_cipe_gsp_cim10':
        ProcApi(name='get_the_cipe_gsp_cim10', input_type=['str', 'int'], genre='cursor'),
    'get_the_indic_amm_ptt_tru':
        ProcApi(name='get_the_indic_amm_ptt_tru', input_type=['str', 'int'], genre='cursor'),
    'get_the_ind_amm_ptt_tru_gsp':
        ProcApi(name='get_the_ind_amm_ptt_tru_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_inter_spe_sac':
        ProcApi(name='get_the_inter_spe_sac', input_type=['str'], genre='cursor'),
    'get_the_inter_gsp_sac':
        ProcApi(name='get_the_inter_gsp_sac', input_type=['str'], genre='cursor'),
    'get_the_incompat_spe_sac':
        ProcApi(name='get_the_incompat_spe_sac', input_type=['str'], genre='cursor'),
    'get_the_incompat_gsp_sac':
        ProcApi(name='get_the_incompat_gsp_sac', input_type=['str'], genre='cursor'),
    'get_the_pso_mm_by_spe':
        ProcApi(name='get_the_pso_mm_by_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_antibio_loc_spe':
        ProcApi(name='get_the_antibio_loc_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_antibio_syst_spe':
        ProcApi(name='get_the_antibio_syst_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_antibio_loc_gsp':
        ProcApi(name='get_the_antibio_loc_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_antibio_syst_gsp':
        ProcApi(name='get_the_antibio_syst_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_hypno_spe':
        ProcApi(name='get_the_hypno_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_hypno_gsp':
        ProcApi(name='get_the_hypno_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_anxio_spe':
        ProcApi(name='get_the_anxio_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_anxio_gsp':
        ProcApi(name='get_the_anxio_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_anticanc_spe':
        ProcApi(name='get_the_anticanc_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_anticanc_gsp':
        ProcApi(name='get_the_anticanc_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_index_vacc':
        ProcApi(name='get_the_index_vacc', input_type=['str', 'int'], genre='cursor'),
    'get_the_unit_prise':
        ProcApi(name='get_the_unit_prise', input_type=['str', 'int'], genre='cursor'),
    'get_the_medic_except_spe':
        ProcApi(name='get_the_medic_except_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_medic_except_gsp':
        ProcApi(name='get_the_medic_except_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_cfo_secable_spe':
        ProcApi(name='get_the_cfo_secable_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_admin_fo_solide_spe':
        ProcApi(name='get_the_admin_fo_solide_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_li_presc_spe':
        ProcApi(name='get_the_li_presc_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_cond_admin_spe':
        ProcApi(name='get_the_cond_admin_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_labo_exploit_spe':
        ProcApi(name='get_the_labo_exploit_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_pr_deriv_sang_spe':
        ProcApi(name='get_the_pr_deriv_sang_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_pr_deriv_sang_gsp':
        ProcApi(name='get_the_pr_deriv_sang_gsp', input_type=['str', 'int'], genre='cursor'),
    'get_the_medic_orph_spe':
        ProcApi(name='get_the_medic_orph_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_pgr_surv_renf_spe':
        ProcApi(name='get_the_pgr_surv_renf_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_comm_cipemg_spe':
        ProcApi(name='get_the_comm_cipemg_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_redond_spe':
        ProcApi(name='get_the_redond_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_spe_indic_by_cim10':
        ProcApi(name='get_the_spe_indic_by_cim10', input_type=['str', 'int'], genre='cursor'),
    'get_the_gsp_indic_by_cim10':
        ProcApi(name='get_the_gsp_indic_by_cim10', input_type=['str', 'int'], genre='cursor'),
    'get_the_info_spe':
        ProcApi(name='get_the_info_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_etat_commer_spe':
        ProcApi(name='get_the_etat_commer_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_effet_inde_spe':
        ProcApi(name='get_the_effet_inde_spe', input_type=['str', 'int'], genre='cursor'),
    'get_the_poso_v2':
        ProcApi(name='get_the_poso_v2', input_type=['str', 'int'], genre='cursor'),
    'get_the_compo_allsub_sp':
        ProcApi(name='get_the_compo_allsub_sp', input_type=['int'], genre='cursor'),
    'get_the_therap_anticanc':
        ProcApi(name='get_the_therap_anticanc', input_type=['str', 'int'], genre='cursor'),
    'get_the_delivre_max':
        ProcApi(name='get_the_delivre_max', input_type=['int'], genre='cursor'),
    'get_the_spe_is_or_bio':
        ProcApi(name='get_the_spe_is_or_bio', input_type=['str'], genre='cursor'),
    'get_the_spe_interop':
        ProcApi(name='get_the_spe_interop', input_type=['str'], genre='cursor'),
    'get_the_spe_hormono':
        ProcApi(name='get_the_spe_hormono', input_type=['str', 'int'], genre='cursor'),
    'get_the_gtiam_txt':
        ProcApi(name='get_the_gtiam_txt', input_type=['str'], genre='cursor'),
    'get_the_reserve_hosp_cip':
        ProcApi(name='get_the_reserve_hosp_cip', input_type=['str', 'int'], genre='cursor')
}
