from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UploadFile
from .forms import UploadFileForm
from django.shortcuts import render, get_object_or_404


#@login_required


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.uploaded_by = request.user  # Assign the logged-in user as the uploader
            upload.updated_by = request.user  # Also assign the logged-in user as the updater initially
            upload.save()
            return redirect('file_list')
    else:
        form = UploadFileForm()
    return render(request, 'fileapp/upload_file.html', {'form': form})

@login_required
def update_file(request, pk):
    upload = get_object_or_404(UploadFile, pk=pk)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES, instance=upload)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.updated_by = request.user  # Assign the logged-in user as the updater
            upload.save()
            return redirect('file_list')
    else:
        form = UploadFileForm(instance=upload)
    return render(request, 'fileapp/update_file.html', {'form': form})

def file_list(request):
    files = UploadFile.objects.all()
    return render(request, 'fileapp/file_list.html', {'files': files})

def file_detail(request, pk):
    file = get_object_or_404(UploadFile, pk=pk)
    return render(request, 'fileapp/file_detail.html', {'file': file})
