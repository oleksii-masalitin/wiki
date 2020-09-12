from django.shortcuts import render

from . import util

def index(request, entry):
    return render(request, f'entries/{entry}.md', {
        "entry": entry
    })