from pyexpat.errors import messages

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Record
from .forms import RecordForm

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('record_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'myapp/login.html')
@login_required(login_url='/login')
def record_list(request):
    records = Record.objects.all()
    return render(request, 'record_list.html', {'records': records})

@login_required(login_url='/login')
def record_create(request):
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = RecordForm()
    return render(request, 'record_form.html', {'form': form})

@login_required(login_url='/login')
def record_update(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = RecordForm(instance=record)
    return render(request, 'record_form.html', {'form': form})

@login_required(login_url='/login')
def record_delete(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('record_list')
    return render(request, 'record_confirm_delete.html', {'record': record})