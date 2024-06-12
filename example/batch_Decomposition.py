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

Sequential.GPT_PATH = 'gpt.exe'

def main():

    print(Fore.YELLOW + '==============================================================================================================================\n')

    # * read a S1 product. 
    # HOME_FOLDER = Path('/media/wk/0273d576-f619-4555-9a74-4745f3f71d09/SAR-IMAGE-DATASET/SAR/Original-Data/201506-202309_S1A_SLC')
    HOME_FOLDER = Path('D:\Dev\SAR_SNAP_Desktop')

    days = list(HOME_FOLDER.iterdir())
    num_days = len(days)
    days.sort()

    target_geo_region = ((31.9049, 121.1212), (31.3880, 121.9957))

    graph = Sequential(
        Radar.Polarimetric.Decomposition(method= 'H-Alpha Dual Pol Decomposition'),
        Radar.Geometric.TerrainCorrection(),
        Raster.Subset(geo_region= target_geo_region)
    )


    input_folder_name = 'C2Mat'
    output_path = 'Decomposition'

    for idx, day in enumerate(days):
        print(Fore.BLUE + f'{day.name} has start...')

        # * second step
        input_path = day / input_folder_name
        files = [file for file in input_path.iterdir() if (file.is_file() and file.suffix == '.dim')]
        input_product = SnapProduct(files[0])

        output_path = day / output_path / f'{day.name}_H-Alpha_Dual_Pol.dim'
        log_path = day / output_path / f'{day.name}_H-Alpha_Dual_Pol.log'
        # graph(input_product, output_path, log_path= log_path)
        graph(input_product, output_path)


        print(Fore.BLUE + f'({idx + 1}/{num_days}) {day.name} has completed!')
        print(Fore.YELLOW + '==============================================================================================================================\n')

        
main()