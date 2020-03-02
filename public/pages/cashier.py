import time

from public.pages.BasePage import BasePage
from public.element.cashier_element import cashierEle


class Cashier(BasePage):

    def add_good(self,i):

        # 选择货品
        select_goods = self.findElement(cashierEle.select_goods)
        self.click(select_goods)
        if i == 0:
            # 选择分组
            select_group = self.findElement(cashierEle.select_group)
            self.click(select_group)

        # 获取货品
        get_good = self.findElement(cashierEle.get_good)
        self.click(get_good)

        # 确认选择的货品
        sure_selected = self.findElement(cashierEle.sure_selected)
        self.click(sure_selected)
        print("type")
        # 输入件数
        input_num = self.findElement(cashierEle.input_num)
        self.type(input_num,10)

    #选择支付方式
    def select_pay_methods(self, pay_methods):
        if pay_methods == 0:  # 现金支付
            # 点击结算完成
            paying = self.findElement(cashierEle.paying)
            self.click(paying)
            finish_pay = self.findElement(cashierEle.finish_pay)
            self.click(finish_pay)
        elif pay_methods == 1:  # 银行卡支付
            # 点击结算完成
            paying = self.findElement(cashierEle.paying)
            self.click(paying)
            bank_card = self.findElement(cashierEle.bank_card)
            bank_card.click()
            pay_by_bank= self.findElement(cashierEle.pay_by_bank)
            pay_by_bank.click()
        elif pay_methods == 2:  # 支付宝支付
            paying = self.findElement(cashierEle.paying)
            self.click(paying)
            alipay_pay = self.findElement(cashierEle.alipay_pay)
            finish_alipay_pay = self.findElement(cashierEle.finish_alipay_pay)
            alipay_pay.click()
            finish_alipay_pay.click()


        elif pay_methods == 3:  # 微信支付
            paying = self.findElement(cashierEle.paying)
            self.click(paying)
            wechat_pay = self.findElement(cashierEle.wechat_pay)
            finish_wechat_pay = self.findElement(cashierEle.finish_wechat_pay)
            wechat_pay.click()
            finish_wechat_pay.click()


        elif pay_methods == 4:  # 支票支付
            paying = self.findElement(cashierEle.paying)
            self.click(paying)
            others_pay = self.findElement(cashierEle.others_pay)
            checks_pay = self.findElement(cashierEle.checks_pay)
            finish_checks_pay = self.findElement(cashierEle.finish_checks_pay)
            others_pay.click()
            checks_pay.click()
            finish_checks_pay.click()

        elif pay_methods == 5:  #组合支付：现金+刷卡
            combined_pay = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[3]/span/a[2]")
            input_cash_pay = self.driver.find_element_by_css_selector(".combine_money_input1")
            finish_combined_pay = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[6]/div[4]/a")
            combined_pay.click()

            input_cash_pay.send_keys(100)
            finish_combined_pay.click()

        elif pay_methods == 6:  #组合支付：微信+支付宝
            combined_pay = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[3]/span/a[2]")
            cash_pay = self.driver.find_element_by_xpath("./html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[6]/div[1]/ul/li[1]/p")
            card_pay = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[6]/div[1]/ul/li[2]/p")
            wechat_pay = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[6]/div[1]/ul/li[4]/p")
            alipay_pay = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[6]/div[1]/ul/li[5]/p")
            input_wechat_pay = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[6]/div[2]/div[1]/div/input")
            finish_combined_pay = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[6]/div[4]/a")
            combined_pay.click()
            cash_pay.click()
            card_pay.click()
            wechat_pay.click()
            alipay_pay.click()
            input_wechat_pay.send_keys(100)
            finish_combined_pay.click()