from django.shortcuts import render
from gym.models import member,trainer
# Create your views here.
from gym.form import trainerForm, memberForm


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello, Django!")
    return render(request, 'home.html') 


def EnterTrainer(request):
    submitted = False
    if request.method == 'POST':
        form = trainerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/') 
   
    else:
        form = trainerForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'trainer.html', {'form': form, 'submitted': submitted})

def EnterMember(request):
    submitted = False
    if request.method == 'POST':
        form = memberForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/') 
    else:
        form = memberForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'member.html', {'form': form, 'submitted': submitted})



def showTrainer(request):
    trainers=[]
    for t in trainer.objects.raw('SELECT * FROM trainer'):
        trainers.append(t.t_name)
    return render(request,"showTrainer.html",{"trainers":trainers})



def showMember(request):
    members=[]
    
    for m in member.objects.raw('SELECT * FROM member'):
        
        members.append(m.m_name)
       

    return render(request,"showMember.html",{'members':members})