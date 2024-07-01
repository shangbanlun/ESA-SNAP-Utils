from pathlib import Path
import sys
sys.path.append(".")


from ESA_SNAP_Utils import SnapProduct
from ESA_SNAP_Utils import Sequential
import ESA_SNAP_Utils.Radar as Radar
import ESA_SNAP_Utils.Raster as Raster

Sequential.GPT_PATH = 'path/to/the/gpt'


def main():

    # * get the sequential operator.
    apply_orbit_file_graph = Sequential(
        Radar.ApplyOrbitFile()
    )

    asm_cal_deb_sub_graph = Sequential(
        Radar.Sentinel_1_TOPS.SliceAssembly(),
        Radar.Radiometric.Calibration(),
        Radar.Sentinel_1_TOPS.Deburst(),
    )


    target_geo_region = ((31.9049, 121.1212), (31.3880, 121.9957))
    mat_ml_sf_dec_tc_graph = Sequential(
        Radar.Polarimetric.MatrixGeneration(),
        Radar.SAR_Utilities.MultiLooking(),
        Radar.Polarimetric.SpeckleFilter(),
        Radar.Polarimetric.Decomposition(method= 'H-Alpha Dual Pol Decomposition'),
        Radar.Geometric.TerrainCorrection(),
        Raster.Subset(geo_region= target_geo_region)
    )


    HOME_FOLDER = Path('./dataset')
    raw_folder_name = 'Raw'
    orbit_output_folder_name = 'Orb'
    basic_target_folder_name = 'Basic_Target'
    H_A_Alpha_folder_name = 'H-Alpha_Dual_Pol_Decomposition_Target'


    # * first step
    input_path = HOME_FOLDER / raw_folder_name
    files = [file for file in input_path.iterdir() if (file.is_file() and file.suffix == '.zip')]
    input_products = [SnapProduct(file) for file in files]

    for input_product in input_products:
        output_path = HOME_FOLDER / orbit_output_folder_name / f'{input_product.product_name}_{orbit_output_folder_name}.dim'
        log_path = HOME_FOLDER / orbit_output_folder_name / f'{input_product.product_name}_{orbit_output_folder_name}.log'
        # apply_orbit_file_graph(input_product, output_path, log_path= log_path)
        apply_orbit_file_graph(input_product, output_path)


    # * second step
    input_path = HOME_FOLDER / orbit_output_folder_name
    files = [file for file in input_path.iterdir() if (file.is_file() and file.suffix == '.dim')]
    input_products = (SnapProduct(files[0]), SnapProduct(files[1]))

    output_path = HOME_FOLDER / basic_target_folder_name / f'{basic_target_folder_name}.dim'
    log_path = HOME_FOLDER / basic_target_folder_name / f'{basic_target_folder_name}.log'
    # asm_cal_deb_sub_graph(input_products, output_path, log_path= log_path)
    asm_cal_deb_sub_graph(input_products, output_path)


    # * third step
    input_path = HOME_FOLDER / basic_target_folder_name
    files = [file for file in input_path.iterdir() if (file.is_file() and file.suffix == '.dim')]
    input_product = SnapProduct(files[0])

    output_path = HOME_FOLDER / H_A_Alpha_folder_name / f'{H_A_Alpha_folder_name}.dim'
    log_path = HOME_FOLDER / H_A_Alpha_folder_name / f'{H_A_Alpha_folder_name}.log'
    # mat_ml_sf_dec_tc_graph(input_product, output_path, log_path= log_path)
    mat_ml_sf_dec_tc_graph(input_product, output_path)

        
main()