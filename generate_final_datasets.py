# This script was used to generate the final posts datasets used in the RoastMe Research Project

import hashlib
import pandas as pd
from PIL import Image
import os
from PIL import UnidentifiedImageError

IMAGE_DELETED_HASH = '45172ac97d574bfd34a1005262a23169'


def get_entire_image_name(image_name):
    for root, dirs, files in os.walk(os.getcwd()):
        for name in files:
            if image_name in name:
                return name


def remove_deleted_images(df):
    mask = []

    for idx, row in df.iterrows():
        image_name = "image" + str(idx + 1) + "."
        image_name = get_entire_image_name(image_name)
        if image_name is not None:
            valid_extensions = [".jpg", ".jpeg", ".png"]
            has_valid_extension = list(filter(image_name.endswith, valid_extensions)) != []
            if has_valid_extension:
                try:
                    with Image.open(image_name) as img:
                        md5hash = hashlib.md5(img.tobytes())
                        mask.append(int(md5hash.hexdigest() == IMAGE_DELETED_HASH))
                except UnidentifiedImageError:
                    mask.append(1)
            else:
                mask.append(1)
        else:
            mask.append(1)

    df.loc[:, "image_deleted"] = mask
    return df


# Read in posts
posts = pd.read_csv("Posts_Info.csv")

# Remove deleted images
posts = remove_deleted_images(posts)
mask = posts["image_deleted"] == 0
posts = posts[mask]

print(posts.shape)

# Created mask to remove locked posts
mask = posts["locked"] == False
posts = posts[mask]

# Remove duplicate posters while keeping their first post
posts = posts.drop_duplicates(subset="author_fullname", keep="first")

# create masks to only keep posts with over a 100 comments and posts over 10 comments
mask_hundred_comments = posts['num_comments'] >= 100
mask_ten_comments = posts['num_comments'] >= 10

posts_hundred_comments = posts[mask_hundred_comments]
posts_ten_comments = posts[mask_ten_comments]

# create mask to remove posts from 2021
unix_epoch_date = 1609419599  # Unix Epoch time for Thursday, December 31, 2020 12:59:59 PM
date_mask_hundred = posts_hundred_comments['created_utc'] <= unix_epoch_date
date_mask_ten = posts_ten_comments['created_utc'] <= unix_epoch_date

posts_hundred_comments_only_twenty_twenty = posts_hundred_comments[date_mask_hundred]
posts_ten_comments_only_twenty_twenty = posts_ten_comments[date_mask_ten]

posts_hundred_comments.to_csv("posts_hundred_comments.csv")
posts_ten_comments.to_csv("posts_ten_comments.csv")
posts_hundred_comments_only_twenty_twenty.to_csv("posts_hundred_comments_only_twenty_twenty.csv")
posts_ten_comments_only_twenty_twenty.to_csv("posts_ten_comments_only_twenty_twenty.csv")
