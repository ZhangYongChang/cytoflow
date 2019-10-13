from django.views.decorators.http import require_http_methods
from backend.models import Specimen
import matplotlib.pyplot as plt
import backend.errormgr as em
import matplotlib
import fcsparser
import base64
import numpy
import json
import uuid
import os
import re
import io


matplotlib.use('agg')

DATASET_ROOTDIR = 'datasets'


# Create your views here.
@require_http_methods(["POST"])
def list_flowmetory(request):
    try:
        subdir = [file for file in os.listdir(
            DATASET_ROOTDIR) if os.path.isdir(os.path.join(DATASET_ROOTDIR, file))]
        return em.create_sucess_response(subdir)
    except Exception as e:
        return em.create_fail_response(e, em.QUERY_SPECIMEN_FAILED)


@require_http_methods(["POST"])
def list_directory_tubor(request):
    params = json.loads(request.body)
    querysubdir = params['querysubdir']
    response = {}
    try:
        fcsfilenames = [filename for filename in os.listdir(
            os.path.join(DATASET_ROOTDIR, querysubdir)) if re.search('.fcs$', filename)]
        return em.create_sucess_response({
            'querysubdir': querysubdir,
            'fcsfilenames': fcsfilenames
        })
    except Exception as e:
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
            'filename': filename,
            'querysubdir': querysubdir,
            'columns': numpy.array(df.columns).tolist()
        })
    except Exception as e:
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def get_tubor_scatter(request):
    try:
        params = json.loads(request.body)
        fcsfilename = params['fcsfilename']
        querysubdir = params['querysubdir']
        x = params['xaxis']
        y = params['yaxis']
        meta, df = fcsparser.parse(os.path.join(
            DATASET_ROOTDIR, querysubdir, fcsfilename))
        return em.create_sucess_response({
            x: df[x].tolist(),
            y: df[y].tolist()
        })
    except Exception as e:
        return em.create_fail_response(e, em.FAIL)


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
        return em.create_sucess_response(dict({
            'filename': filename,
            'querysubdir': querysubdir
        }, **cols))
    except Exception as e:
        return em.create_fail_response(e, em.FAIL)


def forward(x):
    return x / 1000


def inverse(x):
    return x * 1000


def axis_prop(ax, xaxis, yaxis, title, xtitle, ytitle):
    ax.set_xscale(xaxis)
    ax.set_yscale(yaxis)
    ax.set_title(title)
    ax.set_xlabel(xtitle)
    ax.set_ylabel(ytitle)


def gen_tubor_fig(fullpath):
    color = ['tab:red']
    meta, df = fcsparser.parse(fullpath)
    fig, ((ax11, ax12, ax13), (ax21, ax22, ax23), (ax31, ax32, ax33)
          ) = plt.subplots(3, 3,  figsize=(12.0, 12.0))
    ax11.scatter(df['FSC-A'] / 1000, df['SSC-A'] /
                 1000, s=2, c=color, alpha=0.5)
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
            'filename': filename,
            'querysubdir': querysubdir,
            'img': gen_tubor_fig(os.path.join(DATASET_ROOTDIR, querysubdir, filename))
        })
    except Exception as e:
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def create_patient(request):
    try:
        params = json.loads(request.body)
        randomdir = str(uuid.uuid4())
        specimen = Specimen(name=params['name'], sex=params['sex'],
                            age=params['age'], specimenno=params['specimenno'],
                            hospital=params['hospital'], bedno=params['bedno'], doctor=params['doctor'],
                            specimentype=params['specimentype'], caseno=params['caseno'],
                            collecttime=params['collecttime'], recvtime=params['recvtime'], specimendir=randomdir)
        specimen.save()
        return em.create_sucess_response(specimen.to_json())
    except Exception as e:
        return em.create_fail_response(e, em.CREATE_SPECIMEN_FAILED)


@require_http_methods(["POST"])
def query_specimen_by_name(request):
    try:
        params = json.loads(request.body)
        name = params['name']
        specimens = Specimen.objects.filter(
            name__icontains=name).values('name', 'specimendir')
        result = []
        for specimen in specimens:
            result.append({'name': specimen['name'], 'specimendir': specimen['specimendir']})
        return em.create_sucess_response(result)
    except Exception as e:
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def query_all_specimen(request):
    try:
        params = json.load(request.body)
        specimens = Specimen.objects.all()
        result = []
        for specimen in specimens:
            result.append({'name': specimen['name'], 'specimendir': specimen['specimendir']})
    except Exception as e:
        return em.create_fail_response(e, em.FAIL)


# input file.name
#   specimendir:filename
@require_http_methods(["POST"])
def upload_specimen(request):
    try:
        file = request.FILES.get("file", None)
        filemeta = file.name
        fileitems = filemeta.split(':')
        if len(fileitems) != 2:
            return em.create_fail_response('vailed param', em.PARAM_FAILED)

        specimenfilepath = os.path.join(
            DATASET_ROOTDIR, fileitems[0], file.name)
        if not file:
            return em.create_fail_response('no files for upload', em.FAIL)

        destination = open(specimenfilepath, 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        return em.create_success_null()
    except Exception as e:
        return em.create_fail_response(e, em.FAIL)


@require_http_methods(["POST"])
def create_gate(request):
    try:
        params = json.load(request.body)
    except Exception as e:
        return em.create_fail_response(e, em.FAIL)
