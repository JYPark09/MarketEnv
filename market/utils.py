import json
import pymysql


def load_config(path: str) -> dict:
  with open(path) as f:
    return json.load(f)


def sql_connect() -> pymysql.Connection:
  config = load_config('config.json')

  return pymysql.connect(host=config['sql']['host'], user=config['sql']['user'], password=config['sql']['password'], db='Invester', charset='utf8')
