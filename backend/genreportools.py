import os
import json

def genreportimg(filespath, gates):
    return []

def render_report(datasetdir, specimen, specimengates):
    fulldir = os.path.join(datasetdir, specimen.specimendir)
    imgs=[]
    for specimengate in specimengates:
        filespath = os.path.join(fulldir, specimengate.fcsfilename)
        gates = json.loads(specimengate.gates)
        imgs = imgs + genreportimg(filespath, gates)
