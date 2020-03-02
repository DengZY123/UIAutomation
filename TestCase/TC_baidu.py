import unittest

from time import sleep
from public.pages import baidu

class Test_Baidu_Search(unittest.TestCase):

    url_value = "https://www.baidu.com"

    def setUp(self):
        pass

    def test_searchBaidu(self):
        try:
            self.base_url = self.url_value

            self.baiduSearch = baidu.Search()
            self.baiduSearch.open(self.base_url)
            sleep(3)

            self.baiduSearch.seratch_value("123")
            sleep(3)
        except Exception as err:
            print("this is error")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
