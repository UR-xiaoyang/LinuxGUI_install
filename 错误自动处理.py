import subprocess
from main import password
from main import dpkg
from 安装命令执行 import 强制安装
def 错误处理机制(错误输出):
    错误输出 = 错误输出.split('\n')
    if 错误输出 in "无法定位软件包":
        print("在您的源中没有找到该软件包，请您检查您的源，或者检查您的输入是否正确")
    elif 错误输出 in "依赖关系问":
        print("正在尝试修复依赖关系")
        sh = f"echo  {password}| sudo -S apt -f install"
        控制台 = subprocess.Popen(sh, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        标准输出,异常输出 = 控制台.communicate()
        异常输出 = 异常输出.decode('utf-8')
        if len(异常输出) != 0:
            选择 = input("依赖关系修复失败，是否使用其他方式安装？[YES/NO](默认为NO)")
            if 选择.lower() in ["yes","y"]:
                print("正在尝试强制安装")
                强制安装标准输出, 强制安装异常输出 = 强制安装(dpkg, password)
                if len(强制安装异常输出) != 0:
                    print("强制安装失败")
                else:
                    print("强制安装成功")
            else:
                print("安装失败")
        else:
            print("依赖关系修复成功，安装成功")












