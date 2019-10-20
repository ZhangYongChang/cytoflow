from django.conf.urls import url, include
import backend.views as views

urlpatterns = [
  # manage specimen object
  url('create_specimen', views.create_specimen, ),
  url('query_specimenid', views.query_specimenid, ),
  # manage specimen files
  url('query_specimen_fcsfiles',views.query_specimen_fcsfiles, ),
  url('upload_specimen_fcsfiles', views.upload_specimen_fcsfiles, ),
  url('query_specimen_tubo', views.query_specimen_tubo, ),
  # gate
  url('save_spceiment_fcsfile_gate', views.save_spceiment_fcsfile_gate, ),
  # report
  url('gen_report', views.gen_report, ),
  url('query_report', views.query_report, ),
  url('query_specimen_report', views.query_specimen_report),
  url('get_tubor_fig', views.get_tubor_fig, ),
]