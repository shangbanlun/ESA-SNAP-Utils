from ... import core
from ... import parameter_parser
from typing import Optional
from enum import Enum


class MatrixType(Enum):
    C2 = 'C2'
    C3 = 'C3'
    C4 = 'C4'
    T3 = 'T3'
    T4 = 'T4'


class MatrixGeneration(core.Operator):
    def __init__(
            self,
            matrix: Optional[MatrixType] = MatrixType.C2
        ) -> None:
        super().__init__()

        self._Operator__operator_name = 'Polarimetric-Matrices'
        self._Operator__parameters = {
            'matrix': matrix.value
        }
    
    def set_parameter():
        pass


class SpeckleFilterMethod(Enum):
    Box_Car = 'Box Car Filter'
    IDAN = 'IDAN Filter'
    Refined_Lee = 'Refined Lee Filter'
    Improved_Lee_Sigma = 'Improved Lee Sigma Filter'

class SpeckleFilter(core.Operator):
    '''
    
    '''
    def __init__(
            self,
            method: Optional[SpeckleFilterMethod] = SpeckleFilterMethod.Refined_Lee,
            num_looks: Optional[int] = 1,
            window_size: Optional[int] = 7
        ) -> None:
        super().__init__()

        self._Operator__operator_name = 'Polarimetric-Speckle-Filter'
        self._Operator__parameters = {
            'filter': method.value,
            'numLooksStr': parameter_parser.integer_parameter_parser(num_looks),
            'windowSize': parameter_parser.window_size_parser(window_size)
        }
    
    def set_parameter():
        pass


class DecompositionMethod(Enum):
    Sinclair = 'Sinclair Decomposition'
    Pauli = 'Pauli Decomposition'
    Freeman_Durden = 'Freeman-Durden Decomposition'
    Generalized_Freeman_Durden = 'Generalized Freeman-Durden Decomposition'
    Yamaguchi = 'Yamaguchi Decomposition'
    van_Zyl = 'van Zyl Decomposition'
    H_A_Alpha_Quad_Pol = 'H-A-Alpha Quad Pol Decomposition'
    H_Alpha_Dual_Pol = 'H-Alpha Dual Pol Decomposition'
    Cloude = 'Cloude Decomposition'

class Decomposition(core.Operator):
    '''
    The method of decomposition must be one of 
    '''
    def __init__(
            self,
            method: Optional[DecompositionMethod] = DecompositionMethod.H_Alpha_Dual_Pol,
            window_size: Optional[int] = 5
        ) -> None:
        super().__init__()

        self._Operator__operator_name = 'Polarimetric-Decomposition'
        self._Operator__parameters = {
            'decomposition': method.value,
            'windowSize': parameter_parser.integer_parameter_parser(window_size)
        }
    
    def set_parameter():
        pass