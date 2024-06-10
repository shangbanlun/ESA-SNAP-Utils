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
        files = [file for file in check_path.iterdir() if (file.is_file() and file.suffix == '.log')]

        check_line = '....10%....20%....30%....40%....50%....60%....70%....80%....90% done.\n'
        for file in files:
            with open(file, 'r') as f:
                lines = f.readlines()
            print(f'day {idx+1}/{num_days} {day.name}', check_line==lines[2], len(lines))
            if len(lines)==15: print(lines[14])

        
main()