from django.shortcuts import render, redirect
from django import forms

from django.http import HttpResponse
from django.urls import reverse

class new_form(forms.Form):
    task=forms.CharField(label='new_task')
    priority=forms.IntegerField(label="priotity", min_value=1, max_value=6)
    
tasks=['foo', 'bar', 'baz']


def index(request):
    return render(request, 'hello/index.html', {
        'tasks':tasks
    })
    
    
def add(request):
    if request.method=="POST":
        form=new_form(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            tasks.append(task)
            # return HttpResponse(reverse('tasks:index'))
            return redirect('tasks:index') 
        else:
            print("Form is not valid!")
            return render(request, 'hello/index2.html')
    return render(request, 'hello/index2.html', {
    "form":new_form()
    })