# coding: utf-8

import time
import common.logger
import datetime
import util.wikipediaMethod
import pandas as pd

log = common.logger.Logger('ビッグバネイト説検証')
log.info('---- ビッグバネイト説検証 Start ----')

now = datetime.datetime.now()
todayStr = now.strftime("%Y%m%d")

try:

    floor = 9

    path = '/Users/syogosuganoya/Documents/趣味/開発/2009_ビッグバネイト説検証/ws/downloads/record.csv'
    df = pd.read_csv(path, encoding="cp932")
    df = df.query('floor == @floor')
    df.drop_duplicates(subset='id', inplace=True)

    df_concat = pd.DataFrame(index=[], columns=[])

    for row in df.itertuples():

        word = row.title
        nextFloor = floor + 1
        addDf = util.wikipediaMethod.get_bllinks_wiki(word, nextFloor)

        df_concat = pd.concat([df_concat, addDf])

    path = '/Users/syogosuganoya/Documents/趣味/開発/2009_ビッグバネイト説検証/ws/downloads/add.csv'
    df_concat.sort_values(['id'], inplace=True)
    # エンコーディングエラー回避
    with open(path, mode="w+", encoding="cp932", errors="ignore")as f:
        df.to_csv(f)

    # 出力結果を結合
    path = '/Users/syogosuganoya/Documents/趣味/開発/2009_ビッグバネイト説検証/ws/downloads/record.csv'
    df1 = pd.read_csv(path, encoding="cp932")

    path = '/Users/syogosuganoya/Documents/趣味/開発/2009_ビッグバネイト説検証/ws/downloads/add.csv'
    df2 = pd.read_csv(path, encoding="cp932")

    df_concat = pd.concat([df1, df2])
    path = '/Users/syogosuganoya/Documents/趣味/開発/2009_ビッグバネイト説検証/ws/downloads/record.csv'
    df_concat.to_csv(path, encoding='cp932', index=False)

    # 重複削除結果の出力
    path = '/Users/syogosuganoya/Documents/趣味/開発/2009_ビッグバネイト説検証/ws/downloads/uniqueRecord.csv'
    df_concat.drop_duplicates(subset='id', inplace=True)
    df_concat.to_csv(path, encoding='cp932', index=False)

except Exception as e :
    log.error('Error occurred!')
    log.error(e)

finally:
    time.sleep(5)
