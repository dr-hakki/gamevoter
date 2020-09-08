"""pollster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from polls import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('pages.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('signup/', views.signupuser, name= "signupuser"),
    path('logout/', views.logoutuser, name= "logoutuser"),
    path('login/', views.loginuser, name= "loginuser"),
    path('application/', views.application, name= "application"),
    path('createpoll/', views.createpoll, name= "createpoll"),
    path('profile/', views.profile, name= "profile"),
    path('faq/', views.faq, name= "faq"),
    path('news/', views.news, name= "news"),
    path('<int:new_id>/', views.newdetail, name='newdetail'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)