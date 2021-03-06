import imp
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

from .view.admin        import Theme as AdminTheme
from .view.game         import Theme as GameTheme
from .view.industrious  import Theme as IndustriousTheme

app_name = 'THEME'

urlpatterns = [
    # path('', views.index),
    
    path('XXX1/<menu>/<pages>/',       AdminTheme.url),
    path('XX1X/<menu>/<pages>/',        GameTheme.url),
    path('XX11/<menu>/<pages>/', IndustriousTheme.url),
    
    path('game/login/',     auth_views.LoginView.as_view(template_name='theme/game/index.html'), name='game_login'),
    path('game/logout/',    auth_views.LogoutView.as_view(), name='game_logout'),
]
