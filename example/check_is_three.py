from pathlib import Path


def main():

    # * read a S1 product. 
    HOME_FOLDER = Path('/media/wk/0273d576-f619-4555-9a74-4745f3f71d09/SAR-IMAGE-DATASET/SAR/Original-Data/201506-202309_S1A_SLC')
    
    days = list(HOME_FOLDER.iterdir())
    num_days = len(days)
    days.sort()


    check_folder_name = 'Asm_Cal_Deb_Mat_ML'


    for idx, day in enumerate(days):

        check_path = day / check_folder_name
        if not check_path.exists() : print(day.name)

main()