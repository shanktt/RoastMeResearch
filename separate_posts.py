import pandas as pd
import time

START_DATE = '2020-01-01'  # Inclusive
END_DATE = '2020-2-01'  # Exclusive
INPUT_FILE = "final_posts.csv"
OUTPUT_FILE = ".csv"  # Name the output file

# load in posts
posts = pd.read_csv(INPUT_FILE)
mask1 = posts['timestamp'] >= START_DATE
mask2 = posts['timestamp'] < END_DATE
mask = mask1 & mask2
posts = posts[mask]

posts.to_csv(OUTPUT_FILE, index=False)
