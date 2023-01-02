from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import SignupForm,LoginForm,AddTaskForm
from .models import User, Task


class IndexView(generic.TemplateView):
    template_name = "todo/index.html"
    
    def get(self,request):
        try:
            set_and_auth = self.request.session["auth"] and self.request.session["user_id"]
        except KeyError:
            self.request.session["auth"] = False 
            self.request.session["user_id"] = -1
            return render(request, "todo/index.html")
        else:
            if set_and_auth:
                return HttpResponseRedirect(reverse("todo:todo-index"))
            else:
                return render(request,"todo/index.html")
            

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        email = request.POST["email"]
        pwd = request.POST["pwd"]

        if form.is_valid():
            if len(pwd) < 8:
                print(len(pwd))
                message = "The length of the password must be 8 or more chars *"
                # form = SignupForm()
                return render(request, "todo/todo_signup.html",{"form":form,"msg":message})
            else:
                print("Form saved successfully")
                form.save()
                user_id = User.objects.get(email=email,pwd=pwd).id
                request.session["auth"] = True
                request.session["user_id"] = user_id
                return HttpResponseRedirect(reverse("todo:todo-index"))
            
         # if form is not valid
        else:
            message = "There's an error while sending the form"
            return render(request, "todo/todo_signup.html",{"form":form,"msg":message})
    else:
        form = SignupForm()
        return render(request, "todo/todo_signup.html",{"form":form})


def login(request):
    msg = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            pwd = request.POST["pwd"]
            form = LoginForm(request.POST)
            t = User.objects.filter(email=email,pwd=pwd).count()
            print(t)

            #Verify if there is a user with the current authentication
            if t > 0:
                user = User.objects.get(email=email,pwd=pwd)
                request.session["auth"] = True
                request.session["user_id"] = user.id
                return HttpResponseRedirect(reverse("todo:todo-index"))
            else:
                msg = "Password or email is not correct !"

        else:
            msg = "There an error while submiting the data"

    form = LoginForm()
    return render(request,"todo/todo_login.html",{"form":form, "msg":msg})


def todoIndex(request):
    
    if request.session["auth"] and request.session["user_id"]:
        user_id = request.session["user_id"]
        tasks = User.objects.get(pk=user_id).task_set.all()
        
        return render(request,"todo/todo_index.html",{"tasks":tasks})
    else: 
        return HttpResponseRedirect(reverse("todo:index"))


def addtask(request):
    if request.session["auth"] and request.session["user_id"]:
                
        addmsg = ""
        if request.method == "POST":
            user = User.objects.get(pk=request.session["user_id"])
            form = AddTaskForm(request.POST)

            if form.is_valid():
                title = form.cleaned_data["title"]
                description = form.cleaned_data["description"]
                date = form.cleaned_data["date"]
                time = form.cleaned_data["time"]

                task = Task.objects.create(title=title,description=description,date=date,time=time,user_fk=user)
                task.save()
                return HttpResponseRedirect(reverse("todo:todo-index"))
        addform = AddTaskForm()
        return render(request,'todo/add.html',{"addform":addform,"addmsg":addmsg})
    
    return HttpResponseRedirect(reverse("todo:index"))
    


def edittask(request, task_id):
    if request.session["auth"] and request.session["user_id"]:
        msg=""
        task = Task.objects.get(pk=task_id)
        
        if request.method == "POST":
            form = AddTaskForm(request.POST, instance=task)
            
            if form.is_valid():
                
                #Form data
                title = form.cleaned_data["title"]
                description = form.cleaned_data["description"]
                date = form.cleaned_data["date"]
                time = form.cleaned_data["time"]

                #Updating data in the task fields
                task.title = title
                task.description = description
                task.date = date
                task.time = time

                task.save()
                return HttpResponseRedirect(reverse("todo:todo-index"))
            else:
                msg = "Error while sending the data"

        editform = AddTaskForm(instance=task)
        return render(request,'todo/update.html',{"editform":editform,"msg":msg,"task":task})

    return HttpResponseRedirect(reverse("todo:index"))


def deletetask(request,task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    print("Task deleted successfully")

    return HttpResponseRedirect(reverse('todo:todo-index'))

def logout(request):
    del request.session["auth"]
    del request.session["user_id"]
    request.session["auth"] = False
    return HttpResponseRedirect(reverse("todo:index"))
