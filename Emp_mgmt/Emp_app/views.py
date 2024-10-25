from django.shortcuts import render,redirect
from .models import Signup, Employee,DynamicField,EmployeeFieldValue
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if name and email and password:  
            if Signup.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered.Try another')
                return redirect('signup')
            new_user = Signup.objects.create(username=email,password=password, email=email, name=name)
            new_user.save()
            return redirect('dashboard')  
    return render(request, 'signup.html')

def dashboard(request):
    emp = Employee.objects.all()
    dynamic_fields = DynamicField.objects.all()
    
    employee_data = []
    for employee in emp:
        field_values = EmployeeFieldValue.objects.filter(employee=employee)
        field_values_dict = {field.dynamic_field.field_name: field.field_value for field in field_values}
        
        employee_data.append({
            'employee': employee,
            'dynamic_fields': field_values_dict
        })
    
    return render(request, 'dashboard.html', {'employee_data': employee_data, 'dynamic_fields': dynamic_fields})


def add_dynamic_field(request):
    if request.method == 'POST':
        field_name = request.POST.get('field_name')
        field_type = request.POST.get('field_type')
        
        DynamicField.objects.create(field_name=field_name, field_type=field_type)
        return redirect('dashboard')  

    return HttpResponse('Invalid request.', status=400)

def save_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        employee = Employee.objects.create(email=email, name=name, phone=phone)

        dynamic_field_ids = request.POST.getlist('dynamic_field_ids')  
        dynamic_field_values = [request.POST.get(f'dynamic_fields[{field_id}]') for field_id in dynamic_field_ids]

        print(f'Dynamic Field IDs: {dynamic_field_ids}')
        print(f'Dynamic Field Values: {dynamic_field_values}')
        print(request.POST)  
        for i in range(len(dynamic_field_ids)):
            field_id = dynamic_field_ids[i]
            
            if i < len(dynamic_field_values):
                field_value = dynamic_field_values[i]  
                
                print(f'Processing Dynamic Field ID: {field_id}, Value: {field_value}')
                
                try:
                    dynamic_field = DynamicField.objects.get(id=field_id)
                    EmployeeFieldValue.objects.create(
                        employee=employee,
                        dynamic_field=dynamic_field,
                        field_value=field_value  
                    )
                except DynamicField.DoesNotExist:
                    print(f'DynamicField with ID {field_id} does not exist.')

        return redirect('dashboard')  

    return HttpResponse('Invalid request.', status=400)


