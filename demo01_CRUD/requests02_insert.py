#0、导包
import requests
#1、设置资源路径，请求方式
url = "https://twecruitpa.hrtools.cn/wecruit/suite/suiteInfo"
#2、设置提交数据--->发送
myJson = {
            ...
         }
response = requests.post(url,json=myJson)
#注意：post提交的数据可以是JSON(json=xxx)也可以是键值对（data=xxx）
#3、处理响应
print("状态码：",response.status_code)
print("响应体：",response.text)
