from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def gear(request):
    return render(request, 'main/gear.html')

def contact(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'main/contact.html')

def project_detail(request, id):
    # Retrieve project details based on the ID
    project = {'id': id, 'title': f'Project {id}', 'description': f'Description of project {id}'}
    return render(request, 'main/project_detail.html', {'project': project})
