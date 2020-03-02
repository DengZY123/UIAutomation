import time
import unittest
from public.pages.cashier import Cashier



class Test_cashier(unittest.TestCase):
    url_value = "https://shimo.im/folder/JDxpjty3GGG8yVtw"

    def setUp(self):
        pass

    def test_addGoods(self):
        try:
            self.base_url = self.url_value

            self.cashier = Cashier()
            cashier = self.cashier
            cashier.open(self.base_url)
            for i in range(0,5):
                if i != 0:
                    time.sleep(3)
                cashier.add_good(i)
                time.sleep(3)
                cashier.select_pay_methods(i)
                time.sleep(3)
        except Exception as err:
            print(err)

    def tearDown(self):
        self.cashier.quit()


if __name__ == "__main__":
    unittest.main()

