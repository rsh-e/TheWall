
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('main-home')
        else:
            messages.error(request, 'Invalid form data')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})