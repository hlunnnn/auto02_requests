#0、导包
import requests
#1、设置资源路径，请求方式
url = "https://twecruitpa.hrtools.cn/wecruit/isLogin/SU6142a94d22d5c64be52a4194"
#2、设置提交数据，两要素设计完毕，发送
myParams = {"iSaJAx":"isAjax"}
response = requests.get(url,params=myParams)
#3、查看响应结果
#response 响应中的API调用
print("---------响应行获取----------")
print("url:",response.url)
print("状态码：",response.status_code)
print("---------响应头获取----------")
print("所有响应头：",response.headers)
print("获取指定响应头：",response.headers.get("Content-Type"))
print("获取编码集：",response.encoding)
print("获取Cookie：",response.cookies)
print("---------响应体获取----------")
print("响应体：",response.text)
print("二进制方式显示响应体：",response.content) #获取图片或音频视频等非文本的二进制数据
print("将响应体数据解析为json格式：",response.json())  #转换为json后可以调用json的解析函数
#如果响应体是非json数据，json()函数调用会抛出异常