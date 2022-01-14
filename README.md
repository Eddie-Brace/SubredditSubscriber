# SubredditSubscriber
A Chrome bot that automates subscribing a Reddit user to a list of subreddits   
Useful for migrating to a new Reddit account.   
Tested on Python 3.8 with Chrome instance running.

Create text file w/ list of subs to subscribe to:
```
r/nuclear
r/redscarepod
r/geopolitics
r/dogelore
```
Sub names should be seperated only by whitespace and "r/" as shown above. This can be done easily by copying the subreddit list (top-left of page) from your old account, chopping off the ends, and using find-all to replace "Subreddit Icon" with a blank string.

Run as:
```bash
pip install selenium
pip install chromedriver-binary==your-chrome-version-or-closest-preceding
python3 SubredditSubscriber.py
```
