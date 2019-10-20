from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, StreamingHttpResponse, FileResponse
from backend.models import SpecimenGate
from backend.models import Specimen
from backend.models import Gate
import backend.genreportools as genreportools
import matplotlib.pyplot as plt
import backend.errormgr as em
import matplotlib
import fcsparser
import datetime
import base64
import numpy
import json
import uuid
import os
import re
import io
import logging

matplotlib.use('agg')

logger = logging.getLogger('log')
DATASET_ROOTDIR = 'datasets'

CLASSFITY_X = 'SSC-A'
CLASSFITY_Y = 'PerCP-A'


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
        os.mkdir(os.path.join(DATASET_ROOTDIR, specimen.specimendir))
        return em.create_sucess_response(specimen.to_json())
    except Exception as e:
        logger.error(e)
        return em.create_fail_response(e, em.CREATE_SPECIMEN_FAILED)


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
        logger.error(e)
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
        logger.error(e)
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
            filename for filename in os.listdir(
                os.path.join(DATASET_ROOTDIR, querysubdir))
            if re.search('.fcs$', filename)
        ]
        return em.create_sucess_response({'fcsfilenames': fcsfilenames})
    except Exception as e:
        logger.error(e)
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def get_tubor_columns(request):
    params = json.loads(request.body)
    filename = params['filename']
    querysubdir = params['querysubdir']
    response = {}
    try:
        meta, df = fcsparser.parse(
            os.path.join(DATASET_ROOTDIR, querysubdir, filename))
        return em.create_sucess_response({
            'filename':
            filename,
            'querysubdir':
            querysubdir,
            'columns':
            numpy.array(df.columns).tolist()
        })
    except Exception as e:
        logger.error(e)
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def get_tubor_scatter(request):
    try:
        params = json.loads(request.body)
        fcsfilename = params['fcsfilename']
        querysubdir = params['querysubdir']
        x = params['xaxis']
        y = params['yaxis']
        meta, df = fcsparser.parse(
            os.path.join(DATASET_ROOTDIR, querysubdir, fcsfilename))
        return em.create_sucess_response({
            x: df[x].tolist(),
            y: df[y].tolist()
        })
    except Exception as e:
        logger.error(e)
        return em.create_fail_response(e, em.FAIL)


# query fcs cols point ok
@require_http_methods(["POST"])
def get_tubor(request):
    try:
        params = json.loads(request.body)
        filename = params['filename']
        querysubdir = params['querysubdir']
        cols = {}
        meta, df = fcsparser.parse(
            os.path.join(DATASET_ROOTDIR, querysubdir, filename))
        for col in numpy.array(df.columns).tolist():
            cols[col] = df[col].tolist()
        cols['filename'] = filename
        cols['querysubdir'] = querysubdir
        return em.create_sucess_response(
            dict({
                'filename': filename,
                'querysubdir': querysubdir
            }, **cols))
    except Exception as e:
        logger.error(e)
        return em.create_fail_response(e, em.FAIL)


# query fcs cols point ok
@require_http_methods(["POST"])
def query_specimen_tubo(request):
    try:
        params = json.loads(request.body)
        filename = params['filename']
        specimenid = params['specimenid']
        specimen = Specimen.objects.get(specimenid=specimenid)
        if specimen is None:
            logger.error('param vaild')

        querysubdir = specimen.specimendir
        cols = {}
        meta, df = fcsparser.parse(
            os.path.join(DATASET_ROOTDIR, querysubdir, filename))
        for col in numpy.array(df.columns).tolist():
            cols[col] = df[col].tolist()
        cols['filename'] = filename
        cols['specimenid'] = specimenid
        return em.create_sucess_response(cols)
    except Exception as e:
        logger.error(e)
        return em.create_fail_response(e, em.FAIL)


def axis_prop(ax, xaxis, yaxis, title, xtitle, ytitle):
    ax.set_xscale(xaxis)
    ax.set_yscale(yaxis)
    ax.set_title(title)
    ax.set_xlabel(xtitle)
    ax.set_ylabel(ytitle)


def gen_tubor_fig(fullpath):
    color = ['tab:red']
    meta, df = fcsparser.parse(fullpath)
    fig, ((ax11, ax12, ax13), (ax21, ax22, ax23), (ax31, ax32,
                                                   ax33)) = plt.subplots(
                                                       3,
                                                       3,
                                                       figsize=(12.0, 12.0))
    ax11.scatter(
        df['FSC-A'] / 1000, df['SSC-A'] / 1000, s=2, c=color, alpha=0.5)
    axis_prop(ax11, 'linear', 'linear', "", "FSC-A", "SSC-A")

    ax12.scatter(df['SSC-A'] / 1000, df['PerCP-A'], s=2, c=color, alpha=0.5)
    axis_prop(ax12, "linear", "log", "", "SSC-A", "PerCP-A")
    ax12.set_ylim(10**1, 10**5)

    ax13.scatter(df['FITC-A'], df['PE-A'], s=2, c=color, alpha=0.5)
    axis_prop(ax13, "log", "log", "", "FITC-A", "PE-A")
    ax13.set_xlim(10**1, 10**5)
    ax13.set_ylim(10**1, 10**5)

    ax21.scatter(df['FITC-A'], df['PE-Cy7-A'], s=2, c=color, alpha=0.5)
    axis_prop(ax21, "log", "log", "", "FITC-A", "PE-Cy7-A")
    ax21.set_xlim(10**1, 10**5)
    ax21.set_ylim(10**1, 10**5)

    ax22.scatter(df['APC-A'], df['APC-Cy7-A'], s=2, c=color, alpha=0.5)
    axis_prop(ax22, "log", "log", "", "FITC-A", "PE-Cy7-A")
    ax22.set_xlim(10**1, 10**5)
    ax22.set_ylim(10**1, 10**5)

    ax23.scatter(df['FITC-A'], df['APC-A'], s=2, c=color, alpha=0.5)
    axis_prop(ax23, "log", "log", "", "FITC-A", "APC-A")
    ax23.set_xlim(10**1, 10**5)
    ax23.set_ylim(10**1, 10**5)

    ax31.scatter(df['PE-Cy7-A'], df['APC-Cy7-A'], s=2, c=color, alpha=0.5)
    axis_prop(ax31, "log", "log", "", "PE-Cy7-A", "APC-Cy7-A")
    ax31.set_xlim(10**1, 10**5)
    ax31.set_ylim(10**1, 10**5)

    ax32.scatter(df['PE-A'], df['PE-Cy7-A'], s=2, c=color, alpha=0.5)
    axis_prop(ax32, "log", "log", "", "PE-A", "PE-Cy7-A")
    ax32.set_xlim(10**1, 10**5)
    ax32.set_ylim(10**1, 10**5)

    imagebuf = io.BytesIO()
    fig.savefig(imagebuf)
    figbytes = base64.b64encode(imagebuf.getvalue())
    imagebuf.close()
    return figbytes.decode()


@require_http_methods(["POST"])
def get_tubor_fig(request):
    try:
        params = json.loads(request.body)
        filename = params['filename']
        querysubdir = params['querysubdir']
        return em.create_sucess_response({
            'filename':
            filename,
            'querysubdir':
            querysubdir,
            'img':
            gen_tubor_fig(
                os.path.join(DATASET_ROOTDIR, querysubdir, filename))
        })
    except Exception as e:
        logger.error(e)
        return em.create_fail_response(e, em.FAIL)


# query specimen by no ok
@require_http_methods(["POST"])
def query_specimenno(request):
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
        logger.error(e)
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def query_all_specimen(request):
    try:
        params = json.loads(request.body)
        specimens = Specimen.objects.all()
        result = []
        for specimen in specimens:
            result.append({
                'name': specimen['name'],
                'specimendir': specimen['specimendir']
            })
    except Exception as e:
        logger.error(e)
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
        specimenfilepath = os.path.join(DATASET_ROOTDIR, storgedir, file.name)
        if not file:
            return em.create_fail_response('no files for upload', em.FAIL)

        destination = open(specimenfilepath, 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        return em.create_success_null()
    except Exception as e:
        logger.error(e)
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def save_spceiment_fcsfile_gate(request):
    try:
        params = json.loads(request.body)
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
        logger.error(e)
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
        logger.error(e)
        return em.create_fail_response(e, em.FAIL)


# only one fig need stat cell num
@require_http_methods(["POST"])
def cell_stat(request):
    try:
        params = json.loads(request.body)
        filename = params['fcsfilename']
        specimenid = params['specimenid']
        polygons = params['polygons']
        specimen = Specimen.objects.get(specimenid=specimenid)
        meta, df = fcsparser.parse(
            os.path.join(DATASET_ROOTDIR, specimen.specimendir, filename))

        points = []
        for i, element in enumerate(df[CLASSFITY_X]):
            points.append([element, df[CLASSFITY_Y][i]])

        gate = Gate(CLASSFITY_X, CLASSFITY_Y, polygons)
        result = gate.stat(points)
        return em.create_sucess_response(result)
    except Exception as e:
        logger.error(e)
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
        return em.create_sucess_response(
            genreportools.render_report(DATASET_ROOTDIR, specimen,
                                        specimengates))
    except Exception as e:
        logger.error(e)
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def query_report(request):
    try:
        params = json.loads(request.body)
        specimenid = params['specimenid']
        specimen = Specimen.objects.get(specimenid=specimenid)
        if specimen is None:
            return em.create_fail_response('file not exist', em.FAIL)
        
        filepath = os.path.join(genreportools.REPORT_TEMP_DIR, '6a9ebc94-4b8c-4021-aed5-832897c5876c.pdf')
        file = open(filepath, 'rb')
        response = FileResponse(file)
        response['Content-Type']='application/pdf'
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition']='attachment;filename="report.pdf"'
        return response
    except Exception as e:
        logger.error(e)
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def query_specimen_report(request):
    pass
