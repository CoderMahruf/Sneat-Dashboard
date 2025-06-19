from django.shortcuts import render,redirect
from .models import CMSModel
from .forms import CMSHomeSec1Form,CMSHomeSec2Form,CMSHomeSec3Form,CMSHomeSec4Form,CMSHomeSec5Form,CMSAboutSec
from django.views.generic import TemplateView
from django.contrib import messages
from web_project import TemplateLayout
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy

# Create your views here.

class CMSView1(CreateView):
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context
    
    model = CMSModel
    form_class = CMSHomeSec1Form
    template_name = "edit.html"
    success_url = reverse_lazy("update")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)
    

class CMSView2(CreateView):
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context
    
    model = CMSModel
    form_class = CMSHomeSec2Form
    template_name = "edit.html"
    success_url = reverse_lazy("update")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)
    

class CMSView3(CreateView):
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context
    
    model = CMSModel
    form_class = CMSHomeSec3Form
    template_name = "edit.html"
    success_url = reverse_lazy("update")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)
    
class CMSView4(CreateView):
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context
    
    model = CMSModel
    form_class = CMSHomeSec4Form
    template_name = "edit.html"
    success_url = reverse_lazy("update")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)
    

class CMSView5(CreateView):
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context
    
    model = CMSModel
    form_class = CMSHomeSec5Form
    template_name = "edit.html"
    success_url = reverse_lazy("update")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)
    

class CMSAboutView(CreateView):
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context
    
    model = CMSModel
    form_class = CMSAboutSec
    template_name = "edit.html"
    success_url = reverse_lazy("cmsabout")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)
