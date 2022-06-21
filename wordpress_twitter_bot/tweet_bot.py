#!/bin/python3
# _*_ coding:utf-8 _*_
# TWEET BOT PY
# VERSION 1.0.0

# MODULE IMPORT(COMMON)
import logging.config
import requests
from bs4 import BeautifulSoup
import random
import time
import sys
import csv
# MODULE IMPORT(TWEETS)
from bot_config import *
import tweepy

# INITIALIZE : LOGGING
logging.config.fileConfig('logging.cfg')
logger = logging.getLogger()

# INITIALIZE : TWEEPY
twitterClient = tweepy.Client(bearer_token = t_BToken, 
consumer_key = t_CKey, 
consumer_secret = t_CS, 
access_token = t_AToken, 
access_token_secret = t_ATokenS)

# FUNCTION : RANDOM WAIT
def randomwait():
    logger.info('RANDOM WAIT : START PROCCESS.')
    st = random.randrange(3600)
    logger.info('RANDOM WAIT : START STANDBY {0} sec.'.format(st))
    time.sleep(st)
    logger.info('RANDOM WAIT : END STANDBY.')
    logger.info('RANDOM WAIT : END PROCCESS.')
    return 0

# FUNCTION : GET SITEMAP
def getsitemap(tgturl):
    lstUrls = []
    lstPrs = []
    lstSms = []
    logger.info('GET SITEMAP : START PROCCESS.')
    logger.info('GET SITEMAP : START GET SITEMAP DATA.')
    try:
        res = requests.get(tgturl)
    except Exception as err:
        logger.error(err)
        logger.error('GET SITEMAP : FAILURE TO OBTAIN SITEMAP.STOPING SYSTEM.')
        sys.exit()
    logger.info('GET SITEMAP : END GET SITEMAP DATA.HTTP STATUS CODE IS {0}.'.format(res.status_code))
    if res.status_code == 200:
        logger.info('GET SITEMAP : START OUT SITEMAP CSV.')
        soup = BeautifulSoup(res.content, 'html.parser')
        tmpUrls = soup.select('loc')
        tmpPrs = soup.select('priority')
        for val in tmpUrls:
            lstUrls.append(val.text)
        for val in tmpPrs:
            lstPrs.append(float(val.text))
        for val1,val2 in zip(lstUrls, lstPrs):
            lstSms.append([val1, val2])
        f = open('sitemap.csv', 'w', newline='')
        csv.writer(f).writerows(lstSms)
        f.close()
        logger.info('GET SITEMAP : END OUT SITEMAP CSV.')
    elif res.status_code != 200:
        logger.error('GET SITEMAP : INCORRECT STATUS CODE.STOPING SYSTEM.')
        sys.exit()
    logger.info('GET SITEMAP : END PROCCESS.')
    return lstSms

# FUNCTION : PRIORITY RESTRAINT
def priorityrestraint(lstSM, pl):
    logger.info('PRIORITY RESTRAINT : START PROCCESS.')
    lstNew = []
    #i = 0
    for val in lstSM:
        if val[1] >= pl:
            lstNew.append(val)
    logger.info('PRIORITY RESTRAINT : END PROCCESS.')
    return lstNew

# FUNCTION : SELECT TARGET URL
def selecttargeturl(sMD):
    rndVal = random.randrange(len(sMD))
    return sMD[rndVal][0]

# FUNCTION : GET CONTENTS DATA
def getcontentsdata(tUrl):
    logger.info('GET CONTENTS DATA : START PROCCESS.')
    lstTag = []
    try:
        res = requests.get(tUrl)
    except Exception as err:
        logger.error(err)
        logger.error('GET CONTENTS DATA : FAILURE TO OBTAIN DATA.STOPING SYSTEM.')
        sys.exit()
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        cti = soup.select('title')
        ctitle = cti[0].text
        cta = soup.find(class_="tags-links")
        cta = cta.find_all('a')
        for val in cta:
            lstTag.append(val.text)
    elif res.status_code != 200:
        logger.error('GET CONTENTS DATA : INCORRECT STATUS CODE.STOPING SYSTEM.')
        sys.exit()
    logger.info('GET CONTENTS DATA : END PROCCESS.')
    return ctitle, lstTag

# FUNCTION : CREATE MESSAGE
def createmessage(tu, cti, cta, fts, ft):
    logger.info('CREATE MESSAGE : START PROCCESS.')
    msg = cti + ' '
    if fts == 'ON':
        msg = msg + ('#' + ft + ' ')
    for val in cta:
        msg = msg + ('#' + val + ' ')
    msg = msg + tu
    logger.info('CREATE MESSAGE : END PROCCESS.')
    return msg

# FUNCTION : PUT TWEET
def puttweet(tm):
    logger.info('PUT TWEET : START PROCCESS.')
    try:
        twitterClient.create_tweet(text=tm)
    except Exception as err:
        logger.error(err)
        logger.error('PUT TWEET : TWEET TERMINATED ABNORMALLY.STOPING SYSTEM.')
        sys.exit()
    logger.info('PUT TWEET : END PROCCESS.')
    return 0

# FUNCTION : MAIN
def main():
    logger.info('MAIN : START PROCCESS.')
    ## GET DATA
    if rndSpSwt == 'ON':
        randomwait()
    siteMapDat = getsitemap(tgtSmUrl)
    if prSwt == 'ON':
        siteMapDat = priorityrestraint(siteMapDat, prLL)  
    tgtUrl = selecttargeturl(siteMapDat)
    conTitle, conTag = getcontentsdata(tgtUrl)
    ## PUT TWEET
    t_Msg = createmessage(tgtUrl, conTitle, conTag, fTagSwt, fTag)
    puttweet(t_Msg)
    logger.info('MAIN : END PROCCESS.')

if __name__ == '__main__':
    main()
