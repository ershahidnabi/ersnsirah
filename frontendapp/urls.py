
from django.urls import path
from.import views

urlpatterns = [
    path('', views.HOME, name="home"),
    path('about/us/', views.ABOUT_US, name="about-us"),
    path('contact/us/', views.CONTACT_US, name="contact-us"),
    path('faq', views.FAQ, name="faq"),
    path('news/detail/', views.NEWS_DETAIL, name="news-detail"),
    path('news/', views.NEWS, name="news"),
    path('pricing/', views.PRICING, name="pricing"),
    path('project/detail/', views.PROJECT_DETAIL, name="project-detail"),
    path('project/', views.PROJECT, name="project"),
    path('service/detail/', views.SERVICE_DETAIL, name="service-detail"),
    path('service/', views.SERVICE, name="service"),
    path('team/detail/', views.TEAM_DETAIL, name="team-detail"),
    path('team/', views.TEAM, name="team"),

]
