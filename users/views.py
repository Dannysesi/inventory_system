from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = forma.cleaned_data.get('username')
            messages.success(request, f'your account has been created! {username}')
            return redirect('login')
        else:
            form = UserCreationForm()
            return render(request, 'users/register.html', {'form': form})