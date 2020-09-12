from django.shortcuts import render

from django.http import HttpResponse

import markdown
def convert(text):
    return markdown.markdown(text, extensions=['md_in_html'])
def index(request, entry):
    with open (f'entries/templates/entries/{entry}.md', 'r') as ent:
        html = convert(ent.read())
    return HttpResponse(request, html)