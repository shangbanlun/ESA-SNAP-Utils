from enum import Enum


class MatrixType(Enum):
    C2 = 'C2'
    C3 = 'C3'
    C4 = 'C4'
    T3 = 'T3'
    T4 = 'T4'


class SpeckleFilterMethod(Enum):
    Box_Car = 'Box Car Filter'
    IDAN = 'IDAN Filter'
    Refined_Lee = 'Refined Lee Filter'
    Improved_Lee_Sigma = 'Improved Lee Sigma Filter'


class Filter(Enum):
    Refined_Lee = 'Refined Lee'


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


class CRS(Enum):
    WGS84DD = 'GEOGCS["WGS84(DD)", DATUM["WGS84", SPHEROID["WGS84", 6378137.0, 298.257223563]], PRIMEM["Greenwich", 0.0], UNIT["degree", 0.017453292519943295], AXIS["Geodetic longitude", EAST], AXIS["Geodetic latitude", NORTH], AUTHORITY["EPSG","4326"]]'
    CGCS2000_SH = 'PROJCS["Transverse_Mercator / World Geodetic System 1984", GEOGCS["World Geodetic System 1984", DATUM["World Geodetic System 1984", SPHEROID["WGS 84", 6378137.0, 298.257223563, AUTHORITY["EPSG","7030"]], AUTHORITY["EPSG","6326"]], PRIMEM["Greenwich", 0.0, AUTHORITY["EPSG","8901"]], UNIT["degree", 0.017453292519943295], AXIS["Geodetic longitude", EAST], AXIS["Geodetic latitude", NORTH]], PROJECTION["Transverse_Mercator"], PARAMETER["semi_minor", 6356752.31414], PARAMETER["central_meridian", 120.0], PARAMETER["latitude_of_origin", 0.0], PARAMETER["scale_factor", 1.0], PARAMETER["false_easting", 40500000.0], PARAMETER["false_northing", 0.0], UNIT["m", 1.0], AXIS["Easting", EAST], AXIS["Northing", NORTH]]'


class WriteType(Enum):
    BEAM_DIMAP = 'BEAM-DIMAP'
    GeoTIFF = 'GeoTIFF'
    JPG = 'JPG'