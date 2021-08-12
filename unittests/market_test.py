from market_env import market

from datetime import date
import unittest


class MarketTests(unittest.TestCase):
  def setUp(self):
    self.env = market.Market()

  def test_get_company_info(self):
    self.assertEqual(self.env.get_company('005930').code, '005930')
    self.assertEqual(self.env.get_company('005930').name, '삼성전자')
    self.assertEqual(self.env.get_company('삼성전자').code, '005930')
    self.assertEqual(self.env.get_company('삼성전자').name, '삼성전자')
    self.assertEqual(str(self.env.get_company('005930')), '삼성전자(005930)')

  def test_get_daily_price(self):
    comp = self.env.get_company('005930')

    data_for_20_days = self.env.get_daily_price(comp, '2021-03-05', 20)
    self.assertEqual(len(data_for_20_days), 20)
    self.assertEqual(data_for_20_days['date'].values[-1], date(2021, 3, 5))

if __name__ == '__main__':
  unittest.main()
