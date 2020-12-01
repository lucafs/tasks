from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from tasks.models import Task
from tasks.serializer import TaskSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many =True)
    return JsonResponse(serializer.data, safe =False)

# @csrf_exempt
# def post_task(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serial = TaskSerializer(data=data)
#         if serial.is_valid():
#             serial.save()
#             return JsonResponse(serializer.data,status =201)
#         else:
#             return JsonResponse(serial.errors, status=400)
#     else:
#         return HttpResponse("...")

@csrf_exempt
def post_task(request):
    if request.method == 'POST':
        serial = TaskSerializer(request.POST)
        if TaskSerializer.is_valid():
            TaskSerializer.save()
            return JsonResponse(TaskSerializer.serial,status =201)
        else:
            return JsonResponse(serial.errors, status=400)
    else:
        return HttpResponse("...")