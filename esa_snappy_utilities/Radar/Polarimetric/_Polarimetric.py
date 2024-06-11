from ... import core
from ... import parameter_parser
from typing import Optional


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


class SpeckleFilter(core.Operator):
    def __init__(
            self,
            filter: Optional[str] = 'Refined Lee Filter',
            num_looks: Optional[int] = 1,
            window_size: Optional[int] = 7
        ) -> None:
        super().__init__()

        self._Operator__operator_name = 'Polarimetric-Speckle-Filter'
        self._Operator__parameters = {
            'filter': filter,
            'numLooksStr': parameter_parser.integer_parameter_parser(num_looks),
            'windowSize': parameter_parser.window_size_parser(window_size)
        }
    
    def set_parameter():
        pass


class Decomposition(core.Operator):
    '''
    The method of decomposition must be one of 
    Sinclair, Pauli, Freeman-Durden, Generalized Freeman-Durden, Yamaguchi, van Zyl, Cloude, H-A-Alpha Dual Pol Decomposition.
    '''
    def __init__(
            self,
            method: Optional[str] = 'Sinclair Decomposition',
            window_size: Optional[int] = 5
        ) -> None:
        super().__init__()

        self._Operator__operator_name = 'Polarimetric-Decomposition'
        self._Operator__parameters = {
            'decomposition': method,
            'windowSize': parameter_parser.integer_parameter_parser(window_size)
        }
    
    def set_parameter():
        pass