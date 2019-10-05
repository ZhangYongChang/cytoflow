from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
import os
import json
import re
import fcsparser
import numpy

rootdir = '/mnt/dataset'
# Create your views here.
@require_http_methods(["POST"])
def list_flowmetory(request):
    response = {}
    try:
        response['subdirs']  = [file for file in os.listdir(rootdir) if os.path.isdir(rootdir + '/' + file)]
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["POST"])
def list_directory_tubor(request):
    params = json.loads(request.body)
    subdir = params['subdir']
    response = {}
    try:
        tubors = [file for file in os.listdir(rootdir + '/' + subdir) if re.search('.fcs$', file)]
        response['subdir'] = subdir
        response['files'] = tubors
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["POST"])
def get_tubor_columns(request):
    params = json.loads(request.body)
    tuborname = params['tuborname']
    tuborpath = params['tuborpath']
    response = {}
    try:
        response['tuborname'] = tuborname
        response['tuborpath'] = tuborpath
        meta, df = fcsparser.parse(rootdir + '/' + tuborpath)
        response['columns'] = numpy.array(df.columns).tolist()
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["POST"])
def get_tubor_scatter(request):
    params = json.loads(request.body)
    tuborname = params['tuborname']
    tuborpath = params['tuborpath']
    xaxis = params['xaxis']
    yaxis = params['yaxis']
    response = {}
    try:
        response['tuborname'] = tuborname
        response['tuborpath'] = tuborpath
        meta, df = fcsparser.parse(rootdir + '/' + tuborpath)
        response[xaxis] = df[xaxis].tolist()
        response[yaxis] = df[yaxis].tolist()
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["POST"])
def get_tubor(request):
    params = json.loads(request.body)
    filename = params['filename']
    subdir = params['subdir']
    response = {}
    try:
        response['filename'] = filename
        response['subdir'] = subdir
        meta, df = fcsparser.parse(rootdir + '/' + subdir + '/' + filename)
        for col in numpy.array(df.columns).tolist():
            response[col] = df[col].tolist()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
