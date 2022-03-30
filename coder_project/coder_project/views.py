from django.http import HttpResponse
from django.template import Template, Context, Loader

def salutation(request):
    return HttpResponse("Best regards")

def age(request, year):
    birth_year = 2022 - int(year)
    return  HttpResponse(birth_year)

 
# def index(request):
    # set html file
    file = open(r"C:\Users\maxim\OneDrive\Documents\django-intro\coder_project\coder_project\templates\index.html", 'r')
    # define a new template
    new_template = Template(file.read())
    # close the file
    file.close()
    # define a new context
    new_context = Context()
    # generate document that will be renderized
    document = new_template.render(new_context)

    # return document
    return HttpResponse(document)

def index(request):
    template = Loader.get_template("index.html")
    document = template.render()
    