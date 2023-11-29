from django.shortcuts import render, redirect
from .models import task
from .forms import myForm

# Create your views here.
def home(request):
    ob = task.objects.all()
    if request.method == 'POST':
        t = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        tas = task(name=t, priority=priority,date=date)
        tas.save()
    return render(request, 'home.html', {'object': ob})


def delete(request, tid):
    t = task.objects.get(id=tid)
    if request.method == 'POST':
        t.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request,tid):
    ts = task.objects.get(id=tid)
    fm = myForm(request.POST or None,request.FILES,instance=ts)
    if fm.is_valid():
        fm.save()
        return redirect('/')
    return render(request, 'update.html',{'fr':fm,'task':ts})
