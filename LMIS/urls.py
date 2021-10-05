"""LMIS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from common.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include(('common.urls', 'common'), namespace='common')),
    # path('japan/inventory/', include(('japan_inventory.urls', 'japan_inventory'), namespace='japan_inventory')),
    # path('philip/inventory/', include(('philip_inventory.urls', 'philip_inventory'), namespace='philip_inventory')),
    # path('pak/inventory/', include(('pak_inventory.urls', 'pak_inventory'), namespace='pak_inventory')),
    path('', HomePageView.as_view(), name='index'),

]