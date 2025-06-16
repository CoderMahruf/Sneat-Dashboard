from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView
from django.views import View
from web_project import TemplateLayout
from .models import Blog
from .forms import BlogForm
from django.shortcuts import get_object_or_404, redirect,render

class BasedView(ListView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context

class BlogView(BasedView):
    template_name = "blogs.html"
    model = Blog
    context_object_name = "blogs"
    paginate_by  = 5


class CreateBlogView(CreateView):
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context
    
    model = Blog
    form_class = BlogForm
    template_name = "edit.html"
    success_url = reverse_lazy("blog")

class UpdateBlogView(View):
    def get_context_data(self, **kwargs):
        return TemplateLayout.init(self, kwargs)

    def get(self, request, pk, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=pk)
        form = BlogForm(instance=blog)
        context = self.get_context_data(form=form, blog=blog)
        return render(request, 'edit.html', context)

    def post(self, request, pk, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=pk)
        form = BlogForm(request.POST, request.FILES,instance = blog)
        context = self.get_context_data(form=form, blog=blog)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.image = form.cleaned_data['image']
            blog.text = form.cleaned_data['text']
            blog.save()
            return redirect('blog')
        return render(request, 'edit.html', context)


class DeleteBlogView(View):
    def post(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return redirect('blog') 