from lib2to3 import pytree
import pandas as pd
import pytz
import sys


# Read in dataframes
posts = pd.read_csv("final_posts.csv")
bios = pd.read_csv("all_bios.csv")

# only keep relevant columns from each df
posts = posts[['Index', 'title', 'id', 'created_utc', 'author']]
bios = bios[['body', 'link_id']]

# Remove any posts missing values
posts = posts.dropna()

# convery epoch time to utc
posts['created_utc'] = pd.to_datetime(posts['created_utc'], unit='s').dt.tz_localize('utc')

# rename column to keep consistent naming
posts = posts.rename(columns={"Index": "index"})

# remove rows that are not actually bios
mask = bios['body'].str.contains("The OP has not provided a Bio for their post.") == False
bios = bios[mask]

# rename column for joining
posts = posts.rename(columns={"id": "link_id"})

# add suffix to columns
posts.columns = [col_name + "_posts" for col_name in posts.columns]
bios.columns = [col_name + "_bios" for col_name in bios.columns]

# remove t3_ suffix from bios for joining
bios['link_id_bios'] = bios['link_id_bios'].str.replace('t3_', '')

# merge both dataframes
merged = pd.merge(posts, bios, left_on='link_id_posts', right_on='link_id_bios',
                  how='left', suffixes=('_posts', '_bios'))

# remove uneeded columns
merged = merged.drop(["link_id_posts", "link_id_bios"], axis=1)

# rename column for readability
merged = merged.rename(columns={"index_posts": "post_index", "title_posts": "post_title", "body_bios": "bios", "created_utc_posts": "created_utc", "author_posts": "post_author"})

# reorder columns
merged = merged[['post_index', 'post_author', 'post_title', 'created_utc', 'bios']]

# Add none to posts without bios
merged['bios'] = merged['bios'].fillna("No bio")

# sort rows by data
merged = merged.sort_values(by="created_utc")

# Write to csv
merged.to_csv("coding_sheet_builder.csv", index=False)
