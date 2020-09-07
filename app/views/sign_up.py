from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..models.user import User
from ..forms.users import UserForm


def sign_up(request):
    return render(request, 'app/sign_up.html')


def register(request):
    user = User()

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('app:sign_up')
    else:
        form = UserForm(instance=user)

    return render(request, 'app/sign_up.html', dict(form=form))
