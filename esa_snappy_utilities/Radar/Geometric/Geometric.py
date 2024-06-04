from ... import core
from typing import Optional


class TerrainCorrection(core.Operator):
    def __init__(
            self,
            DEM_name: Optional[str]= 'SRTM 3Sec',
            is_save_DEM: Optional[bool] = True,
            is_save_LatLon: Optional[bool]= False
        ) -> None:
        super().__init__()

        self.__operator_name = 'Terrain-Correction'
        self.__parameters = {
            'demName': DEM_name,
            'saveDEM': 'ture' if is_save_DEM else 'false'
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