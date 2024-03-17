import subprocess
def apt(dpkg,password):
    sh = ""
    # 自动判断是否为deb文件
    if dpkg[-5:] in ".deb":
        sh = f"echo  {password} | sudo -S dpkg -i {dpkg}"
    else:
        sh = f"echo  {password} | sudo -S apt install {dpkg}"
    # 在Shell下执行sh，且重定向到一个管道中
    控制台 = subprocess.Popen(sh, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # 返回一个包含标准输出和错误单元组
    标准输出,异常输出 = 控制台.communicate()
    return 标准输出,异常输出
def 强制安装(dpkg,password):
    sh = f"echo  {password}| sudo -S dpkg -i --force-all {dpkg}"
    控制台 = subprocess.Popen(sh, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    标准输出,异常输出 = 控制台.communicate()
    return 标准输出,异常输出

def 兼容性安装(dpkg,password):
    print("开始尝试兼容性安装")
    print("正在尝试进入兼容性模式")
    sh = f"bookworm-run"
    控制台 = subprocess.Popen(sh, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    标准输出,异常输出 = 控制台.communicate()
    if 异常输出 == 0:
        print("进入兼容性模式成功")
    else:
        是否安装兼容性模式 = input("进入兼容性模式失败，是否安装兼容性模式？[默认为YES]")
        if 是否安装兼容性模式.lower() in ["no","n"]:
            print("正在尝试安装兼容性模式")
            # 下载兼容性模式安装包
            sh = f"wget -O ~/Downloads/ https://"
            sh = f"wget -O ~/Downloads/ "
            控制台 = subprocess.Popen(sh, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            sh = f"echo {password} | sudo -S dpkg -i ~/Downloads/bookworm_1.1.2_amd64.deb"
            控制台 = subprocess.Popen(sh, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            标准输出,异常输出 = 控制台.communicate()
            if 异常输出 == 0:
                print("安装兼容性模式成功")
            else:
                print("安装兼容性模式失败")
    sh = f"echo {password} | sudo -S dpkg -i --force-all {dpkg}"
    控制台 = subprocess.Popen(sh, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    标准输出,异常输出 = 控制台.communicate()
    return 标准输出,异常输出