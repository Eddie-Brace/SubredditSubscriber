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
Sub names seperated only by whitespace and "r/" as shown above.

Run as:
```bash
pip install selenium
python3 SubredditSubscriber.py
```
