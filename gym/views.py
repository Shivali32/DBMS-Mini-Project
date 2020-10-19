from django.shortcuts import render
from gym.models import member,trainer
# Create your views here.
from gym.form import trainerForm, memberForm
from django.db import connection
import itertools  
import plotly as plt
from plotly.offline import plot
import plotly.graph_objects as go
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import pandas as pd

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
    trainersName=[]
    trainersAge=[]
    trainersNumber=[]
    trainersSalary=[]
    for t in trainer.objects.raw('SELECT * FROM trainer;'):
        trainersName.append(t.t_name)
        trainersAge.append(t.t_age)
        trainersNumber.append(t.t_phno)
        trainersSalary.append(t.t_salary)
    df=getDataframeTrainer(trainersAge,trainersName,trainersNumber,trainersSalary)
    plotlyDict=showtableTrainer(df)
    return render(request,"showTrainer.html",plotlyDict)



def showMember(request):
    membersName=[]
    membersAge=[]
    membersNumber=[]
    for m in member.objects.raw('SELECT * FROM member;'):
        
        membersAge.append(m.m_age)
        membersNumber.append(m.m_phno)
        membersName.append(m.m_name)
    df=getDataframeMember(membersAge,membersName,membersNumber)
    plotlyDict=showtableMember(df)
    return render(request,"showMember.html",plotlyDict)



def deleteMember(request):

    membersName=[]
    membersAge=[]
    membersNumber=[]
    if request.method == 'GET':
        #do_something()
        for m in member.objects.raw('SELECT * FROM member'):
             membersAge.append(m.m_age)
             membersNumber.append(m.m_phno)
             membersName.append(m.m_name)
        df=getDataframeMember(membersAge,membersName,membersNumber)
        plotlyDict=showtableMember(df)
        return render(request,"deleteMember.html",plotlyDict)
    elif request.method == 'POST':
        name=request.POST['name']
        print(name)
        with connection.cursor() as c:
            c.execute("DELETE FROM member WHERE m_name = %s; " ,
        [name])
        for m in member.objects.raw('SELECT * FROM member;'):
            membersAge.append(m.m_age)
            membersNumber.append(m.m_phno)
            membersName.append(m.m_name)
        #do_something_else()
        df=getDataframeMember(membersAge,membersName,membersNumber)
        plotlyDict=showtableMember(df)
        return render(request,"deleteMember.html",plotlyDict)



def deleteTrainer(request):
    trainersName=[]
    trainersAge=[]
    trainersNumber=[]
    trainersSalary=[]
    
    if request.method == 'GET':
        for t in trainer.objects.raw('SELECT * FROM trainer;'):
            trainersName.append(t.t_name)
            trainersAge.append(t.t_age)
            trainersNumber.append(t.t_phno)
            trainersSalary.append(t.t_salary)
            #do_something()
        df=getDataframeTrainer(trainersAge,trainersName,trainersNumber,trainersSalary)
        plotlyDict=showtableTrainer(df)
        return render(request,"deleteTrainer.html",plotlyDict)
    elif request.method == 'POST':
        name=request.POST['name']
        print(name)
        with connection.cursor() as c:
            c.execute("DELETE FROM trainer WHERE t_name = %s " ,
        [name])
        for t in trainer.objects.raw('SELECT * FROM trainer;'):
            trainersName.append(t.t_name)
            trainersAge.append(t.t_age)
            trainersNumber.append(t.t_phno)
            trainersSalary.append(t.t_salary)
        #do_something_else()
        df=getDataframeTrainer(trainersAge,trainersName,trainersNumber,trainersSalary)
        plotlyDict=showtableTrainer(df)
        return render(request,"deleteTrainer.html",plotlyDict)


def showtableMember(df):
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(["Name", "Age","Number"]),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df['Name'], df['Age'], df['Number']],
               fill_color='lavender',
               align='left'))
    ])
    plot_div = plot(fig,output_type='div',include_plotlyjs=True)
    plotDict={'plot_div':plot_div}
    return plotDict


def getDataframeMember(membersAge,membersName,membersNumber):
    df = pd.DataFrame(columns = ['Name', 'Age','Number']) 
    for (a,b,c) in zip(membersAge,membersName,membersNumber):
        df = df.append({'Name': b}, ignore_index=True)
        df = df.append({'Age': a}, ignore_index=True)
        df = df.append({'Number': c}, ignore_index=True)

    return df


def getDataframeTrainer(trainersAge,trainersName,trainersNumber,trainersSalary):
    df = pd.DataFrame(columns = ['Name', 'Age','Number','Salary']) 
    for (a,b,c,d) in zip(trainersAge,trainersName,trainersNumber,trainersSalary):
        df = df.append({'Name': b}, ignore_index=True)
        df = df.append({'Age': a}, ignore_index=True)
        df = df.append({'Number': c}, ignore_index=True)
        df = df.append({'Salary': d}, ignore_index=True)
    return df


def showtableTrainer(df):
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(["Name", "Age","Number","Salary"]),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df['Name'], df['Age'], df['Number'],df['Salary']],
               fill_color='lavender',
               align='left'))
    ])
    plot_div = plot(fig,output_type='div',include_plotlyjs=True)
    plotDict={'plot_div':plot_div}
    return plotDict