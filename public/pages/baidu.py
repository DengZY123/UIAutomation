from public.pages.BasePage import BasePage
from time import sleep
from public.element.baidu_ele import baiduEle
class Search(BasePage):

    def seratch_value(self,SearchValue):
        searchValue = self.findElement(baiduEle.SearchId)
        self.type(searchValue,SearchValue)

        sleep(1)
        searchBtn = self.findElement(baiduEle.SearchBtn)
        self.click(searchBtn)

        self.quit()


