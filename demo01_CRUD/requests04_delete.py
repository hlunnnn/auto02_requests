#0、导包
import requests
#1、设置资源路径，请求方式
url = "https://twecruitpa.hrtools.cn/wecruit/suite/suiteInfo"
#2、设置提交数据--->发送
myParam = {}
response = requests.delete(url,params=myParam)
#3、处理响应
print("状态码：",response.status_code)
print("响应体：",response.text)
