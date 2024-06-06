from pathlib import Path
HOME_FOLDER = Path(__file__).parent
import sys
sys.path.append(".")
from colorama import init as colorama_init
colorama_init(autoreset= True)
from colorama import Fore
from esa_snappy_utilities import SnapProduct
from esa_snappy_utilities import Sequential
import esa_snappy_utilities.Radar as R


def main():

    print(Fore.YELLOW + '==================================================================================\n')

    # * read a S1 product. / 读入一个哨兵一号影像产品
    one_day_data_path = Path('./example/data/2015-06-02')
    graph = Sequential(
        # R.ApplyOrbitFile(),
        R.Radiometric.Calibration(),
        # R.Sentinel_1_TOPS.Split(1, bursts= (8,9)),
        # R.Sentinel_1_TOPS.Deburst()
    )

    for file in one_day_data_path.iterdir():
        print(str(file))
        product = SnapProduct(str(file))
        graph(product, f'{one_day_data_path}\{product.product_name}__Orb.dim')


main()