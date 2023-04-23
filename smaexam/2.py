# pip install facebook-scraper
# pip install pandas
from facebook_scraper import get_posts
import pandas as pd

fbPosts = [{x: post[x] for x in ['post_id', 'text', 'comments', 'likes']} for post in get_posts('myntra', pages=10)]
df = pd.DataFrame(fbPosts)
print(f"Latest Facebook posts:\n {df}")
df.to_csv("fb.csv", index=False)