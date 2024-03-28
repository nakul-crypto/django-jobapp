from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader

from app_1.models import JobPost

# Create your views here.

job_title = [

    "Software Developer",
    "Software Tester",
    "DevOps Engineer",
    "Cloud Engineer",
    "Business Analyst"

]

job_description = [
    "Software Developer job role description",
    "Software Tester job role description",
    "DevOps Engineer job role description",
    "Cloud Engineer job role description",
    "Business Analyst job role description"
]
def hello(request):
    return HttpResponse("<h1>Hello World</h1>")

class TempClass:
    x = 5


def hello(request):
    # template = loader.get_template('app_1/hello.html')
    list = ['alpha', 'beta']
    temp = TempClass()
    age = 36
    is_authenticated = True
    context = {'name':'django', 'first_list': list, 'temp_object': temp, 'person_age': age, 'authentication': is_authenticated}
    # return HttpResponse(template.render(context, request))
    return render(request,'app_1/hello.html', context)


def job_list(request):
    # <ul> <li> Job 1 </li> <li> Job 2 </li> <li> Job 3 </li> <ul>

    list_of_jobs = "<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     detail_url= reverse('jobs_detail', args=(job_id,))
    #     list_of_jobs += f"<li> <a href= '{detail_url}'>{j} </li>"
    # list_of_jobs += "</ul>"
    # # return HttpResponse(list_of_jobs)
    jobs = JobPost.objects.all()
    context = {"jobs":jobs}
    return render(request,'app_1/index.html', context)


def job_detail_page(request,id):
    print(id)
    print(request)
    # return HttpResponse(f"<h2>Welcome to the Job Detail Page {id}</h2>")
    # site = "https://google.com"
    # return HttpResponse(f"Visit <a href={site}> Google here </a>")
    
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        # return_html = f"<h1>{job_title[id]}</h1> <h2>{job_description[id]}</h2>"
        # return HttpResponse(return_html)
        job = JobPost.objects.get(id=id)
        context = {"job": job}
        # context = {'job_title': job_title[id], 'job_description': job_description[id]}
        return render(request,'app_1/job_detail_page.html', context)
    except:
        return HttpResponseNotFound("Page Not Found")   
        
    

