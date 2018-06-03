from django.shortcuts import render,redirect
from .forms import RegisterForm

# Create your views here.
# 用户注册
def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>

    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        #检查数据合法性
        if form.is_valid():
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',context={'form':form,'next':redirect_to})

def index(request):
    return render(request,'mygis/gis.html')