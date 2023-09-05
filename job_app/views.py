from django.shortcuts import render, redirect,get_object_or_404
from .models import Job, Category
from .forms import JobForm
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import EditJobForm
from django.http import HttpResponseForbidden
from .models import ContactMessage
from django.contrib import messages


@login_required
def user_jobs(request):
    user_jobs = Job.objects.filter(user=request.user)
    return render(request, 'user/user_jobs.html', {'user_jobs': user_jobs})

class CustomRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('login')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})


def index(request):
    latest_jobs = Job.objects.order_by('-created_at')[:10]
    categories = Category.objects.all()
    marketing_job = Job.objects.all().filter(category__name="Marketing").order_by('-created_at')[1:6]
    business_job = Job.objects.all().filter(category__name="Business & Development").order_by('-created_at')[1:6]
    sales_job = Job.objects.all().filter(category__name="Sales & Communication").order_by('-created_at')[1:6]
    design_job = Job.objects.all().filter(category__name="Design & Creative").order_by('-created_at')[1:6]
    customer_job = Job.objects.all().filter(category__name="Customer Service").order_by('-created_at')[1:6]
    software_job = Job.objects.all().filter(category__name="Software Engineering").order_by('-created_at')[1:6]
    teachingedu_job = Job.objects.all().filter(category__name="Teaching & Education").order_by('-created_at')[1:6]
    human_job = Job.objects.all().filter(category__name="Human Resource").order_by('-created_at')[1:6]

    context = {
        'latest_jobs':latest_jobs,
        'categories':categories,
        'marketing_job':marketing_job,
        'business_job':business_job,
        'sales_job':sales_job,
        'design_job':design_job,
        'customer_job':customer_job,
        'software_job':software_job,
        'teachingedu_job':teachingedu_job,
        'human_job':human_job,

    }
    return render(request, 'home/index.html', context=context)

def view404(request):
    return render(request, "home/404.html")

def about(request):
    return render(request, "home/about.html")

def category(request):
    return render(request, "home/category.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        contact_message = ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        contact_message.save()

        messages.success(request, 'Your message has been successfully sent.')
        return redirect('contact')

    return render(request, 'home/contact.html')


@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if job.user == request.user:
        if request.method == 'POST':
            form = EditJobForm(request.POST, instance=job)
            if form.is_valid():
                form.save()
                return redirect('user_jobs')
        else:
            form = EditJobForm(instance=job)
        
        context = {
            'job': job,
            'form': form,  # Передаем форму в контекст для использования в шаблоне
        }
        return render(request, 'user/edit_job.html', context)
    else:
        return HttpResponseForbidden("You are not allowed to edit this job.")

@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if job.user == request.user:
        if request.method == 'POST':
            job.delete()
            return redirect('user_jobs')
        else:
            context = {
                'job': job,
            }
            return render(request, 'user/delete_job.html', context)
    else:
        return HttpResponseForbidden("You are not allowed to delete this job.")






def testimonial(request):
    return render(request, "home/testimonial.html")



@login_required  
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)  
            job.user = request.user  
            job.save()  
            return redirect('user_jobs')  
    else:
        form = JobForm()
    context = {
        'form': form,
    }
    return render(request, 'home/postjob.html', context)

def custom_logout(request):
    logout(request)
    return redirect('index')

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'home/job-list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'home/job-detail.html', {'job': job})



class MarketingView(ListView):
    model = Job
    template_name = 'home/marketing.html'
    context_object_name = 'marketing_job'

    def get_queryset(self):
        job = super().get_queryset().filter(category__name='Marketing')
        return job
    
class CustomerServiceView(ListView):
    model = Job
    template_name = 'home/customer.html'
    context_object_name = 'customer_job_list'

    def get_queryset(self):
        job = super().get_queryset().filter(category__name='Customer Service')
        return job
    
class HumanResourceView(ListView):
    model = Job
    template_name = 'home/human.html'
    context_object_name = 'human_job'

    def get_queryset(self):
        job = super().get_queryset().filter(category__name='Human Resource')
        return job    
    
class SoftwareEngineeringView(ListView):
    model = Job
    template_name = 'home/software.html'
    context_object_name = 'software_job'

    def get_queryset(self):
        job = super().get_queryset().filter(category__name='Software Engineering')
        return job    
    
class BusinessDevelopmentView(ListView):
    model = Job
    template_name = 'home/business.html'
    context_object_name = 'business_job'

    def get_queryset(self):
        job = super().get_queryset().filter(category__name='Business Development')
        return job    
    
class SalesCommunicationView(ListView):
    model = Job
    template_name = 'home/sales.html'
    context_object_name = 'sales_job'

    def get_queryset(self):
        job = super().get_queryset().filter(category__name='Sales & Communication')
        return job    
    
class TeachingEduView(ListView):
    model = Job
    template_name = 'home/teachingedu.html'
    context_object_name = 'teachingedu_job'

    def get_queryset(self):
        job = super().get_queryset().filter(category__name='Teaching & Education')
        return job    
    
class DesignCreativeView(ListView):
    model = Job
    template_name = 'home/design.html'
    context_object_name = 'design_job'

    def get_queryset(self):
        job = super().get_queryset().filter(category__name='Design & Creative')
        return job    
    

class SearchResultList(ListView):
    model = Job
    template_name = 'home/search_result.html'
    context_object_name = 'all_jobs'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Job.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )    
