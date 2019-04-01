from django.shortcuts import render
from .forms import UserInputForm
from .models import JobUser


def UserJobView(request):
    import pdb;
    form_data = UserInputForm()
    if request.method=='POST':
        pdb.set_trace()
        form_data=UserInputForm(request.POST, request.FILES)
        if not form_data.is_valid() and not request.FILES:
            raise ValueError('User should fill all required fields')
        resume_doc=request.FILES['file']
        mapper_obj = JobUser(name=form_data.data['name'], description=form_data.data['description'],resume_title=form_data.data['resumetitle'], resume=resume_doc)
        mapper_obj.save()

    return render(request, 'user.html', {'form': form_data})

