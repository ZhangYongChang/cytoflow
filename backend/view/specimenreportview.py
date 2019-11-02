from django.views.decorators.http import require_http_methods
from backend.models.models import (Specimen, SpecimenGate, SpecimenReport, Gate)
from backend.common.config import (get_fcsfilepath, SSC_A, PerCP_A)
from backend.util.pdfreportrender import PdfReportRender
import backend.common.errormgr as em
import fcsparser
import datetime
import numpy
import json
import logging

logger = logging.getLogger('log')


@require_http_methods(["POST"])
def gen_report(request):
    try:
        params = json.loads(request.body)
        specimenid = params['specimenid']
        specimen = Specimen.objects.get(specimenid=specimenid)
        if specimen is None:
            return em.create_fail_response('object not exist', em.FAIL)

        specimengates = SpecimenGate.objects.filter(specimenid=specimenid)
        render = PdfReportRender(specimen, specimengates)
        filename = render.render_report()
        createtime = datetime.datetime.now()
        try:
            hisreport = SpecimenReport.objects.get(specimenid=specimenid)
            hisreport.delete()
        except Exception as e:
            logger.exception(e)

        report = SpecimenReport(
            specimenid=specimenid,
            specimenreportpath=filename,
            createtime=createtime)
        report.save()
        logger.info('report file:' + filename)
        return em.create_sucess_response(report.to_json())
    except Exception as e:
        logger.exception(e)
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def query_report(request):
    try:
        params = json.loads(request.body)
        specimenid = params['specimenid']
        report = SpecimenReport.objects.filter(
            specimenid=specimenid).order_by('createtime')[0]
        return em.create_sucess_response({
            'filename':
                report.specimenreportpath,
            'token':
                datetime.datetime.now()
        })
    except Exception as e:
        logger.exception(e)
        return em.create_fail_response(e, em.FAIL)


# only one fig need stat cell num
@require_http_methods(["POST"])
def cell_stat(request):
    try:
        params = json.loads(request.body)
        filename = params['fcsfilename']
        specimenid = params['specimenid']
        polygons = params['polygongate']
        specimen = Specimen.objects.get(specimenid=specimenid)
        meta, df = fcsparser.parse(
            get_fcsfilepath(specimen.specimendir, filename))
        actual_x = df[SSC_A]
        actual_y = df[PerCP_A]
        gate = Gate()
        gate.load(polygons)
        x = actual_x.values.reshape(actual_x.values.size, 1)
        y = actual_y.values.reshape(actual_y.values.size, 1)
        points = numpy.concatenate((x, y), axis=1)
        result = gate.stat(points)
        result['detail'] = {}
        return em.create_sucess_response(result)
    except Exception as e:
        logger.exception(e)
        return em.create_fail_response(e, em.FAIL)
