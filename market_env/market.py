from market_env.utils import sql_connect

import pandas as pd

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


  def get_company_code(self, code):
    code_keys = list(self.codes.keys())
    code_names = list(self.codes.values())

    if code in code_keys:
      return code
    if code in code_names:
      return code_keys[code_names.index(code)]

    raise ValueError(f"invalid code '{code}'")

  def get_company_name(self, code):
    code = self.get_company_code(code)
    return self.codes[code]
