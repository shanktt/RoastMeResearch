from stat import filemode
import pandas as pd
import sys

BADLY_ENCODED_STRINGS = "\x19"
filename = sys.argv[1]
comments = pd.read_csv(filename)
output_file = ""

comments['comment'] = comments['comment'].str.replace(BADLY_ENCODED_STRINGS, '\'')

new_col = []
curr_idx = 0
for index, row in comments.iterrows():
    comment_id = row['comment_id']

    if '_' in comment_id:
        new_col.append(0)
        new_col[curr_idx] += 1
    else:
        curr_idx = index
        new_col.append(0)

comments['number_of_child_comments'] = new_col

mask = ~(comments['comment_id'].str.contains('_'))
comments = comments[mask]

comments['link_id'] = comments['url'].str.extract(r'\/comments\/([A-Za-z0-9 _]+)\/')

comments.to_csv(output_file, index=False, encoding='utf-8-sig')
