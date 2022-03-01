import hashlib
import pandas as pd
import requests

IMAGE_DELETED_HASH = "f17b01901c752c1bb04928131d1661af"


def remove_deleted_images(df):
    mask = []

    for _, row in df.iterrows():
        response = requests.get(row["url"])
        hash = res = hashlib.md5(response.content)
        mask.append(int(hash == IMAGE_DELETED_HASH))

    return df[mask]

    # Read in posts
posts = pd.read_csv("Posts_Info.csv")

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

print(posts_hundred_comments.shape)
print(posts_ten_comments.shape)

# create mask to remove posts from 2021
unix_epoch_date = 1609419599  # Unix Epoch time for Thursday, December 31, 2020 12:59:59 PM GMT
date_mask_hundred = posts_hundred_comments['created_utc'] <= unix_epoch_date
date_mask_ten = posts_ten_comments['created_utc'] <= unix_epoch_date

posts_hundred_comments_only_twenty_twenty = posts_hundred_comments[date_mask_hundred]
posts_ten_comments_only_twenty_twenty = posts_ten_comments[date_mask_ten]

print(posts_hundred_comments_only_twenty_twenty.shape)
print(posts_ten_comments_only_twenty_twenty.shape)

# image_mask = build_deleted_images_mask(posts_hundred_comments)
# print(posts_hundred_comments.shape)


posts_hundred_comments_removed_img_deleted = remove_deleted_images(posts_hundred_comments)
posts_ten_comments_removed_img_deleted = remove_deleted_images(posts_ten_comments)
posts_hundred_comments_only_twenty_twenty_removed_img_deleted = remove_deleted_images(posts_hundred_comments_only_twenty_twenty)
posts_ten_comments_only_twenty_twenty_removed_img_deleted = remove_deleted_images(posts_ten_comments_only_twenty_twenty)

posts_hundred_comments_removed_img_deleted.to_csv("posts_hundred_comments_removed_img_deleted.csv")
posts_ten_comments_removed_img_deleted.to_csv("posts_ten_comments_removed_img_deleted.csv")
posts_hundred_comments_only_twenty_twenty_removed_img_deleted.to_csv("posts_hundred_comments_only_twenty_twenty_removed_img_deleted.csv")
posts_ten_comments_only_twenty_twenty_removed_img_deleted.to_csv("posts_ten_comments_only_twenty_twenty_removed_img_deleted.csv")
