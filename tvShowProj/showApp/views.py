from django.shortcuts import render, redirect
from showApp.models import Show
from django.contrib import messages #added to use validations

# Create your views here.
def shows(request):
    context = {
        "all_shows" : Show.objects.all()
    }
    return render(request, "shows.html", context)

def new_show(request):
    return render(request, 'new.html')

def create_new_show(request):
    #add a new show to the database
    #checking for validations:
    #first add postdata in a variable
    errors = Show.objects.basic_validator(request.POST)
    
    #check if errors is empty, if not loop through to display error messages
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        
        #redirect the user back to fix the errors
        return redirect('/shows/new')


    else:
        new_show = Show.objects.create(title = request.POST['title'], network = request.POST['network'], release_date=request.POST['date'], desc=request.POST['desc'])
    
        return redirect(f'/shows/{new_show.id}')

def edit(request, id):
    context = {
        "selected_show" : Show.objects.get(id=id)
    }

    return render(request, "edit.html", context)

def destroy(request, id):
    Show.objects.get(id=id).delete()

    return redirect('/')

def update(request):
    #checking for validations:
    #first add postdata in a variable
    errors = Show.objects.basic_validator(request.POST)
    to_update = Show.objects.get(id=request.POST['id'])

    #check if errors is empty, if not loop through to display error messages
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        #redirect the user back to fix the errors
        return redirect(f'/shows/{to_update.id}/edit')

    else:  
        if(request.POST['title'] != ''):
            to_update.title = request.POST['title']
        if(request.POST['network'] != ''):
            to_update.network = request.POST['network']
        if(request.POST['date'] != ''):
            to_update.release_date = request.POST['date']
        if(request.POST['desc'] != ''):
            to_update.desc = request.POST['desc']
        to_update.save()

    context = {
        'selected_show' : Show.objects.get(id=request.POST['id'])
    }

    return render(request, "show.html", context)

def show(request, id):
    context = {
        "selected_show" : Show.objects.get(id = id)
    }

    return render(request, "show.html", context)

    
