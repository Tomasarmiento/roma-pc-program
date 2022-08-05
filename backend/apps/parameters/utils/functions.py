# from apps.control.utils import variables as ctrl_vars
from . import variables as param_vars


def init_params():        # params: query with all parameters in database
    from apps.parameters.models import Parameter
    params = Parameter.objects.all()
    saved_params = dict([(param.name, param.value) for param in params])
    saved_keys = saved_params.keys()
    saved_values = saved_params.values()
    print(saved_keys)
    # hola = list(saved_keys)[0]
    # print(hola)

    for option in param_vars.MACHINE_MODEL_OPTIONS:
        print(option)
    # param_vars.MACHINE_SELECTED_MODEL = saved_params['machine_model']

def toggle_disable_machine(machine_name, turn_on_off):
    from apps.parameters.models import Parameter
    model_machine = Parameter.objects.get(name=machine_name)
    if turn_on_off == True:
        model_machine.value = 1
    else:
        model_machine.value = 0
    model_machine.save()


    
