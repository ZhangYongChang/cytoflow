from django.views.decorators.http import require_http_methods
from backend.models import (Specimen, SpecimenGate, SpecimenReport, Gate)
from backend.config import (get_fcsfiledir, get_fcsfilepath, SSC_A, PerCP_A)
from backend.pdfreportrender import PdfReportRender
import backend.errormgr as em
import fcsparser
import datetime
import numpy
import json
import uuid
import os
import re
import logging

logger = logging.getLogger('log')


@require_http_methods(["POST"])
def create_specimen(request):
    try:
        params = json.loads(request.body)
        randomdir = str(uuid.uuid4())
        specimen = Specimen(
            name=params['name'],
            sex=params['sex'],
            age=params['age'],
            specimenno=params['specimenno'],
            hospital=params['hospital'],
            department=params['department'],
            bedno=params['bedno'],
            doctor=params['doctor'],
            specimentype=params['specimentype'],
            caseno=params['caseno'],
            collecttime=params['collecttime'],
            recvtime=params['recvtime'],
            specimendir=randomdir)
        specimen.save()
        os.mkdir(get_fcsfiledir(specimen.specimendir))
        return em.create_sucess_response(specimen.to_json())
    except Exception as e:
        logger.exception(e)
        return em.create_fail_response(e, em.CREATE_SPECIMEN_FAILED)


@require_http_methods(["POST"])
def delete_specimen(request):
    try:
        params = json.loads(request.body)
        specimen = Specimen.objects.get(specimenid=params['specimenid'])
        specimen.delete()
        return em.create_success_null()
    except Exception as e:
        logger.exception(e)
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def query_specimenid(request):
    try:
        params = json.loads(request.body)
        specimenno = params['specimenno']
        specimens = Specimen.objects.filter(specimenno__contains=specimenno)
        result = []
        for specimen in specimens:
            result.append({
                'specimenno': specimen.specimenno,
                'specimendir': specimen.specimendir,
                'specimenid': specimen.specimenid
            })
        return em.create_sucess_response(result)
    except Exception as e:
        logger.exception(e)
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def query_specimen_suggest(request):
    try:
        specimens = Specimen.objects.all()[:20]
        result = []
        for specimen in specimens:
            result.append(specimen.to_json())
        return em.create_sucess_response(result)
    except Exception as e:
        logger.exception(e)
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def query_specimen_fcsfiles(request):
    try:
        params = json.loads(request.body)
        specimenid = params['specimenid']
        specimen = Specimen.objects.get(specimenid=specimenid)
        querysubdir = specimen.specimendir
        response = {}
        fcsfilenames = [
            filename for filename in os.listdir(get_fcsfiledir(querysubdir))
            if re.search('.fcs$', filename)
        ]
        return em.create_sucess_response({'fcsfilenames': fcsfilenames})
    except Exception as e:
        logger.exception(e)
        return em.create_fail_response(e, em.FAIL)


# upload specimen file ok
@require_http_methods(["POST"])
def upload_specimen_fcsfiles(request):
    try:
        file = request.FILES.get("file", None)
        filemeta = file.name
        specimenid = int(request.POST['specimenid'])
        specimen = Specimen.objects.get(specimenid=specimenid)
        if specimen is None:
            return em.create_fail_response('specimen is not exist', em.FAIL)

        storgedir = specimen.specimendir
        specimenfilepath = get_fcsfilepath(storgedir, file.name)
        if not file:
            return em.create_fail_response('no files for upload', em.FAIL)

        destination = open(specimenfilepath, 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        return em.create_success_null()
    except Exception as e:
        logger.exception(e)
        return em.create_fail_response(e, em.FAIL)


# query fcs cols point ok
@require_http_methods(["POST"])
def query_specimen_fcsfile_data(request):
    try:
        params = json.loads(request.body)
        filename = params['filename']
        specimenid = params['specimenid']
        specimen = Specimen.objects.get(specimenid=specimenid)
        if specimen is None:
            logger.error('param vaild')

        querysubdir = specimen.specimendir
        cols = {}
        meta, df = fcsparser.parse(get_fcsfilepath(querysubdir, filename))
        for col in numpy.array(df.columns).tolist():
            cols[col] = df[col].tolist()
        cols['filename'] = filename
        cols['specimenid'] = specimenid
        return em.create_sucess_response(cols)
    except Exception as e:
        logger.exception(e)
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def save_spceiment_fcsfile_gate(request):
    try:
        params = json.loads(request.body)
        # delete history gate
        hisgates = SpecimenGate.objects.filter(specimenid=params['specimenid'],
                                               fcsfilename=params['fcsfilename'],
                                               gatetype=params['gatetype'])
        if hisgates is not None:
            hisgates.delete()
            logger.info("delete history gate success")
        
        now_time = datetime.datetime.now()
        gate = SpecimenGate(
            specimenid=params['specimenid'],
            fcsfilename=params['fcsfilename'],
            gates=json.dumps(params['gates']),
            gatetype=params['gatetype'],
            createtime=now_time,
            modifytime=now_time)
        gate.save()
        return em.create_sucess_response(gate.to_json())
    except Exception as e:
        logger.exception(e)
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def query_gate(request):
    try:
        params = json.loads(request.body)
        specimenid = params['specimenid']
        gates = SpecimenGate.objects.get(specimenid=specimenid)
        result = []
        for gate in gates:
            result.append(gate.to_json())
        return em.create_sucess_response(result)
    except Exception as e:
        logger.exception(e)
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def query_fcsfile_gate(request):
    try:
        params = json.loads(request.body)
        specimenid = params['specimenid']
        fcsfilename = params['fcsfilename']
        gates = SpecimenGate.objects.filter(
            specimenid=specimenid, fcsfilename=fcsfilename)
        result = []
        for gate in gates:
            result.append(gate.to_json())
        return em.create_sucess_response(result)
    except Exception as e:
        logger.exception(e)
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def delete_gate(request):
    try:
        params = json.loads(request.body)
        gates = SpecimenGate.objects.filter(specimenid=params['specimenid'], fcsfilename=params['fcsfilename'],
                                            gatetype=params['gatetype'])
        if gates is not None:
            gates.delete()
        return em.create_success_null()
    except Exception as e:
        logger.exception(e)
        return em.create_fail_response(e, em.FAIL)


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
