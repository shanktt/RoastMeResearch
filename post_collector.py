from pmaw import PushshiftAPI
import datetime as dt
import pandas as pd
import numpy as np

start_year = 2019
start_month = 1
start_day = 1

end_year = 2021
end_month = 12
end_day = 31

OUTPUT_FILE = "Posts_Info.csv"

start_epoch = int(dt.datetime(start_year, start_month, start_day).timestamp())
end_epoch = int(dt.datetime(end_year, end_month, end_day).timestamp())

api = PushshiftAPI()

# Get posts info
gen = api.search_submissions(subreddit="roastme", after=start_epoch, before=end_epoch)
post_list = [p for p in gen]
df = pd.DataFrame(post_list)
df.to_csv(OUTPUT_FILE)
print(len(post_list))

# # Get comment ids
# post_ids = list(df.loc[:, 'id'])
# comment_ids = api.search_submission_comment_ids(ids=post_ids)
# comment_id_list = [c_id for c_id in comment_ids]
# df2 = pd.DataFrame(comment_id_list)
# df2.to_csv("Comment_Ids.csv")
# print(len(comment_id_list))
