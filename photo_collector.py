from re import sub
import config
import praw
import pandas as pd
import requests

config = {
    "username": config.USERNAME,
    "client_id": config.CLIENT_ID,
    "client_secret": config.CLIENT_SECRET,
    "password": config.PASSWORD,
    "user_agent": config.USERAGENT
}

reddit = praw.Reddit(client_id=config['client_id'],
                     client_secret=config['client_secret'],
                     user_agent=config['user_agent'],
                     passwword=config['password'],
                     username=config['username'])

# csv of posts goes here
df = pd.read_csv("Posts_Info.csv")

urls = df["url"]

image_links = []

for url in urls:
    submission = reddit.submission(url=url)
    image_links.append(submission.url)

print(image_links)

df['Image_Links'] = image_links

i = 1
for url in image_links:
    file_extension = url.split(".")[-1]
    try:
        with requests.get(url, stream=True) as r:
            with open("iamge_" + str(i) + "." + file_extension, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
    except Exception as e:
        print(e)
    i += 1

print("Completed downloading images")
df.to_csv("/Users/ashanktomar/Documents/comm_research/RoastMe/RoastMeAppended_Posts.csv")
