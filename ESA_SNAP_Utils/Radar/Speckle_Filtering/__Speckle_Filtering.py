from typing import Optional, Tuple
from enum import Enum

from ... import core
from ... import parameter_parser


class Filter(Enum):
    Refined_Lee = 'Refined Lee'

class SingleProductSpeckleFilter(core.Operator):
    def __init__(
            self,
            polarisations: Optional[str] = None,
            filter: Optional[Filter] = Filter.Refined_Lee,
        ) -> None:
        super().__init__()

        self._Operator__operator_name = 'Speckle-Filter'
        self._Operator__parameters = {
            'sourceBands': parameter_parser.selected_polarisations_parser(polarisations),
            'filter': filter.value,
            # 'filterSizeX': '3',
            # 'filterSizeY': '3',
            # 'dampingFactor': '2',
            # 'estimateENL': 'true',
            # 'enl': '1.0',
            # 'numLooksStr': '1',
            # 'windowSize': '7x7',
            # 'targetWindowSizeStr': '3x3',
            # 'sigmaStr': '0.9',
            # 'anSize': '0'
        }

    def set_parameter():
        pass