from django.db.models import Q
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import SimpleSearchForm, CategoryForms
from webapp.models import Category


class CategoryView(ListView):
    model = Category
    template_name = 'categories/category_view.html'
    context_object_name = 'category'

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search']
        return None

    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(title__icontains=self.search_value) |
                                       Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class ProjectDetailView(DetailView):
    model = Category
    template_name = 'categories/category_view.html'


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'categories/category_create.html'
    form_class = CategoryForms

    def get_success_url(self):
        return reverse('category_view', kwargs={'pk': self.object.pk})
