from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Client, Case
from .filters import ClientFilter, CaseFilter
from .forms import ClientForm, CaseForm


# Create your views here.
@login_required(login_url='account:log_in')
def index(request):
    # 1 получение клиентов
    clients = Client.objects.all()

    # 2 создаём фильтры
    clients_filter = ClientFilter(request.GET, queryset=clients)
    clients = clients_filter.qs

    # 3 создание контекста
    context = {}
    context['clients'] = clients
    context['clients_filter'] = clients_filter

    # 3 рендер шаблона
    return render(request, 'clients/index.html', context)


@login_required(login_url='account:log_in')
def create_client(request):
    form = ClientForm()

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('clients:create'))

    context = {}
    context['form'] = form

    return render(request, 'clients/client_form.html', context)


@login_required(login_url='account:log_in')
def details(request, cid):
    client = Client.objects.get(pk=cid)
    client_cases = client.case_set.all()

    cases_filter = CaseFilter(request.GET, queryset=client_cases)
    client_cases = cases_filter.qs

    context = {}
    context['client'] = client
    context['client_cases'] = client_cases
    context['cases_filter'] = cases_filter

    return render(request, 'clients/client.html', context)


@login_required(login_url='account:log_in')
def update(request, cid):
    client = Client.objects.get(pk=cid)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect(reverse('clients:index'))

    context = {}
    context['client'] = client
    context['form'] = form

    return render(request, 'clients/client_form.html', context)


@login_required(login_url='account:log_in')
def delete(request, cid):
    client = Client.objects.get(pk=cid)
    
    if request.method == 'POST':
        client.delete()
        return redirect(reverse('clients:index'))
    
    context = {}
    context['client'] = client

    return render(request, 'clients/delete_client.html', context)


@login_required(login_url='account:log_in')
def create_case(request, cid):
    client = Client.objects.get(pk=cid)
    form = CaseForm()
    
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.client = client
            instance.coordinator = request.user.employee
            instance.save()
            return redirect(reverse('clients:create_case', args=[cid]))

    context = {}
    context['client'] = client
    context['form'] = form

    return render(request, 'clients/case_form.html', context)


@login_required(login_url='account:log_in')
def update_case(request, case_id):
    case = Case.objects.get(pk=case_id)
    client = case.client
    form = CaseForm(instance=case)

    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect(reverse('clients:details', args=[case.client.id]))

    context = {}
    context['case'] = case
    context['client'] = client
    context['form'] = form

    return render(request, 'clients/case_form.html', context)


@login_required(login_url='account:log_in')
def delete_case(request, case_id):
    case = Case.objects.get(pk=case_id)
    
    if request.method == 'POST':
        case.delete()
        return redirect(reverse('clients:details', args=[case.client.id]))
    
    context = {}
    context['case'] = case

    return render(request, 'clients/delete_case.html', context)

