import pandas as pd
import shutil
import os

POST_INPUT_FILE = ".csv"  # posts csv collected from pushshift
COMMENTS_INPUT_FILE = ".csv"  # comments csv collected from RedditExtractor

# Read in posts and comments
posts = pd.read_csv(POST_INPUT_FILE)
comments = pd.read_csv(COMMENTS_INPUT_FILE)

# Remove rows that are not actually bios
mask = comments['author'] == 'roastbot'
bios = comments[mask]

# Clean Bios
bios['comment'] = bios['comment'].str.split('&gt;').str[1].str.split('---').str[0]
bios['comment'] = bios['comment'].str.strip()

# only keep relevant columns from each df
# posts = posts[['Index', 'author', 'id','title']]
posts = posts[['Index', 'author', 'id', 'title', 'url']]  # delete
bios = bios[['comment', 'id']]

# merge both dataframes
merged = pd.merge(posts, bios, left_on='id', right_on='id', how='left')

# Replace blank bios with indicator
merged['comment'] = merged['comment'].fillna("No Bio")

# Rename and reorder columns
# merged = merged.rename(columns={"title": "Title", 'author': 'Username', 'comment': 'Bio', 'Index': 'Post #', 'id': 'Post Id'})
merged = merged.rename(columns={"title": "Title", 'author': 'Username', 'comment': 'Bio', 'Index': 'Post #', 'id': 'Post Id', 'url': 'url'})  # del
# merged = merged[['Post #', 'Post Id', 'Username', 'Title', 'Bio']]
merged = merged[['Post #', 'Post Id', 'Username', 'Title', 'Bio', 'url']]  # del


def get_entire_image_name(image_name):
    for root, dirs, files in os.walk(PATH):
        for name in files:
            if image_name in name:
                return name


ALL_PHOTOS_FOLDER = "final_photos"  # Folder where all collected photos reside
PHOTO_FOLDER_PARENT = ""  # Folder where coding sheet and folder of associated photos will reside
COPIED_PHOTOS_FOLDER = ""  # Subfolder where copied pictures will reside
OUTPUT_FILE = ""  # Name of the coding sheet
PATH = os.path.join(os.getcwd(), ALL_PHOTOS_FOLDER)
FINAL_FOLDER = os.path.join(PHOTO_FOLDER_PARENT, COPIED_PHOTOS_FOLDER)
os.mkdir(FINAL_FOLDER)

image_names = []

for idx, row in merged.iterrows():
    # Get the index of the image in df
    image_index = int(row['Post #'])

    # Create the partial image_name
    partial_image_name = "image" + str(image_index) + "."

    image_name = get_entire_image_name(partial_image_name)

    _, image_extension = os.path.splitext(image_name)

    shutil.copy(os.path.join(PATH, image_name), os.path.join(FINAL_FOLDER, image_name))
    image_names.append(image_name)

merged['Image Name'] = image_names

merged.to_csv(os.path.join(PHOTO_FOLDER_PARENT, OUTPUT_FILE), index=False, encoding='utf-8-sig')
