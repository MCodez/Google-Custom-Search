# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 00:10:47 2017

@author: LALIT ARORA
"""

from googleapiclient.discovery import build
import pprint

my_api_key = "Google Developer API Key"
my_cse_id = "your search engine id"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key,cache_discovery=False)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def googlesearch(searchitem):
    
    results = google_search(searchitem, my_api_key, my_cse_id, num=10)
    for i in range(len(results)):
        pprint.pprint(results[i]["link"])

if __name__ == "__main__":
    take=input().strip()
    googlesearch(take)


