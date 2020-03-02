class cashierEle():

#添加货品
    select_goods = "/html/body/div[1]/div[1]/div[5]/div[3]/div/div[2]/div/div[1]/div[1]/a"
#选择分组
    select_group = "/html/body/div[2]/div/div[2]/div[2]/div[1]/ul/li[1]/div[1]/span[2]"
#选中货品
    get_good ="/html/body/div[2]/div/div[2]/div[2]/div[1]/ul/li[1]/div[2]/ul/li[8]/div[1]/div/span[2]"
# 确认选择的货品
    sure_selected ="/html/body/div[2]/div/div[3]/a[1]"
# 输入件数
    input_num ="/html/body/div[1]/div[1]/div[5]/div[3]/div/div[1]/div[2]/div[2]/table/tbody/tr/td[5]/input"


#点击结算完成
    paying = "/html/body/div[1]/div[1]/div[5]/div[3]/div/div[2]/div/div[2]/a/span"
#结算完成
    finish_pay ="/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[5]/table/tbody/tr[2]/td[7]"
#选择银行卡支付
    bank_card = "/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[4]/div[1]/ul/li[2]/img"
#银行卡结算
    pay_by_bank = "/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[4]/div[3]/div/a"
#选择支付宝支付
    alipay_pay = "/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[4]/div[1]/ul/li[3]/img"
#支付宝结算
    finish_alipay_pay = "/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[4]/div[6]/div/a"
#选择微信支付
    wechat_pay = "/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[4]/div[1]/ul/li[4]/img"
#微信结算
    finish_wechat_pay = "/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[4]/div[5]/div/a"
#选择其他支付
    others_pay = "/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[4]/div[1]/ul/li[6]/img"
#选择支票支付
    checks_pay = "/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[4]/div[8]/ul/li"
#支票结算
    finish_checks_pay = "/html/body/div[1]/div[1]/div[5]/div[3]/div/div[3]/div/div[4]/div[8]/div[2]/a"

