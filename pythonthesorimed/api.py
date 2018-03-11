
"""
Attention  : fichier autogénéré.
Ne pas l'éditer à la main.
Pour l'éditer, utiliser parseur
Il faut configurer host, dbn user et password à la main.

"""



import psycopg2
from psycopg2.extras import NamedTupleCursor

def connect():
    """
    Base fonction to connect to database.
    Return a pscipg connection
    """

    return psycopg2.connect(host="127.0.0.1", dbname="aaa", user="j", password="j")

def appel_refcursor(name, req, params):

    # convert [int,int,int] to 'int,int, int'
    req = list(req)
    for i in range(len(req)):
        if 'str' in params[i]:
            req[i] = ','.join(map(str,req[i]))
    #create connection
    with connect() as con:
        with con.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute("SET search_path TO thesorimed, public")
            curs.callproc("thesorimed."+name,req)

            cc = curs.fetchone()[0] #get the cursor
            a = '"' + cc + '"'
            f = "FETCH ALL IN {0};".format(a) #retrieve from cursor
            curs.execute(f)
            cc = curs.fetchall()
    return cc

def appel_character(name, req, params):
    """
    DEal With procedure wich retruns a value
    """

    req = list(req) #list to modify tupple
    if 'str' in params[0]:  # turn arg to str if varchar
        req[0]=str(req[0])


    with connect() as con:
        with con.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute("SET search_path TO thesorimed, public")
            curs.callproc("thesorimed."+name, req)
            res = curs.fetchone()
            cc = getattr(res, name)
    return cc

def get_cip(*req):
    return appel_character("get_cip", req, ['int6'])

def get_frm(*req):
    return appel_character("get_frm", req, ['int6'])

def get_voie(*req):
    return appel_character("get_voie", req, ['int6'])

def is_atu(*req):
    return appel_character("is_atu", req, ['int6'])

def is_retro(*req):
    return appel_character("is_retro", req, ['int6'])

def is_t2a(*req):
    return appel_character("is_t2a", req, ['int6'])

def get_cons(*req):
    return appel_character("get_cons", req, ['str13'])

def is_hormono(*req):
    return appel_character("is_hormono", req, ['int6'])

def get_the_gen_equiv(*req):
    return appel_refcursor("get_the_gen_equiv", req, ['int', 'int'])

def get_the_spe_details(*req):
    return appel_refcursor("get_the_spe_details", req, ['str', 'int'])

def get_the_cim10(*req):
    return appel_refcursor("get_the_cim10", req, ['int'])

def get_the_cipemg_id(*req):
    return appel_refcursor("get_the_cipemg_id", req, ['int', 'str'])

def get_the_incompat_fiche(*req):
    return appel_refcursor("get_the_incompat_fiche", req, ['int'])

def get_the_inter(*req):
    return appel_refcursor("get_the_inter", req, ['str', 'int'])

def get_the_conservation_spe(*req):
    return appel_refcursor("get_the_conservation_spe", req, ['str'])

def get_the_inter_sacinter_sac(*req):
    return appel_refcursor("get_the_inter_sacinter_sac", req, ['str', 'str'])

def get_the_cim10_by_code(*req):
    return appel_refcursor("get_the_cim10_by_code", req, ['str'])

def get_the_spe_by_ind_ucd(*req):
    return appel_refcursor("get_the_spe_by_ind_ucd", req, ['str'])

def get_the_spe_by_ind_ucdind(*req):
    return appel_refcursor("get_the_spe_by_ind_ucdind", req, ['str'])

def get_the_cipemg_text_sp(*req):
    return appel_refcursor("get_the_cipemg_text_sp", req, ['int', 'str'])

def get_the_hyper_code_by_name(*req):
    return appel_refcursor("get_the_hyper_code_by_name", req, ['str'])

def get_the_spe_same_cls(*req):
    return appel_refcursor("get_the_spe_same_cls", req, ['int', 'int'])

def get_the_code_cim10(*req):
    return appel_refcursor("get_the_code_cim10", req, ['str'])

def get_the_smr_asmr_spe(*req):
    return appel_refcursor("get_the_smr_asmr_spe", req, ['str', 'int'])

def get_the_smr_asmr_gsp(*req):
    return appel_refcursor("get_the_smr_asmr_gsp", req, ['str', 'int'])

def get_the_produit_stup(*req):
    return appel_refcursor("get_the_produit_stup", req, ['str', 'int'])

def get_the_produit_stup_gsp(*req):
    return appel_refcursor("get_the_produit_stup_gsp", req, ['str', 'int'])

def get_the_produit_dop(*req):
    return appel_refcursor("get_the_produit_dop", req, ['str', 'int'])

def get_the_produit_dop_gsp(*req):
    return appel_refcursor("get_the_produit_dop_gsp", req, ['str', 'int'])

def get_the_reserve_hosp(*req):
    return appel_refcursor("get_the_reserve_hosp", req, ['str', 'int'])

def get_the_reserve_hosp_gsp(*req):
    return appel_refcursor("get_the_reserve_hosp_gsp", req, ['str', 'int'])

def get_the_prescr_rest(*req):
    return appel_refcursor("get_the_prescr_rest", req, ['str', 'int'])

def get_the_prescr_rest_gsp(*req):
    return appel_refcursor("get_the_prescr_rest_gsp", req, ['str', 'int'])

def get_the_delivr_rest(*req):
    return appel_refcursor("get_the_delivr_rest", req, ['str', 'int'])

def get_the_delivr_rest_gsp(*req):
    return appel_refcursor("get_the_delivr_rest_gsp", req, ['str', 'int'])

def get_the_gen_ref(*req):
    return appel_refcursor("get_the_gen_ref", req, ['str', 'int'])

def get_the_spe_dsp(*req):
    return appel_refcursor("get_the_spe_dsp", req, ['str', 'int'])

def get_the_gsp_dsp(*req):
    return appel_refcursor("get_the_gsp_dsp", req, ['str', 'int'])

def get_the_prix(*req):
    return appel_refcursor("get_the_prix", req, ['str', 'int'])

def get_the_atu(*req):
    return appel_refcursor("get_the_atu", req, ['str', 'int'])

def get_the_atu_gsp(*req):
    return appel_refcursor("get_the_atu_gsp", req, ['str', 'int'])

def get_the_vigi_conduct(*req):
    return appel_refcursor("get_the_vigi_conduct", req, ['str', 'int'])

def get_the_vigi_conduct_gsp(*req):
    return appel_refcursor("get_the_vigi_conduct_gsp", req, ['str', 'int'])

def get_the_atc_ddd_v2(*req):
    return appel_refcursor("get_the_atc_ddd_v2", req, ['str', 'int'])

def get_the_atc_ddd_gsp_v2(*req):
    return appel_refcursor("get_the_atc_ddd_gsp_v2", req, ['str', 'int'])

def get_the_solute(*req):
    return appel_refcursor("get_the_solute", req, ['str', 'int'])

def get_the_solute_gsp(*req):
    return appel_refcursor("get_the_solute_gsp", req, ['str', 'int'])

def get_the_virtuel(*req):
    return appel_refcursor("get_the_virtuel", req, ['str', 'int'])

def get_the_forme_spe_v2(*req):
    return appel_refcursor("get_the_forme_spe_v2", req, ['str', 'int'])

def get_the_forme_gsp(*req):
    return appel_refcursor("get_the_forme_gsp", req, ['str', 'int'])

def get_the_compo_spe(*req):
    return appel_refcursor("get_the_compo_spe", req, ['str', 'int'])

def get_the_compo_gsp(*req):
    return appel_refcursor("get_the_compo_gsp", req, ['str', 'int'])

def get_the_compo_synth_spe(*req):
    return appel_refcursor("get_the_compo_synth_spe", req, ['str', 'int'])

def get_the_compo_synth_gsp(*req):
    return appel_refcursor("get_the_compo_synth_gsp", req, ['str', 'int'])

def get_the_effet_notoire_spe(*req):
    return appel_refcursor("get_the_effet_notoire_spe", req, ['str', 'int'])

def get_the_effet_notoire_gsp(*req):
    return appel_refcursor("get_the_effet_notoire_gsp", req, ['str', 'int'])

def get_the_fic_info_thera(*req):
    return appel_refcursor("get_the_fic_info_thera", req, ['str'])

def get_the_fic_info_thera_gsp(*req):
    return appel_refcursor("get_the_fic_info_thera_gsp", req, ['str'])

def get_the_ter_cipemg_age(*req):
    return appel_refcursor("get_the_ter_cipemg_age", req, ['str', 'int', 'int'])

def get_the_ter_cipemg_age_gsp(*req):
    return appel_refcursor("get_the_ter_cipemg_age_gsp", req, ['str', 'int', 'int'])

def get_the_ter_cipemg_pds(*req):
    return appel_refcursor("get_the_ter_cipemg_pds", req, ['str', 'int', 'int'])

def get_the_ter_cipemg_pds_gsp(*req):
    return appel_refcursor("get_the_ter_cipemg_pds_gsp", req, ['str', 'int', 'int'])

def get_the_ter_cipemg_clr(*req):
    return appel_refcursor("get_the_ter_cipemg_clr", req, ['str', 'int', 'int'])

def get_the_ter_cipemg_clr_gsp(*req):
    return appel_refcursor("get_the_ter_cipemg_clr_gsp", req, ['str', 'int', 'int'])

def get_the_ter_cipemg_surf(*req):
    return appel_refcursor("get_the_ter_cipemg_surf", req, ['str', 'int', 'int'])

def get_the_ter_cipemg_sur_gsp(*req):
    return appel_refcursor("get_the_ter_cipemg_sur_gsp", req, ['str', 'int', 'int'])

def get_the_proc_spe(*req):
    return appel_refcursor("get_the_proc_spe", req, ['str', 'int'])

def get_the_proc_gsp(*req):
    return appel_refcursor("get_the_proc_gsp", req, ['str', 'int'])

def get_the_proc_spev2(*req):
    return appel_refcursor("get_the_proc_spev2", req, ['str', 'int', 'int'])

def get_the_proc_gspv2(*req):
    return appel_refcursor("get_the_proc_gspv2", req, ['str', 'int', 'int'])

def get_the_sexe_spe(*req):
    return appel_refcursor("get_the_sexe_spe", req, ['str', 'int'])

def get_the_sexe_gsp(*req):
    return appel_refcursor("get_the_sexe_gsp", req, ['str', 'int'])

def get_the_ter_cipemg_gr(*req):
    return appel_refcursor("get_the_ter_cipemg_gr", req, ['str', 'int', 'int'])

def get_the_ter_cipemg_gr_gsp(*req):
    return appel_refcursor("get_the_ter_cipemg_gr_gsp", req, ['str', 'int', 'int'])

def get_the_ter_cipemg_al(*req):
    return appel_refcursor("get_the_ter_cipemg_al", req, ['str', 'int'])

def get_the_ter_cipemg_al_gsp(*req):
    return appel_refcursor("get_the_ter_cipemg_al_gsp", req, ['str', 'int'])

def get_the_spe_to_hyper(*req):
    return appel_refcursor("get_the_spe_to_hyper", req, ['str'])

def get_the_gsp_to_hyper(*req):
    return appel_refcursor("get_the_gsp_to_hyper", req, ['str'])

def get_the_gsp_to_hyper_sac(*req):
    return appel_refcursor("get_the_gsp_to_hyper_sac", req, ['str'])

def get_the_hyper_to_spe(*req):
    return appel_refcursor("get_the_hyper_to_spe", req, ['str', 'int'])

def get_the_hyper_to_spe(*req):
    return appel_refcursor("get_the_hyper_to_spe", req, ['str', 'int'])

def get_the_indic_spe(*req):
    return appel_refcursor("get_the_indic_spe", req, ['str', 'int'])

def get_the_indic_gsp(*req):
    return appel_refcursor("get_the_indic_gsp", req, ['str', 'int'])

def get_the_cipe_spe_cim10(*req):
    return appel_refcursor("get_the_cipe_spe_cim10", req, ['str', 'int'])

def get_the_cipe_gsp_cim10(*req):
    return appel_refcursor("get_the_cipe_gsp_cim10", req, ['str', 'int'])

def get_the_indic_amm_ptt_tru(*req):
    return appel_refcursor("get_the_indic_amm_ptt_tru", req, ['str', 'int'])

def get_the_ind_amm_ptt_tru_gsp(*req):
    return appel_refcursor("get_the_ind_amm_ptt_tru_gsp", req, ['str', 'int'])

def get_the_inter_spe_sac(*req):
    return appel_refcursor("get_the_inter_spe_sac", req, ['str'])

def get_the_inter_gsp_sac(*req):
    return appel_refcursor("get_the_inter_gsp_sac", req, ['str'])

def get_the_incompat_spe_sac(*req):
    return appel_refcursor("get_the_incompat_spe_sac", req, ['str'])

def get_the_incompat_gsp_sac(*req):
    return appel_refcursor("get_the_incompat_gsp_sac", req, ['str'])

def get_the_pso_mm_by_spe(*req):
    return appel_refcursor("get_the_pso_mm_by_spe", req, ['str', 'int'])

def get_the_antibio_loc_spe(*req):
    return appel_refcursor("get_the_antibio_loc_spe", req, ['str', 'int'])

def get_the_antibio_syst_spe(*req):
    return appel_refcursor("get_the_antibio_syst_spe", req, ['str', 'int'])

def get_the_antibio_loc_gsp(*req):
    return appel_refcursor("get_the_antibio_loc_gsp", req, ['str', 'int'])

def get_the_antibio_syst_gsp(*req):
    return appel_refcursor("get_the_antibio_syst_gsp", req, ['str', 'int'])

def get_the_hypno_spe(*req):
    return appel_refcursor("get_the_hypno_spe", req, ['str', 'int'])

def get_the_hypno_gsp(*req):
    return appel_refcursor("get_the_hypno_gsp", req, ['str', 'int'])

def get_the_anxio_spe(*req):
    return appel_refcursor("get_the_anxio_spe", req, ['str', 'int'])

def get_the_anxio_gsp(*req):
    return appel_refcursor("get_the_anxio_gsp", req, ['str', 'int'])

def get_the_anticanc_spe(*req):
    return appel_refcursor("get_the_anticanc_spe", req, ['str', 'int'])

def get_the_anticanc_gsp(*req):
    return appel_refcursor("get_the_anticanc_gsp", req, ['str', 'int'])

def get_the_index_vacc(*req):
    return appel_refcursor("get_the_index_vacc", req, ['str', 'int'])

def get_the_unit_prise(*req):
    return appel_refcursor("get_the_unit_prise", req, ['str', 'int'])

def get_the_medic_except_spe(*req):
    return appel_refcursor("get_the_medic_except_spe", req, ['str', 'int'])

def get_the_medic_except_gsp(*req):
    return appel_refcursor("get_the_medic_except_gsp", req, ['str', 'int'])

def get_the_cfo_secable_spe(*req):
    return appel_refcursor("get_the_cfo_secable_spe", req, ['str', 'int'])

def get_the_admin_fo_solide_spe(*req):
    return appel_refcursor("get_the_admin_fo_solide_spe", req, ['str', 'int'])

def get_the_li_presc_spe(*req):
    return appel_refcursor("get_the_li_presc_spe", req, ['str', 'int'])

def get_the_cond_admin_spe(*req):
    return appel_refcursor("get_the_cond_admin_spe", req, ['str', 'int'])

def get_the_labo_exploit_spe(*req):
    return appel_refcursor("get_the_labo_exploit_spe", req, ['str', 'int'])

def get_the_pr_deriv_sang_spe(*req):
    return appel_refcursor("get_the_pr_deriv_sang_spe", req, ['str', 'int'])

def get_the_pr_deriv_sang_gsp(*req):
    return appel_refcursor("get_the_pr_deriv_sang_gsp", req, ['str', 'int'])

def get_the_medic_orph_spe(*req):
    return appel_refcursor("get_the_medic_orph_spe", req, ['str', 'int'])

def get_the_pgr_surv_renf_spe(*req):
    return appel_refcursor("get_the_pgr_surv_renf_spe", req, ['str', 'int'])

def get_the_comm_cipemg_spe(*req):
    return appel_refcursor("get_the_comm_cipemg_spe", req, ['str', 'int'])

def get_the_redond_spe(*req):
    return appel_refcursor("get_the_redond_spe", req, ['str', 'int'])

def get_the_spe_indic_by_cim10(*req):
    return appel_refcursor("get_the_spe_indic_by_cim10", req, ['str', 'int'])

def get_the_gsp_indic_by_cim10(*req):
    return appel_refcursor("get_the_gsp_indic_by_cim10", req, ['str', 'int'])

def get_the_info_spe(*req):
    return appel_refcursor("get_the_info_spe", req, ['str', 'int'])

def get_the_etat_commer_spe(*req):
    return appel_refcursor("get_the_etat_commer_spe", req, ['str', 'int'])

def get_the_effet_inde_spe(*req):
    return appel_refcursor("get_the_effet_inde_spe", req, ['str', 'int'])

def get_the_poso_v2(*req):
    return appel_refcursor("get_the_poso_v2", req, ['str', 'int'])

def get_the_compo_allsub_sp(*req):
    return appel_refcursor("get_the_compo_allsub_sp", req, ['int'])

def get_the_therap_anticanc(*req):
    return appel_refcursor("get_the_therap_anticanc", req, ['str', 'int'])

def get_the_delivre_max(*req):
    return appel_refcursor("get_the_delivre_max", req, ['int'])

def get_the_spe_is_or_bio(*req):
    return appel_refcursor("get_the_spe_is_or_bio", req, ['str'])

def get_the_spe_interop(*req):
    return appel_refcursor("get_the_spe_interop", req, ['str'])

def get_the_spe_hormono(*req):
    return appel_refcursor("get_the_spe_hormono", req, ['str', 'int'])

def get_the_gtiam_txt(*req):
    return appel_refcursor("get_the_gtiam_txt", req, ['str'])

def get_the_reserve_hosp_cip(*req):
    return appel_refcursor("get_the_reserve_hosp_cip", req, ['str', 'int'])
