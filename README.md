# RoastMe Scripts

## Files

 - `post_collector.py`
	 - Script to collect posts from the Pushshift API
 - `photo_collector.py`
	 - Script to collect photos from posts collected from the Pushshift API
 - `generate_final_datasets.py`
	 - Script to filter posts data by daterange, delete photos, and multiple posts from the same user
 -  `copy_final_photos.py`
	 - Script to move photos associated with posts filtered from `generate_final_datasets.py` into a new folder
 - `separate_posts.py`
	 - Script to generate a new dataset of posts within a specified daterange 
- `r_comment_collector.R`
	 - Script to collect comments of reddit posts 
- `reddit_extractor_comment_cleaner.py`
	 - Script to fix corrupted apostrophes when collecting comments from RedditExtractor
- `codebook_creator.py`
	 - Script to create codebooks for human coding of reddit postse
- `image_link_inserter.py`
	 - Script to add links in the codebook pointing to the images associated with each post 
- `condense_comments.py`
	 - Script to condense the comments collected from RedditExtractor so that only top-level comments remain
- `merge_codings_and_comments.py`
	 - Script to join codings and comments datasets
