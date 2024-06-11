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


    # * get the sequential operator.
    apply_orbit_file_graph = Sequential(
        Radar.ApplyOrbitFile()
    )

    target_geo_region = ((31.9049, 121.1212), (31.3880, 121.9957))

    asm_cal_deb_sub_graph = Sequential(
        Radar.Sentinel_1_TOPS.SliceAssembly(),
        Radar.Radiometric.Calibration(),
        Radar.Sentinel_1_TOPS.Deburst(),
        Raster.Subset(geo_region= target_geo_region)
    )

    mat_ml_sf_dec_tc_graph = Sequential(
        Radar.Polarimetric.MatrixGeneration(),
        Radar.SAR_Utilities.MultiLooking(),
        Radar.Polarimetric.SpeckleFilter(),
        Radar.Polarimetric.Decomposition(method= 'H-Alpha Dual Pol Decomposition'),
        Radar.Geometric.TerrainCorrection()
    )

    raw_folder_name = 'Raw'
    orbit_output_folder_name = 'Orb'
    basic_target_folder_name = 'Basic_Target'
    H_A_Alpha_folder_name = 'H-Alpha_Dual_Pol_Decomposition_Target'

    for idx, day in enumerate(days):
        print(Fore.BLUE + f'{day.name} has start...')

        # * first step
        input_path = day / raw_folder_name
        files = [file for file in input_path.iterdir() if (file.is_file() and file.suffix == '.zip')]
        input_products = [SnapProduct(file) for file in files]

        for input_product in input_products:
            output_path = day / orbit_output_folder_name / f'{input_product.product_name}_{orbit_output_folder_name}.dim'
            log_path = day / orbit_output_folder_name / f'{input_product.product_name}_{orbit_output_folder_name}.log'
            # apply_orbit_file_graph(input_product, output_path, log_path= log_path)
            apply_orbit_file_graph(input_product, output_path)


        # * second step
        input_path = day / orbit_output_folder_name
        files = [file for file in input_path.iterdir() if (file.is_file() and file.suffix == '.dim')]
        input_products = (SnapProduct(files[0]), SnapProduct(files[1]))

        output_path = day / basic_target_folder_name / f'{day.name}_{basic_target_folder_name}.dim'
        log_path = day / basic_target_folder_name / f'{day.name}_{basic_target_folder_name}.log'
        # asm_cal_deb_sub_graph(input_products, output_path, log_path= log_path)
        asm_cal_deb_sub_graph(input_products, output_path)


        # * third step
        input_path = day / basic_target_folder_name
        files = [file for file in input_path.iterdir() if (file.is_file() and file.suffix == '.dim')]
        input_product = SnapProduct(files[0])

        output_path = day / H_A_Alpha_folder_name / f'{day.name}_{H_A_Alpha_folder_name}.dim'
        log_path = day / H_A_Alpha_folder_name / f'{day.name}_{H_A_Alpha_folder_name}.log'
        # mat_ml_sf_dec_tc_graph(input_product, output_path, log_path= log_path)
        mat_ml_sf_dec_tc_graph(input_product, output_path)


        print(Fore.BLUE + f'({idx + 1}/{num_days}) {day.name} has completed!')
        print(Fore.YELLOW + '==============================================================================================================================\n')

        
main()