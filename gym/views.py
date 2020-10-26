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
    
    df = dfn = dfa_g = dfa_l = dfp = dfh_g = dfh_l = dfs_g = dfs_l = pd.DataFrame(columns = ['Name', 'Age','Number','Hours','Salary']) 
    #df.drop(columns = ['Name', 'Age','Number','Hours','Salary'])

    if request.method == 'GET':
        for t in trainer.objects.raw('SELECT * FROM trainer;'):
            df = df.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)            
        print(df)
        plotlyDict=showtableTrainer(df)
        return render(request,"showTrainer.html",plotlyDict)
    elif request.method == 'POST':
        name  = request.POST['name']
        age_g  = request.POST['age_g']
        age_l  = request.POST['age_l']
        phno  = request.POST['phno']
        hours_g  = request.POST['hours_g']
        hours_l  = request.POST['hours_l']
        salary_g  = request.POST['salary_g']
        salary_l  = request.POST['salary_l']        
        trainers = [name,age_g,age_l,phno,hours_g,hours_l,salary_g,salary_l]
        print(trainers)
        
        if name:
            for t in trainer.objects.raw('SELECT * FROM trainer WHERE t_name == %s ;', [name]):
                dfn = dfn.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)            
            print(dfn)
        else:
            for t in trainer.objects.raw('SELECT * FROM trainer;'):
                dfn = dfn.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)                      
        if age_g:
            for t in trainer.objects.raw('SELECT * FROM trainer WHERE t_age >= %s ;', [age_g]):
                dfa_g = dfa_g.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)            
            print(dfa_g)
        else:
            for t in trainer.objects.raw('SELECT * FROM trainer;'):
                dfa_g = dfa_g.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)                      
        dfm = pd.merge(dfn, dfa_g, how ='inner')
        if age_l:
            for t in trainer.objects.raw('SELECT * FROM trainer WHERE t_age <= %s ;', [age_l]):
                dfa_l = dfa_l.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)            
            print(dfa_l)
        else:
            for t in trainer.objects.raw('SELECT * FROM trainer;'):
                dfa_l = dfa_l.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)                      
        dfm = pd.merge(dfm, dfa_l, how ='inner')
        if phno:
            for t in trainer.objects.raw('SELECT * FROM trainer WHERE t_phno == %s ;', [phno]):
                dfp = dfp.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)            
            print(dfp)
        else:
            for t in trainer.objects.raw('SELECT * FROM trainer;'):
                dfp = dfp.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)                      
        dfm = pd.merge(dfm, dfp, how ='inner')
        if hours_g:
            for t in trainer.objects.raw('SELECT * FROM trainer WHERE t_hours >= %s ;', [hours_g]):
                dfh_g = dfh_g.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)            
            print(dfh_g)
        else:
            for t in trainer.objects.raw('SELECT * FROM trainer;'):
                dfh_g = dfh_g.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)                      
        dfm = pd.merge(dfm, dfh_g, how ='inner')
        if hours_l:
            for t in trainer.objects.raw('SELECT * FROM trainer WHERE t_hours <= %s ;', [hours_l]):
                dfh_l = dfh_l.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)            
            print(dfh_l)
        else:
            for t in trainer.objects.raw('SELECT * FROM trainer;'):
                dfh_l = dfh_l.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)                      
        dfm = pd.merge(dfm, dfh_l, how ='inner')
        if salary_g:
            for t in trainer.objects.raw('SELECT * FROM trainer WHERE t_salary >= %s ;', [salary_g]):
                dfs_g = dfs_g.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)            
            print(dfs_g)
        else:
            for t in trainer.objects.raw('SELECT * FROM trainer;'):
                dfs_g = dfs_g.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)                      
        dfm = pd.merge(dfm, dfs_g, how ='inner')
        if salary_l:
            for t in trainer.objects.raw('SELECT * FROM trainer WHERE t_salary <= %s ;', [salary_l]):
                dfs_l = dfs_l.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)            
            print(dfs_l)
        else:
            for t in trainer.objects.raw('SELECT * FROM trainer;'):
                dfs_l = dfs_l.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)                      
        dfm = pd.merge(dfm, dfs_l, how ='inner')
                
        
        print('dfm' + dfm) 
        plotlyDict=showtableTrainer(dfm)
        return render(request,"showTrainer.html",plotlyDict)


def showMember(request):
    df = dfn = dfa_g = dfa_l = dfp = dft = dfy_g = dfy_l = pd.DataFrame(columns = ['Name', 'Age','Number','Time','Years','Trainer','Facility']) 
    
    if request.method == 'GET':
        for m in member.objects.raw('SELECT * FROM member;'):
            trainerName=str(m.m_tid)
            facilityName=str(m.m_fid)
            
            df = df.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years,'Trainer':trainerName,'Facility':facilityName}, ignore_index=True)        
        #df=getDataframeMember(membersAge,membersName,membersNumber)
        #print (df)
        plotlyDict=showtableMember(df)
        return render(request,"showMember.html",plotlyDict)
    elif request.method == 'POST':
        name  = request.POST['name']
        age_g  = request.POST['age_g']
        age_l  = request.POST['age_l']
        phno  = request.POST['phno']
        time  = request.POST['time']
        years_g  = request.POST['years_g']
        years_l  = request.POST['years_l']        
        members = [name,age_g,age_l,phno,time,years_g,years_l]
        #print(members)
        
        if name:
            for m in member.objects.raw('SELECT * FROM member WHERE m_name == %s ;', [name]):
                
                dfn = dfn.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years}, ignore_index=True)        
            #print(dfn)
        else:
            for m in member.objects.raw('SELECT * FROM member;'):
                dfn = dfn.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years}, ignore_index=True)        
        if age_g:
            for m in member.objects.raw('SELECT * FROM member WHERE m_age >= %s ;', [age_g]):
                dfa_g = dfa_g.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years}, ignore_index=True)        
            #print(dfa_g)
        else:
            for m in member.objects.raw('SELECT * FROM member;'):
                dfa_g = dfa_g.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years}, ignore_index=True)        
        dfm = pd.merge(dfn, dfa_g, how ='inner')
        if age_l:
            for m in member.objects.raw('SELECT * FROM member WHERE m_age <= %s ;', [age_l]):
                dfa_l = dfa_l.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years}, ignore_index=True)        
            #print(dfa_l)
        else:
            for m in member.objects.raw('SELECT * FROM member;'):
                dfa_l = dfa_l.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years}, ignore_index=True)        
        dfm = pd.merge(dfm, dfa_l, how ='inner')
        if phno:
            for m in member.objects.raw('SELECT * FROM member WHERE m_phno == %s ;', [phno]):
                dfp = dfp.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years}, ignore_index=True)        
            #print(dfp)
        else:
            for m in member.objects.raw('SELECT * FROM member;'):
                dfp = dfp.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years}, ignore_index=True)        
        dfm = pd.merge(dfm, dfp, how ='inner')
        if time:
            for m in member.objects.raw('SELECT * FROM member WHERE m_time >= %s ;', [time]):
                dft = dft.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years}, ignore_index=True)        
            #print(dft)
        else:
            for m in member.objects.raw('SELECT * FROM member;'):
                dft = dft.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years}, ignore_index=True)        
        dfm = pd.merge(dfm, dft, how ='inner')
        if years_g:
            for m in member.objects.raw('SELECT * FROM member WHERE m_years >= %s ;', [years_g]):
                dfy_g = dfy_g.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years}, ignore_index=True)        
            #print(dfy_g)
        else:
            for m in member.objects.raw('SELECT * FROM member;'):
                dfy_g = dfy_g.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years}, ignore_index=True)        
        dfm = pd.merge(dfm, dfy_g, how ='inner')
        if years_l:
            for m in member.objects.raw('SELECT * FROM member WHERE m_years <= %s ;', [years_l]):
                dfy_l = dfy_l.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years}, ignore_index=True)        
            #print(dfy_l)
        else:
            for m in member.objects.raw('SELECT * FROM member;'):
                dfy_l = dfy_l.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years}, ignore_index=True)        
        dfm = pd.merge(dfm, dfy_l, how ='inner')
                
        
        #print('dfm' + dfm) 
        plotlyDict=showtableMember(dfm)
        return render(request,"showMember.html",plotlyDict)



def deleteMember(request):

    df = pd.DataFrame(columns = ['Name', 'Age','Number','Time','Years']) 
   
    if request.method == 'GET':
        #do_something()
        for m in member.objects.raw('SELECT * FROM member'):
              df = df.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years}, ignore_index=True)        
       
        #df=getDataframeMember(membersAge,membersName,membersNumber)
        plotlyDict=showtableMember(df)
        return render(request,"deleteMember.html",plotlyDict)
    elif request.method == 'POST':
        name=request.POST['name']
        print(name)
        with connection.cursor() as c:
            c.execute("DELETE FROM member WHERE m_name = %s; " ,
        [name])
        for m in member.objects.raw('SELECT * FROM member;'):
            df = df.append({'Name':m.m_name ,'Age': m.m_age,'Number':m.m_phno,'Time': m.m_time,'Years':m.m_years}, ignore_index=True)        
       
        #do_something_else()
        
        plotlyDict=showtableMember(df)
        return render(request,"deleteMember.html",plotlyDict)



def deleteTrainer(request):
    
    df = pd.DataFrame(columns = ['Name', 'Age','Number','Hours','Salary']) 
    
    if request.method == 'GET':
        for t in trainer.objects.raw('SELECT * FROM trainer;'):
            df = df.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)            
       
            #do_something()
        plotlyDict=showtableTrainer(df)
        return render(request,"deleteTrainer.html",plotlyDict)
    elif request.method == 'POST':
        name=request.POST['name']
        print(name)
        with connection.cursor() as c:
            c.execute("DELETE FROM trainer WHERE t_name = %s " ,
        [name])
        for t in trainer.objects.raw('SELECT * FROM trainer;'):
            df = df.append({'Name':t.t_name ,'Age': t.t_age,'Number':t.t_phno,'Hours':t.t_hours,'Salary': t.t_salary}, ignore_index=True)            
       
        #do_something_else()
        plotlyDict=showtableTrainer(df)
        return render(request,"deleteTrainer.html",plotlyDict)


def showtableMember(df):
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(["Name", "Age","Number","Time","Years","Trainer","Facility"]),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df['Name'], df['Age'], df['Number'],df['Time'],df['Years'],df['Trainer'],df['Facility']],
               fill_color='lavender',
               align='left'))
    ])
    plot_div = plot(fig,output_type='div',include_plotlyjs=True)
    plotDict={'plot_div':plot_div}
    return plotDict


def getDataframeMember(membersAge,membersName,membersNumber,membersTime,membersYears):
    df = pd.DataFrame(columns = ['Name', 'Age','Number','Time','Years']) 
    for (a,b,c,d,e) in zip(membersAge,membersName,membersNumber,membersTime,membersYears):
        df = df.append({'Name': b}, ignore_index=True)
        df = df.append({'Age': a}, ignore_index=True)
        df = df.append({'Number': c}, ignore_index=True)
        df = df.append({'Time': d}, ignore_index=True)
        df = df.append({'Years': e}, ignore_index=True)
    return df


def getDataframeTrainer(trainersAge,trainersName,trainersNumber,trainerHours,trainersSalary):
    df = pd.DataFrame(columns = ['Name', 'Age','Number','Hours','Salary']) 
    for (a,b,c,d,e) in zip(trainersAge,trainersName,trainersNumber,trainerHours,trainersSalary):
        df = df.append({'Name': b}, ignore_index=True)
        df = df.append({'Age': a}, ignore_index=True)
        df = df.append({'Number': c}, ignore_index=True)
        df = df.append({'Hours': d}, ignore_index=True)
        df = df.append({'Salary': e}, ignore_index=True)
    

    return df


def showtableTrainer(df):
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(["Name", "Age","Number","Hours","Salary"]),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df['Name'], df['Age'], df['Number'],df['Hours'],df['Salary']],
               fill_color='lavender',
               align='left'))
    ])
    plot_div = plot(fig,output_type='div',include_plotlyjs=True)
    plotDict={'plot_div':plot_div}
    return plotDict


