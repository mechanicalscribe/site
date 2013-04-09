from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Count
from django.core.paginator import Paginator
from mechanicalscribe.settings import PREFIX, MEDIA_URL
from notes.models import Note
import re, sqlite3, datetime, sys, json

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#sys.path.append(PREFIX + "/scripts/")

def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))
    
def get_note(request, note_uid):
    n = get_object_or_404(Note, slug=note_uid)
    return render_to_response('note.html', {'note' : n}, context_instance=RequestContext(request))
 