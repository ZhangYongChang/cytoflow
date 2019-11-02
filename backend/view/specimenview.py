from django.views.decorators.http import require_http_methods
from backend.models.models import Specimen
from backend.common.config import get_fcsfiledir
import backend.common.errormgr as em
import json
import uuid
import os
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
