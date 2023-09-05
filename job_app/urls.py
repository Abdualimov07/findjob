from django.urls import path
from .views import index,view404,about,contact,category,job_detail,job_list,testimonial,post_job
from .views import MarketingView,BusinessDevelopmentView,SalesCommunicationView,SoftwareEngineeringView,CustomerServiceView,TeachingEduView,HumanResourceView,DesignCreativeView,SearchResultList
from.views import user_jobs,user_login,edit_job,delete_job,CustomRegistrationView
from .views import custom_logout
from django.views.i18n import set_language

urlpatterns = [
    path("", index, name='index'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
    path("view404/", view404, name='view404'),
    path("category/", category, name='category'),
    path('jobs/<int:job_id>/', job_detail, name='job_detail'),
    path("job_list/", job_list, name='job_list'),
    path("testimonial/", testimonial, name='testimonial'),
    path("postjob/", post_job, name='postjob'),
    path("marketing/", MarketingView.as_view(), name='marketing'),
    path("business/", BusinessDevelopmentView.as_view(), name='business'),
    path("sales/", SalesCommunicationView.as_view(), name='sales'),
    path("software/", SoftwareEngineeringView.as_view(), name='software'),
    path("customer/", CustomerServiceView.as_view(), name='customer'),
    path("human/", HumanResourceView.as_view(), name='human'),
    path("teachingedu/", TeachingEduView.as_view(), name='teachingedu'),
    path("design/", DesignCreativeView.as_view(), name='design'),
    path('searchresult/', SearchResultList.as_view(), name='search_result'),
    path("register", CustomRegistrationView.as_view(), name='register'),
    path("login", user_login, name='login'),
    path("user_jobs", user_jobs, name='user_jobs'),
    path("edit_job/<int:job_id>/", edit_job, name='edit_job'),
    path("delete_job<int:job_id>/", delete_job, name='delete_job'),
    path('logout/', custom_logout, name='logout'),
    path('set_language/', set_language, name='set_language'),

]