#0、导包
import requests
#1、设置资源路径，请求方式
url = "https://twecruitpa.hrtools.cn/wecruit/suite/suiteInfo"
#2、设置提交数据，两要素设计完毕，发送
myParams = {"suiteKey":"6142a94d22d5c64be52a4194"}
# response = requests.get("https://twecruitpa.hrtools.cn/wecruit/suite/suiteInfo?iSaJAx=isAjax&request_locale=en&t=1650272716582&suiteKey=6142a94d22d5c64be52a4194")
response = requests.get(url,params=myParams)
#9、10两行代码等价
#3、查看响应结果
print("状态码：",response.status_code)
print("响应体：",response.text)
