#0、导包
import requests
#1、先获取session对象
session = requests.Session()
#2、登录
url1 = "https://twecruitpa.hrtools.cn/wecruit/login/SU6142a94d22d5c64be52a4194"
myData = {"username":"0fc9949f1eb384bfb4dccbc58e5a026235f333e18877f3ddf075d1c553db660c",
          "password":"201bc869fb7ced4023225898ceada7c8",
          "pictureCode":"9999",
          "remember":"true"}
response1 = session.post(url1,data=myData)
print(response1.content)

#3、查询我的投递记录
url2 = "https://twecruitpa.hrtools.cn/wecruit/delivery/list/myRecord/SU6142a94d22d5c64be52a4194"
myParam2={'recruitType':'2,1,12'}
response2 = session.get(url2,params=myParam2)
print("状态码：",response2.status_code)
print("响应体：",response2.text)
#ps: session=requests+cookie  简化代码实现，提高编写效率