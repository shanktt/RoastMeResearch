from pmaw import PushshiftAPI
import datetime as dt
import pandas as pd
import numpy as np
start_epoch = int(dt.datetime(2019, 1, 1).timestamp())
end_epoch = int(dt.datetime(2021, 10, 25).timestamp())

api = PushshiftAPI(num_workers=20)

df_comments = pd.read_csv("Comment_Ids_Two.csv")
comment_id_list = df_comments["0"]

num_comments = len(comment_id_list)
print(f'{num_comments} comments to store in CSV')
chunksize = 1000000
out_csv = 'comment_info.csv'
total_stored = 0
for i in range(0, num_comments, chunksize):
    start_idx = i
    end_idx = i + chunksize
    c_arr = comment_id_list[start_idx: end_idx]
    store = len(c_arr)
    print(f'Processing {store} comments')
    comment_arr = api.search_comments(ids=c_arr)
    comment_list = [c for c in comment_arr]
    df = pd.DataFrame(comment_list)
    writing = len(comment_list)
    if i == 0:
        print(f'Writing {writing} comments to df')
        df.to_csv(out_csv, index=False, header=True, chunksize=chunksize)
    else:
        print(f'Writing {writing} comments to df')
        df.to_csv(out_csv, index=False, header=False, mode='a', chunksize=chunksize)
