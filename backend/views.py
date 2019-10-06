from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
import os
import json
import re
import fcsparser
import numpy
import io
import base64
import matplotlib
matplotlib.use('agg')
from matplotlib.mlab import bivariate_normal
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.multiarray import arange

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
    fig, ((ax11, ax12, ax13), (ax21, ax22, ax23), (ax31, ax32, ax33)) = plt.subplots(3, 3,  figsize=(12.0 , 12.0))
    ax11.scatter(df['FSC-A'] / 1000, df['SSC-A'] / 1000, s=4, c=color, alpha=0.5)
    axis_prop(ax11, 'linear', 'linear', "", "FSC-A", "SSC-A")

    ax12.scatter(df['SSC-A'] / 1000, df['PerCP-A'], s=4, c=color, alpha=0.5)
    axis_prop(ax12, "linear", "log", "", "SSC-A", "PerCP-A")
    ax12.set_ylim(10**1, 10**5)

    ax13.scatter(df['FITC-A'], df['PE-A'], s=4, c=color, alpha=0.5)
    axis_prop(ax13, "log", "log", "", "FITC-A", "PE-A")
    ax13.set_xlim(10**1, 10**5)
    ax13.set_ylim(10**1, 10**5)

    ax21.scatter(df['FITC-A'], df['PE-Cy7-A'], s=4, c=color, alpha=0.5)
    axis_prop(ax21, "log", "log", "", "FITC-A", "PE-Cy7-A")
    ax21.set_xlim(10**1, 10**5)
    ax21.set_ylim(10**1, 10**5)

    ax22.scatter(df['APC-A'], df['APC-Cy7-A'], s=4, c=color, alpha=0.5)
    axis_prop(ax22, "log", "log", "", "FITC-A", "PE-Cy7-A")
    ax22.set_xlim(10**1, 10**5)
    ax22.set_ylim(10**1, 10**5)

    ax23.scatter(df['FITC-A'], df['APC-A'], s=4, c=color, alpha=0.5)
    axis_prop(ax23, "log", "log", "", "FITC-A", "APC-A")
    ax23.set_xlim(10**1, 10**5)
    ax23.set_ylim(10**1, 10**5)

    ax31.scatter(df['PE-Cy7-A'], df['APC-Cy7-A'], s=4, c=color, alpha=0.5)
    axis_prop(ax31, "log", "log", "", "PE-Cy7-A", "APC-Cy7-A")
    ax31.set_xlim(10**1, 10**5)
    ax31.set_ylim(10**1, 10**5)

    ax32.scatter(df['PE-A'], df['PE-Cy7-A'], s=4, c=color, alpha=0.5)
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
    params = json.loads(request.body)
    filename = params['filename']
    subdir = params['subdir']
    response = {}
    try:
        response['filename'] = filename
        response['subdir'] = subdir
        fullpath = rootdir + '/' + subdir + '/' + filename
        response['img'] = gen_tubor_fig(fullpath)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
