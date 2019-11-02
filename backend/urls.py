from django.conf.urls import url, include
import backend.view.specimenreportview as specimenreportview
import backend.view.specimenview as specimenview
import backend.view.specimenfcsfileview as specimenfcsfileview
import backend.view.specimengateview as specimengateview

urlpatterns = [
    # manage specimen object
    url('create_specimen', specimenview.create_specimen),
    url('query_specimenid', specimenview.query_specimenid),
    url('query_specimen_suggest', specimenview.query_specimen_suggest),
    url('delete_specimen', specimenview.delete_specimen),
    # manage specimen files
    url('query_specimen_fcsfiles', specimenfcsfileview.query_specimen_fcsfiles),
    url('upload_specimen_fcsfiles', specimenfcsfileview.upload_specimen_fcsfiles),
    url('query_specimen_fcsfile_data', specimenfcsfileview.query_specimen_fcsfile_data),
    # speciment files gate
    url('save_spceiment_fcsfile_gate', specimengateview.save_spceiment_fcsfile_gate),
    url('query_fcsfile_gate', specimengateview.query_fcsfile_gate),
    # report
    url('gen_report', specimenreportview.gen_report),
    url('query_report', specimenreportview.query_report),
    url('cell_stat', specimenreportview.cell_stat)
]
