from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='login')
def home(request):
    tasks = Task.objects.filter(owner=request.user).order_by('-id')
    form = TaskForm()
    nTotalTasks = len(Task.objects.filter(owner=request.user))
    nCompletedTasks = len(Task.objects.filter(owner=request.user).filter(Completed=True))
    nUncompletedTasks = (nTotalTasks) - (nCompletedTasks)
    contesto = {
        'tasks': tasks,
        'form': form,
        'totalTasks': nTotalTasks,
        'completedTasks': nCompletedTasks,
        'nUncompletedTasks':nUncompletedTasks
    }

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(commit=False).owner = request.user
            form.save(commit=False).title = request.POST.get("title").capitalize()
            #commit=false crea un'istanza del form (in questo caso Task) ma non lo salva nel database, in questo modo possiamo aggiungere l'owner del task prima che venga salvato nel database, altrimenti genera errore
            # It seems that save(commit=False) does create a model instance, which it returns to you. Which is neat for some post processing before actually saving it!
            form.save()
            return redirect(reverse('home'))

    return render(request, 'todo/home.html', contesto)

@login_required(login_url='login')
def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if task.owner == request.user:  
        if request.method == "POST":
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
            return redirect(reverse('home'))
    else:
        return redirect(reverse('home'))
    contesto = {
        'form': form,
        'task': task
    }
    return render(request, 'todo/update.html', contesto)

@login_required(login_url='login')
def delete(request, pk):
    task = Task.objects.get(id=pk)
    if task.owner == request.user:
        if request.method == 'POST':
            task.delete()
            return redirect(reverse('home'))
    else:
        return redirect(reverse('home'))
    contesto = {
        'task': task
    }
    return render(request, 'todo/delete.html', contesto)

@login_required(login_url='login')
def check(request, pk):
    task = Task.objects.get(id=pk)
    if task.Completed == True:
        task.Completed = False
        task.save()
        return redirect(reverse('home'))
    elif task.Completed == False:
        task.Completed = True
        task.save()
        return redirect(reverse('home'))


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            pass
        
        user = authenticate(username=username, password=password)
        if user != None :
            login(request, user) #creates a session in the database for the browser
            return redirect('home')
        else:
            messages.error(request, "Username o password non validi.")
    return render(request, 'todo/login.html')

def logoutView(request):
    logout(request)
    if request.method == 'POST':
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            pass
        
        user = authenticate(username=username, password=password)
        if user != None :
            login(request, user) #crea una sessione nel the database per il browser
            return redirect('home')
        else:
            messages.error(request, "Username o password non corretti.")
    success = 'Disconnesso correttamente.'
    return render(request, 'todo/login.html', {
        'success':success
    })

def registerView(request):
    register = True;
    form = RegisterUser()
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect(reverse('home'))
        else:
            #Error messages
            if len(request.POST.get("username")) < 6:
                messages.error(request, "Assicurati che il tuo username sia almeno di 6 caratteri.")
                return redirect(reverse('register'))
            if User.objects.filter(username=request.POST.get("username")):
                messages.error(request, "Utente già esistente.")
                return redirect(reverse('register'))
            elif request.POST.get("password1") != request.POST.get("password2"):
                messages.error(request, "Le password non coincidono.")
                return redirect(reverse('register'))
            elif len(request.POST.get("password1")) < 8:
                messages.error(request, "Assicurati che la password sia almeno di 8 caratteri.")
                return redirect(reverse('register'))
            else:
                messages.error(request, "Password debole.")
                return redirect(reverse('register'))
    return render(request, 'todo/login.html', {
        'register':register,
        'form': form
    })