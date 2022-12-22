import json
import http.client
import time

import urllib3
from urllib3.exceptions import InsecureRequestWarning
import urllib
import os

from pickle import TRUE
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect



from apps.ws.utils.functions import send_front_message
from apps.ws.utils.variables import frontState,WEBSOCKET
from apps.service.api.protocols import OPCProtocol



from apps.parameters.utils.functions import toggle_disable_machine
from apps.parameters.models import Parameter

from apps.control.utils.variables import OKUMA,MESA,PLC_TOKEN,M_PROGS_SEMIAUTO,PLC_DEFAULT_VARIABLES
from apps.control.utils.functions import derived_sensores_states,obtain_token_plc,send_message_semi,send_message_auto,FrontWs,sensores_states_plc




@csrf_exempt
def msge_test(request):
    OPCProtocol().write_value_bool('ns=3;s="tags"."Man_MA1_CG"',False)
    
    if (PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_1"] == True) and (PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_2"] == True) and (PLC_DEFAULT_VARIABLES["MA1_I_DR_D_NS"] == True):
        OPCProtocol().write_value_bool('ns=3;s="tags"."Man_MA1_DRU_FD"',False)
        OPCProtocol().write_value_bool('ns=3;s="tags"."Man_MA1_DRD_FD"',True)
        time.sleep(5)
        if PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_1"] == False and PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_2"] == False and PLC_DEFAULT_VARIABLES["MA1_I_DR_D_NS"] == False:
            OPCProtocol().write_value_bool('ns=3;s="tags"."Man_MA1_CG"',True)

    elif PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_1"] == False and PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_2"] == False and PLC_DEFAULT_VARIABLES["MA1_I_DR_D_NS"] == False:
        OPCProtocol().write_value_bool('ns=3;s="tags"."Man_MA1_DRU_FD"',True)
        OPCProtocol().write_value_bool('ns=3;s="tags"."Man_MA1_DRD_FD"',False)
        time.sleep(5)
        print(PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_1"],PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_2"],PLC_DEFAULT_VARIABLES["MA1_I_DR_D_NS"])

        if PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_1"] == True and PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_2"] == True and PLC_DEFAULT_VARIABLES["MA1_I_DR_D_NS"] == False:
            OPCProtocol().write_value_bool('ns=3;s="tags"."Man_MA1_CG"',True)

    
    return JsonResponse({})


# @csrf_exempt
# def msge_test(request):
#     print("acaaa2")
#     inicio = time.time()
#     import http.client
#     import ssl

#     # c = urllib3.HTTPSConnectionPool('192.168.3.150', port=8000, cert_reqs='CERT_NONE',assert_hostname=False)
#     # c.request('POST', '/api/jsonrpc',body=payload,headers=header)


#     header = {
#         'X-Auth-Token': PLC_TOKEN['token'],
#         'Content-Type': 'application/json',
#     }

#     payload = json.dumps([{"jsonrpc":"2.0","id":"1","method":"PlcProgram.Read","params":{"var":"\"CH1_I_M181\""}},])

#     http = urllib3.PoolManager()

#     # response = http.request('POST', "https://192.168.3.150/api/jsonrpc",body=payload,headers=header)

#     c = urllib3.HTTPSConnectionPool('192.168.3.150', cert_reqs='CERT_NONE',assert_hostname=False)
#     c.request('POST', '/api/jsonrpc',body=payload,headers=header)
#     # c.status # ensure this equals 200, or otherwise handle it
#     # c.data # the response text as bytes

#     delta = time.time() - inicio
#     print("tiempo",delta)
#     return JsonResponse({})



@csrf_exempt
def token_register(request):
    msg = 'hello world'
    frontState.log_messages.append(msg)
    print()



@csrf_exempt
def disable_okuma(request):
    post_req = request.POST
    model_machine = post_req['model_machine']
    model_machine2 = str(model_machine)
    toggle_disable_machine(model_machine2)
    print("enter to button")
    
    return JsonResponse({})



#funcion para pedir de a un solo dato en hash1
@csrf_exempt
def switch_led_state_off(request):
    print("click")
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    conn = http.client.HTTPSConnection("192.168.3.150")
    payload = json.dumps([
    # {"jsonrpc":"2.0","id":"1","method":"PlcProgram.Read","params":{"var":"\"CH1_I_M181\""}},
    # {"jsonrpc":"2.0","id":"2","method":"PlcProgram.Read","params":{"var":"\"CH1_I_AL\""}},
    # {"jsonrpc":"2.0","id":"3","method":"PlcProgram.Read","params":{"var":"\"CH1_I_M182\""}},
    # {"jsonrpc":"2.0","id":"4","method":"PlcProgram.Read","params":{"var":"\"CH1_I_M183\""}},
    # {"jsonrpc":"2.0","id":"5","method":"PlcProgram.Read","params":{"var":"\"CH1_I_PSA\""}},
    # # {"jsonrpc":"2.0","id":"6","method":"PlcProgram.Read","params":{"var":"\"CH1_I_HO\""}},#ACA
    # {"jsonrpc":"2.0","id":"7","method":"PlcProgram.Read","params":{"var":"\"CH1_I_NPA\""}},
    # {"jsonrpc":"2.0","id":"8","method":"PlcProgram.Read","params":{"var":"\"CH1_I_NPR\""}},
    # {"jsonrpc":"2.0","id":"9","method":"PlcProgram.Read","params":{"var":"\"CH2_I_RA\""}},
    # {"jsonrpc":"2.0","id":"10","method":"PlcProgram.Read","params":{"var":"\"CH2_I_AL\""}},
    # {"jsonrpc":"2.0","id":"11","method":"PlcProgram.Read","params":{"var":"\"CH2_I_ID\""}},
    # {"jsonrpc":"2.0","id":"12","method":"PlcProgram.Read","params":{"var":"\"CH2_I_MB\""}},
    # {"jsonrpc":"2.0","id":"13","method":"PlcProgram.Read","params":{"var":"\"CH2_I_PSA\""}},
    # {"jsonrpc":"2.0","id":"14","method":"PlcProgram.Read","params":{"var":"\"CH2_I_HO\""}},
    # {"jsonrpc":"2.0","id":"15","method":"PlcProgram.Read","params":{"var":"\"CH2_I_NPA\""}},
    # {"jsonrpc":"2.0","id":"16","method":"PlcProgram.Read","params":{"var":"\"CH2_I_NPR\""}},
    # {"jsonrpc":"2.0","id":"17","method":"PlcProgram.Read","params":{"var":"\"CH3_I_RA\""}},
    # {"jsonrpc":"2.0","id":"18","method":"PlcProgram.Read","params":{"var":"\"CH3_I_AL\""}},
    # {"jsonrpc":"2.0","id":"19","method":"PlcProgram.Read","params":{"var":"\"CH3_I_ID\""}},
    # {"jsonrpc":"2.0","id":"20","method":"PlcProgram.Read","params":{"var":"\"CH3_I_MB\""}},
    # {"jsonrpc":"2.0","id":"21","method":"PlcProgram.Read","params":{"var":"\"CH3_I_PSA\""}},
    # {"jsonrpc":"2.0","id":"22","method":"PlcProgram.Read","params":{"var":"\"CH3_I_HO\""}},
    # {"jsonrpc":"2.0","id":"23","method":"PlcProgram.Read","params":{"var":"\"CH3_I_NPA\""}},
    # {"jsonrpc":"2.0","id":"24","method":"PlcProgram.Read","params":{"var":"\"CH3_I_NPR\""}},
    # {"jsonrpc":"2.0","id":"25","method":"PlcProgram.Read","params":{"var":"\"CH4_I_RA\""}},
    # {"jsonrpc":"2.0","id":"26","method":"PlcProgram.Read","params":{"var":"\"CH4_I_AL\""}},
    # {"jsonrpc":"2.0","id":"27","method":"PlcProgram.Read","params":{"var":"\"CH4_I_ID\""}},
    # {"jsonrpc":"2.0","id":"28","method":"PlcProgram.Read","params":{"var":"\"CH4_I_MB\""}},
    # {"jsonrpc":"2.0","id":"29","method":"PlcProgram.Read","params":{"var":"\"CH4_I_PSA\""}},
    # {"jsonrpc":"2.0","id":"30","method":"PlcProgram.Read","params":{"var":"\"CH4_I_HO\""}},
    # {"jsonrpc":"2.0","id":"31","method":"PlcProgram.Read","params":{"var":"\"CH4_I_NPA\""}},
    # {"jsonrpc":"2.0","id":"32","method":"PlcProgram.Read","params":{"var":"\"CH4_I_NPR\""}},
    # {"jsonrpc":"2.0","id":"33","method":"PlcProgram.Read","params":{"var":"\"R_I_AL\""}},
    # {"jsonrpc":"2.0","id":"34","method":"PlcProgram.Read","params":{"var":"\"R_I_HF\""}},
    # {"jsonrpc":"2.0","id":"35","method":"PlcProgram.Read","params":{"var":"\"R_I_ID\""}},
    # {"jsonrpc":"2.0","id":"44","method":"PlcProgram.Read","params":{"var":"\"R_I_G1_PS\""}},
    # {"jsonrpc":"2.0","id":"45","method":"PlcProgram.Read","params":{"var":"\"R_I_G2_PS\""}},
    # {"jsonrpc":"2.0","id":"46","method":"PlcProgram.Read","params":{"var":"\"R_I_FLS\""}},
    # {"jsonrpc":"2.0","id":"47","method":"PlcProgram.Read","params":{"var":"\"R_I_RLS\""}},
    # {"jsonrpc":"2.0","id":"48","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_PS_1\""}},
    # {"jsonrpc":"2.0","id":"49","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_PS_2\""}},
    # {"jsonrpc":"2.0","id":"50","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_PS_1\""}},
    # {"jsonrpc":"2.0","id":"51","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_PS_2\""}},
    # {"jsonrpc":"2.0","id":"52","method":"PlcProgram.Read","params":{"var":"\"MA1_I_GS_UP\""}},
    # {"jsonrpc":"2.0","id":"53","method":"PlcProgram.Read","params":{"var":"\"MA1_I_GS_DN\""}},
    # {"jsonrpc":"2.0","id":"54","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_ES_1\""}},
    # {"jsonrpc":"2.0","id":"55","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_ES_2\""}},
    # {"jsonrpc":"2.0","id":"56","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_ES_1\""}},
    # {"jsonrpc":"2.0","id":"57","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_ES_2\""}},
    # {"jsonrpc":"2.0","id":"58","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_NS\""}},
    # {"jsonrpc":"2.0","id":"59","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_NS\""}},
    # {"jsonrpc":"2.0","id":"60","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_BP_1_SA\""}},
    # {"jsonrpc":"2.0","id":"61","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_BP_1_SR\""}},
    # {"jsonrpc":"2.0","id":"62","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_BP_2_SA\""}},
    # {"jsonrpc":"2.0","id":"63","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_BP_2_SR\""}},
    # {"jsonrpc":"2.0","id":"64","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_BP_1_SA\""}},
    # {"jsonrpc":"2.0","id":"65","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_BP_1_SR\""}},
    # {"jsonrpc":"2.0","id":"66","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_BP_2_SA\""}},
    # {"jsonrpc":"2.0","id":"67","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_BP_2_SR\""}},
    # {"jsonrpc":"2.0","id":"68","method":"PlcProgram.Read","params":{"var":"\"MA1_I_OB\""}},
    # {"jsonrpc":"2.0","id":"69","method":"PlcProgram.Read","params":{"var":"\"MA1_I_EMS\""}},
    # {"jsonrpc":"2.0","id":"70","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_PS_1\""}},
    # {"jsonrpc":"2.0","id":"71","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_PS_2\""}},
    # {"jsonrpc":"2.0","id":"72","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_PS_1\""}},
    # {"jsonrpc":"2.0","id":"73","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_PS_2\""}},
    # {"jsonrpc":"2.0","id":"74","method":"PlcProgram.Read","params":{"var":"\"MA2_I_GS_UP\""}},
    # {"jsonrpc":"2.0","id":"75","method":"PlcProgram.Read","params":{"var":"\"MA2_I_GS_DN\""}},
    # {"jsonrpc":"2.0","id":"76","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_ES_1\""}},
    # {"jsonrpc":"2.0","id":"77","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_ES_2\""}},
    # {"jsonrpc":"2.0","id":"78","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_ES_1\""}},
    # {"jsonrpc":"2.0","id":"79","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_ES_2\""}},
    # {"jsonrpc":"2.0","id":"80","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_NS\""}},
    # {"jsonrpc":"2.0","id":"81","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_NS\""}},
    # {"jsonrpc":"2.0","id":"82","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_BP_1_SA\""}},
    # {"jsonrpc":"2.0","id":"83","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_BP_1_SR\""}},
    # {"jsonrpc":"2.0","id":"84","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_BP_2_SA\""}},
    # {"jsonrpc":"2.0","id":"85","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_BP_2_SR\""}},
    # {"jsonrpc":"2.0","id":"86","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_BP_1_SA\""}},
    # {"jsonrpc":"2.0","id":"87","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_BP_1_SR\""}},
    # {"jsonrpc":"2.0","id":"88","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_BP_2_SA\""}},
    # {"jsonrpc":"2.0","id":"89","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_BP_2_SR\""}},
    # {"jsonrpc":"2.0","id":"90","method":"PlcProgram.Read","params":{"var":"\"MA2_I_OB\""}},
    # {"jsonrpc":"2.0","id":"91","method":"PlcProgram.Read","params":{"var":"\"MA2_I_EMS\""}},
    # {"jsonrpc":"2.0","id":"96","method":"PlcProgram.Read","params":{"var":"\"Emergency\""}},
    # {"jsonrpc":"2.0","id":"98","method":"PlcProgram.Read","params":{"var":"\"Robot_IDLE\""}},
    # {"jsonrpc":"2.0","id":"99","method":"PlcProgram.Read","params":{"var":"\"R_I_AUT_SEM\""}},
    # {"jsonrpc":"2.0","id":"100","method":"PlcProgram.Read","params":{"var":"\"R_I_30_40\""}},
    # {"jsonrpc":"2.0","id":"101","method":"PlcProgram.Read","params":{"var":"\"R_I_CAS\""}},
    # {"jsonrpc":"2.0","id":"102","method":"PlcProgram.Read","params":{"var":"\"R_I_BIT0_CH\""}},
    # {"jsonrpc":"2.0","id":"103","method":"PlcProgram.Read","params":{"var":"\"R_I_BIT1_CH\""}},
    # {"jsonrpc":"2.0","id":"104","method":"PlcProgram.Read","params":{"var":"\"R_I_PAL\""}},
    # {"jsonrpc":"2.0","id":"105","method":"PlcProgram.Read","params":{"var":"\"R_I_DRW\""}},
    # {"jsonrpc":"2.0","id":"106","method":"PlcProgram.Read","params":{"var":"\"R_I_MA\""}},
    # {"jsonrpc":"2.0","id":"107","method":"PlcProgram.Read","params":{"var":"\"R_I_GET_PUT\""}},
    # {"jsonrpc":"2.0","id":"108","method":"PlcProgram.Read","params":{"var":"\"R_I_MA_CH\""}},
    # {"jsonrpc":"2.0","id":"109","method":"PlcProgram.Read","params":{"var":"\"Robot_GO\""}},
    # {"jsonrpc":"2.0","id":"110","method":"PlcProgram.Read","params":{"var":"\"GRL_I_EMS\""}},
    # {"jsonrpc":"2.0","id":"111","method":"PlcProgram.Read","params":{"var":"\"System_Active\""}},
    # {"jsonrpc":"2.0","id":"112","method":"PlcProgram.Read","params":{"var":"\"Start_system_button\""}},
    # {"jsonrpc":"2.0","id":"113","method":"PlcProgram.Read","params":{"var":"\"Stop_system_button\""}},
    # # {"jsonrpc":"2.0","id":"114","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_U_1_OP40\""}},
    # # {"jsonrpc":"2.0","id":"115","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_U_2_OP40\""}},
    # {"jsonrpc":"2.0","id":"116","method":"PlcProgram.Read","params":{"var":"\"Gen_Program\""}},
    # {"jsonrpc":"2.0","id":"117","method":"PlcProgram.Read","params":{"var":"\"unblock_pallet\""}},
    # {"jsonrpc":"2.0","id":"118","method":"PlcProgram.Read","params":{"var":"\"unblocked_pallet_sensor\""}},
    # {"jsonrpc":"2.0","id":"119","method":"PlcProgram.Read","params":{"var":"\"neumatic_forward\""}},
    # {"jsonrpc":"2.0","id":"120","method":"PlcProgram.Read","params":{"var":"\"neumatic_advanced\""}},
    # {"jsonrpc":"2.0","id":"121","method":"PlcProgram.Read","params":{"var":"\"INF30\""}},
    # {"jsonrpc":"2.0","id":"122","method":"PlcProgram.Read","params":{"var":"\"Blower\""}},
    # {"jsonrpc":"2.0","id":"123","method":"PlcProgram.Read","params":{"var":"\"Booster\""}},
    # {"jsonrpc":"2.0","id":"124","method":"PlcProgram.Read","params":{"var":"\"INF40\""}},
    # {"jsonrpc":"2.0","id":"125","method":"PlcProgram.Read","params":{"var":"\"pallet_free\""}},
    # # {"jsonrpc":"2.0","id":"126","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_D_1_OP20\""}},
    # # {"jsonrpc":"2.0","id":"127","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_D_2_OP20\""}},
    # # {"jsonrpc":"2.0","id":"128","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_U_1_OP20\""}},
    # # {"jsonrpc":"2.0","id":"129","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_U_2_OP20\""}},
    # {"jsonrpc":"2.0","id":"130","method":"PlcProgram.Read","params":{"var":"\"OP20_available\""}},
    # # {"jsonrpc":"2.0","id":"131","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_D_2_OP40\""}},
    # # {"jsonrpc":"2.0","id":"132","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_D_1_OP40\""}},
    # {"jsonrpc":"2.0","id":"133","method":"PlcProgram.Read","params":{"var":"\"R_I_MA1F\""}},
    # {"jsonrpc":"2.0","id":"134","method":"PlcProgram.Read","params":{"var":"\"R_I_MA2F\""}},
    # {"jsonrpc":"2.0","id":"135","method":"PlcProgram.Read","params":{"var":"\"okuma_available\""}},

    # # ERROR
    # {"jsonrpc":"2.0","id":"136","method":"PlcProgram.Read","params":{"var":"\"errors\".emergency_active"}},
    # {"jsonrpc":"2.0","id":"137","method":"PlcProgram.Read","params":{"var":"\"errors\".ma1_drd_endstops"}},
    # {"jsonrpc":"2.0","id":"138","method":"PlcProgram.Read","params":{"var":"\"errors\".ma1_dru_endstops"}},
    # {"jsonrpc":"2.0","id":"139","method":"PlcProgram.Read","params":{"var":"\"errors\".ma1_gs_dn"}},
    # {"jsonrpc":"2.0","id":"140","method":"PlcProgram.Read","params":{"var":"\"errors\".ma1_nsense"}},
    # {"jsonrpc":"2.0","id":"141","method":"PlcProgram.Read","params":{"var":"\"errors\".r_program"}},
    # {"jsonrpc":"2.0","id":"142","method":"PlcProgram.Read","params":{"var":"\"errors\".r_gp1_not_free"}},
    # {"jsonrpc":"2.0","id":"143","method":"PlcProgram.Read","params":{"var":"\"errors\".r_gp2_not_free"}},
    # {"jsonrpc":"2.0","id":"144","method":"PlcProgram.Read","params":{"var":"\"errors\".r_not_idle"}},
    # {"jsonrpc":"2.0","id":"145","method":"PlcProgram.Read","params":{"var":"\"errors\".r_not_home"}},
    # {"jsonrpc":"2.0","id":"146","method":"PlcProgram.Read","params":{"var":"\"errors\".r_alarm"}},
    # {"jsonrpc":"2.0","id":"147","method":"PlcProgram.Read","params":{"var":"\"errors\".r_flimit"}},
    # {"jsonrpc":"2.0","id":"148","method":"PlcProgram.Read","params":{"var":"\"errors\".r_rlimit"}},
    # {"jsonrpc":"2.0","id":"149","method":"PlcProgram.Read","params":{"var":"\"errors\".ch1_nsense_ret"}},
    # {"jsonrpc":"2.0","id":"150","method":"PlcProgram.Read","params":{"var":"\"errors\".ch1_alarm"}},
    # {"jsonrpc":"2.0","id":"151","method":"PlcProgram.Read","params":{"var":"\"errors\".init_error"}},
    # {"jsonrpc":"2.0","id":"152","method":"PlcProgram.Read","params":{"var":"\"errors\".max_unblock_error"}},
    # {"jsonrpc":"2.0","id":"153","method":"PlcProgram.Read","params":{"var":"\"errors\".max_pallet_present"}},
    # {"jsonrpc":"2.0","id":"154","method":"PlcProgram.Read","params":{"var":"\"errors\".max_dr_position"}},
    # {"jsonrpc":"2.0","id":"155","method":"PlcProgram.Read","params":{"var":"\"errors\".chx_robot_not_allowed"}},
    # {"jsonrpc":"2.0","id":"156","method":"PlcProgram.Read","params":{"var":"\"errors\".chx_pressure_error"}},
    # {"jsonrpc":"2.0","id":"157","method":"PlcProgram.Read","params":{"var":"\"errors\".chx_nsense_adv"}},
    # {"jsonrpc":"2.0","id":"158","method":"PlcProgram.Read","params":{"var":"\"errors\".chx_nsense_ret"}},
    # {"jsonrpc":"2.0","id":"159","method":"PlcProgram.Read","params":{"var":"\"errors\".chx_alarm"}},
    # {"jsonrpc":"2.0","id":"160","method":"PlcProgram.Read","params":{"var":"\"errors\".chx_not_available"}},


    #TEST
    # {"jsonrpc":"2.0","id":"125","method":"PlcProgram.Read","params":{"var":"\"errors\".r_manualmode"}},
    # {"jsonrpc":"2.0","id":"125","method":"PlcProgram.Read","params":{"var":"\"errors\".r_gp1_free"}},
    # {"jsonrpc":"2.0","id":"125","method":"PlcProgram.Read","params":{"var":"\"errors\".r_gp2_free"}},
    # {"jsonrpc":"2.0","id":"125","method":"PlcProgram.Read","params":{"var":"\"errors\".ch1_nsense_adv"}},
    # {"jsonrpc":"2.0","id":"125","method":"PlcProgram.Read","params":{"var":"\"errors\".ch1_psa"}},
    # {"jsonrpc":"2.0","id":"125","method":"PlcProgram.Read","params":{"var":"\"errors\".max_block_error"}},
    # {"jsonrpc":"2.0","id":"107","method":"PlcProgram.Write","params":{"var":"\"tags\".pause_semi", "value": False}},
    # {"jsonrpc":"2.0","id":"125","method":"PlcProgram.Read","params":{"var":"\"tags\".pause_auto"}},
    # {"jsonrpc":"2.0","id":"5","method":"PlcProgram.Read","params":{"var":"\"CH1_I_NCR\""}},
    # {"jsonrpc":"2.0","id":"107","method":"PlcProgram.Write","params":{"var":"\"tags\".CH1_FreePallet", "value": True}},   
    # {"jsonrpc":"2.0","id":"107","method":"PlcProgram.Write","params":{"var":"\"tags\".CH1_FreePallet", "value": True}},
    # {"jsonrpc":"2.0","id":"107","method":"PlcProgram.Write","params":{"var":"\"tags\".pause_semi", "value": True}},
    # {"jsonrpc":"2.0","id":"135","method":"PlcProgram.Write","params":{"var":"\"M_PRG_DRW\"", "value": False}},
    {"jsonrpc":"2.0","id":"107","method":"PlcProgram.Read","params":{"var":"\"array\".ar"}},
    

    ])
    
    


    headers = {
        'X-Auth-Token': PLC_TOKEN['token'],
        'Content-Type': 'application/json',
        # 'verify': False
    }
    # print(payload)
    inicio = time.time()

    conn.request("POST", "https://192.168.3.150/api/jsonrpc", payload, headers)

    
    res = conn.getresponse()
    data = res.read()
    data_json = data.decode("utf-8")
    data_parsed = json.loads(data_json)
    delta = time.time() - inicio
    print(delta)
    # sensor_value = data_parsed["result"]
    # print(f"El valor que trae del plc es {sensor_value}")
    print("la data:", data_parsed)

    return JsonResponse({})

@csrf_exempt
def switch_led_state_on(request):
    obtain_token_plc()

    return JsonResponse({})

@csrf_exempt
def sensores_okuma_identify(request):
    post_req = request.POST
    if post_req['model_machine']:
        okuma_model = str(post_req['model_machine'])
        okuma_especific_model = okuma_model[6]
        OKUMA['okuma_current_selected'] = int(okuma_especific_model)
        # if OKUMA['okuma_current_selected'] == 1:
        #     return HttpResponseRedirect(reverse('okuma_1_neumatic'))
        print(OKUMA['okuma_current_selected'])
        return JsonResponse({})


@csrf_exempt
def sensores_mesa_identify(request):
    post_req = request.POST
    print(post_req)
    if post_req['model_table']:
        mesa_model = str(post_req['model_table'])
        mesa_especific_model = mesa_model[5]
        MESA['mesa_current_selected'] = int(mesa_especific_model)
        # if OKUMA['okuma_current_selected'] == 1:
        #     return HttpResponseRedirect(reverse('okuma_1_neumatic'))
        print(MESA['mesa_current_selected'])
        return JsonResponse({})


#ARMA MENSAJE PARA MANDAR COMANDOS DE NEUMATICA
@method_decorator(csrf_exempt, name='dispatch')
class ManualPneumatic(View):

    def post(self, request):
        from apps.ws.utils import variables as ws_vars
        
        ws_vars.WEBSOCKET = False
        print("post manual neumatic")
        post_req = request.POST
        # print("entro al post")
        
        req_data = []
        
        for item in post_req.items():   # Item is in (key, value) format
            req_data.append(item)

        # print("req_Data", req_data)
        # command = int(req_data[0][1])
        menu = req_data[0][1]
        name = req_data[1][1]
        btn = req_data[2][1]
        print('MENU:', menu)
        print('NOMBRE:', name)
        print('BOTON:', btn)

        if menu == 'mesa1':
            if name == 'persiana':
                name_routine = ['Man_MA1_CG']
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                # self.send_message(name_routine,bool_value_1,False)
                OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name_routine[0]}"',bool_value_1)

            if name == 'drawerU':
                name_routine = ['Man_MA1_DRU_FD']
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name_routine[0]}"',bool_value_1)
                # self.send_message(name_routine,bool_value_1,True)

            elif name == 'drawerD':
                name_routine = ['Man_MA1_DRD_FD']
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name_routine[0]}"',bool_value_1)
                # self.send_message(name_routine,bool_value_1,True)
                
                # sensores_states_plc()

            elif name == 'clampeo1U':
                name_routine = ['Man_MA1_OP_U1']
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                OPCProtocol().write_value_bool(f'ns=3;s="{name_routine[0]}"',bool_value_1)
                # self.send_message(name_routine,bool_value_1,False)

            elif name == 'clampeo2U':
                name_routine = ['Man_MA1_OP_U2']
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                OPCProtocol().write_value_bool(f'ns=3;s="{name_routine[0]}"',bool_value_1)
                # self.send_message(name_routine,bool_value_1,False)

            elif name == 'clampeo1D':
                name_routine = ['Man_MA1_OP_D1']
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                OPCProtocol().write_value_bool(f'ns=3;s="{name_routine[0]}"',bool_value_1)
                # self.send_message(name_routine,bool_value_1,False)

            elif name == 'clampeo2D':
                name_routine = ['Man_MA1_OP_D2']
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                OPCProtocol().write_value_bool(f'ns=3;s="{name_routine[0]}"',bool_value_1)
                # self.send_message(name_routine,bool_value_1,False)
            
            elif name == 'venturi':
                name_routine = ['Man_MA1_OP_BLW']
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                OPCProtocol().write_value_bool(f'ns=3;s="{name_routine[0]}"',bool_value_1)
                # self.send_message(name_routine,bool_value_1,False)
            

        if menu == 'okuma1':

            if name == 'inflador':
                name_routine = ['Man_CH1_NFA','Man_CH1_NFR']
                if btn == 'On':
                    bool_value_1  = True
                    bool_value_2  = False
                
                else:
                    bool_value_1  = False
                    bool_value_2  = True

                for n in range(0,len(name_routine)):
                    OPCProtocol().write_value_bool(f'ns=3;s="{name_routine[n]}"',locals()[f"bool_value_{n+1}"])
                    
                # self.send_message(name_routine[0], bool_value_1, False, name_routine[1], bool_value_2)

            elif name == 'garra':
                name_routine = ['Man_CH1_NC']
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False

                inicio = time.time()
                # OPCProtocol().read_input_value('ns=3;s="Man_CH1_NC"')
                OPCProtocol().write_value_bool(f'ns=3;s="{name_routine[0]}"',bool_value_1)
                delta = time.time() - inicio
                print(delta)
                # self.send_message(name_routine[0], bool_value_1, False)

            elif name == 'booster':
                name_routine = ['Man_CH1_BOO']
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                # self.send_message(name_routine,bool_value_1,False)
                OPCProtocol().write_value_bool(f'ns=3;s="{name_routine[0]}"',bool_value_1)
            
            elif name == 'venturi_up':
                name_routine = ['Man_CH1_BLWUP']
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                # self.send_message(name_routine,bool_value_1,False)
                OPCProtocol().write_value_bool(f'ns=3;s="{name_routine[0]}"',bool_value_1)

            elif name == 'venturi_down':
                name_routine = ['Man_CH1_BLWDN']
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                # self.send_message(name_routine,bool_value_1,False)
                OPCProtocol().write_value_bool(f'ns=3;s="{name_routine[0]}"',bool_value_1)

            elif name == 'soplador':
                name_routine = ['Man_CH1_BLW']
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                # self.send_message(name_routine,bool_value_1,False)
                OPCProtocol().write_value_bool(f'ns=3;s="{name_routine[0]}"',bool_value_1)
            
            elif name == 'desclampeo30':
                name_routine = ['Man_CH1_INF30']
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                # self.send_message(name_routine,bool_value_1,False)
                OPCProtocol().write_value_bool(f'ns=3;s="{name_routine[0]}"',bool_value_1)

            elif name == 'desclampeo40':
                name_routine = ['Man_CH1_INF40']
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                # self.send_message(name_routine,bool_value_1,False)
                OPCProtocol().write_value_bool(f'ns=3;s="{name_routine[0]}"',bool_value_1)
        
        ws_vars.WEBSOCKET = True
        # # time.sleep(5)
        # FrontWs().start()
        
        return JsonResponse({})

            

    def send_message(self,name_routine, bool_value, data_base_plc_direction, second_name_routine=None, second_bool_value=None):
        # print('send mesage')
        inicio = time.time()
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
        # vars para armar mensaje
        msg_data_directions_container = []
        if data_base_plc_direction == True:
            first = '\"tags\"'
            last = ""
        else:
            first = '\"'
            last = '\"'

        try:
            conn = http.client.HTTPSConnection("192.168.3.150")
        except:
            print("Conexion con plc no establecida")    
        
        #arma el mensaje
        if second_name_routine:
            # print("2 valores")
            payload = json.dumps([{"jsonrpc":"2.0","id":"1","method":"PlcProgram.Write","params":{"var":(first+name_routine+last),"value":bool_value}},
            {"jsonrpc":"2.0","id":"2","method":"PlcProgram.Write","params":{"var":(first+second_name_routine+last),"value":second_bool_value}}])
        else:
            payload = json.dumps([{"jsonrpc":"2.0","id":"1","method":"PlcProgram.Write","params":{"var":(first+name_routine+last),"value":bool_value}},
            ])
            # msg_data_directions_container.append(msg_data_directions)

        #mensaje armado
        # payload = json.dumps(msg_data_directions_container)

        headers = {
            'X-Auth-Token': PLC_TOKEN['token'],
            'Content-Type': 'application/json',
        }

        #se manda el mensaje
        conn.request("POST", "/api/jsonrpc", payload, headers)


        res = conn.getresponse()
        data = res.read()
        data_json = data.decode("utf-8")
        data_parsed = json.loads(data_json)
        # sensor_value = data_parsed["result"]
        # print(f"El valor que trae del plc es {sensor_value}")
        delta = time.time() - inicio
        print("tiempo",delta)
        print("la data:", data_parsed)


        #respuesata mensaje
        # res = conn.getresponse()
        # data = res.read()
        # data_json = data.decode("utf-8")
        # data_parsed = json.loads(data_json)
        # bool_state_sensor = data_parsed["result"]
        # print(f"el valor cambio a{bool_state_sensor}")


#ARMA MENSAJE PARA MANDAR COMANDOS DE SEMIAUTOMATICO
@csrf_exempt
def send_command_bit(request):

    from apps.ws.utils import variables as ws_vars
        
    ws_vars.WEBSOCKET = False

    post_req = request.POST
    print("la post",post_req)

    req_data = []
        
    for item in post_req.items():   # Item is in (key, value) format
        req_data.append(item)


    menu = req_data[0][1]
    name = req_data[1][1]
    print(menu,name)
    # print("el m prog es",M_PROGS_SEMIAUTO['M_PRG_30_40'])

    #CAMBIADOR DE BITS DE RUTINAS DEL ROBOT
    if name == "mesa1":
        name = ["M_PRG_MA","M_PRG_MA_CH"]
        bool_value_1 = False
        bool_value_2 = False
        # send_message_semi(name,bool_value)
        for n in range(0,len(name)):
            OPCProtocol().write_value_bool(f'ns=3;s="{name[n]}"',locals()[f"bool_value_{n+1}"])
        # send_message_semi(name[0],bool_value_1,name[1],bool_value_2)

    elif name == "mesa2":
        name = ["M_PRG_MA","M_PRG_MA_CH"]
        bool_value_1 = True
        bool_value_2 = False
        # send_message_semi(name,bool_value)
        for n in range(0,len(name)):
            OPCProtocol().write_value_bool(f'ns=3;s="{name[n]}"',locals()[f"bool_value_{n+1}"])
        # send_message_semi(name[0],bool_value_1,name[1],bool_value_2)
    
    elif name == "okuma1":
        name = ["M_PRG_BIT0_CH","M_PRG_BIT1_CH","M_PRG_MA_CH"]
        bool_value_1 = False
        bool_value_2 = False
        bool_value_3 = True
        for n in range(0,len(name)):
            OPCProtocol().write_value_bool(f'ns=3;s="{name[n]}"',locals()[f"bool_value_{n+1}"])
        # send_message_semi(name[0],bool_value_1,name[1],bool_value_2,name[2],bool_value_3)

    elif name == "okuma2":
        name = ["M_PRG_BIT0_CH","M_PRG_BIT1_CH","M_PRG_MA_CH"]
        bool_value_1 = True
        bool_value_2 = False
        bool_value_3 = True
        for n in range(0,len(name)):
            OPCProtocol().write_value_bool(f'ns=3;s="{name[n]}"',locals()[f"bool_value_{n+1}"])
        # send_message_semi(name[0],bool_value_1,name[1],bool_value_2,name[2],bool_value_3)
    
    elif name == "okuma3":
        name = ["M_PRG_BIT0_CH","M_PRG_BIT1_CH","M_PRG_MA_CH"]
        bool_value_1 = False
        bool_value_2 = True
        bool_value_3 = True
        for n in range(0,len(name)):
            OPCProtocol().write_value_bool(f'ns=3;s="{name[n]}"',locals()[f"bool_value_{n+1}"])
        # send_message_semi(name[0],bool_value_1,name[1],bool_value_2,name[2],bool_value_3)

    elif name == "okuma4":
        name = ["M_PRG_BIT0_CH","M_PRG_BIT1_CH","M_PRG_MA_CH"]
        bool_value_1 = True
        bool_value_2 = True
        bool_value_3 = True
        for n in range(0,len(name)):
            OPCProtocol().write_value_bool(f'ns=3;s="{name[n]}"',locals()[f"bool_value_{n+1}"])
        # send_message_semi(name[0],bool_value_1,name[1],bool_value_2,name[2],bool_value_3)

    elif name == "arriba":
        name = ["M_PRG_DRW"]
        bool_value_1 = True
        OPCProtocol().write_value_bool(f'ns=3;s="{name[0]}"',bool_value_1)

    elif name == "abajo":
        name = ["M_PRG_DRW"]
        bool_value_1 = False
        OPCProtocol().write_value_bool(f'ns=3;s="{name[0]}"',bool_value_1)
        
    elif name == "pos1":
        name = ["M_PRG_PAL"]
        bool_value_1 = False
        OPCProtocol().write_value_bool(f'ns=3;s="{name[0]}"',bool_value_1)

    elif name == "pos2":
        name = ["M_PRG_PAL"]
        bool_value_1 = True
        OPCProtocol().write_value_bool(f'ns=3;s="{name[0]}"',bool_value_1)

    elif name == "tomar":
        name = ["M_PRG_GET_PUT"]
        bool_value_1 = False
        OPCProtocol().write_value_bool(f'ns=3;s="{name[0]}"',bool_value_1)

    elif name == "dejar":
        name = ["M_PRG_GET_PUT"]
        bool_value_1 = True
        OPCProtocol().write_value_bool(f'ns=3;s="{name[0]}"',bool_value_1)

    elif name == "op30":
        name = ["M_PRG_30_40"]
        bool_value_1 = False
        OPCProtocol().write_value_bool(f'ns=3;s="{name[0]}"',bool_value_1)

    elif name == "op40":
        name = ["M_PRG_30_40"]
        bool_value_1 = True
        OPCProtocol().write_value_bool(f'ns=3;s="{name[0]}"',bool_value_1)

    elif name == "casita1":
        name = ["M_PRG_CAS"]
        bool_value_1 = False
        OPCProtocol().write_value_bool(f'ns=3;s="{name[0]}"',bool_value_1)

    elif name == "casita2":
        name = ["M_PRG_CAS"]
        bool_value_1 = True
        OPCProtocol().write_value_bool(f'ns=3;s="{name[0]}"',bool_value_1)

    #BOTON PARA EJECUTAR RUTINA EN SEMIAUTOMATICO
    elif name == "comenzar":
        name = ["pause_semi"]
        bool_value_1 = False
        OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_1)
        # send_message_auto(name,bool_value)

    elif name == "detener":
        name = ["pause_semi"]
        bool_value_1 = True
        OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_1)
        # send_message_auto(name,bool_value)

    elif name == "reset_program":
        name = ["reset_semi"]
        bool_value_1 = True
        OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_1)
        # send_message_auto(name,bool_value)
        
    elif name == "step_step":
        name = ["step_semi"]
        bool_value_1 = True
        # OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_1)
        OPCProtocol().write_value_bool(f'ns=3;s="{name[0]}"',bool_value_1)
        # send_message_auto(name,bool_value)

    elif name == "ejecutar":
        name = ["run_semi"]
        print('execute')
        bool_value_1 = True
        # OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_1)
        OPCProtocol().write_value_bool(f'ns=3;s="{name[0]}"',bool_value_1)
        # send_message_semi(name,bool_value)

    ws_vars.WEBSOCKET = True
    return JsonResponse({})

@csrf_exempt
def cmd_automatic_routines(request):
    print("entro a cmd command")

    from apps.ws.utils import variables as ws_vars
        
    ws_vars.WEBSOCKET = False

    post_req = request.POST
    print("la post",post_req)

    req_data = []
        
    for item in post_req.items():   # Item is in (key, value) format
        req_data.append(item)


    menu = req_data[0][1]
    cmd = req_data[1][1]
    print(menu,cmd)


    if menu == "auto":
        if cmd == "comenzar":
            name = ["pause_auto"]
            bool_value_1 = False
            OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_1)
            # send_message_auto(name,bool_value_1)

        elif cmd == "detener":
            name = ["pause_auto"]
            bool_value_1 = True
            OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_1)
            # send_message_auto(name,bool_value_1)

        elif cmd == "terminarON":
            name = ["last_auto"]
            bool_value_1 = True
            OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_1)
            # send_message_auto(name,bool_value_1)
        
        elif cmd == "terminarOFF":
            name = ["last_auto"]
            bool_value_1 = False
            OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_1)
            # send_message_auto(name,bool_value_1)

        elif cmd == "reset_program":
            name = ["reset_auto"]
            bool_value_1 = True
            OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_1)
            # send_message_auto(name,bool_value_1)

        elif cmd == "step_step":
            name = [".tap_auto"]
            bool_value_1 = True
            OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_1)
            # send_message_auto(name,bool_value_1)

    ws_vars.WEBSOCKET = True
    return JsonResponse({})

@csrf_exempt
def cmd_disable_okuma(request):

    from apps.ws.utils import variables as ws_vars
        
    ws_vars.WEBSOCKET = False

    post_req = request.POST
    print("la post",post_req)

    req_data = []
        
    for item in post_req.items():   # Item is in (key, value) format
        req_data.append(item)


    menu = req_data[0][1]
    ok = req_data[1][1]
    print(menu,ok)

    if menu == "ch_disable":
        if ok =="okuma1":
            name = ["CH1_DISABLE"]
            bool_value_1 = True
            bool_value_2 = False
            # send_message_semi(name,bool_value)
            if PLC_DEFAULT_VARIABLES[".CH1_DISABLE"] == True:
                OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_2)
            else:
                print("falso")
                OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_1)

        elif ok == "okuma2":
            name = ["CH2_DISABLE"]
            bool_value_1 = True
            bool_value_2 = False
            # send_message_semi(name,bool_value)
            if PLC_DEFAULT_VARIABLES[".CH2_DISABLE"] == True:
                OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_2)
            else:
                print("falso")
                OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_1)
                

        elif ok == "okuma3":
            name = ["CH3_DISABLE"]
            bool_value_1 = True
            bool_value_2 = False
            # send_message_semi(name,bool_value)
            if PLC_DEFAULT_VARIABLES[".CH3_DISABLE"] == True:
                OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_2)
            else:
                print("falso")
                OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_1)
        
        elif ok == "okuma4":
            name = ["CH4_DISABLE"]
            bool_value_1 = True
            bool_value_2 = False
            # send_message_semi(name,bool_value)
            if PLC_DEFAULT_VARIABLES[".CH4_DISABLE"] == True:
                OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_2)
            else:
                print("falso")
                OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_1)

    if menu == "mesa_disable":
        if ok =="mesa1":
            name = ["MA1_DISABLE"]
            bool_value_1 = True
            bool_value_2 = False
            # send_message_semi(name,bool_value)
            if PLC_DEFAULT_VARIABLES[".MA1_DISABLE"] == True:
                OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_2)
            else:
                print("falso")
                OPCProtocol().write_value_bool(f'ns=3;s="tags"."{name[0]}"',bool_value_1)


    ws_vars.WEBSOCKET = True
    return JsonResponse({})
    

@csrf_exempt
def index_change(request):

    post_req = request.POST
    print("la post",post_req)

    req_data = []
        
    for item in post_req.items():   # Item is in (key, value) format
        req_data.append(item)


    hash_routine_change = req_data[0][1]
    # print(hash_routine_change)

    if hash_routine_change == "auto_routine_change":
        name = ["M_PRG_AUT_SEM"]
        bool_value_1 = False
        OPCProtocol().write_value_bool(f'ns=3;s="{name[0]}"',bool_value_1)
        # send_message_semi("M_PRG_AUT_SEM", False)

    elif hash_routine_change == "semi_routine_change":
        name = ["M_PRG_AUT_SEM"]
        bool_value_1 = True
        OPCProtocol().write_value_bool(f'ns=3;s="{name[0]}"',bool_value_1)
        # send_message_semi("M_PRG_AUT_SEM", True)

    # send_message_semi(hash_routine_change, true)

    # print(request)
    # print('dentro de  index_change')
    return JsonResponse({})

