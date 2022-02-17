from numpy import column_stack
import pandas as pd

bios = pd.read_csv("bios.csv")
posts = pd.read_csv("posts_hundred_comments_only_twenty_twenty.csv")

# only keep relevant columns from each df
posts = posts[['Unnamed: 0', 'author', 'full_link', 'id', 'permalink', 'updated_utc', 'url']]
bios = bios[['body', 'link_id']]

# add suffix to columns
posts.columns = [col_name + "_posts" for col_name in posts.columns]
bios.columns = [col_name + "_bios" for col_name in bios.columns]

# rename column for joining
posts = posts.rename(columns={"id_posts": "link_id_posts"})

# remove t3_ suffix from bios
bios['link_id_bios'] = bios['link_id_bios'].str.replace('t3_', '')

# merge both dataframes
merged = pd.merge(posts, bios, left_on='link_id_posts', right_on='link_id_bios',
                  how='outer', suffixes=('_posts', '_bios'))

# Remove rows that are not actually bios
mask = merged['body_bios'].str.contains("The OP has not provided a Bio for their post.") == False
merged = merged[mask]

# Write to csv
merged.to_csv("bios_combined_with_posts_final.csv")
