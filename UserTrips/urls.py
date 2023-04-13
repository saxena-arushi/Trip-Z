from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',views.LandingPage),
    path('login/',views.Login, name="Login"),
    path('signup/',views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
    path('preferences', views.preferences, name="preferences"),
    path('recommendations', views.recommendations, name="recommendations"),
    path('personal-dashboard/', views.personalDashboard, name="personal-dashboard"),
    path('userprofile/<str:username>/', views.userprofile, name='userprofile'),
    path('aboutus', views.aboutus, name="aboutus"),
    path('contactus', views.contactus, name="contactus"),
    #path('publish_trip/', views.publish_trip, name='publish_trip'),    
    path('publish_a_trip/', views.publish_a_trip, name='publish_a_trip'),
    path('retrieve/', views.retrieve,name="retrieve")
    #path('accounts/login/', LoginView.as_view(), name='login'),
]

