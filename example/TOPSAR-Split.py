from pathlib import Path
HOME_FOLDER = Path(__file__).parent
import sys
sys.path.append(".")
from colorama import init as colorama_init
colorama_init(autoreset= True)
from colorama import Fore
from esa_snappy_utilities import SnapProduct
import esa_snappy_utilities.Radar as R


def main():

    print(Fore.YELLOW + '==================================================================================\n')

    # * read a S1 product. / 读入一个哨兵一号影像产品
    file_path = '.\example\data\S1A_IW_SLC__1SDV_20150602T215750_20150602T215817_006200_008158_DB54.zip'
    product = SnapProduct(file_path)

    # * new a Operator and apply it to a SnapProduct. / 实例化一个
    split_operator = R.Sentinel_1_TOPS.Split(1, bursts= (8, 9))
    output = split_operator(product)

    # * write the output SnapProduct.
    output.write_product(f'./example/data/{output.product_name}_IW1_Brusts-8-9.dim')
    
main()