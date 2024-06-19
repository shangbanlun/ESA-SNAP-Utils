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

# Sequential.GPT_PATH = '/home/wk/program_files/ESA-SNAP/10.0/esa-snap/bin/gpt'
Sequential.GPT_PATH = 'gpt.exe'


def batch_orb_process(home_folder: Path, input_folder_name: str, output_folder_name: str):
    graph = Sequential(
        Radar.ApplyOrbitFile()
    )
        
    # * list all the days in the home_folder
    days = list(home_folder.iterdir())
    num_days = len(days)
    days.sort()

    for idx, day in enumerate(days):
        print(Fore.BLUE + f'{day.name} has start...')

        input_path = day / input_folder_name
        files = [file for file in input_path.iterdir() if (file.is_file() and file.suffix == '.zip')]
        input_products = (SnapProduct(files[0]), SnapProduct(files[1]))

        product: SnapProduct
        for product in input_products:
            output_path = day / output_folder_name / f'{product.product_name}_{output_folder_name}.dim'
            log_path = day / output_folder_name / f'{product.product_name}_{output_folder_name}.log'

            # graph(product, output_path, log_path= log_path)
            graph(product, output_path)


        print(Fore.BLUE + f'({idx + 1}/{num_days}) {day.name} has completed!')
        print(Fore.YELLOW + '==============================================================================================================================\n')

        break


def batch_graph_process(home_folder: Path, graph: Sequential, input_folder_name: str, output_folder_name: str):
    # * list all the days in the home_folder
    days = list(home_folder.iterdir())
    num_days = len(days)
    days.sort()

    for idx, day in enumerate(days):
        print(Fore.BLUE + f'{day.name} has start...')

        input_path = day / input_folder_name
        files = [file for file in input_path.iterdir() if (file.is_file() and file.suffix == '.dim')]
        if len(files) == 2 : input_products = (SnapProduct(files[0]), SnapProduct(files[1]))
        else :
            input_products = SnapProduct(files[0])

        output_path = day / output_folder_name / f'{day.name}_{output_folder_name}.dim'
        log_path = day / output_folder_name / f'{day.name}_{output_folder_name}.log'
        # graph(input_products, output_path, log_path= log_path)
        graph(input_products, output_path)


        print(Fore.BLUE + f'({idx + 1}/{num_days}) {day.name} has completed!')
        print(Fore.YELLOW + '==============================================================================================================================\n')


def main():

    print(Fore.YELLOW + '==============================================================================================================================\n')

    home_folder = Path('D:\Dataset\Image')

    # batch_orb_process(home_folder, 'Raw', 'Orb')


    graph = Sequential(
        Radar.Sentinel_1_TOPS.SliceAssembly(),
        Radar.Radiometric.Calibration(is_ouput_sigma0_band= True),
        Radar.Speckle_Filtering.SingleProductSpeckleFilter(),
        Radar.Geometric.TerrainCorrection(map_projection= CRS.CGCS2000_SH),
        Raster.Data_Conversion.LinearToFromdB()
    )

    
    input_folder_name = 'Orb'
    output_folder_name = 'Sigma_dB'

    batch_graph_process(home_folder, graph, input_folder_name, output_folder_name)



main()