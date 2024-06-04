from ... import core
from typing import Optional
    
class Calibration(core.Operator):
    def __init__(
            self,
            is_save_as_complex_output: Optional[bool] = True,
            is_save_as_scale_in_db: Optional[bool] = False,
            is_ouput_sigma0_band: Optional[bool] = True,
            is_ouput_gamma0_band: Optional[bool] = False,
            is_ouput_beta0_band: Optional[bool] = False,
        ) -> None:
        super().__init__()


        self._Operator__operator_name = 'Calibration'
        self._Operator__parameters = {
            # 'sourceBands': 'VH,VV',
            'outputImageInComplex': 'true' if is_save_as_complex_output else 'false',
            'outputImageScaleInDb': 'true' if is_save_as_scale_in_db else 'false',
            'outputSigmaBand': 'true' if is_ouput_sigma0_band else 'false',
            'outputGammaBand': 'true' if is_ouput_gamma0_band else 'false',
            'outputBetaBand': 'true' if is_ouput_beta0_band else 'false'
        }

    def set_parameter(self, **kwargs):
        pass



