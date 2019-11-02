from django.views.decorators.http import require_http_methods
from backend.models.models import Specimen
from backend.common.config import (get_fcsfiledir, get_fcsfilepath)
import backend.common.errormgr as em
import fcsparser
import numpy
import json
import os
import logging

logger = logging.getLogger('log')


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