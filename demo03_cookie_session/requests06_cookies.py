#0、导包
import requests
#1、登录 ---- 服务器产生session ,并响应回cookie
url1 = "https://twecruitpa.hrtools.cn/wecruit/login/SU6142a94d22d5c64be52a4194"
myData = {"username":"0fc9949f1eb384bfb4dccbc58e5a026235f333e18877f3ddf075d1c553db660c",
          "password":"201bc869fb7ced4023225898ceada7c8",
          "pictureCode":"9999",
          "remember":"true"}
response1 = requests.post(url1,data=myData)
print("状态码：",response1.status_code)
print("响应体：",response1.json())
#如何提交cookie?
#A) 从第一次响应中提取cookie
print("响应回的cookie：",response1.cookies)
#获取cookie的值
cookie_value = response1.cookies.get("RESUMEJSESSIONID")

#B) 从第二次访问时，提交cookie
#2、查看我的投递记录---提交cookie
#组织cookie对象
cookie = {"RESUMEJSESSIONID":cookie_value}
url2 = "https://twecruitpa.hrtools.cn/wecruit/delivery/list/myRecord/SU6142a94d22d5c64be52a4194"
myParam2={'recruitType':'2,1,12'}
response2 = requests.get(url2,cookies=cookie,params=myParam2)
print("状态码：",response2.status_code)
print("响应体：",response2.text)
