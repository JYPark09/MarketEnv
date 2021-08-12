from market_env.market import Market, Company

from datetime import datetime
import talib
import pandas as pd
import numpy as np
from typing import Union, List


class SimpleMovingAverage:
  def __init__(self, period: Union[int, List[int]]):
    self.period = period if isinstance(period, list) else [period]

  def __call__(self, market: Market, comp: Company, date: Union[datetime, str], days: int) -> pd.DataFrame:
    max_period = max(self.period)

    df = market.get_daily_price(comp, date, days + max_period - 1)
    closes = df['close'].to_numpy().astype(np.float64)

    results = {}

    for period in self.period:
      sma = talib.SMA(closes, timeperiod=period)[-days:]
      results[f'sma_{period}'] = sma

    return pd.DataFrame(results)


class BollingerBand:
  def __call__(self, market: Market, comp: Company, date: Union[datetime, str], days: int) -> pd.DataFrame:
    period = 20

    df = market.get_daily_price(comp, date, days + period - 1)
    closes = df['close'].to_numpy().astype(np.float64)

    upper, middle, lower = talib.BBANDS(closes, timeperiod=period, nbdevup=2, nbdevdn=2)

    results = {}
    results['bb_middle'] = middle
    results['bb_upper'] = upper
    results['bb_lower'] = lower

    results = { k: v[-days:] for k, v in results.items() }

    return pd.DataFrame(results)
