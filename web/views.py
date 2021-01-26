from django.shortcuts import render,redirect,HttpResponse
from repository import models
from django.urls import reverse
from django.http import JsonResponse
from utils import get_check_code
from io import BytesIO
# Create your views here.
def index(request):
    type_list = models.Article.type_of_article
    return render(request,'index.html',locals())

#注册
def register(request):
    ret = {"status":0,"msg":0}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        models.UserInfo.objects.create(
            username = username,
            password = password,
            email = email
        )
        ret["msg"] = "注册成功！"
        # print(request.session["check_code"])
        return JsonResponse(ret)
    return render(request,'register.html',locals())

#获取验证码
def get_code(request):
    text,image = get_check_code.gene_code()
    buf = BytesIO()
    image.save(buf,'png')
    request.session["check_code"] = text
    return HttpResponse(buf.getvalue(),'image/png')
#检验验证码
def check_code(request):
    ret = {"status":0,"msg":""}
    s_code = request.session["check_code"]
    code = request.GET.get("code")
    if code.lower() == s_code.lower():
        ret["status"] = 1
        return JsonResponse(ret)
    ret["msg"] = "验证码输入错误！"
    return JsonResponse(ret)
def article(request,kwargs):
    if kwargs:
        types_id = int(kwargs)
    type_list = models.Article.type_of_article
    return render(request,'articles.html',locals())

def login(request):
    ret = {
        "status":0,
        "msg":""
    }
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = models.UserInfo.objects.filter(username=username)
        if user:
            if password != user[0].password:
                ret["status"] = 1
                ret["msg"] = "密码错误，请重新输入！"
                return JsonResponse(ret)
            else:
                request.session["user"] = 1
                ret["msg"] = "/index/"
                return JsonResponse(ret)
        else:
            ret["msg"] = "用户名不存在！"
            ret["status"] = 1
            return JsonResponse(ret)
    return render(request,'login.html',locals())

#注销
def logout(request):
    request.session["user"] = 0
    return redirect("/index/login/")

#检查用户名是是否存在
def check_user(request):
    ret = {
        "msg":"",
        "status":0
    }
    username = request.POST.get("username")
    if username:
        user = models.UserInfo.objects.filter(username=username)
        if user:
            ret["status"] = 1
            ret["msg"] = "用户名已存在！"
            return JsonResponse(ret)
        ret["msg"] = "恭喜，用户名可用！"
        return JsonResponse(ret)
    ret["status"] = 1
    ret["msg"] = "用户名不能为空"
    return  JsonResponse(ret)

