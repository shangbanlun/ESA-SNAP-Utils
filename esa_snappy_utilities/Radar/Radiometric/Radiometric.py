from ... import core
from ... import parameter_parser
from typing import Optional
    
class Calibration(core.Operator):
    def __init__(
            self,
            is_save_as_complex_output: Optional[bool] = True,
            is_save_in_db: Optional[bool] = False,
            is_ouput_sigma0_band: Optional[bool] = True,
            is_ouput_gamma0_band: Optional[bool] = False,
            is_ouput_beta0_band: Optional[bool] = False,
        ) -> None:
        super().__init__()


        self._Operator__operator_name = 'Calibration'
        self._Operator__parameters = {
            'outputImageInComplex': parameter_parser.boolean_parameter_parser(is_save_as_complex_output),
            'outputImageScaleInDb': parameter_parser.boolean_parameter_parser(is_save_in_db),
            'outputSigmaBand': parameter_parser.boolean_parameter_parser(is_ouput_sigma0_band),
            'outputGammaBand': parameter_parser.boolean_parameter_parser(is_ouput_gamma0_band),
            'outputBetaBand': parameter_parser.boolean_parameter_parser(is_ouput_beta0_band)
        }

    def set_parameter(self, **kwargs):
        pass



