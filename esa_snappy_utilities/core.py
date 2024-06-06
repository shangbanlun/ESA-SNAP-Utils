from typing import Union, Optional, Any
from pathlib import Path
import numpy as np

from esa_snappy import ProductIO
from esa_snappy import File
from esa_snappy import GPF
from esa_snappy import ProgressMonitor

from colorama import Fore

from datetime import datetime
import xml.etree.ElementTree as ET
from subprocess import run


# * This class serves as a wrapper for the ESA-SNAP (Sentinel Application Platform) Product class,
# * providing a more user-friendly and Pythonic interface for interacting with satellite imagery data.
# * ESA-SNAP is a comprehensive toolbox for the scientific exploitation of Earth Observation missions,
# * especially those of the Sentinel series developed by the European Space Agency (ESA).
class SnapProduct():
    def __init__(self, input: Union[Any, str]) -> None:
        if isinstance(input, str):
            self.__product = ProductIO.readProduct(input)
            self.__path = input
        else:
            self.__product = input
            
        self.__product_name = self.__product.getName()
        self.__band_names = list(self.__product.getBandNames())
        self.__band_num = len(self.__band_names)

        self.__height = self.__product.getSceneRasterHeight()
        self.__width = self.__product.getSceneRasterWidth()


    def __del__(self):
        self.__product.closeIO()

    @property
    def product(self):
        return self.__product
    
    @property
    def path(self):
        return self.__path

    @property
    def product_name(self):
        return self.__product_name
    
    @property
    def band_names(self):
        return self.__band_names
    
    @property
    def size(self):
        return self.__height, self.__width

    def __getitem__(self, band_name: str):
        return self.__product.getBand(band_name)
    
    def info(self):
        return f'INFO about {self.__product_name} :: resolution: {self.__width}x{self.__height}, bands: {self.__band_names}.'


    def to_numpy(self) -> np.ndarray:
        '''
        return a numpy.ndarray with each band as axis 0, each row as axis 1 and each col as axis 2, namely the shape of ndarray is (band_num x height x width).
        '''
        output = np.empty((self.__band_num, self.__height * self.__width), dtype= np.float64)

        for idx, band_name in enumerate(self.__band_names):
            band = self.__product.getBand(band_name)

            temp = np.empty((self.__width * self.__height), dtype= np.float64)
            band.readPixels(0, 0, self.__width, self.__height, temp)
            output[idx] = temp
            print(f'{idx + 1}/{self.__band_num} band {band_name} completed.')

        return np.reshape(output, (self.__band_num, self.__height, self.__width))
    
    def write_product(self, path: str, format: Optional[str] = 'BEAM-DIMAP'):
        '''
        write the product.
        '''
        print(Fore.BLUE + 'Product writting' + Fore.WHITE + ' for ' + Fore.GREEN + self.product_name + Fore.WHITE + ' starts...')
        # ProductIO.writeProduct(self.__product, path, format)
        GPF.writeProduct(self.product, File(path), format, False, ProgressMonitor.NULL)
        print(Fore.BLUE + 'Product writting' + Fore.WHITE + ' for ' + Fore.GREEN + self.product_name + Fore.WHITE + ' has completed.')
        print(Fore.YELLOW + '======================================================================================\n')


class SnapBand():
    def __init__(self) -> None:
        pass


# * 仅部分操作
OPERATOR_LIST = [
    'Apply-Orbit-File',
    'Calibration',
    'Ellipsoid-Correction-RD',
    'Multilook',
    'Polarimetric-Decomposition',   # * 极化分解
    'Polarimetric-Matrices',    # * 生成极化矩阵
    'Subset',   # * 裁剪
    'Terrain-Correction',   # * 距离多普勒地形改正
    'TOPSAR-Deburst',   # * 
    'TOPSAR-Merge',
    'TOPSAR-Split',
]

from abc import ABC, abstractmethod

class Operator(ABC):
    def __init__(self) -> None:

        self.__operator_name = None
        self.__parameters = None

    @property
    def name(self):
        return self.__operator_name
    
    @property
    def parameters(self):
        return self.__parameters

    @abstractmethod
    def set_parameter():
        pass

    def __call__(self, product: SnapProduct) -> SnapProduct:
        print(Fore.BLUE + self.__operator_name + Fore.WHITE + ' for ' + Fore.GREEN + product.product_name + Fore.WHITE + ' starts ...')

        print(f'gpt {self.__operator_name} -Ssource="{product.path}" -t "{product.path}.dim"')
        
        print(Fore.BLUE + self.__operator_name + Fore.WHITE + ' for ' + Fore.GREEN + product.product_name + Fore.WHITE + ' has completed.')
        print(Fore.YELLOW + '======================================================================================\n')
        return 'Successfully Operation.'
    

def blank_graph_xml():
    root = ET.Element('graph')
    root.set('id', 'Graph')

    version = ET.SubElement(root, 'version')
    version.text = '1.0'

    return root

def add_node(root, id: str, processing_parameters: dict, source_product: Optional[str]= None):
    node = ET.SubElement(root, 'node')
    node.set('id', id)

    operator = ET.SubElement(node, 'operator')
    operator.text = id

    sources = ET.SubElement(node, 'sources')
    if source_product != None :
        sourceProduct = ET.SubElement(sources, 'sourceProduct')
        sourceProduct.set('refid', source_product)

    parameters = ET.SubElement(node, 'parameters')
    parameters.set('class', 'com.bc.ceres.binding.dom.XppDomElement')

    for parameter_name in processing_parameters:
        para = ET.SubElement(parameters, parameter_name)
        if processing_parameters[parameter_name] != None:
            para.text = processing_parameters[parameter_name]

    return root

class Sequential():
    def __init__(self, *args) -> None:
        # * Get the current date and time.
        home_folder = Path.cwd()
        current_time = datetime.now()
        self.__xml_path = f'{home_folder}/graph_{current_time.date()}-{current_time.hour}-{current_time.minute}-{current_time.second}-{current_time.microsecond}.xml'
        self.__operators = args


    def __call__(self, product: SnapProduct, path) -> None:
        read_parameters = {
            'useAdvancedOptions': 'false',
            'file': product.path,
            'formatName': 'SENTINEL-1',
            'copyMetadata': 'true',
            'bandNames': None,
            'pixelRegion': f'0,0,{product.size[1]},{product.size[0]}',
            'maskNames': None
        }

        root = blank_graph_xml()
        root = add_node(root, 'Read', read_parameters)
        before_name = 'Read'
        operator: Operator
        for operator in self.__operators:
            root = add_node(root, operator.name, operator.parameters, before_name)
            before_name = operator.name
        
        write_parameters = {
            'file': path,
            'formatName': 'BEAM-DIMAP'
        }
        root = add_node(root, 'Write', write_parameters, before_name)

        # * save the graph xml file.
        tree = ET.ElementTree(root)
        tree.write(self.__xml_path)

        # * run the gpt graph xml in file.
        run(f'gpt {self.__xml_path}')

        Path(self.__xml_path).unlink()

        print(f'graph process over.')