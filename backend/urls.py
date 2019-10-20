from django.conf.urls import url, include
import backend.views as views

urlpatterns = [
    url('list_flowmetory', views.query_flowmetory, ),
    url('list_directory_tubor', views.list_directory_tubor, ),
    url('get_tubor_scatter', views.get_tubor_scatter, ),
    url('get_tubor_columns', views.get_tubor_columns, ),
    url('get_tubor_fig', views.get_tubor_fig, ),
    url('get_tubor', views.get_tubor, ),
    url('create_specimen', views.create_specimen, ),
    url('query_specimenno', views.query_specimenno, ),
    url('query_specimenid', views.query_specimenid, ),
    url('query_specimen_fcsfilenames',views.query_specimen_fcsfilenames, ),
    url('get_specimen_tubo', views.get_specimen_tubo, ),
    url('upload_specimen', views.upload_specimen, ),
    url('create_gate', views.create_gate, ),
    url('gen_report', views.gen_report, ),
]