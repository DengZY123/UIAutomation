import time

from public.pages.BasePage import BasePage
from public.element.cashier_element import cashierEle


class Shimo(BasePage):
    def open_file(self,i,j):

        test_file = "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/section[2]/div/div[2]/div[1]/div/div/div["+str(j)+"]/li["+str(i)+"]/div/a/div[1]/div"
        open_test_file = self.findElement(test_file)
        self.click(open_test_file)



    def export_file(self):
        menu_xpath = "/html/body/div[1]/div/div[1]/div[1]/div[1]/div[3]/button[3]"
        menu = self.findElement(menu_xpath)
        self.move_and_clcik(menu)


    def return_back(self):
        return_xpath = "/html/body/div[1]/div/div[1]/div[1]/div[1]/div[1]/button[1]"
        return_btn = self.findElement(return_xpath)
        self.click(return_btn)








"""

        export_xpath = "/html/body/div[10]/div/div/div/ul/li[7]/div"
        export = self.findElement(export_xpath)
        self.move(export)
        print(3)
        time.sleep(0.5)
        
        export_word_xpath = "/html/body/div[13]/div/div/div/ul/li[7]/ul/li[3]"
        export_word_css = "#FILE_MENU_EXPORT_DOC\$Menu > li:nth-child(2) > div:nth-child(1)"
        export_word = self.findElement(export_word_css,"css")
        self.click(export_word)
        print(4)
        
         pf_file = "/ html / body / div[1] / div / div[2] / div[2] / div / div[1] / div / section[2] / div / div[2] / div[1] / div / div / div[2] / li[1] / div / a / div[1] / div"
        open_pf_file = self.findElement(pf_file)
        self.click(open_pf_file)
        time.sleep(2)

        reback_file = "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/section[2]/div/div[2]/div[1]/div/div/div/li[2]/div/a/div[1]/div"
        open_reback_file = self.findElement(reback_file)
        self.click(open_reback_file)

        time.sleep(2)
        file = "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/section[2]/div/div[2]/div[1]/div/div/div[1]/li[1]/div/a/div[1]/div"
        open_file = self.findElement(file)
        self.click(open_file)
"""


