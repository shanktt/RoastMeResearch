import requests
import pandas as pd
import time

START_IDX = 626
REGEX_PATTERN = r'\/comments\/([A-Za-z0-9 _]+)\/'
SLEEP = 5


def get_pushshift_data(link_id):
    request = f'''https://api.pushshift.io/reddit/comment/search/?link_id={link_id}&limit=20000'''

    r = requests.get(request)

    while r.status_code != 200:
        time.sleep(SLEEP + SLEEP)
        r = requests.get(request)

    json = r.json()
    return pd.DataFrame.from_dict(json['data'])


# load in posts
posts = pd.read_excel("RoastMe_Posts.xlsx")

# TODO Remove:
posts = posts[START_IDX:]

posts['link_id'] = posts['URL'].str.extract(REGEX_PATTERN)

link_ids = posts['link_id']

comments = pd.DataFrame()

for idx, id in enumerate(link_ids):
    print(idx)
    comments = comments.append(get_pushshift_data(id))
    time.sleep(SLEEP)

comments.to_csv("comments.csv", index=False)
