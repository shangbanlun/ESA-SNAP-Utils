from typing import Tuple, Union


def integer_parameter_parser(value: int) -> str:
    return str(value)


def float_parameter_parser(value: float) -> str:
    return str(value)


def boolean_parameter_parser(value: bool) -> str:
    return 'true' if value else 'false'


def selected_polarisations_parser(value: str):
    if value == 'DV' : return 'VH,VV'
    elif value == 'DH' : return 'VH,HH'
    elif value in ['VH', 'HV', 'VV', 'HH'] : return value
    else : raise ValueError('The format of selected polarisations you input is not right, it must be one of [DV, DH, VV, HH, VH, HV].')


def subswath_parser(value: int) -> str:
    if value not in [1,2,3] :
        raise ValueError('The format of selected subswath you input is not right, it must be one of 1, 2 and 3.')
    
    return f'IW{value}'


def burst_range_parser(value: Tuple[int, int]) -> Tuple[str, str]:
    if not set(value).issubset([1, 2, 3, 4, 5, 6, 7, 8, 9]) :
        raise ValueError('The format of selected burst range you input is not right, it must be two integer between 1 and 9.')
    
    if value[0] < value[1] : return (str(value[0]), str(value[1]))
    else : return (str(value[1]), str(value[0]))


def region_parser(value: Tuple[Tuple[float, float], Tuple[float, float]]) -> str:
    x, y = value[0]
    x2, y2 = value[1]
    width, height = x2 - x, y2 - y

    return f'{x},{y},{width},{height}'


def geo_region_parser(value: Tuple[Tuple[float, float], Tuple[float, float]]) -> str:
    if not isinstance(value, tuple) or not all(isinstance(item, tuple) for item in value):
        raise TypeError('The format of the input must be ((float, float), (float, float))')
    if not all(isinstance(item, float) for item in value[0]) or not all(isinstance(item, float) for item in value[1]):
        raise TypeError('The latitude or the longitude you input must be the float number.')
    
    lat1, lon1 = value[0]
    lat2, lon2 = value[1]
    if any([lat1>90. or lat1<0., lat2>90. or lat2<0.]):
        raise ValueError('The latitude you input is out of range of 0 ~ 90.')
    if any([lon1>180. or lon1<0., lon2>180. or lon2<0.]):
        raise ValueError('The longitude you input is out of range of 0 ~ 180.')
    
    return f'POLYGON(({lon1} {lat1}, {lon2} {lat1}, {lon2} {lat2}, {lon1} {lat2}, {lon1} {lat1}))'


def window_size_parser(value: int) -> str:
    if not isinstance(value, int) : TypeError('The window size you input must be integer.')
    if value not in [5, 7, 9, 11, 13, 15, 17]: raise ValueError('The window size you input must be one 5, 7, 9, 11, 13, 15, 17.')
    
    return f'{value}x{value}'