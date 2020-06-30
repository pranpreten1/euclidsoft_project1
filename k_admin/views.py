from django.shortcuts import render


def module_list(request):
    return render(request, 'k_admin/module_list.html', {})
