#!/bin/python3
# _*_ coding:utf-8 _*_

# COMMON SETTING
## 自サイトのSITEMAP(POSTTYPE)のURLを指定
tgtSmUrl = 'http://XXXXXXXX/sitemap-posttype-post.YYYY.xml'
## RANDOM WAIT SWITCH.
## ONの時、プログラム開始から0-60分の何れかでTWEETする。
rndSpSwt = 'ON'
## PRIORITY LIMIT SWITCH.
## ONの時、指定したプライオリティ値（prLL）以上のエントリーをTWEETする
## 0かOFFにした場合SITEMAP上の全てのエントリーが対象になる。
prSwt = 'ON'
prLL = 0.5
## FIXED TAG SWITCH.
## ONの時指定した固定タグ（fTag）を入れてTWEETする。
fTagSwt = 'ON'
fTag = 'XXXXXXXX'

# TWITTER SETTING
## TwitterDeveloper側のAppの設定はOAuth2.0と1.0両方ONにし
## OAuth1.0側の設定をRead and writeとすること。

## bearer token
t_BToken = 'XXXXX'
## api key
t_CKey = 'XXXXX'
## api key secret
t_CS = 'XXXXX'
## access token
t_AToken = 'XXXXX'
## access token secret
t_ATokenS = 'XXXXX'