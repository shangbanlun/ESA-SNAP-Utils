from .. import core
from typing import Optional

class ApplyOrbitFile(core.Operator):
    def __init__(
            self, 
            orbit_type: Optional[str]= 'Sentinel Precise (Auto Download)',
            poly_degree: Optional[int] = 3,
            is_continue_on_fail: Optional[bool] = True
        ) -> None:


        self._Operator__operator_name = 'Apply-Orbit-File'
        self._Operator__parameters = {
            'orbitType': orbit_type,
            'polyDegree': str(poly_degree),
            'continueOnFail': 'true' if is_continue_on_fail else 'false'
        }


    def set_parameter(self, **kwargs):
        
        self.__parameters = {
            'orbitType': kwargs['orbit_type'],
            'polyDegree': str(kwargs['poly_degree']),
            'continueOnFail': 'true' if kwargs['is_continue_on_fail'] else 'false'
        }

