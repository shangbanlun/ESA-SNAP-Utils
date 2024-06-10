from .. import core
from .. import parameter_parser
from typing import Optional, Tuple


class Subset(core.Operator):
    def __init__(
            self,
            source_bands: Optional[str] = None,
            tie_point_grids: Optional[str] = None,
            region: Optional[Tuple[int]] = ((0, 0), (0, 0)),
            reference_band: Optional[str] = None,
            geo_region: Optional[Tuple[Tuple[float, float], Tuple[float, float]]] = ((.0, .0), (.0, .0)),
            sub_sampling_x: Optional[int] = 1,
            sub_sampling_y: Optional[int] = 1,
            is_full_swath: Optional[bool] = False,
            is_copy_metadata: Optional[bool] = True
        ) -> None:
        super().__init__()

        self._Operator__operator_name = 'Subset'
        self._Operator__parameters = {
            'sourceBands': source_bands,
            'tiePointGrids': tie_point_grids,
            'region': parameter_parser.region_parser(region),
            'referenceBand': reference_band,
            'geoRegion': parameter_parser.geo_region_parser(geo_region),
            'subSamplingX': parameter_parser.integer_parameter_parser(sub_sampling_x),
            'subSamplingY': parameter_parser.integer_parameter_parser(sub_sampling_y),
            'fullSwath': parameter_parser.boolean_parameter_parser(is_full_swath),
            'copyMetadata': parameter_parser.boolean_parameter_parser(is_copy_metadata)
        }

    
    def set_parameter():
        pass