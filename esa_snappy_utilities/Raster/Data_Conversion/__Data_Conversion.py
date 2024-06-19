from typing import Optional, Tuple

from ... import core
from ... import parameter_parser


class LinearToFromdB(core.Operator):
    def __init__(
            self,
            source_bands: Optional[str] = None,
        ) -> None:
        super().__init__()

        self._Operator__operator_name = 'LinearToFromdB'
        self._Operator__parameters = {
            'sourceBands': parameter_parser.selected_polarisations_parser(source_bands),
        }

    
    def set_parameter():
        pass