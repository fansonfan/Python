import requests

req = requests.Session()

headers={

}
def signin():
    # 验证码坐标(拿验证码->获得位置->手动提交位置点->验证成功)
    #获取验证码图片
    response=req.get('验证码url')
    codeImg=response.content
    fn =open('code.png','wb')
    fn.write(codeImg)
    fn.close()
    #验证码校验
    codeStr =input("请输入验证码坐标：")
    data={
        'answer':'34,40',
        'login_site':'E',
        'rand':'sjrand'
    }
    response=req.post('https://',data=data,headers=headers)
    result = response.json()
    if result['result_code']='4':
        print('验证码验证成功')
    else:
        print('验证码验证失败')
        signin()
        return
    #登录
    data = {
        'username':user.user,
        'password':user.password,
        'appid':'otn'
    }
    response = req.post('url',data=data,headers=headers)
signin()


