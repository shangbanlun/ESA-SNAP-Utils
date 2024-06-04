from typing import Optional, Tuple, Union


def selected_polarisations_parser(value: str):
    if value == 'DV' : return 'VH,VV'
    elif value == 'DH' : return 'VH,HH'
    elif value in ['VH', 'HV', 'VV', 'HH'] : return value
    else : raise ValueError('The format of selected polarisations you input is not right, it must be one of [DV, DH, VV, HH, VH, HV].')


def subswath_parser(value: int) -> str:
    if value not in [1,2,3] :
        raise ValueError('The format of selected subswath you input is not right, it must be one of 1, 2 and 3.')
    else : return f'IW{value}'


def burst_range_parser(value: Tuple[int, int]) -> Tuple[str, str]:
    if not set(value).issubset([1, 2, 3, 4, 5, 6, 7, 8, 9]) :
        raise ValueError('The format of selected burst range you input is not right, it must be two integer between 1 and 9.')
    
    if value[0] < value[1] : return (str(value[0]), str(value[1]))
    else : return (str(value[1]), str(value[0]))
