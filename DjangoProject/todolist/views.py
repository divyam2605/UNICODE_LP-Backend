from django.shortcuts import render
from .models import Task
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

tasks = [{
    'author': 'Divyam Dedhia',
    'title': 'To Do List 1',
    'tasks': 'Task1',
    'tbd': '23/10/2022'
},
{
    'author': 'Dimple Dedhia',
    'title': 'To Do List 2',
    'tasks': 'Task2',
    'tbd': '23/10/2022'
},
]

def home(request):
    context = {
        'tasks' : Task.objects.all()
    }
    return render(request, 'home.html', context)
'''Task.objects.all()'''

class PostListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'
    #ordering = ['-date_posted']

class PostDetailView(DetailView):
    template_name = 'task_detail.html'
    model = Task
    
class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'task_form.html'
    model = Task
    fields = ['task_name', 'description']

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'task_form.html'
    model = Task
    fields = ['task_name', 'description']

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    template_name = 'task_delete.html'
    model = Task
    success_url = '/'

def about(request):
    return render(request, 'about.html', {'title': 'Title'})