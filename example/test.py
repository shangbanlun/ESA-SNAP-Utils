from pathlib import Path
HOME_FOLDER = Path(__file__).parent
import sys
sys.path.append(".")
from colorama import init as colorama_init
colorama_init(autoreset= True)
from colorama import Fore
from esa_snappy_utilities import SnapProduct
import esa_snappy_utilities.Radar as R

def test():

    print(Fore.YELLOW + '==================================================================================\n')
    filename = './example/data/S1A_IW_SLC__1SDV_20150609T214949_20150609T215019_006302_008458_8F40.zip'
    product = SnapProduct(filename)
    apply_orbit_operator = R.ApplyOrbitFile()
    calibration_operator = R.Radiometric.Calibration()

    output = apply_orbit_operator(product)
    output = calibration_operator(output)

    output.write_product('./example/data/output.dim')
    
test()