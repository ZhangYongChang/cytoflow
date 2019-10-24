from backend.reporttemplate import REPORT_TEMPLATE
from backend.models import Gate
from backend.funcscale import (FuncScale, FuncScale1000)
from backend.config import (get_fcsfilepath, get_reportfilepath, get_reporttmpdir)
from matplotlib import pyplot as plt
from matplotlib import scale as scale
from jinja2 import Template
import matplotlib
import numpy
import os
import json
import uuid
import pdfkit
import fcsparser
import io
import base64

matplotlib.use('agg')
scale.register_scale(FuncScale)
scale.register_scale(FuncScale1000)


class FlowFigDrawer(object):
    def __init__(self, fcsfiledir, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.row = 4
        self.col = 3
        self.color = ['tab:red']
        self.fcsfiledir = fcsfiledir
        self.imgs = []
        self.fig = None
        self.count = 0

    def axis_prop(self, ax, xaxis, yaxis, title, xtitle, ytitle):
        ax.set_xscale(xaxis)
        ax.set_yscale(yaxis)
        ax.set_title(title)
        ax.set_xlabel(xtitle)
        ax.set_ylabel(ytitle)

    def get_axes(self):
        if self.fig is None:
            self.fig = plt.figure(figsize=[12.0, 16.0])

        if self.count < self.row * self.col:
            self.count = self.count + 1
            return self.fig.add_subplot(self.row, self.col, self.count)
        else:
            self.count = 1
            self.copy_last_plot()
            self.fig = plt.figure(figsize=[12.0, 16.0])
            return self.fig.add_subplot(self.row, self.col, self.count)

    def copy_last_plot(self):
        plt.tight_layout(pad=2, h_pad=2, w_pad=2)
        imagebuf = io.BytesIO()
        self.fig.savefig(imagebuf)
        figbytes = base64.b64encode(imagebuf.getvalue())
        imagebuf.close()
        self.imgs.append(bytes.decode(figbytes))

    def draw_normal_gate(self, filename, gate, df):
        draw_ax = self.get_axes()
        if gate['xaxis'] == 'FSC-A' and gate['yaxis'] == 'SSC-A':
            x = df['FSC-A']
            y = df['SSC-A']
            draw_ax.scatter(x, y, s=2, c=self.color, alpha=0.5)
            draw_ax.set_xlim(0, 250000)
            draw_ax.set_ylim(0, 250000)
            (x0, xmax) = draw_ax.get_xlim()
            (y0, ymax) = draw_ax.get_ylim()
            draw_ax.hlines(gate['point'][1], x0, xmax, color="black")
            draw_ax.vlines(gate['point'][0], y0, ymax, color="black")
            self.axis_prop(draw_ax, 'funcscale1000',
                           'funcscale1000', "", "FSC-A", "SSC-A")
        if gate['xaxis'] == 'FITC-A' and gate['yaxis'] == 'PE-A':
            draw_ax.scatter(
                df['FITC-A'], df['PE-A'], s=2, c=self.color, alpha=0.5)
            self.axis_prop(draw_ax, "log", "log", "", "FITC-A", "PE-A")
            draw_ax.set_xlim(10 ** 1, 10 ** 5)
            draw_ax.set_ylim(10 ** 1, 10 ** 5)
            draw_ax.hlines(gate['point'][1], 10 ** 1, 10 ** 5, color="black")
            draw_ax.vlines(gate['point'][0], 10 ** 1, 10 ** 5, color="black")
        if gate['xaxis'] == 'FITC-A' and gate['yaxis'] == 'PE-Cy7-A':
            draw_ax.scatter(
                df['FITC-A'], df['PE-Cy7-A'], s=2, c=self.color, alpha=0.5)
            self.axis_prop(draw_ax, "log", "log", "", "FITC-A", "PE-Cy7-A")
            draw_ax.set_xlim(10 ** 1, 10 ** 5)
            draw_ax.set_ylim(10 ** 1, 10 ** 5)
            draw_ax.hlines(gate['point'][1], 10 ** 1, 10 ** 5, color="black")
            draw_ax.vlines(gate['point'][0], 10 ** 1, 10 ** 5, color="black")
        if gate['xaxis'] == 'APC-A' and gate['yaxis'] == 'APC-Cy7-A':
            draw_ax.scatter(
                df['APC-A'], df['APC-Cy7-A'], s=2, c=self.color, alpha=0.5)
            self.axis_prop(draw_ax, "log", "log", "", "APC-A", "APC-Cy7-A")
            draw_ax.set_xlim(10 ** 1, 10 ** 5)
            draw_ax.set_ylim(10 ** 1, 10 ** 5)
            draw_ax.hlines(gate['point'][1], 10 ** 1, 10 ** 5, color="black")
            draw_ax.vlines(gate['point'][0], 10 ** 1, 10 ** 5, color="black")
        if gate['xaxis'] == 'FITC-A' and gate['yaxis'] == 'APC-A':
            draw_ax.scatter(
                df['FITC-A'], df['APC-A'], s=2, c=self.color, alpha=0.5)
            self.axis_prop(draw_ax, "log", "log", "", "FITC-A", "APC-A")
            draw_ax.set_xlim(10 ** 1, 10 ** 5)
            draw_ax.set_ylim(10 ** 1, 10 ** 5)
            draw_ax.hlines(gate['point'][1], 10 ** 1, 10 ** 5, color="black")
            draw_ax.vlines(gate['point'][0], 10 ** 1, 10 ** 5, color="black")
        if gate['xaxis'] == 'PE-Cy7-A' and gate['yaxis'] == 'APC-Cy7-A':
            draw_ax.scatter(
                df['PE-Cy7-A'], df['APC-Cy7-A'], s=2, c=self.color, alpha=0.5)
            self.axis_prop(draw_ax, "log", "log", "", "PE-Cy7-A", "APC-Cy7-A")
            draw_ax.set_xlim(10 ** 1, 10 ** 5)
            draw_ax.set_ylim(10 ** 1, 10 ** 5)
            draw_ax.hlines(gate['point'][1], 10 ** 1, 10 ** 5, color="black")
            draw_ax.vlines(gate['point'][0], 10 ** 1, 10 ** 5, color="black")
        if gate['xaxis'] == 'PE-A' and gate['yaxis'] == 'PE-Cy7-A':
            draw_ax.scatter(
                df['PE-A'], df['PE-Cy7-A'], s=2, c=self.color, alpha=0.5)
            self.axis_prop(draw_ax, "log", "log", "", "PE-A", "PE-Cy7-A")
            draw_ax.set_xlim(10 ** 1, 10 ** 5)
            draw_ax.set_ylim(10 ** 1, 10 ** 5)
            draw_ax.hlines(gate['point'][1], 10 ** 1, 10 ** 5, color="black")
            draw_ax.vlines(gate['point'][0], 10 ** 1, 10 ** 5, color="black")

    def draw_vetx_gate(self, filename, vetx_gate, df):
        draw_ax = self.get_axes()
        actual_x = df['SSC-A']
        actual_y = df['PerCP-A']
        # 统计
        gate = Gate()
        gate.load(vetx_gate)
        x = actual_x.values.reshape(actual_x.values.size, 1)
        y = actual_y.values.reshape(actual_y.values.size, 1)
        points = numpy.concatenate((x, y), axis=1)
        result = gate.stat(points)
        # 绘图
        for key, item in result['detail'].items():
            draw_x = item[:, 0]
            draw_y = item[:, 1]
            draw_ax.scatter(draw_x, draw_y, s=2, c=key, alpha=0.5)
        self.axis_prop(draw_ax, "funcscale1000", "log", "", "SSC-A", "PerCP-A")
        # 配置坐标宽度
        draw_ax.set_xlim(0, 250000)
        draw_ax.set_ylim(10 ** 1, 10 ** 5)
        return result

    def draw(self, specimengates):
        result = None
        for specimengate in specimengates:
            filename = specimengate.fcsfilename
            filepath = get_fcsfilepath(self.fcsfiledir, filename)
            meta, df = fcsparser.parse(filepath)
            normal_gates = None
            vetx_gate = None
            if specimengate.gatetype == 0:
                normal_gates = json.loads(specimengate.gates)
            elif specimengate.gatetype == 1:
                vetx_gate = json.loads(specimengate.gates)

            if normal_gates is not None:
                for gate in normal_gates:
                    self.draw_normal_gate(filename, gate, df)

            if vetx_gate is not None:
                result = self.draw_vetx_gate(filename, vetx_gate, df)
        self.copy_last_plot()
        return self.imgs, result


class PdfReportRender(object):
    def __init__(self, specimen, specimengates, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.specimen = specimen
        self.specimengates = specimengates

    def render_report(self):
        template = Template(REPORT_TEMPLATE)
        if os.path.exists(get_reporttmpdir()) is not True:
            os.mkdir(get_reporttmpdir())

        drawer = FlowFigDrawer(self.specimen.specimendir)
        imgs, result = drawer.draw(self.specimengates)
        fileuuid = str(uuid.uuid4())
        htmlfilepath = get_reportfilepath(fileuuid + ".html")
        pdfreportfilename = fileuuid + ".pdf"
        pdfreportpath = get_reportfilepath(pdfreportfilename)
        stat = {
            'green': str(round(result['stat']['green'] * 100)) + '%',
            'yellow': str(round(result['stat']['yellow'] * 100)) + '%',
            'red': str(round(result['stat']['red'] * 100)) + '%',
            'purple': str(round(result['stat']['purple'] * 100)) + '%'
        }
        html = template.render(
            specimen=self.specimen.to_json(), imgs=imgs, stat=stat)
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
        return pdfreportfilename
