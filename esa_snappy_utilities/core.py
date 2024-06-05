import numpy as np
from esa_snappy import ProductIO
from esa_snappy import HashMap
from esa_snappy import File
from esa_snappy import GPF
from esa_snappy import ProgressMonitor
from typing import Union, Any, Optional
from colorama import Fore


# * This class serves as a wrapper for the ESA-SNAP (Sentinel Application Platform) Product class,
# * providing a more user-friendly and Pythonic interface for interacting with satellite imagery data.
# * ESA-SNAP is a comprehensive toolbox for the scientific exploitation of Earth Observation missions,
# * especially those of the Sentinel series developed by the European Space Agency (ESA).
class SnapProduct():
    def __init__(self, input: Union[Any, str]) -> None:
        if isinstance(input, str):
            self.__product = ProductIO.readProduct(input)
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
        # ProductIO.writeProduct(self.__product, path, format)
        print(Fore.BLUE + 'Product writting' + Fore.WHITE + ' for ' + Fore.GREEN + self.product_name + Fore.WHITE + ' starts...')
        GPF.writeProduct(self.product, File(path), format, False, ProgressMonitor.NULL)
        print(Fore.BLUE + 'Product writting' + Fore.WHITE + ' for ' + Fore.GREEN + self.product_name + Fore.WHITE + ' has completed.')
        print(Fore.YELLOW + '======================================================================================\n')


class SnapBand():
    def __init__(self) -> None:
        pass


def _dict2hashmap(dict_: dict):
    hashmap = HashMap()
    for key in dict_:
        hashmap.put(key, dict_[key])
    
    return hashmap

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

    @abstractmethod
    def set_parameter():
        pass

    def __call__(self, product: SnapProduct) -> SnapProduct:
        print(Fore.BLUE + self.__operator_name + Fore.WHITE + ' for ' + Fore.GREEN + product.product_name + Fore.WHITE + ' starts ...')
        processing_parameters = _dict2hashmap(self.__parameters)
        output = GPF.createProduct(self.__operator_name, processing_parameters, product.product)
        print(Fore.BLUE + self.__operator_name + Fore.WHITE + ' for ' + Fore.GREEN + product.product_name + Fore.WHITE + ' has completed.')
        print(Fore.YELLOW + '======================================================================================\n')
        return SnapProduct(output)
    

class Sequential():
    def __init__(self) -> None:
        pass