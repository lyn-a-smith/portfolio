from django.shortcuts import render

# Create your views here.
def about_me_view(request):
    return render(request, 'pages/about_me.html')
def contact_view(request):
    return render(request, 'pages/contact.html')
def experience_view(request):
    return render(request, 'pages/experience.html')