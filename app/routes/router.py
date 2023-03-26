from fastapi import APIRouter

from app.schemas.item_scheme import ItemScheme

router = APIRouter()


@router.post('/ML/Perceptron/adjust', tags=['Machine Learning'])
def create_machine(data: ItemScheme):
    gates = ('and', 'or', 'nand', 'nor')
    gate_assigned = data.gate
    gate_assigned = gate_assigned.lower()
    if (gate_assigned in gates):
        # res = neuron_activ(data.w1, data.w2, data.x1,
        #                    data.x2, data.th, data.gate)
        # print('flag')
        # if (res['result']):
        #     return {
        #         "Estado": "Neurona activada",
        #         "Value": res['value'],
        #         "Data": {
        #             "X1": data.x1,
        #             "X2": data.x2,
        #             "W1": data.w1,
        #             "W2": data.w2,
        #             "Th": data.th
        #         }
        #     }
        # else:
        #     return 'ok'  # <----------
        try:
            res = neuron_activ(data.w1, data.w2, data.x1,
                               data.x2, data.th, data.gate)
            # print('flag')
            if (res['result']):
                return {
                    "Estado": "Neurona activada",
                    "Value": res['values'],
                    "Data": {
                        "X1": data.x1,
                        "X2": data.x2,
                        "W1": data.w1,
                        "W2": data.w2,
                        "Th": data.th
                    }
                }
            else:
                return {
                    "Estado": "Necesita recálculo",
                    "Value": res['values'],
                    "Data": {
                        "X1": data.x1,
                        "X2": data.x2,
                        "W1": data.w1,
                        "W2": data.w2,
                        "Th": data.th
                    }
                }  # <----------
        except:
            return {
                "Estado": "Algo fue mal, el servicio no está disponible",
                "Value": None,
                "Data": {
                    "X1": data.x1,
                    "X2": data.x2,
                    "W1": data.w1,
                    "W2": data.w2,
                    "Th": data.th
                }
            }
    else:
        return {
            "Estado": "Compuerta lógica no válida",
            "Value": None,
            "Data": {
                "X1": data.x1,
                "X2": data.x2,
                "W1": data.w1,
                "W2": data.w2,
                "Th": data.th
            }
        }
