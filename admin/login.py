# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import subprocess

from domain.persistable import User


# 表单
@csrf_exempt
def login_form(request):
	return render_to_response('login.html')

# 接收请求的登录数据
@csrf_exempt
def login(request):
	request.encoding='utf-8'
        username = request.POST['username'].encode("utf-8")
        password = request.POST['password'].encode("utf-8")
        c = {'username': username, 'password': password}
        all_entries = User.objects.all()
        print all_entries



	return render_to_response( "index.html", c)