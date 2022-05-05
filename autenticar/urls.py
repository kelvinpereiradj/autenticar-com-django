
from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views

app_name = 'autenticar'
urlpatterns = [
	path('opcoes/', views.autenticar_opcoes_view, name="autenticar_opcoes"),
	path('logar/', views.logar_view, name="logar"),
	path('deslogar/', views.deslogar_view, name="deslogar"),
	path('usuario_criar/', views.usuario_criar_view, name="usuario_criar"),
	path('senha_mudar/', views.senha_mudar_view, name="senha_mudar"),
	path('usuario_informacoes/', views.usuario_informacoes_view, name="usuario_informacoes"),



	#path('/', views.ConversaView.as_view(), name="conversas")
	#path('signup/', views.signup_view, name="signup"),
	#path('add_email/', views.add_email_view, name="add_email"),
	path('login_google/', views.login_google_view, name="login_google"),
	#path('set_password/', views.set_password_view, name="setpassword"),
	path('password_reset/', views.password_reset_view, name="password_reset"),
	#path('reset_password_key', views.reset_password_key_view, name="reset_password_key"),
	path('login_rede_social/', views.login_rede_social_view, name="login_rede_social"),
	path('login_rede_social_redirecionar/', views.login_rede_social_redirecionar_view, name="login_rede_social_redirecionar"),
	#path('social_auth/', include('social_django.urls', namespace='social_auth')),

	path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
	path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
	path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
	path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]
