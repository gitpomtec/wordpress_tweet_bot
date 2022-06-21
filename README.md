# wordpress_tweet_bot
## SUMMARY
Script to post to Twitter based on the sitemap (POSTTYPE) output by WordPress.
## SYSTEM REQUIREMENTS
Python 3.10.5
  beautifulsoup4==4.11.1
  lxml==4.9.0
  requests==2.28.0
  tweepy==4.10.0
## TREATMENT
1. Place the wordpress_tweet_bot folder in any folder on the computer where you want to run it.
2. Create an app on the twitter developer platform(https://developer.twitter.com/en).
3. Modify bot_config.py to match your environment.
4. Install Python libraries as needed, referring to SYSTEM REQUIREMENTS.
5. Run tweet_bot.py in crontab or task scheduler.
