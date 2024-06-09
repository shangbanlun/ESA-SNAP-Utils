from ... import core
from ... import parameter_parser
from typing import Optional, Tuple


class MultiLooking(core.Operator):
    def __init__(
            self,
            source_bands: Optional[str] = None,
            n_range_looks: Optional[int] = 4,
            n_azimuth_looks: Optional[int] = 1,
            is_output_intensity: Optional[bool] = False,
            is_gr_square_pixel: Optional[bool] = True
        ) -> None:
        super().__init__()

        self._Operator__operator_name = 'Multilook'
        self._Operator__parameters = {
            'sourceBands': source_bands,
            'nRgLooks': str(n_range_looks),
            'nAzLooks': str(n_azimuth_looks),
            'outputIntensity': parameter_parser.boolean_parameter_parser(is_output_intensity),
            'grSquarePixel': parameter_parser.boolean_parameter_parser(is_gr_square_pixel)
        }

    def set_parameter():
        pass