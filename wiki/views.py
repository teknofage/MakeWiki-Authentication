from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from wiki.models import Page
from wiki.forms import PageCreateForm

class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })
        
class CreatePageView(CreateView):
     
    def get(self, request, *args, **kwargs):
        context = {'form': PageCreateForm()}
        return render(request, 'partials/new_page.html', context)

    def post(self, request, *args, **kwargs):
        form = PageCreateForm(request.POST)
        if form.is_valid():
            page = form.save()
            return HttpResponseRedirect(reverse_lazy('pages:detail', args=[page.id]))
        return render(request, 'partials/new_page.html', {'form': form})

