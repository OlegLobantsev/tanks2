from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Record
from .forms import RecordForm

# Функция для входа в систему
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему.')
            return redirect('record_list')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'myapp/login.html')

# Представление для списка записей
@login_required(login_url='/login/')
def record_list(request):
    records = Record.objects.all()
    return render(request, 'record_list.html', {'records': records})

# Представление для создания записи
@login_required(login_url='/login/')
def record_create(request):
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись успешно создана.')
            return redirect('record_list')
    else:
        form = RecordForm()
    return render(request, 'record_form.html', {'form': form})

# Представление для обновления записи
@login_required(login_url='/login/')
def record_update(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись успешно обновлена.')
            return redirect('record_list')
    else:
        form = RecordForm(instance=record)
    return render(request, 'record_form.html', {'form': form})

# Представление для удаления записи
@login_required(login_url='/login/')
def record_delete(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        record.delete()
        messages.success(request, 'Запись успешно удалена.')
        return redirect('record_list')
    return render(request, 'record_confirm_delete.html', {'record': record})