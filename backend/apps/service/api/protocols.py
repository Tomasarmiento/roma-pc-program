from opcua import Client, ua
import time

from apps.ws.utils.variables import OPC_variables
from apps.control.utils import variables as control_vars

class OPCProtocol():

    def __init__(self):
        super().__init__()


    def read_input_value(self,node_id,sensor_peticion):
        # print("refresh")
        from apps.control.utils.functions import update_msg_error,derived_sensores_states
        client_node = OPC_variables.CLIENT.get_node(node_id)  # get node
        client_node_value = client_node.get_value()  # read node value
        # print(len(list(client_node_value)))
        if sensor_peticion == True:
            update_msg_error(derived_sensores_states(list(client_node_value)))
        else:
            control_vars.PLC_DEFAULT_VARIABLES_INT[".step_auto"] = list(client_node_value)[0]
            control_vars.PLC_DEFAULT_VARIABLES_INT[".step_semi"] = list(client_node_value)[1]
        

        # print("Value of : " + str(client_node) + ' : ' + str(client_node_value))


    def write_value_int(self,node_id, value):
        client_node = OPC_variables.CLIENT.get_node(node_id)  # get node
        client_node_value = value
        client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Int16))
        client_node.set_value(client_node_dv)
        print("Value of : " + str(client_node) + ' : ' + str(client_node_value))


    def write_value_bool(self,node_id, value, second_node_id=None, second_value=None):
        client_node = OPC_variables.CLIENT.get_node(node_id)
        client_node_value = value
        client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Boolean))
        client_node.set_value(client_node_dv)
        print("Value of : " + str(client_node) + ' : ' + str(client_node_value))
        
        if second_node_id:
            client_node,second_client_node = OPC_variables.CLIENT.get_node(node_id),OPC_variables.CLIENT.get_node(second_node_id)  # get node
            client_node_value,second_client_node_value = value,second_value
            client_node_dv,second_client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Boolean)),ua.DataValue(ua.Variant(second_client_node_value, ua.VariantType.Boolean))
            client_node.set_value(client_node_dv)
            second_client_node.set_value(second_client_node_dv)

            print("Value of : " + str(second_client_node) + ' : ' + str(second_client_node_value))

