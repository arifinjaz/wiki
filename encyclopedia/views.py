from django.shortcuts import render
from . import util
from django.http import Http404
from markdown2 import markdown,markdown_path
from django.contrib.sites.shortcuts import get_current_site
from django import forms
from random import choice

class processforms(forms.Form):
    task = forms.CharField(label="new task")


def index(request):
    random(request)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "encyclopedia":"encyclopedia",
        "test":"Test"
    })

#Handles all entries
def entries (request,entry):
    valid = util.get_entry(entry)
    if valid == None:
        return render(request, "encyclopedia/notfound.html")
    else:
        return render(request, "encyclopedia/entries.html", {
            "page":markdown(valid),
            "link":entry
        })


def edit(request, link):
    print(link)
    if request.method == "POST":
         content = request.POST
         util.save_entry(content["title"], content["entry"])
         return render(request, "encyclopedia/entries.html", {
        "page":markdown(util.get_entry(content["title"])),
        "link":content["title"]
    })

    content = util.get_entry(link)
    if content:
        return render(request, "encyclopedia/edit.html",{
            "content":content,
            "link":link
        })



#Handles Search all conditions
def search (request):
    input = request.GET["q"]
    list = []

    #If conditionals handles rendering template if search matches
    if input in util.list_entries():
        page = markdown(util.get_entry(input))
        return render(request, "encyclopedia/entries.html", {
        "page":page,
        "link":input
        })
    #else handles match substring
    else:
        for item in util.list_entries():
            if input in item:
                list.append(item)
    return render(request, "encyclopedia/results.html", {"list":list})


#Handles new page
def newpage(request):
    if request.method == "POST":
        info = request.POST
        print(info)
        if info['title'] in util.list_entries():
            return render(request, "404.html", {
                "error": "Please select a different Title. An encyclopedia exists with the same name."
            })
        else:
            content = markdown(info['entry'])
            print(content)
            util.save_entry(info['title'],info['entry'])
        
        return render(request,"encyclopedia/entries.html", {
            "page":markdown(util.get_entry(info['title'])),
            "link": info['title']
        })
    return render(request, "encyclopedia/Newpage.html")

def random(request):
    list = util.list_entries()
    return entries(request, choice(list))