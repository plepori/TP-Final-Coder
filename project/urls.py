"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from blog.views import index as blog_index, PostList, PostCrear, PostBorrar, PostActualizar, BlogLogin, BlogLogout #SearchPostByName

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog_index, name='index-blog'),
    path('blog/listado_blog/', PostList.as_view()), 
    path('blog/crear', PostCrear.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('blog/<int:pk>/borrar', PostBorrar.as_view(), name="familiar-borrar"), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('blog/<int:pk>/actualizar', PostActualizar.as_view(), name='familiar-actualizar'), 
    #path('search-by-name/', SearchPostByName.as_view(), name="search-by-name-post"),
    path('login/', BlogLogin.as_view(), name="blog-login"),
    path('logout/', BlogLogout.as_view(), name="blog-logout"),
]
