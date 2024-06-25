from ... import core
from ... import parameter_parser
from ...parameter_enum import CRS
from typing import Optional


class TerrainCorrection(core.Operator):
    def __init__(
            self,
            source_bands: Optional[str] = None,
            DEM_name: Optional[str] = 'SRTM 3Sec',
            map_projection: Optional[CRS] = CRS.WGS84DD,
            external_DEM_file: Optional[str] = None,
            external_DEM_no_data_value: Optional[float] = 0.0,
            is_external_DEM_apply_EGM: Optional[bool] = True,
            DEM_resampling_method: Optional[str] = 'BILINEAR_INTERPOLATION',
            img_resampling_method: Optional[str] = 'BILINEAR_INTERPOLATION',
            is_no_data_value_at_sea: Optional[bool] = False,
            is_save_DEM: Optional[bool] = False,
            is_save_LatLon: Optional[bool]= False
        ) -> None:
        super().__init__()

        self._Operator__operator_name = 'Terrain-Correction'
        self._Operator__parameters = {
            'sourceBands': source_bands,
            'demName': DEM_name,
            'externalDEMFile': external_DEM_file,
            'externalDEMNoDataValue': parameter_parser.float_parameter_parser(external_DEM_no_data_value),
            'externalDEMApplyEGM': parameter_parser.boolean_parameter_parser(is_external_DEM_apply_EGM),
            'demResamplingMethod': DEM_resampling_method,
            'imgResamplingMethod': img_resampling_method,
            'mapProjection': map_projection.value,
            'alignToStandardGrid': 'false',
            'standardGridOriginX': '0.0',
            'standardGridOriginY': '0.0',
            'nodataValueAtSea': parameter_parser.boolean_parameter_parser(is_no_data_value_at_sea),
            'saveDEM': parameter_parser.boolean_parameter_parser(is_save_DEM),
            'saveLatLon': parameter_parser.boolean_parameter_parser(is_save_LatLon),
            'saveIncidenceAngleFromEllipsoid': 'false',
            'saveLocalIncidenceAngle': 'false',
            'saveProjectedLocalIncidenceAngle': 'false',
            'saveSelectedSourceBand': 'true',
            'saveLayoverShadowMask': 'false',
            'outputComplex': 'false',
            'applyRadiometricNormalization': 'false',
            'saveSigmaNought': 'false',
            'saveGammaNought': 'false',
            'saveBetaNought': 'false',
            'incidenceAngleForSigma0': 'Use projected local incidence angle from DEM',
            'incidenceAngleForGamma0': 'Use projected local incidence angle from DEM',
            'auxFile': 'Latest Auxiliary File'
        }
    
    def set_parameter(self, **kwargs):
        para_dict = {
            'sourceBands': '',
            'demName': 'DEM_name',
            'externalDEMFile': 'D:\Downloads\srtm_61_06\srtm_61_06.tif',
            'externalDEMNoDataValue': '0.0',
            'externalDEMApplyEGM': 'true',
            'demResamplingMethod': 'BILINEAR_INTERPOLATION',
            'imgResamplingMethod': 'BILINEAR_INTERPOLATION',
            'pixelSpacingInMeter': '15.994918731590458',
            'pixelSpacingInDegree': '1.4368479964837338E-4',
            'mapProjection': 'GEOGCS["WGS84(DD)", DATUM["WGS84", SPHEROID["WGS84", 6378137.0, 298.257223563]], PRIMEM["Greenwich", 0.0], UNIT["degree", 0.017453292519943295], AXIS["Geodetic longitude", EAST], AXIS["Geodetic latitude", NORTH], AUTHORITY["EPSG","4326"]]',
            'alignToStandardGrid': 'false',
            'standardGridOriginX': '0.0',
            'standardGridOriginY': '0.0',
            'nodataValueAtSea': 'false',
            'saveDEM': 'ture',
            'saveLatLon': 'ture',
            'saveIncidenceAngleFromEllipsoid': 'false',
            'saveLocalIncidenceAngle': 'false',
            'saveProjectedLocalIncidenceAngle': 'false',
            'saveSelectedSourceBand': 'true',
            'saveLayoverShadowMask': 'false',
            'outputComplex': 'false',
            'applyRadiometricNormalization': 'false',
            'saveSigmaNought': 'false',
            'saveGammaNought': 'false',
            'saveBetaNought': 'false',
            'incidenceAngleForSigma0': 'Use projected local incidence angle from DEM',
            'incidenceAngleForGamma0': 'Use projected local incidence angle from DEM',
            'auxFile': 'Latest Auxiliary File'
        }