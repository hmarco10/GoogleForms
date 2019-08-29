"""blog_project URL Configuration

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

#quickstart
from rest_framework import routers
from quickstart import views

#token
#from rest_framework.authtoken import views 
 


#quickstart
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewset)
#router.register(r'answers',views.AnswerList)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('GoogleForms/', include('posts.urls')),
    path('GoogleForms/answers/', include('posts.urls')),
    path('GoogleForms/questions/', include('posts.urls')),
    #quickstart
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #paratoken
    #path('stackOverFlow-token-auth/', views.obtain_auth_token, name='stackOverFlow-token-auth'),
    
]
