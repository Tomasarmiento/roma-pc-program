# from apps.control.utils import variables as ctrl_vars
from . import variables as param_vars


def init_params():        # params: query with all parameters in database
    from apps.parameters.models import Parameter
    params = Parameter.objects.all()
    saved_params = dict([(param.name, param.value) for param in params])
    saved_keys = saved_params.keys()
    for key, value in param_vars.DEFAULT_PARAMS.items():         
        if key not in saved_keys:
            param_vars.PARAMS[key] = value
        else:
            param_vars.PARAMS[key] = saved_params[key]
    

def toggle_disable_machine(machine_name):
    from apps.parameters.models import Parameter
    model_machine = Parameter.objects.get(name=machine_name)
    if model_machine.value == 1:
        model_machine.value = 0
    else:
        model_machine.value = 1
    model_machine.save()
    update_model_machine_params()

def update_model_machine_params():
    from apps.parameters.models import Parameter
    param_vars.PARAMS['okuma_1'] = Parameter.objects.get(name='okuma_1').value
    param_vars.PARAMS['okuma_2'] = Parameter.objects.get(name='okuma_2').value
    param_vars.PARAMS['okuma_3'] = Parameter.objects.get(name='okuma_3').value
    param_vars.PARAMS['okuma_4'] = Parameter.objects.get(name='okuma_4').value
    print("parametros",param_vars.PARAMS)
    
