import pandas as pd

sept_oct_comments = pd.read_csv('Sept_and_Oct_2019_Comments_Condensed.csv')
nov_dev_comments = pd.read_csv('Nov_and_Dec_2019_Comments_Condensed.csv')
jan_comments = pd.read_csv('Jan_2020_Comments_Condensed.csv')
feb_and_march_comments = pd.read_csv('Feb and March 2020 Comments_Condensed.csv')
april_jun_comments = pd.read_csv('April_to_June_2020_Comments_Condensed.csv')
july_aug_comments = pd.read_csv('July_and_August_2020_Comments_Condensed.csv')

codings = pd.read_excel('All_CombinedRemoved.xlsx')

all_comments = pd.concat([sept_oct_comments, nov_dev_comments, jan_comments, feb_and_march_comments, april_jun_comments, july_aug_comments], ignore_index=True)

all_comments.columns = [col_name + "_comments" for col_name in all_comments.columns]
codings.columns = [col_name + "_codings" for col_name in codings.columns]

merged = pd.merge(all_comments, codings, left_on='link_id_comments', right_on='Post_ID_codings',
                  how='inner', suffixes=('_comments', '_codings'))

merged.to_csv("merged.csv", index=False, encoding='utf-8-sig')
