from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('register_view/', views.register_view, name='register_view'),
    path('register/', views.register, name='register'),
    path('login/', views.login1, name='login1'),
    path('login_view/', views.login_view, name='login_view'),
    path('admin_dashboard/,',views.admin_dashboard, name='admin_dashboard') ,
    path('logout_view/', views.logout_view, name='logout_view'),
    path('password_reset/', views.password_recovery, name='password_reset'),
    path('about/', views.about, name='about'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('otp_verification/', views.otp_verification, name='otp_verification'),
    path('profile_view/', views.profile_view, name='profile_view'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    

    path('add-challenge/', views.add_challenge, name='add_challenge'),
    path('challenges/', views.challenge_list, name='challenge_list'), 
    path('challenge/<int:id>/', views.challenge_detail, name='challenge_detail'),
    path('challenge/<int:id>/take/', views.take_challenge, name='take_challenge'),
    path('edit-challenge/<int:challenge_id>/', views.edit_challenge, name='edit_challenge'),
    path('delete-challenge/<int:challenge_id>/', views.delete_challenge, name='delete_challenge'),
    path('admin_challenges/', views.admin_challenge_list, name='admin_challenge_list'),
    path('challenge/<int:challenge_id>/code_editor/', views.code_editor, name='code_editor'),
    path('challenge/<int:challenge_id>/submit/', views.submit_code, name='submit_code'),
    path("result/<str:token>/", views.get_result, name="get_result"),
    path('challenge/<int:challenge_id>/code_editor/', views.code_editor, name='code_editor'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('contest/<int:contest_id>/context/', views.contest_context, name='contest_context'),
    # Other URL patterns...

    
 
    path('challenge/<int:challenge_id>/code_editor/', views.code_editor, name='code_editor'),
    path("create-contest/", views.create_contest, name="create_contest"),
    path("join-contest/", views.join_contest, name="join_contest"),
     path('contest/<int:contest_id>/<int:challenge_id>/', views.contest_detail, name='contest_detail'),

    path("contest/<int:contest_id>/challenge/<int:challenge_id>/submit/", views.submit_code, name="submit_code"),
    path("contest/<int:contest_id>/leaderboard/", views.leaderboard, name="leaderboard"),
]