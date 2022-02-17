from re import sub
import config
import praw
import pandas as pd
import requests
import time

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

df = pd.read_csv("Posts_Info.csv")
image_links = df["url"]

print(len(image_links))
WAIT_TIME = 1

i = 1
for url in image_links:
    print(i)
    file_extension = url.split(".")[-1]
    try:
        with requests.get(url, stream=True) as r:
            with open("image" + str(i) + "." + file_extension, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
    except Exception as e:
        print(e)
        print(str(i) + "picture not saved")
    time.sleep(WAIT_TIME)
    i += 1
    