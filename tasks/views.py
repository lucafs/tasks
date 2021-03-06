from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tasks.models import Task
from tasks.serializer import TaskSerializer
from .forms import TaskForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many =True)
    return JsonResponse(serializer.data, safe =False)

@csrf_exempt
def post_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse(form.data,status =201)
        return HttpResponse("...")