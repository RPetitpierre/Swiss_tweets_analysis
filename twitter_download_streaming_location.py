'''
Created on Mar 16, 2019

@author: tphan@idiap.ch
'''
from __future__ import unicode_literals
from twitter import Api
import time
import os, sys
import json
          

consumer_key='c8LX5nBbfAbs30J9EIGAfMgjx'
consumer_secret='Exzp2n46dQP5gN29plm2rAYjeal5i182shTCwgnLpFgcFK9v4N'
resource_owner_key='2380467042-03tndCSr9CJh8B9DLkpx568qrMolfRQoAOqCJlP'
resource_owner_secret='kkf5aSXFyOIY55DWATMJ4wwySaco01RIbAREfpzkzagRA'

api = Api(consumer_key=consumer_key,
				   consumer_secret=consumer_secret,
				   access_token_key=resource_owner_key,
				   access_token_secret=resource_owner_secret)


if __name__ == '__main__':
	while True:
		try:
			print('=== Scrapper Launched ===')
			# Bounding Box for Switzerland
			Switzerland_LOCATIONS = ["5.9559113","45.817994999999996","10.4922941","47.8084648"]
			for tweet in api.GetStreamFilter(locations=Switzerland_LOCATIONS, stall_warnings=True):
				if tweet:
					if tweet.get('created_at', None) != None:
						with open('data.json', 'a') as outfile:
							json.dump(tweet, outfile)
							outfile.write('\n')
							time.sleep(6)	

		except Exception as e:
			print('error (Switzerland): '+str(e))
			time.sleep(300)
