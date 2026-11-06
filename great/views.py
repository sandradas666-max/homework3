from django.shortcuts import render
def index(request):
    students=[
        {'name':'John Doe','grade':'B','passed':True},
        {'name':'Jane Smith','grade':'A','passed':True},
        {'name':'Mike Johnson','grade':'C','passed':False},
        {'name':'Emily Davis','grade':'B','passed':True},
        {'name':'David Wilson','grade':'D','passed':False},
    ]
    return render(request,'index.html',{'students':students})

# Create your views here.
