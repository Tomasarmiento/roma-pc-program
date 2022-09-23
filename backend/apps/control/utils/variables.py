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
    'CH1_I_PS': False,
    'CH1_I_HO': False,
    'CH1_I_NPA': False,
    'CH1_I_NPR': False,
    'CH2_I_RA': False,
    'CH2_I_AL': False,
    'CH2_I_ID': False,
    'CH2_I_MB': False,
    'CH2_I_PS': False,
    'CH2_I_HO': False,
    'CH2_I_NPA': False,
    'CH2_I_NPR': False,
    'CH3_I_RA': False,
    'CH3_I_AL': False,
    'CH3_I_ID': False,
    'CH3_I_MB': False,
    'CH3_I_PS': False,
    'CH3_I_HO': False,
    'CH3_I_NPA': False,
    'CH3_I_NPR': False,
    'CH4_I_RA': False,
    'CH4_I_AL': False,
    'CH4_I_ID': False,
    'CH4_I_MB': False,
    'CH4_I_PS': False,
    'CH4_I_HO': False,
    'CH4_I_NPA': False,
    'CH4_I_NPR': False,

    'R_I_AL': False,
    'R_I_HF': False,
    'R_I_ID': False,
    'R_I_RUT_1': False,
    'R_I_RUT_2': False,
    'R_I_RUT_3': False,
    'R_I_RUT_4': False,
    'R_I_RUT_5': False,
    'R_I_RUT_6': False,
    'R_I_RUT_7': False,
    'R_I_RUT_8': False,
    'R_I_RUT_9': False,#id es 300 y aca 53
    'R_I_RUT_10': False,#id es 300 y aca 53
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


    'GRL_I_EMS': False,
    'System_Active': False,
    'Start_system_button': False,
    'Stop_system_button': False,
    'Emergency': False,
    'Robot_GO': False,
    'Robot_IDLE': False,
    'Trig_MA1DRU1': False,
    'MA1_DR_U_1_OP40': False,
    'Trig_MA1DRU2': False,
    'MA1_DR_U_2_OP40': False,
    'Gen_Program': False,
    'unblock_pallet': False,
    'unblocked_pallet_sensor': False,
    'neumatic_forward': False,
    'neumatic_advance': False,
    'INF30': False,
    'Blower': False,
    'Booster': False,
    'INF40': False,
    'pallet_sensor': False,
    'MA1_DR_D_1_OP20': False,
    'MA1_DR_D_2_OP20': False,
    'MA1_DR_U_1_OP20': False,
    'MA1_DR_U_2_OP20': False,
    'OP20_available': False,
    'Trig_MA1DRD1': False,
    'MA1_DR_D_2_OP40': False,
    'Trig_MA1DRD2': False,
    'MA1_DR_D_1_OP40': False,
    'R_I_MA1F': False,
    'R_I_MA2F': False,
    'okuma_available': False,
    'M_PRG_0': False,
    'M_PRG_1': False,
    'M_PRG_2': False,
    'M_PRG_3': False,
    'M_PRG_4': False,
    'M_PRG_5': False,
    'M_PRG_6': False,
    'M_PRG_7': False,
    'gen': False,
}

PLC_VARIABLES = {
}

# -------------------------------------------------------------------------------------------- #
# ------------------------------ PLC DIRECCIONAMIENTOS --------------------------------------- #
# -------------------------------------------------------------------------------------------- #

LIST_OF_DIRECTIONS = [
"CH1_I_RA","CH1_I_AL","CH1_I_ID","CH1_I_MB","CH1_I_PS","CH1_I_HO","CH1_I_NPA","CH1_I_NPR",
"CH2_I_RA","CH2_I_AL","CH2_I_ID","CH2_I_MB","CH2_I_PS","CH2_I_HO","CH2_I_NPA","CH2_I_NPR",
"CH3_I_RA","CH3_I_AL","CH3_I_ID","CH3_I_MB","CH3_I_PS","CH3_I_HO","CH3_I_NPA","CH3_I_NPR",
"CH4_I_RA","CH4_I_AL","CH4_I_ID","CH4_I_MB","CH4_I_PS","CH4_I_HO","CH4_I_NPA","CH4_I_NPR",

"R_I_AL","R_I_HF","R_I_ID",
"R_I_RUT_1","R_I_RUT_2","R_I_RUT_3","R_I_RUT_4","R_I_RUT_5","R_I_RUT_6","R_I_RUT_7","R_I_RUT_8","R_I_RUT_9","R_I_RUT_10",
"R_I_G1_PS","R_I_G2_PS","R_I_FLS","R_I_RLS",

"MA1_I_DR_U_PS_1","MA1_I_DR_U_PS_2","MA1_I_DR_D_PS_1","MA1_I_DR_D_PS_2","MA1_I_GS_UP",
"MA1_I_GS_DN","MA1_I_DR_U_ES_1","MA1_I_DR_U_ES_2","MA1_I_DR_D_ES_1","MA1_I_DR_D_ES_2",
"MA1_I_DR_U_NS","MA1_I_DR_D_NS","MA1_I_DR_U_BP_1_SA","MA1_I_DR_U_BP_1_SR","MA1_I_DR_U_BP_2_SA",
"MA1_I_DR_U_BP_2_SR","MA1_I_DR_D_BP_1_SA","MA1_I_DR_D_BP_1_SR","MA1_I_DR_D_BP_2_SA","MA1_I_DR_D_BP_2_SR","MA1_I_OB","MA1_I_EMS",


"MA2_I_DR_U_PS_1","MA2_I_DR_U_PS_2","MA2_I_DR_D_PS_1","MA2_I_DR_D_PS_2","MA2_I_GS_UP",
"MA2_I_GS_DN","MA2_I_DR_U_ES_1","MA2_I_DR_U_ES_2","MA2_I_DR_D_ES_1","MA2_I_DR_D_ES_2",
"MA2_I_DR_U_NS","MA2_I_DR_D_NS","MA2_I_DR_U_BP_1_SA","MA2_I_DR_U_BP_1_SR","MA2_I_DR_U_BP_2_SA",
"MA2_I_DR_U_BP_2_SR","MA2_I_DR_D_BP_1_SA","MA2_I_DR_D_BP_1_SR","MA2_I_DR_D_BP_2_SA","MA2_I_DR_D_BP_2_SR","MA2_I_OB","MA2_I_EMS",


"GRL_I_EMS","System_Active",
"Start_system_button","Stop_system_button","Emergency","Robot_GO","Robot_IDLE","Trig_MA1DRU1",
"MA1_DR_U_1_OP40","Trig_MA1DRU2","MA1_DR_U_2_OP40","Gen_Program","unblock_pallet","unblocked_pallet_sensor",
"neumatic_forward","neumatic_advance","INF30","Blower","Booster","INF40","pallet_sensor",
"MA1_DR_D_1_OP20","MA1_DR_D_2_OP20","MA1_DR_U_1_OP20","MA1_DR_U_2_OP20","OP20_available",
"Trig_MA1DRD1","MA1_DR_D_2_OP40","Trig_MA1DRD2","MA1_DR_D_1_OP40","R_I_MA1F","R_I_MA2F","okuma_available",
"M_PRG_0","M_PRG_1","M_PRG_2","M_PRG_3","M_PRG_4","M_PRG_5","M_PRG_6","M_PRG_7","gen",
]


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