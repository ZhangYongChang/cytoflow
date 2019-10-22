from backend.reporttemplate import REPORT_TEMPLATE
from backend.models import Gate
from jinja2 import Template
import matplotlib.pyplot as plt
import backend.errormgr as em
import matplotlib
import numpy
import os
import json
import uuid
import pdfkit
import logging
import fcsparser
import io
import base64

logger = logging.getLogger('log')

REPORT_TEMP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_TEMP_DIR = os.path.join(REPORT_TEMP_DIR, "tmp")


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


class DrawHelp(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = ['tab:red']
        self.imgs = []
        self.fig, self.ax = plt.subplots(row, col, figsize=(12.0, 12.0))
        self.count = 0

    def new_plot(self):
        self.copy_last_plot()

    def copy_last_plot(self):
        imagebuf = io.BytesIO()
        self.fig.savefig(imagebuf)
        figbytes = base64.b64encode(imagebuf.getvalue())
        imagebuf.close()
        self.imgs.append(bytes.decode(figbytes))
        self.fig, self.ax = plt.subplots(
            self.row, self.col, figsize=(12.0, 12.0))
        self.count = 0

    def draw_normal_gate(self, filename, gate, df):
        i = int(self.count / self.col)
        j = self.count % self.col
        draw_ax = self.ax[i][j]
        if gate['xaxis'] == 'FSC-A' and gate['yaxis'] == 'SSC-A':
            x = df['FSC-A'] / 1000
            y = df['SSC-A'] / 1000
            draw_ax.scatter(x, y, s=2, c=self.color, alpha=0.5)
            draw_ax.hlines(gate['point'][1] / 1000, 0, 250, color="black")
            draw_ax.vlines(gate['point'][0] / 1000, 0, 250, color="black")
            axis_prop(draw_ax, 'linear', 'linear', "", "FSC-A", "SSC-A")
        if gate['xaxis'] == 'FITC-A' and gate['yaxis'] == 'PE-A':
            draw_ax.scatter(
                df['FITC-A'], df['PE-A'], s=2, c=self.color, alpha=0.5)
            axis_prop(draw_ax, "log", "log", "", "FITC-A", "PE-A")
            draw_ax.set_xlim(10**1, 10**5)
            draw_ax.set_ylim(10**1, 10**5)
            draw_ax.hlines(gate['point'][1], 10**1, 10**5, color="black")
            draw_ax.vlines(gate['point'][0], 10**1, 10**5, color="black")
        if gate['xaxis'] == 'FITC-A' and gate['yaxis'] == 'PE-Cy7-A':
            draw_ax.scatter(
                df['FITC-A'], df['PE-Cy7-A'], s=2, c=self.color, alpha=0.5)
            axis_prop(draw_ax, "log", "log", "", "FITC-A", "PE-Cy7-A")
            draw_ax.set_xlim(10**1, 10**5)
            draw_ax.set_ylim(10**1, 10**5)
            draw_ax.hlines(gate['point'][1], 10**1, 10**5, color="black")
            draw_ax.vlines(gate['point'][0], 10**1, 10**5, color="black")
        if gate['xaxis'] == 'APC-A' and gate['yaxis'] == 'APC-Cy7-A':
            draw_ax.scatter(
                df['APC-A'], df['APC-Cy7-A'], s=2, c=self.color, alpha=0.5)
            axis_prop(draw_ax, "log", "log", "", "APC-A", "APC-Cy7-A")
            draw_ax.set_xlim(10**1, 10**5)
            draw_ax.set_ylim(10**1, 10**5)
            draw_ax.hlines(gate['point'][1], 10**1, 10**5, color="black")
            draw_ax.vlines(gate['point'][0], 10**1, 10**5, color="black")
        if gate['xaxis'] == 'FITC-A' and gate['yaxis'] == 'APC-A':
            draw_ax.scatter(
                df['FITC-A'], df['APC-A'], s=2, c=self.color, alpha=0.5)
            axis_prop(draw_ax, "log", "log", "", "FITC-A", "APC-A")
            draw_ax.set_xlim(10**1, 10**5)
            draw_ax.set_ylim(10**1, 10**5)
            draw_ax.hlines(gate['point'][1], 10**1, 10**5, color="black")
            draw_ax.vlines(gate['point'][0], 10**1, 10**5, color="black")
        if gate['xaxis'] == 'PE-Cy7-A' and gate['yaxis'] == 'APC-Cy7-A':
            draw_ax.scatter(
                df['PE-Cy7-A'], df['APC-Cy7-A'], s=2, c=self.color, alpha=0.5)
            axis_prop(draw_ax, "log", "log", "", "PE-Cy7-A", "APC-Cy7-A")
            draw_ax.set_xlim(10**1, 10**5)
            draw_ax.set_ylim(10**1, 10**5)
            draw_ax.hlines(gate['point'][1], 10**1, 10**5, color="black")
            draw_ax.vlines(gate['point'][0], 10**1, 10**5, color="black")
        if gate['xaxis'] == 'PE-A' and gate['yaxis'] == 'PE-Cy7-A':
            draw_ax.scatter(
                df['PE-A'], df['PE-Cy7-A'], s=2, c=self.color, alpha=0.5)
            axis_prop(draw_ax, "log", "log", "", "PE-A", "PE-Cy7-A")
            draw_ax.set_xlim(10**1, 10**5)
            draw_ax.set_ylim(10**1, 10**5)
            draw_ax.hlines(gate['point'][1], 10**1, 10**5, color="black")
            draw_ax.vlines(gate['point'][0], 10**1, 10**5, color="black")
        self.count = self.count + 1

    def draw_vetx_gate(self, filename, vetx_gate, df):
        i = int(self.count / self.col)
        j = self.count % self.col
        draw_ax = self.ax[i][j]
        actual_x = df['SSC-A']
        x = df['SSC-A'] / 1000
        y = df['PerCP-A']
        draw_ax.scatter(x, y, s=2, c=self.color, alpha=0.5)
        axis_prop(draw_ax, "linear", "log", "", "SSC-A", "PerCP-A")
        draw_ax.set_xlim(0, 250)
        draw_ax.set_ylim(10**1, 10**5)
        self.count = self.count + 1
        gate = Gate()
        gate.load(vetx_gate)
        actual_x = actual_x.values.reshape(x.values.size, 1)
        y = y.values.reshape(y.values.size, 1)
        points = numpy.concatenate((actual_x, y), axis=1)
        return gate.stat(points)

    def draw(self, fulldir, specimengates):
        result = None
        for specimengate in specimengates:
            filename = specimengate.fcsfilename
            filepath = os.path.join(fulldir, filename)
            meta, df = fcsparser.parse(filepath)
            normal_gates = None
            vetx_gate = None
            if specimengate.gatetype == 0:
                normal_gates = json.loads(specimengate.gates)
            elif specimengate.gatetype == 1:
                vetx_gate = json.loads(specimengate.gates)

            if normal_gates is not None:
                for gate in normal_gates:
                    if self.count >= self.row * self.col:
                        self.new_plot()
                    self.draw_normal_gate(filename, gate, df)

            if vetx_gate is not None:
                if self.count >= self.row * self.col:
                    self.new_plot()
                result = self.draw_vetx_gate(filename, vetx_gate, df)
        self.copy_last_plot()
        return self.imgs, result


def render_report(datasetdir, specimen, specimengates):
    fulldir = os.path.join(datasetdir, specimen.specimendir)
    template = Template(REPORT_TEMPLATE)
    if os.path.exists(REPORT_TEMP_DIR) is not True:
        os.mkdir(REPORT_TEMP_DIR)

    drawer = DrawHelp(3, 3)
    imgs, result = drawer.draw(fulldir, specimengates)
    fileuuid = str(uuid.uuid4())
    logger.info("starting gen file " + fileuuid + ".pdf")
    htmlfilepath = os.path.join(REPORT_TEMP_DIR, fileuuid + ".html")
    pdfreportpath = os.path.join(REPORT_TEMP_DIR, fileuuid + ".pdf")
    stat = {
        'red': str(round(result['stat']['red'] * 100)) + '%',
        'gred': str(round(result['stat']['gred'] * 100)) + '%',
        'blue': str(round(result['stat']['blue'] * 100)) + '%',
        'black': str(round(result['stat']['black'] * 100)) + '%'
    }
    html = template.render(specimen=specimen.to_json(), imgs=imgs, stat=stat)
    file = open(htmlfilepath, 'w+')
    file.write(html)
    file.close()
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None
    }
    pdfkit.from_file(htmlfilepath, pdfreportpath, options=options)
    return fileuuid + ".pdf"
