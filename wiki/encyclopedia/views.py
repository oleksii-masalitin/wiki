from django.shortcuts import render
from django.http import HttpResponse

from . import util
from django import forms

class NewTaskForm(forms.Form):
    entry = forms.CharField()

def index(request):
    if request.method == "POST":
        return HttpResponseRedirect('/wiki')
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": NewTaskForm(),
    })

def entries(request, entry):
    return render(request, f'encyclopedia/{entry}.md', {
        "entry": entry
    })