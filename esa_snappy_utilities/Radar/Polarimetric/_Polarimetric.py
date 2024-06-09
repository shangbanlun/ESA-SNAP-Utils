from ... import core
from ... import parameter_parser
from typing import Optional, Tuple


class MatrixGeneration(core.Operator):
    def __init__(
            self,
            matrix: Optional[str] = 'C2'
        ) -> None:
        super().__init__()

        self._Operator__operator_name = 'Polarimetric-Matrices'
        self._Operator__parameters = {
            'matrix': matrix
        }
    
    def set_parameter():
        pass