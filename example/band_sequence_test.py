from typing import List
from pathlib import Path
import sys
sys.path.append(".")
from colorama import init as colorama_init
colorama_init(autoreset= True)
from colorama import Fore

from esa_snappy_utilities import SnapProduct
from esa_snappy_utilities import Sequential
import esa_snappy_utilities.Radar as Radar
import esa_snappy_utilities.Raster as Raster
from esa_snappy_utilities.parameter_enum import CRS
from esa_snappy_utilities.parameter_enum import WriteType

geo_region = ((31.906, 121.141), (31.387, 122.017))
graph = Sequential(
    Raster.Subset(source_bands= 'Sigma0_VV_db,Sigma0_VH_db', geo_region= geo_region)
)

graph(SnapProduct('../Data/Image/2023-05-03/Sigma_dB/2023-05-03_Sigma_dB.dim'), 'test.dim')