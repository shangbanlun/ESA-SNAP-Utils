from ... import core
from ... import parameter_parser
from typing import Optional, Tuple


class SliceAssembly(core.Operator):
    def __init__(
            self,
            polarisations: Optional[str] = None
        ) -> None:
        super().__init__()

        self._Operator__operator_name = 'SliceAssembly'
        self._Operator__parameters = {
            'selectedPolarisations': parameter_parser.selected_polarisations_parser(polarisations)
        }

    def set_parameter():
        pass

class Split(core.Operator):
    def __init__(
            self,
            subswath: Optional[int] = 1,
            polarisations: Optional[str] = None,
            bursts: Optional[Tuple[int, int]] = (1, 9)
        ) -> None:
        super().__init__()

        first_burst_index, last_burst_index = parameter_parser.burst_range_parser(bursts)
        self._Operator__operator_name = 'TOPSAR-Split'
        self._Operator__parameters = {
            'subswath': parameter_parser.subswath_parser(subswath),
            'selectedPolarisations': parameter_parser.selected_polarisations_parser(polarisations),
            'firstBurstIndex': first_burst_index,
            'lastBurstIndex': last_burst_index
        }


    def set_parameter(self, **kwargs):
        pass


class Deburst(core.Operator):
    def __init__(
            self,
            polarisations: Optional[str] = None
        ) -> None:
        super().__init__()


        self._Operator__operator_name = 'TOPSAR-Deburst'
        self._Operator__parameters = {
            'selectedPolarisations' : parameter_parser.selected_polarisations_parser(polarisations)
        }

    def set_parameter(self, **kwargs):
        pass


# class Merge(core.Operator):
#     def __init__(
#             self,

#         ) -> None:
#         super().__init__()


#         self._Operator__operator_name = ''
#         self._Operator__parameters = {

#         }

#     def set_parameter(self, **kwargs):
#         pass