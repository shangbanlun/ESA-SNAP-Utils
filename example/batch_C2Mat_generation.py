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

# Sequential.GPT_PATH = '/home/wk/program_files/ESA-SNAP/10.0/esa-snap/bin/gpt'
Sequential.GPT_PATH = 'gpt.exe'


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

    # * read a S1 product. 
    # HOME_FOLDER = Path('/media/wk/0273d576-f619-4555-9a74-4745f3f71d09/SAR-IMAGE-DATASET/SAR/Original-Data/201506-202309_S1A_SLC')
    home_folder = Path('D:\Dev\SAR_SNAP_Desktop')

    # large_geo_region = ((32.1919, 120.8933), (31.0971, 122.3110))

    # graph = Sequential(
    #     Radar.Sentinel_1_TOPS.SliceAssembly(),
    #     Radar.Radiometric.Calibration(),
    #     Radar.Sentinel_1_TOPS.Deburst(),
    #     Raster.Subset(geo_region= large_geo_region)
    # )

    # input_folder_name = 'Orb'
    # output_folder_name = 'Complex_Dual_Pol_Image'


    # graph = Sequential(
    #     Radar.Polarimetric.MatrixGeneration(),
    #     Radar.SAR_Utilities.MultiLooking(),
    #     Radar.Polarimetric.SpeckleFilter()
    # )

    # input_folder_name = 'Complex_Dual_Pol_Image'
    # output_folder_name = 'C2Mat'


    target_geo_region = ((31.9049, 121.1212), (31.3880, 121.9957))

    graph = Sequential(
        Radar.Polarimetric.Decomposition(method= Radar.Polarimetric.DecompositionMethod.H_Alpha_Dual_Pol),
        Radar.Geometric.TerrainCorrection(),
        Raster.Subset(geo_region= target_geo_region)
    )

    input_folder_name = 'C2Mat'
    output_folder_name = 'Decomposition'

    batch_graph_process(home_folder, graph, input_folder_name, output_folder_name)


main()