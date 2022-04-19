#1、搭框架
import requests
import unittest
class Test500(unittest.TestCase):
    #创建setUp函数初始化session
    def setUp(self):
        self.session = requests.session()
    #销毁session
    def tearDown(self):
        self.session.close()

    # 2、requests库调用各个接口
    # 3、断言判断响应
    #函数1：登录
    def test_login(self):
        url1 = "https://twecruitpa.hrtools.cn/wecruit/login/SU6142a94d22d5c64be52a4194"
        myData = {"username": "0fc9949f1eb384bfb4dccbc58e5a026235f333e18877f3ddf075d1c553db660c",
                  "password": "201bc869fb7ced4023225898ceada7c8",
                  "pictureCode": "9999",
                  "remember": "true"}
        response = self.session.post(url1,data=myData)
        print(response.json())
        self.assertEqual("200",response.json().get("state"))

    #函数1：登录---输入未注册的账号名
    def test_login_wrong_username(self):
        url1 = "https://twecruitpa.hrtools.cn/wecruit/login/SU6142a94d22d5c64be52a4194"
        myData = {"username": "5023f8bac28e6fe254e92011564fdcab35f333e18877f3ddf075d1c553db660c",
                  "password": "201bc869fb7ced4023225898ceada7c8",
                  "pictureCode": "9999",
                  "remember": "true"}
        response = self.session.post(url1,data=myData)
        print(response.json())
        self.assertEqual("NOT_CORP_USER_VALID",response.json().get("state"))
        self.assertEqual("您还未注册，请先注册！",response.json().get("msg"))
    #函数1：登录---输入已注册的账号名和错误的密码
    def test_login_wrong_password(self):
        url1 = "https://twecruitpa.hrtools.cn/wecruit/login/SU6142a94d22d5c64be52a4194"
        myData = {"username": "0fc9949f1eb384bfb4dccbc58e5a026235f333e18877f3ddf075d1c553db660c",
                  "password": "d5ad495b0c8a04e499f9873bdcdb2de930ac1b95827fad8b177778d2d4f038c0",
                  "pictureCode": "9999",
                  "remember": "true"}
        response = self.session.post(url1,data=myData)
        print(response.json())
        self.assertEqual("LOGIN_FAIL_000006",response.json().get("state"))
        self.assertEqual("用户名或密码错误",response.json().get("msg"))
    #函数2：查询投递记录
    def test_get_delivery_record(self):
        self.test_login()
        url2 = "https://twecruitpa.hrtools.cn/wecruit/delivery/list/myRecord/SU6142a94d22d5c64be52a4194"
        myParam2 = {'recruitType': '2,1,12'}
        response2 = self.session.get(url2, params=myParam2)
        print(response2.json())
        self.assertIn("银行安保员",response2.text)  #assertIn 是否包含
