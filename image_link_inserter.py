import pandas as pd

INPUT_FILE_PATH = r''  # Relative path to the coding sheet
CODING_FOLDER = ""  # Name of folder on dropbox that contains coding sheet and photos folder
PHOTOS_FOLDER = ""  # name of photos folder

LINK_FORMAT = 'https://www.dropbox.com/home/RoastMe/{}/{}?preview={}'

codings = pd.read_csv(r'Sept_and_Oct_2019_Codings\Sept_and_Oct_2019_Codings.csv')

codings['Image Link'] = [LINK_FORMAT.format(CODING_FOLDER, PHOTOS_FOLDER, x) for x in codings['Image Name']]

codings.to_csv(r'Sept_and_Oct_2019_Codings\Sept_and_Oct_2019_Codings.csv', encoding='utf-8-sig', index=False)
