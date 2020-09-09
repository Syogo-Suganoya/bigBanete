# coding: utf-8

import time
import common.logger

import pandas as pd
import requests
import json

log = common.logger.Logger('wikipedia  | util')
log.info('---- wikipedia | util Start ----')

def get_bllinks_wiki(word, floor):
    '''
    wikipediaの被リンクを返却する

    Parameters
    ----------
    word : String
        検索語句
    url : String
        階層

    Returns
    -------
    dataflame
        検索結果
    '''
    try:
        url = "http://ja.wikipedia.org/w/api.php"
        payload = {"format":"json", "action":"query", "list":"backlinks", "blnamespace":"0"}
        payload['bltitle'] = word
        r = requests.get(url, params=payload)

        # json整形
        json_load = r.json()
        json_load = json.dumps(json_load)
        json_load = json.loads(json_load)

        # 一部切り出し
        json_load = json_load['query']['backlinks']

        theList = []
        # 記事分をループ
        for value in json_load:

            theDict = {}
            theDict['id'] = value['pageid']
            theDict['title'] = value['title']

            theDict['blTitle'] = word

            theDict['url'] = 'https://ja.wikipedia.org/wiki/' + value['title']
            theDict['floor'] = floor
            theDict['ns'] = value['ns']

            theList.append(theDict)

        dataFrame = pd.io.json.json_normalize(theList)
        return dataFrame

    except Exception as e :
        log.error('Error occurred!')
        log.error(e)

    finally:
        time.sleep(5)
