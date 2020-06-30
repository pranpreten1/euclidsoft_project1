from django.shortcuts import render


def main_page(request):
    return render(request, 'k_user/main_page.html', {})


def login_page(request):
    return render(request, 'k_user/login_page.html', {})