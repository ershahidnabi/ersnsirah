from django.shortcuts import render

# Create your views here.

def HOME(request):
    return render(request, 'pages/home.html')

def ABOUT_US(request):
    return render(request, 'pages/about-us.html')

def CONTACT_US(request):
    return render(request, 'pages/contact-us.html')

def FAQ(request):
    return render(request, 'pages/faq.html')

def NEWS_DETAIL(request):
    return render(request, 'pages/news-detail.html')

def NEWS(request):
    return render(request, 'pages/news.html')

def PRICING(request):
    return render(request, 'pages/pricing.html')

def PROJECT_DETAIL(request):
    return render(request, 'pages/project-detail.html')

def PROJECT(request):
    return render(request, 'pages/project.html')

def SERVICE_DETAIL(request):
    return render(request, 'pages/service-detail.html')

def SERVICE(request):
    return render(request, 'pages/service.html')

def TEAM_DETAIL(request):
    return render(request, 'pages/team-detail.html')

def TEAM(request):
    return render(request, 'pages/team.html')


