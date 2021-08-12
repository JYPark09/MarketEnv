from market_env import market

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


if __name__ == '__main__':
  unittest.main()
