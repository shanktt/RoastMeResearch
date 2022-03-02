import pandas as pd
import shutil
import os


def get_entire_image_name(image_name):
    for root, dirs, files in os.walk(os.getcwd()):
        for name in files:
            if image_name in name:
                return name


PATH = os.getcwd()
df = pd.read_csv("posts_hundred_comments_only_twenty_twenty.csv")
FINAL_FOLDER = "final_photos"

for idx, row in df.iterrows():
    # Get the index of the image in df
    image_index = row['Unnamed: 0']

    # Create the partial image_name
    # Images are 1-indexed and rows in the df are 0-indexed so an offest of 1 is required
    partial_image_name = "image" + str(image_index + 1) + "."
    image_name = get_entire_image_name(partial_image_name)

    _, image_extension = os.path.splitext(image_name)

    # Copy image to the final folder while 0-indexing the images
    # This "fixes" the image names to be indexed the same as the post indexes
    shutil.copy(image_name, PATH + "\\" + FINAL_FOLDER + "\\" + "image" + str(image_index) + image_extension)
