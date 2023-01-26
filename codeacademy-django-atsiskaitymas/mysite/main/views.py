from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


@login_required
def index(response, id):
    ls = ToDoList.objects.get(id=id)

    print(ls.id)

    if ls in response.user.todolist.all():
        if response.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")

        return render(response, "main/list.html", {"ls": ls})
    return render(response, "main/view.html", {})


def home(response):
    return render(response, "main/home.html", {})


@login_required
def home_login(response):
    return render(response, "main/home_login.html", {})


@login_required
def base_login(response):
    return render(response, "main/base_login.html", {})


@login_required
def create(response):
    # response.user
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form": form})


@login_required
def view(response):
    return render(response, "main/view.html", {})


@login_required
def delete(request, id):
    project = ToDoList.objects.get(id=id)
    project.delete()
    return render(request, "main/view.html", {})


@login_required
def edit(request, n):
    pass


@login_required
def upload_picture():
    pass
