from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from libraryinv.forms import *
from django.forms import modelformset_factory



def index(request):
    publication = Publication.objects.all()
    context_dict = {'publication': publication}
    return render(request, "libraryinv/index.html", context_dict)


def about(request):
    return render_to_response('libraryinv/about.html')


def manage_pubtitles(request):
    PublicationFormSet = modelformset_factory(Publication, fields=('publication_title', 'publication_number'))
    if request.method == 'POST':
        formset = PublicationFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            if Publication.account_number == Publisher.account_number and Publication.publication_number == Publisher.publication_number:
                return Publisher.publication_title
            elif Publication.account_number == Publisher.account_number and Publisher.publication_number == "NULL":
                return Publisher.publication_title
            else:
                input('Publisher not found. Add new Publisher?')
                return render_to_response('libraryinv/add_publisher.html')
    else:
        formset = PublicationFormSet()
    return render_to_response('libraryinv/add_title.html', {'formset': formset})


def add_title(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = PublicationForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
    else:
        form = PublicationForm()
    return render_to_response('libraryinv/add_title.html', {'form': form}, context)


def add_publisher(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = PublisherForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = PublisherForm()
    return render_to_response('libraryinv/add_publisher.html', {'form': form}, context)
