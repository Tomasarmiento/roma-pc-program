# -------------------------------------------------------------------------------------------- #
# ---------------------------------- Parts parameters ---------------------------------------- #
# -------------------------------------------------------------------------------------------- #
PLC_TOKEN = {
    "token" : 0,
}

PLC_DEFAULT_VARIABLES = {
    'CH1_I_RA': False,
    'CH1_I_AL': False,
    'CH1_I_ID': False,
    'CH1_I_MB': False,
    'CH1_I_PSA': False,
    'CH1_I_HO': False,
    'CH1_I_NPA': False,
    'CH1_I_NPR': False,

    'CH2_I_RA': False,
    'CH2_I_AL': False,
    'CH2_I_ID': False,
    'CH2_I_MB': False,
    'CH2_I_PSA': False,
    'CH2_I_HO': False,
    'CH2_I_NPA': False,
    'CH2_I_NPR': False,

    'CH3_I_RA': False,
    'CH3_I_AL': False,
    'CH3_I_ID': False,
    'CH3_I_MB': False,
    'CH3_I_PSA': False,
    'CH3_I_HO': False,
    'CH3_I_NPA': False,
    'CH3_I_NPR': False,

    'CH4_I_RA': False,
    'CH4_I_AL': False,
    'CH4_I_ID': False,
    'CH4_I_MB': False,
    'CH4_I_PSA': False,
    'CH4_I_HO': False,
    'CH4_I_NPA': False,
    'CH4_I_NPR': False,

    'R_I_AL': False,
    'R_I_HF': False,
    'R_I_ID': False,
    'R_I_AUT_SEM': False,####
    'R_I_30_40': False,
    'R_I_CAS': False,
    'R_I_BIT0_CH': False,
    'R_I_BIT1_CH': False,
    'R_I_PAL': False,
    'R_I_DRW': False,
    'R_I_MA': False,
    'R_I_GET_PUT': False,
    'R_I_MA_CH': False,########
    'R_I_G1_PS': False,
    'R_I_G2_PS': False,
    'R_I_FLS': False,
    'R_I_RLS': False,

    'MA1_I_DR_U_PS_1': False,
    'MA1_I_DR_U_PS_2': False,
    'MA1_I_DR_D_PS_1': False,
    'MA1_I_DR_D_PS_2': False,
    'MA1_I_GS_UP': False,
    'MA1_I_GS_DN': False,
    'MA1_I_DR_U_ES_1': False,
    'MA1_I_DR_U_ES_2': False,
    'MA1_I_DR_D_ES_1': False,
    'MA1_I_DR_D_ES_2': False,
    'MA1_I_DR_U_NS': False,
    'MA1_I_DR_D_NS': False,
    'MA1_I_DR_U_BP_1_SA': False,
    'MA1_I_DR_U_BP_1_SR': False,
    'MA1_I_DR_U_BP_2_SA': False,
    'MA1_I_DR_U_BP_2_SR': False,
    'MA1_I_DR_D_BP_1_SA': False,
    'MA1_I_DR_D_BP_1_SR': False,
    'MA1_I_DR_D_BP_2_SA': False,
    'MA1_I_DR_D_BP_2_SR': False,
    'MA1_I_OB': False,
    'MA1_I_EMS': False,


    'MA2_I_DR_U_PS_1': False,
    'MA2_I_DR_U_PS_2': False,
    'MA2_I_DR_D_PS_1': False,
    'MA2_I_DR_D_PS_2': False,
    'MA2_I_GS_UP': False,
    'MA2_I_GS_DN': False,
    'MA2_I_DR_U_ES_1': False,
    'MA2_I_DR_U_ES_2': False,
    'MA2_I_DR_D_ES_1': False,
    'MA2_I_DR_D_ES_2': False,
    'MA2_I_DR_U_NS': False,
    'MA2_I_DR_D_NS': False,
    'MA2_I_DR_U_BP_1_SA': False,
    'MA2_I_DR_U_BP_1_SR': False,
    'MA2_I_DR_U_BP_2_SA': False,
    'MA2_I_DR_U_BP_2_SR': False,
    'MA2_I_DR_D_BP_1_SA': False,
    'MA2_I_DR_D_BP_1_SR': False,
    'MA2_I_DR_D_BP_2_SA': False,
    'MA2_I_DR_D_BP_2_SR': False,
    'MA2_I_OB': False,
    'MA2_I_EMS': False,


    'Emergency': False,
    'Robot_IDLE': False,


    '.emergency_active':False,
    '.ma1_drd_endstops':False,
    '.ma1_dru_endstops':False,
    '.ma1_gs_dn':False,
    '.ma1_nsense':False,
    '.r_program':False,
    '.r_gp1_not_free':False,
    '.r_gp2_not_free':False,
    '.r_not_idle':False,
    '.r_not_home':False,
    '.r_alarm':False,
    '.r_flimit':False,
    '.r_rlimit':False,
    '.ch1_nsense_ret':False,
    '.ch1_alarm':False,
    '.init_error':False,
    '.max_unblock_error':False,
    '.max_pallet_present':False,
    '.max_dr_position':False,
    '.chx_robot_not_allowed':False,
    '.chx_pressure_error':False,
    '.chx_nsense_adv':False,
    '.chx_nsense_ret':False,
    '.chx_alarm':False,
    '.chx_not_available':False,
}

PLC_VARIABLES = {
    

}

# -------------------------------------------------------------------------------------------- #
# ------------------------------ PLC DIRECCIONAMIENTOS --------------------------------------- #
# -------------------------------------------------------------------------------------------- #

LIST_OF_DIRECTIONS = [
"CH1_I_RA","CH1_I_AL","CH1_I_ID","CH1_I_MB","CH1_I_PSA","CH1_I_HO","CH1_I_NPA","CH1_I_NPR",
"CH2_I_RA","CH2_I_AL","CH2_I_ID","CH2_I_MB","CH2_I_PSA","CH2_I_HO","CH2_I_NPA","CH2_I_NPR",
"CH3_I_RA","CH3_I_AL","CH3_I_ID","CH3_I_MB","CH3_I_PSA","CH3_I_HO","CH3_I_NPA","CH3_I_NPR",
"CH4_I_RA","CH4_I_AL","CH4_I_ID","CH4_I_MB","CH4_I_PSA","CH4_I_HO","CH4_I_NPA","CH4_I_NPR",

"R_I_AL","R_I_HF","R_I_ID",
"R_I_AUT_SEM","R_I_30_40","R_I_CAS","R_I_BIT0_CH","R_I_BIT1_CH","R_I_PAL","R_I_DRW","R_I_MA","R_I_GET_PUT","R_I_MA_CH",
"R_I_G1_PS","R_I_G2_PS","R_I_FLS","R_I_RLS",

"MA1_I_DR_U_PS_1","MA1_I_DR_U_PS_2","MA1_I_DR_D_PS_1","MA1_I_DR_D_PS_2","MA1_I_GS_UP",
"MA1_I_GS_DN","MA1_I_DR_U_ES_1","MA1_I_DR_U_ES_2","MA1_I_DR_D_ES_1","MA1_I_DR_D_ES_2",
"MA1_I_DR_U_NS","MA1_I_DR_D_NS","MA1_I_DR_U_BP_1_SA","MA1_I_DR_U_BP_1_SR","MA1_I_DR_U_BP_2_SA",
"MA1_I_DR_U_BP_2_SR","MA1_I_DR_D_BP_1_SA","MA1_I_DR_D_BP_1_SR","MA1_I_DR_D_BP_2_SA","MA1_I_DR_D_BP_2_SR","MA1_I_OB","MA1_I_EMS",


"MA2_I_DR_U_PS_1","MA2_I_DR_U_PS_2","MA2_I_DR_D_PS_1","MA2_I_DR_D_PS_2","MA2_I_GS_UP",
"MA2_I_GS_DN","MA2_I_DR_U_ES_1","MA2_I_DR_U_ES_2","MA2_I_DR_D_ES_1","MA2_I_DR_D_ES_2",
"MA2_I_DR_U_NS","MA2_I_DR_D_NS","MA2_I_DR_U_BP_1_SA","MA2_I_DR_U_BP_1_SR","MA2_I_DR_U_BP_2_SA",
"MA2_I_DR_U_BP_2_SR","MA2_I_DR_D_BP_1_SA","MA2_I_DR_D_BP_1_SR","MA2_I_DR_D_BP_2_SA","MA2_I_DR_D_BP_2_SR","MA2_I_OB","MA2_I_EMS","Emergency","Robot_IDLE",

    '.emergency_active',
    '.ma1_drd_endstops',
    '.ma1_dru_endstops',
    '.ma1_gs_dn',
    '.ma1_nsense',
    '.r_program',
    '.r_gp1_not_free',
    '.r_gp2_not_free',
    '.r_not_idle',
    '.r_not_home',
    '.r_alarm',
    '.r_flimit',
    '.r_rlimit',
    '.ch1_nsense_ret',
    '.ch1_alarm',
    '.init_error',
    '.max_unblock_error',
    '.max_pallet_present',
    '.max_dr_position',
    '.chx_robot_not_allowed',
    '.chx_pressure_error',
    '.chx_nsense_adv',
    '.chx_nsense_ret',
    '.chx_alarm',
    '.chx_not_available',
]

MSG_ERROR_DIRECTIONS = [
    '.emergency_active',
    '.ma1_drd_endstops',
    '.ma1_dru_endstops',
    '.ma1_gs_dn',
    '.ma1_nsense',
    '.r_program',
    '.r_gp1_not_free',
    '.r_gp2_not_free',
    '.r_not_idle',
    '.r_not_home',
    '.r_alarm',
    '.r_flimit',
    '.r_rlimit',
    '.ch1_nsense_ret',
    '.ch1_alarm',
    '.init_error',
    '.max_unblock_error',
    '.max_pallet_present',
    '.max_dr_position',
    '.chx_robot_not_allowed',
    '.chx_pressure_error',
    '.chx_nsense_adv',
    '.chx_nsense_ret',
    '.chx_alarm',
    '.chx_not_available',
]

#error messages

MSG_ERROR_CODIFICATION = {
    '.emergency_active':'error emergencia activa',
    '.ma1_drd_endstops':'error diferencia endstops ma1 drawer down',
    '.ma1_dru_endstops':'error diferencia endstops ma1 drawer up',
    '.ma1_gs_dn':'error sensor persiana baja',
    '.ma1_nsense':'error sensor neumatico del otro cajón',
    '.r_program':'error diferencia entre programa (bits) kuka y plc',
    '.r_gp1_not_free':'error gripper 1 con pieza',
    '.r_gp2_not_free':'error gripper 2 con pieza',
    '.r_not_idle':'error robot sin idle',
    '.r_not_home':'error robot sin home flag',
    '.r_alarm':'error alarma de robot',
    '.r_flimit':'error forward limit sensor',
    '.r_rlimit':'error reverse limit sensor',
    '.ch1_nsense_ret':'error okuma 1 neumatica no retraida',
    '.ch1_alarm':'error okuma 1 alarma',
    '.init_error':'error en check inicial',
    '.max_unblock_error':'error desbloqueo pallet',
    '.max_pallet_present':'error hay un pallet en la posición',
    '.max_dr_position':'error ma1 posicion drawer',
    '.chx_robot_not_allowed':'error de ingreso robot',
    '.chx_pressure_error':'error presion neumatica',
    '.chx_nsense_adv':'error sensor avance neumatico',
    '.chx_nsense_ret':'error sensor retroceso neumatico',
    '.chx_alarm':'error alarma okuma',
    '.chx_not_available':'error okuma no disponible',
}




# -------------------------------------------------------------------------------------------- #
# ---------------------------------- Routines Parameters ------------------------------------- #
# -------------------------------------------------------------------------------------------- #


OKUMA = {
    'okuma_1' : 1,
    'okuma_2' : 2,
    'okuma_3' : 3,
    'okuma_4' : 4,
    'okuma_current_selected': 0,
}

MESA = {
    'mesa_1' : 1,
    'mesa_2' : 2,
    'mesa_current_selected': 0,
}


# -------------------------------------------------------------------------------------------- #
# ----------------------------------- ROUTING PROGRAM ---------------------------------------- #
# -------------------------------------------------------------------------------------------- #

M_PROGS_SEMIAUTO = {
    'M_PRG_AUT_SEMI' : False,
    'M_PRG_30_40' : False,
    'M_PRG_CAS' : False,
    'M_PRG_BIT0_CH': False,
    'M_PRG_BIT1_CH': False,
    'M_PRG_PAL': False,
    'M_PRG_DRW': False,
    'M_PRG_MA': False,
    'M_PRG_GET_PUT': False,
    'M_PRG_MA_CH': False,
}