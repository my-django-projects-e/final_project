from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, EmployeeSettingsForm
from .models import Employee


def log_in(request):
    # 1 ограничение залогиненым юзерам
    if request.user.is_authenticated:
        # передаю аргумент profile, то есть id юзера
        # args принимает список, kwargs словарь
        return redirect(reverse('account:profile', args=[request.user.id]))

    # 2 обработка POST запроса
    if request.method == 'POST':
        # так обрабатываются формы, не созданные Django
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # перенаправление залогиневшегося юзера
        if user:
            login(request, user)
            return redirect(reverse('account:profile', args=[request.user.id]))
        messages.info(request, 'Неравильный логин или пароль')

    # 3 рендер шаблона
    return render(request, 'account/log_in.html')


@login_required(login_url='account:log_in')
def log_out(request):
    logout(request)
    return redirect('account:log_in')


def register(request):
    # 1 ограничение залогиненым юзерам
    if request.user.is_authenticated:
        # передаю аргумент profile, то есть id юзера
        # args принимает список, kwargs словарь
        return redirect(reverse('account:profile', args=[request.user.id]))

    # 2 обработка отправленной формы
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            Employee.objects.create(
                user=user,
                name=user.username,
                email=user.email
            )

            messages.success(request, 'Аккаунт был создан для ' + str(user))
            return redirect(reverse('account:log_in'))

    # 3 упаковка формы в контекст
    form = RegisterForm()
    context = {}
    context['form'] = form

    # 4 рендеринг страницы регистрации
    return render(request, 'account/register.html', context)


@login_required(login_url='account:log_in')
def profile(request, uid):
    employee = request.user.employee
    context = {}
    context['employee'] = employee
    return render(request, 'account/profile.html', context)


@login_required(login_url='account:log_in')
def profile_settings(request, uid):
    employee = request.user.employee
    form = EmployeeSettingsForm(instance=employee)

    if request.method == 'POST':
         form = EmployeeSettingsForm(request.POST, request.FILES, instance=employee)
         if form.is_valid():
             form.save()

    context = {}
    context['employee'] = employee
    context['form'] = form

    return render(request, 'account/settings.html', context)
