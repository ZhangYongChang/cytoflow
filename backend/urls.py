from django.conf.urls import url, include
import backend.views as views

urlpatterns = [
    url('list_flowmetory', views.list_flowmetory, ),
    url('list_directory_tubor', views.list_directory_tubor, ),
    url('get_tubor_scatter', views.get_tubor_scatter, ),
    url('get_tubor_columns', views.get_tubor_columns, ),
    url('get_tubor_fig', views.get_tubor_fig, ),
    url('get_tubor', views.get_tubor, ),
    url('create_patient', views.create_patient, ),
    url('query_specimenno', views.query_specimenno, ),
    url('upload_specimen', views.upload_specimen, ),
    url('create_gate', views.create_gate, ),
    url('gen_report', views.gen_report, ),
]