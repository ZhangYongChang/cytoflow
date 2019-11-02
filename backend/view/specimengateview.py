from django.views.decorators.http import require_http_methods
from backend.models.models import SpecimenGate
import backend.common.errormgr as em
import datetime
import json
import logging

logger = logging.getLogger('log')


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

