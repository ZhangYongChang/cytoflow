from django.http import JsonResponse

SUCCESS = 0
FAIL = 1
PARAM_FAILED = 2

CREATE_SPECIMEN_FAILED = 10001
QUERY_SPECIMEN_FAILED = 10002


def create_fail_response(msg, code):
    return JsonResponse({'msg': str(msg), 'error_num': code})


def create_sucess_response(data):
    return JsonResponse({'data': data, 'msg': 'success', 'error_num': 0})


def create_success_null():
    return JsonResponse({'msg': 'success', 'error_num': 0})
