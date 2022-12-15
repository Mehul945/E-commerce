from django.shortcuts import render,HttpResponse,redirect
from .helper import graphs
import pandas as pd

def home(request):
    return render(request,"index.html")

def file_handle(request):
    if request.method=="POST":
        file=request.FILES.get("features")
        if file ==None:
            return redirect("/")
        data=pd.read_csv(file)
        data.to_csv("static/e_commerce.csv")
        return render(request,"result.html")
    return redirect("/")

def plot(request):
    if request.method=="POST":
        graph=request.POST.get("graph")
        print("[GRAPH]   ",graph)
        img=graphs[graph]
        data=pd.read_csv("static/e_commerce.csv")
        img(data)
    return HttpResponse(f"""<img src='static/{graph}.png'>""")

