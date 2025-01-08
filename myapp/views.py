# user_api/views.py
import csv
from django.shortcuts import render
from .forms import CSVUploadForm
from .serializers import UserSerializer
from .models import User

def upload_csv_view(request):
    form = CSVUploadForm()
    errors = []
    valid_records = 0
    invalid_records = 0

    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if not file.name.endswith('.csv'):
                errors.append("Please upload a valid .csv file.")
            else:
                decoded_file = file.read().decode('utf-8')
                csv_reader = csv.DictReader(decoded_file.splitlines())

                # Strip whitespace from field names
                csv_reader.fieldnames = [field.strip() for field in csv_reader.fieldnames]

                for row in csv_reader:
                    serializer = UserSerializer(data=row)
                    if serializer.is_valid():
                        serializer.save()
                        valid_records += 1
                    else:
                        invalid_records += 1
                        errors.append(f"Row {row}: {serializer.errors}")
        else:
            errors.append("Form submission failed. Please try again.")

    context = {
        "form": form,
        "valid_records": valid_records,
        "invalid_records": invalid_records,
        "errors": errors,
    }
    return render(request, "upload_csv.html", context)
