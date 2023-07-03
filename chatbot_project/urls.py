"""
URL configuration for chatbot_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from chatbot_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('api/chatbot/', views.chatbot_api_view, name='chatbot_api'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
