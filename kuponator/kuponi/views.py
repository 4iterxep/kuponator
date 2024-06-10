from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Kuponi
# Create your views here.


def home(request):
    kupons = Kuponi.objects.order_by('title')
    return render(request, 'kuponi/home_kuponi.html', {'kupons': kupons})


class SearchResultsView(ListView):
    model = Kuponi
    template_name = 'kuponi/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Kuponi.objects.filter(
            Q(title=query)
        )
        return object_list


class KuponDetailView(DetailView):
    model = Kuponi
    template_name = 'kuponi/detail_view.html'
    context_object_name = 'kupon'