"""DjangoGis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/',include('users.urls')),
    url(r'^mygis/',include('mygis.urls')),
    # 将auth应用中的urls模块包含进来
    url(r'^users/',include('django.contrib.auth.urls')),
    # url(r'^mygis/',include('django.contrib.auth.urls')),
    url(r'^$',views.index,name='index'),
]
