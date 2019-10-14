import os
import json
import uuid
import pdfkit
import logging
from jinja2 import Template
from backend.reporttemplate import REPORT_TEMPLATE

logger = logging.getLogger('log')

REPORT_TEMP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_TEMP_DIR = os.path.join(REPORT_TEMP_DIR, "tmp")


def genreportimg(filespath, gates):
    return []


def render_report(datasetdir, specimen, specimengates):
    fulldir = os.path.join(datasetdir, specimen.specimendir)
    imgs = []
    for specimengate in specimengates:
        filespath = os.path.join(fulldir, specimengate.fcsfilename)
        gates = json.loads(specimengate.gates)
        imgs = imgs + genreportimg(filespath, gates)
    template = Template(REPORT_TEMPLATE)
    if os.path.exists(REPORT_TEMP_DIR) is not True:
        os.mkdir(REPORT_TEMP_DIR)

    fileuuid = str(uuid.uuid4())
    logger.info("starting gen file " + fileuuid + ".pdf")
    htmlfilepath = os.path.join(REPORT_TEMP_DIR, fileuuid + "html")
    pdfreportpath = os.path.join(REPORT_TEMP_DIR, fileuuid + ".pdf")
    html = template.render(specimen=specimen.to_json())
    file = open(htmlfilepath, 'w+')
    file.write(html)
    file.close()
    pdfkit.from_file(htmlfilepath, pdfreportpath)
