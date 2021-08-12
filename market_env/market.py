from market_env.utils import sql_connect

from datetime import datetime
import pandas as pd
from typing import Union


class Company:
  def __init__(self, code, name):
    self.code = code
    self.name = name

  def __str__(self):
    return f'{self.name}({self.code})'


class Market:
  def __init__(self):
    self.conn = sql_connect()

    self.codes = dict()
    self._get_company_list()

  def __del__(self):
    if hasattr(self, 'conn') and self.conn is not None:
      self.conn.close()

  def _get_company_list(self):
    sql = "SELECT * FROM company_info"
    krx = pd.read_sql(sql, self.conn)

    codes = krx['code'].tolist()
    names = krx['company'].tolist()

    for code, name in zip(codes, names):
      self.codes[code] = name

  def get_company(self, code_or_name):
    code_keys = list(self.codes.keys())
    code_names = list(self.codes.values())

    if code_or_name in code_keys:
      return Company(code_or_name, self.codes[code_or_name])
    if code_or_name in code_names:
      return Company(code_keys[code_names.index(code_or_name)], code_or_name)

    raise ValueError(f"invalid company '{code_or_name}'")

  def get_company_list(self):
    return [Company(code, self.codes[code]) for code in self.codes]


  def get_daily_price(self, comp: Company, end_date: Union[datetime, str], days: int = 1) -> pd.DataFrame:
    if isinstance(end_date, datetime):
      end_date = end_date.strftime('%Y-%m-%d')

    sql = f"SELECT * FROM (SELECT * FROM daily_price WHERE code = '{comp.code}' AND date <= '{end_date}' ORDER BY date DESC LIMIT {days}) sub ORDER BY date ASC"
    return pd.read_sql(sql, self.conn)
