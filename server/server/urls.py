"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
# from ..authentication.admin import sales_admin

value = settings.BASE_DIR


import sys

## In order to import a file from another directory we have to use the sys.path.insert method
## Refer to the below link to get a better understanding
## https://www.codegrepper.com/code-examples/python/django+import+file+from+another+directory

sys.path.insert(1,'/authentication')
import authentication.admin


## This changes the header of the admin page

admin.site.site_header = 'Leads Management Platform'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('authentication.urls')),
    path('salesadmin/', authentication.admin.sales_admin.urls)
]


