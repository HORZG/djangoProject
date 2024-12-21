"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from users.views import register,homepage, gotologinpage,login_view
from depenses.views import alldepenses,adddepense,gotoadddepense,delete_depense,update_depense,gotoupdate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage ,name='home'),
    path('api/login/', gotologinpage, name='loginpage'),
    path('api/login/access', login_view, name='login'),
    path('api/register/', register, name='register'),
    
    path('api/alldepenses', alldepenses, name="depenses"),
    path('api/depenses/add',adddepense , name='adddepense'),
    path('api/add/depense', gotoadddepense, name ='gotoadddepense'),

    path('api/depenses/delete/<str:depense_id>/', delete_depense, name='delete_depense'),
    path('api/depense/letsupdate',gotoupdate , name="gotoupdate"),
    path('api/depenses/update/<str:depense_id>/', update_depense, name='update_depense'),
    
]
