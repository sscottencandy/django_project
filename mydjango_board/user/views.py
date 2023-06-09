from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout 
from django.utils import timezone

def index(request):
    # print(request.session)
    # for k, v in request.session.items():
    #     print(k, v)
    # request.session['visit_profile']= timezone.now().timestamp()
    resp =render (request, 'user/profile.html')
    resp.set_cookie('cookie_test', 'test_value')
    return resp

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('user:index'))
    return render(request, 'user/register.html', {'form':form})

# def user_profile(request):
#     return HttpResponse("""
#                         <h1>나의 프로필</h1>
#                         <ul>
#                             <li>이름 : 정훈</li>
#                             <li>별명 : JH</li>
#                         </ul>
#                         """)