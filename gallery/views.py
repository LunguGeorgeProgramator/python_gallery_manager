from django.shortcuts import render
from gallery.loadFiles import LoadFiles 
from gallery.pagination import Pagination
import random

def index(request, last_item = None):
    s = LoadFiles()
    r = Pagination(last_item)
    files = s.scanDirFunc()[r.prev:r.lastPage]
    return render(request, 'index.html', { 
        'complete_list': s.getFirstFile(files),
        'next': r.next,
        'prev': r.prev
    })

def view(request, folder_name, last_item = None):
    s = LoadFiles()
    r = Pagination(last_item)
    return render(request, 'view.html', {
        'files': s.getPhotosFiles(folder_name)[r.prev:r.lastPage],
        'folder_name': folder_name,
        'next': r.next,
        'prev': r.prev
    })

def search(request, search = None):
    s = LoadFiles()
    files = s.scanDirFunc()
    search_get = request.GET['search']
    if search_get:
        search = search_get
    if not search_get and not search: # check if empty string
        files = []
    return render(request, 'index.html', { 
        'complete_list': s.getFirstFile(files, True, search),
        'next': None,
        'prev': None
    })
