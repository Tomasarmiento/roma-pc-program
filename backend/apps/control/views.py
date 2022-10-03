import json
import http.client
from pickle import TRUE
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect



from apps.ws.utils.functions import send_front_message
from apps.ws.utils.variables import frontState

from apps.parameters.utils.functions import toggle_disable_machine
from apps.parameters.models import Parameter

from apps.control.utils.variables import OKUMA,MESA,PLC_TOKEN,M_PROGS_SEMIAUTO
from apps.control.utils.functions import derived_sensores_states,obtain_token_plc,send_message_semi


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
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    conn = http.client.HTTPSConnection("192.168.3.150")
    payload = json.dumps([
    # {"jsonrpc":"2.0","id":"1","method":"PlcProgram.Read","params":{"var":"\"CH1_I_RA\""}},
    # {"jsonrpc":"2.0","id":"2","method":"PlcProgram.Read","params":{"var":"\"CH1_I_AL\""}},
    # {"jsonrpc":"2.0","id":"3","method":"PlcProgram.Read","params":{"var":"\"CH1_I_ID\""}},
    # {"jsonrpc":"2.0","id":"4","method":"PlcProgram.Read","params":{"var":"\"CH1_I_MB\""}},
    # {"jsonrpc":"2.0","id":"5","method":"PlcProgram.Read","params":{"var":"\"CH1_I_PS\""}},
    # {"jsonrpc":"2.0","id":"6","method":"PlcProgram.Read","params":{"var":"\"CH1_I_HO\""}},
    # {"jsonrpc":"2.0","id":"7","method":"PlcProgram.Read","params":{"var":"\"CH1_I_NPA\""}},
    # {"jsonrpc":"2.0","id":"8","method":"PlcProgram.Read","params":{"var":"\"CH1_I_NPR\""}},
    # {"jsonrpc":"2.0","id":"9","method":"PlcProgram.Read","params":{"var":"\"CH2_I_RA\""}},
    # {"jsonrpc":"2.0","id":"10","method":"PlcProgram.Read","params":{"var":"\"CH2_I_AL\""}},
    # {"jsonrpc":"2.0","id":"11","method":"PlcProgram.Read","params":{"var":"\"CH2_I_ID\""}},
    # {"jsonrpc":"2.0","id":"12","method":"PlcProgram.Read","params":{"var":"\"CH2_I_MB\""}},
    # {"jsonrpc":"2.0","id":"13","method":"PlcProgram.Read","params":{"var":"\"CH2_I_PS\""}},
    # {"jsonrpc":"2.0","id":"14","method":"PlcProgram.Read","params":{"var":"\"CH2_I_HO\""}},
    # {"jsonrpc":"2.0","id":"15","method":"PlcProgram.Read","params":{"var":"\"CH2_I_NPA\""}},
    # {"jsonrpc":"2.0","id":"16","method":"PlcProgram.Read","params":{"var":"\"CH2_I_NPR\""}},
    # {"jsonrpc":"2.0","id":"17","method":"PlcProgram.Read","params":{"var":"\"CH3_I_RA\""}},
    # {"jsonrpc":"2.0","id":"18","method":"PlcProgram.Read","params":{"var":"\"CH3_I_AL\""}},
    # {"jsonrpc":"2.0","id":"19","method":"PlcProgram.Read","params":{"var":"\"CH3_I_ID\""}},
    # {"jsonrpc":"2.0","id":"20","method":"PlcProgram.Read","params":{"var":"\"CH3_I_MB\""}},
    # {"jsonrpc":"2.0","id":"21","method":"PlcProgram.Read","params":{"var":"\"CH3_I_PS\""}},
    # {"jsonrpc":"2.0","id":"22","method":"PlcProgram.Read","params":{"var":"\"CH3_I_HO\""}},
    # {"jsonrpc":"2.0","id":"23","method":"PlcProgram.Read","params":{"var":"\"CH3_I_NPA\""}},
    # {"jsonrpc":"2.0","id":"24","method":"PlcProgram.Read","params":{"var":"\"CH3_I_NPR\""}},
    # {"jsonrpc":"2.0","id":"25","method":"PlcProgram.Read","params":{"var":"\"CH4_I_RA\""}},
    # {"jsonrpc":"2.0","id":"26","method":"PlcProgram.Read","params":{"var":"\"CH4_I_AL\""}},
    # {"jsonrpc":"2.0","id":"27","method":"PlcProgram.Read","params":{"var":"\"CH4_I_ID\""}},
    # {"jsonrpc":"2.0","id":"28","method":"PlcProgram.Read","params":{"var":"\"CH4_I_MB\""}},
    # {"jsonrpc":"2.0","id":"29","method":"PlcProgram.Read","params":{"var":"\"CH4_I_PS\""}},
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
    # {"jsonrpc":"2.0","id":"92","method":"PlcProgram.Read","params":{"var":"\"GRL_I_EMS\""}},
    # {"jsonrpc":"2.0","id":"93","method":"PlcProgram.Read","params":{"var":"\"System_Active\""}},
    # {"jsonrpc":"2.0","id":"94","method":"PlcProgram.Read","params":{"var":"\"Start_system_button\""}},
    # {"jsonrpc":"2.0","id":"95","method":"PlcProgram.Read","params":{"var":"\"Stop_system_button\""}},
    # {"jsonrpc":"2.0","id":"96","method":"PlcProgram.Read","params":{"var":"\"Emergency\""}},
    # {"jsonrpc":"2.0","id":"97","method":"PlcProgram.Read","params":{"var":"\"Robot_GO\""}},
    # {"jsonrpc":"2.0","id":"98","method":"PlcProgram.Read","params":{"var":"\"Robot_IDLE\""}},
    # {"jsonrpc":"2.0","id":"99","method":"PlcProgram.Read","params":{"var":"\"Trig_MA1DRU1\""}},
    # {"jsonrpc":"2.0","id":"100","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_U_1_OP40\""}},
    # {"jsonrpc":"2.0","id":"101","method":"PlcProgram.Read","params":{"var":"\"Trig_MA1DRU2\""}},
    # {"jsonrpc":"2.0","id":"102","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_U_2_OP40\""}},
    # {"jsonrpc":"2.0","id":"103","method":"PlcProgram.Read","params":{"var":"\"Gen_Program\""}},
    # {"jsonrpc":"2.0","id":"104","method":"PlcProgram.Read","params":{"var":"\"unblock_pallet\""}},
    # {"jsonrpc":"2.0","id":"105","method":"PlcProgram.Read","params":{"var":"\"unblocked_pallet_sensor\""}},
    # {"jsonrpc":"2.0","id":"106","method":"PlcProgram.Read","params":{"var":"\"neumatic_forward\""}},
    # {"jsonrpc":"2.0","id":"107","method":"PlcProgram.Read","params":{"var":"\"neumatic_advance\""}},
    # {"jsonrpc":"2.0","id":"108","method":"PlcProgram.Read","params":{"var":"\"INF30\""}},
    # {"jsonrpc":"2.0","id":"109","method":"PlcProgram.Read","params":{"var":"\"Blower\""}},
    # {"jsonrpc":"2.0","id":"110","method":"PlcProgram.Read","params":{"var":"\"Booster\""}},
    # {"jsonrpc":"2.0","id":"111","method":"PlcProgram.Read","params":{"var":"\"INF40\""}},
    # {"jsonrpc":"2.0","id":"112","method":"PlcProgram.Read","params":{"var":"\"pallet_sensor\""}},
    # {"jsonrpc":"2.0","id":"113","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_D_1_OP20\""}},
    # {"jsonrpc":"2.0","id":"114","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_D_2_OP20\""}},
    # {"jsonrpc":"2.0","id":"115","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_U_1_OP20\""}},
    # {"jsonrpc":"2.0","id":"116","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_U_2_OP20\""}},
    # {"jsonrpc":"2.0","id":"117","method":"PlcProgram.Read","params":{"var":"\"OP20_available\""}},
    # {"jsonrpc":"2.0","id":"118","method":"PlcProgram.Read","params":{"var":"\"Trig_MA1DRD1\""}},
    # {"jsonrpc":"2.0","id":"119","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_D_2_OP40\""}},
    # {"jsonrpc":"2.0","id":"120","method":"PlcProgram.Read","params":{"var":"\"Trig_MA1DRD2\""}},
    # {"jsonrpc":"2.0","id":"121","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_D_1_OP40\""}},
    # {"jsonrpc":"2.0","id":"122","method":"PlcProgram.Read","params":{"var":"\"R_I_MA1F\""}},
    # {"jsonrpc":"2.0","id":"123","method":"PlcProgram.Read","params":{"var":"\"R_I_MA2F\""}},
    # {"jsonrpc":"2.0","id":"124","method":"PlcProgram.Read","params":{"var":"\"okuma_available\""}},
    # {"jsonrpc":"2.0","id":"133","method":"PlcProgram.Read","params":{"var":"\"gen\""}},
    # {"jsonrpc":"2.0","id":"107","method":"PlcProgram.Write","params":{"var":"\"tags\".Man_MA1_DRD_FD", "value": True}},
    {"jsonrpc":"2.0","id":"133","method":"PlcProgram.Write","params":{"var":"\"CH1_O_EMS\"", "value": True}},
    # {"jsonrpc":"2.0","id":"133","method":"PlcProgram.Write","params":{"var":"\"M_PRG_BIT0_CH\"", "value": False}},
    # {"jsonrpc":"2.0","id":"133","method":"PlcProgram.Write","params":{"var":"\"M_PRG_BIT1_CH\"", "value": True}},
    # {"jsonrpc":"2.0","id":"133","method":"PlcProgram.Read","params":{"var":"\"R_O_BIT0_CH\""}},
    # {"jsonrpc":"2.0","id":"133","method":"PlcProgram.Read","params":{"var":"\"R_O_BIT1_CH\""}},
    # {"jsonrpc":"2.0","id":"107","method":"PlcProgram.Write","params":{"var":"\"tags\"M_PRG_AUT_SEM", "value": True}},
    # {"jsonrpc":"2.0","id":"132","method":"PlcProgram.Read","params":{"var":"\"R_I_AUT_SEM\""}},
    # {"jsonrpc":"2.0","id":"132","method":"PlcProgram.Read","params":{"var":"\"R_I_30_40\""}},
    # {"jsonrpc":"2.0","id":"132","method":"PlcProgram.Read","params":{"var":"\"R_I_CAS\""}},
    # {"jsonrpc":"2.0","id":"132","method":"PlcProgram.Read","params":{"var":"\"R_I_BIT0_CH\""}},
    # {"jsonrpc":"2.0","id":"132","method":"PlcProgram.Read","params":{"var":"\"R_I_BIT1_CH\""}},
    # {"jsonrpc":"2.0","id":"132","method":"PlcProgram.Read","params":{"var":"\"R_I_PAL\""}},
    # {"jsonrpc":"2.0","id":"132","method":"PlcProgram.Read","params":{"var":"\"R_I_DRW\""}},
    # {"jsonrpc":"2.0","id":"132","method":"PlcProgram.Read","params":{"var":"\"R_I_MA\""}},
    # {"jsonrpc":"2.0","id":"132","method":"PlcProgram.Read","params":{"var":"\"R_I_GET_PUT\""}},
    # {"jsonrpc":"2.0","id":"132","method":"PlcProgram.Read","params":{"var":"\"R_I_MA_CH\""}},
    ])


    headers = {
        'X-Auth-Token': PLC_TOKEN['token'],
        'Content-Type': 'application/json',
        # 'verify': False
    }

    conn.request("POST", "/api/jsonrpc", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data_json = data.decode("utf-8")
    data_parsed = json.loads(data_json)
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



@method_decorator(csrf_exempt, name='dispatch')
class ManualPneumatic(View):

    def post(self, request):
        post_req = request.POST
        print("entro al post")
        
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
            if name == 'drawerU':
                name_routine = '.Man_MA1_DRU_FD'
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                self.send_message(name_routine,bool_value_1,True)

            elif name == 'drawerD':
                name_routine = '.Man_MA1_DRD_FD'
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                self.send_message(name_routine,bool_value_1,True)

            elif name == 'clampeo1U':
                name_routine = 'Man_MA1_OP_U1'
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                self.send_message(name_routine,bool_value_1,False)

            elif name == 'clampeo2U':
                name_routine = 'Man_MA1_OP_U2'
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                self.send_message(name_routine,bool_value_1,False)

            elif name == 'clampeo1D':
                name_routine = 'Man_MA1_OP_D1'
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                self.send_message(name_routine,bool_value_1,False)

            elif name == 'clampeo2D':
                name_routine = 'Man_MA1_OP_D2'
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                self.send_message(name_routine,bool_value_1,False)

        if menu == 'okuma1':
            if name == 'inflador':
                name_routine = 'Man_CH1_NF'
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                self.send_message(name_routine,bool_value_1,False)

            elif name == 'booster':
                name_routine = 'Man_CH1_BOO'
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                self.send_message(name_routine,bool_value_1,False)

            elif name == 'soplador':
                name_routine = 'Man_CH1_BLW'
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                self.send_message(name_routine,bool_value_1,False)
            
            elif name == 'desclampeo30':
                name_routine = 'Man_CH1_INF30'
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                self.send_message(name_routine,bool_value_1,False)

            elif name == 'desclampeo40':
                name_routine = 'Man_CH1_INF40'
                if btn == 'On':
                    bool_value_1  = True
                
                else:
                    bool_value_1  = False
                
                self.send_message(name_routine,bool_value_1,False)
                
        return JsonResponse({})

            

    def send_message(self,name_routine, bool_value, data_base_plc_direction):
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
        msg_data_directions = {"jsonrpc":"2.0","method":"PlcProgram.Write","params":{"var":(first+name_routine+last),"value":bool_value}}
        msg_data_directions_container.append(msg_data_directions)

        #mensaje armado
        payload = json.dumps(msg_data_directions_container)

        headers = {
            'X-Auth-Token': PLC_TOKEN['token'],
            'Content-Type': 'application/json',
        }

        #se manda el mensaje
        conn.request("POST", "/api/jsonrpc", payload, headers)

        #respuesata mensaje
        # res = conn.getresponse()
        # data = res.read()
        # data_json = data.decode("utf-8")
        # data_parsed = json.loads(data_json)
        # bool_state_sensor = data_parsed["result"]
        # print(f"el valor cambio a{bool_state_sensor}")


@csrf_exempt
def send_command_bit(request):
    post_req = request.POST
    print(post_req)

    req_data = []
        
    for item in post_req.items():   # Item is in (key, value) format
        req_data.append(item)


    menu = req_data[0][1]
    name = req_data[1][1]
    print(menu,name)
    # print("el m prog es",M_PROGS_SEMIAUTO['M_PRG_30_40'])

    if name == "mesa1":
        name = ["M_PRG_MA","M_PRG_MA_CH"]
        bool_value_1 = False
        bool_value_2 = False
        # send_message_semi(name,bool_value)
        send_message_semi(name[0],bool_value_1,name[1],bool_value_2)

    elif name == "mesa2":
        name = ["M_PRG_MA","M_PRG_MA_CH"]
        bool_value = True
        bool_value_2 = False
        # send_message_semi(name,bool_value)
        send_message_semi(name[0],bool_value_1,name[1],bool_value_2)
    
    elif name == "okuma1":
        name = ["M_PRG_BIT0_CH","M_PRG_BIT1_CH","M_PRG_MA_CH"]
        bool_value_1 = False
        bool_value_2 = False
        bool_value_3 = True
        send_message_semi(name[0],bool_value_1,name[1],bool_value_2,name[2],bool_value_3)

    elif name == "okuma2":
        name = ["M_PRG_BIT0_CH","M_PRG_BIT1_CH","M_PRG_MA_CH"]
        bool_value_1 = False
        bool_value_2 = True
        bool_value_3 = True
        send_message_semi(name[0],bool_value_1,name[1],bool_value_2,name[2],bool_value_3)
    
    elif name == "okuma3":
        name = ["M_PRG_BIT0_CH","M_PRG_BIT1_CH","M_PRG_MA_CH"]
        bool_value_1 = True
        bool_value_2 = False
        bool_value_3 = True
        send_message_semi(name[0],bool_value_1,name[1],bool_value_2,name[2],bool_value_3)

    elif name == "okuma4":
        name = ["M_PRG_BIT0_CH","M_PRG_BIT1_CH","M_PRG_MA_CH"]
        bool_value_1 = False
        bool_value_2 = False
        bool_value_3 = True
        send_message_semi(name[0],bool_value_1,name[1],bool_value_2,name[2],bool_value_3)

    elif name == "u1":
        name = ["M_PRG_DRW","M_PRG_PAL"]
        bool_value_1 = True
        bool_value_2 = False
        send_message_semi(name[0],bool_value_1,name[1],bool_value_2)
        
    elif name == "u2":
        name = ["M_PRG_DRW","M_PRG_PAL"]
        bool_value_1 = True
        bool_value_2 = True
        send_message_semi(name[0],bool_value_1,name[1],bool_value_2)
    
    elif name == "d1":
        name = ["M_PRG_DRW","M_PRG_PAL"]
        bool_value_1 = False
        bool_value_2 = False
        send_message_semi(name[0],bool_value_1,name[1],bool_value_2)

    elif name == "d2":
        name = ["M_PRG_DRW","M_PRG_PAL"]
        bool_value_1 = False
        bool_value_2 = True
        send_message_semi(name[0],bool_value_1,name[1],bool_value_2)

    elif name == "tomar":
        name = "M_PRG_GET_PUT"
        bool_value = False
        send_message_semi(name,bool_value)

    elif name == "dejar":
        name = "M_PRG_GET_PUT"
        bool_value = True
        send_message_semi(name,bool_value)

    elif name == "op30":
        name = "M_PRG_30_40"
        bool_value = False
        send_message_semi(name,bool_value)

    elif name == "op40":
        name = "M_PRG_30_40"
        bool_value = True
        send_message_semi(name,bool_value)

    elif name == "casita1":
        name = "M_PRG_CAS"
        bool_value = False
        send_message_semi(name,bool_value)

    elif name == "casita2":
        name = "M_PRG_CAS"
        bool_value = True
        send_message_semi(name,bool_value)

   
    return JsonResponse({})
        