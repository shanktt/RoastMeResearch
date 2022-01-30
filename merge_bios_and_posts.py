import pandas as pd

bios = pd.read_csv("bios.csv")
posts = pd.read_csv("Posts_Info.csv")

# rename column in posts so merge is easy
posts = posts.rename(columns={"id": "link_id"})

# left merge on bios
merged = pd.merge(bios, posts, how="left", on="link_id")

# mask to remove comments that don't actually contain the bio
mask = merged['body'].str.contains("The OP has not provided a Bio for their post.") == False
merged = merged[mask]

merged.to_csv("combined.csv")
