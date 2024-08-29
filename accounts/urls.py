from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# urlpatterns = [
# post views
   # path('login/', views.user_login, name='login'),
#     path('', views.dashboard, name='dashboard'),
#     path('login/', auth_views.LoginView.as_view(), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('password_change/',auth_views.PasswordChangeView.as_view(), name='password_change'),
#     path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
#     path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
#     path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
#     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
#     path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


# ]

urlpatterns = [
    path('', views.dashboard, name='dashboard1'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout1'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('creative/',views.creative,name='creative'),
    path('contact/',views.contact,name='contact'),
    path('people/',views.people,name='people'),
    path('expertise/',views.expertise,name='expertise'),
    path('projects/',views.projects,name='projects'),
    path('details/',views.details,name='details'),
    path('prcreative/',views.prcreative,name='prcreative'),
    path('blog/',views.bloghtml,name='blog'),
    path('test/',views.testhtml,name = 'test')
  
]