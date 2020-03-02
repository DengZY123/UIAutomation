import time
import unittest
from public.pages.shimo import Shimo



class Test_shimo(unittest.TestCase):
    url_value = "https://shimo.im/folder/ECLnGMwiXJAp6iFW"

    def setUp(self):
        pass


    def test_shimo(self):
        try:
            self.base_url = self.url_value
            shimo = Shimo()
            self.shimo = shimo

            shimo.open(self.base_url)
            for j in range(5,6):
                for i in range(1,7):
                    shimo.open_file(i,j)
                    time.sleep(5)
                    shimo.export_fiel()
                    time.sleep(5)
                    shimo.return_back()
                    time.sleep(3)
                    print("("+str(i)+","+str(j)+")")


        except Exception as err:
            print(err)




    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

