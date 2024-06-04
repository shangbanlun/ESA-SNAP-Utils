from pathlib import Path
HOME_FOLDER = Path(__file__).parent
import sys
sys.path.append(".\\")

from esa_snappy_utilities import SnapProduct
# from esa_snappy_utilities import Radar
import esa_snappy_utilities.Radar as R

def test():

    filename = './example/data/S1A_IW_SLC__1SDV_20150602T215750_20150602T215817_006200_008158_DB54.zip'
    product = SnapProduct(filename)
    
    apply_orbit_operator = R.ApplyOrbitFile()
    calibration_operator = R.Radiometric.Calibration()

    output = apply_orbit_operator(product)
    output = calibration_operator(output)

    output.write_product('./example/data/output.dim')
    
test()