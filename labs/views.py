from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Lab 


def lab_list(request):
    object_list = Lab.published.all()
    paginator = Paginator(object_list, 3) # 3 labs in each page
    page = request.GET.get('page')
    try:
        labs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        labs = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        labs = paginator.page(paginator.num_pages)
    return render(request,
                  'labs/list.html',
                  {'page': page,
                   'labs': labs})


def lab_detail(request, skill, lab):
    lab = get_object_or_404(Lab, slug=lab,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'labs/detail.html',
                  {'lab': lab})


class LabListView(ListView):
    queryset = Lab.published.all()
    context_object_name = 'labs'
    paginate_by = 3
    template_name = 'labs/list.html'
