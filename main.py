from 安装命令执行 import apt
from 检测是否有错误 import 检测错误
dpkg = input("请输入deb包的完整路径或者输入软件包名")
password = input("请输入root密码")

标准输出,异常输出 = apt(dpkg, password)
# 矫正
矫正标准输出 = 标准输出.decode('utf-8')
矫正异常输出 = 异常输出.decode('utf-8')

# 调用错误处理
检测错误(矫正异常输出)


