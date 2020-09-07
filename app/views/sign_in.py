from django.http import HttpResponse
from django.shortcuts import render


def sign_in(request):
    return render(request, 'app/sign_in.html')
