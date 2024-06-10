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

    print(Fore.YELLOW + '==============================================================================================================================\n')

    # * read a S1 product. 
    HOME_FOLDER = Path('/media/wk/0273d576-f619-4555-9a74-4745f3f71d09/SAR-IMAGE-DATASET/SAR/Original-Data/201506-202309_S1A_SLC')
    
    days = list(HOME_FOLDER.iterdir())
    num_days = len(days)
    days.sort()

    input_folder_name = 'Orb'
    output_folder_name = 'Asm_Cal_Deb_Mat_ML'


    # * get the sequential operator.
    graph = Sequential(
        R.Sentinel_1_TOPS.SliceAssembly(),
        R.Radiometric.Calibration(),
        R.Sentinel_1_TOPS.Deburst(),
        R.Polarimetric.MatrixGeneration(),
        R.SAR_Utilities.MultiLooking()
    )


    for idx, day in enumerate(days):

        input_path = day / input_folder_name
        files = [file for file in input_path.iterdir() if (file.is_file() and file.suffix == '.dim')]


        output_path = day / output_folder_name
        if not output_path.exists():
            products = (SnapProduct(files[0]), SnapProduct(files[1]))
            output_product_path = f'{output_path}/{day.name}_{output_folder_name}.dim'
            output_log_path = f'{output_path}/{day.name}_{output_folder_name}.log'

            print(f'graph for {day.name} has started...')
            # graph(products, output_product_path)
            graph(products, output_product_path, log_path= output_log_path)
            print(f'graph {day.name} is over.')

        else: 
            continue
        
        print(Fore.BLUE + f'{idx + 1}/{num_days} has completed!')
        print(Fore.YELLOW + '==============================================================================================================================\n')
        
main()