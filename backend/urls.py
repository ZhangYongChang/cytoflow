from django.conf.urls import url, include
import backend.views as views

urlpatterns = [
    # manage specimen object
    url('create_specimen', views.create_specimen),
    url('query_specimenid', views.query_specimenid),
    url('query_specimen_suggest', views.query_specimen_suggest),
    url('delete_specimen', views.delete_specimen),
    # manage specimen files
    url('query_specimen_fcsfiles', views.query_specimen_fcsfiles),
    url('upload_specimen_fcsfiles', views.upload_specimen_fcsfiles),
    url('query_specimen_fcsfile_data', views.query_specimen_fcsfile_data),
    # gate
    url('save_spceiment_fcsfile_gate', views.save_spceiment_fcsfile_gate),
    url('query_fcsfile_gate', views.query_fcsfile_gate),
    # report
    url('gen_report', views.gen_report),
    url('query_report', views.query_report),
    url('cell_stat', views.cell_stat)
]
