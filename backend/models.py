from django.db import models
from backend.poiwithinpolygon import isPoiWithinPoly
import matplotlib.path as mplPath
import numpy as np
import json

# Create your models here.


class Specimen(models.Model):
    class Meta:
        db_table = 'specimen'

    specimenid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, help_text=u'名字')
    sex = models.CharField(max_length=8, help_text=u'年龄')
    age = models.IntegerField()
    specimenno = models.CharField(max_length=16)
    hospital = models.CharField(max_length=64)
    department = models.CharField(max_length=64)
    bedno = models.CharField(max_length=16)
    doctor = models.CharField(max_length=16)
    specimentype = models.CharField(max_length=16)
    caseno = models.CharField(max_length=32)
    collecttime = models.DateTimeField()
    recvtime = models.DateTimeField()
    specimendir = models.CharField(max_length=64)

    def to_json(self):
        return {
            'specimenid': self.specimenid,
            'name': self.name,
            'sex': self.sex,
            'age': self.age,
            'specimenno': self.specimenno,
            'hospital': self.hospital,
            'department': self.department,
            'bedno': self.bedno,
            'doctor': self.doctor,
            'specimentype': self.specimentype,
            'caseno': self.caseno,
            'collecttime': self.collecttime,
            'recvtime': self.recvtime
        }


class SpecimenGate(models.Model):
    class Meta:
        db_table = 'specimengate'

    specimengateid = models.AutoField(primary_key=True)
    specimenid = models.IntegerField()
    fcsfilename = models.CharField(max_length=256, help_text=u'文件名称')
    gates = models.CharField(max_length=4096, help_text=u'门')
    createtime = models.DateTimeField()
    modifytime = models.DateTimeField()
    gatetype = models.IntegerField()

    def to_json(self):
        return {
            'specimengateid': self.specimengateid,
            'specimenid': self.specimenid,
            'fcsfilename': self.fcsfilename,
            'gatetype': self.gatetype,
            'gates': self.gates,
            'createtime': self.createtime,
            'modifytime': self.modifytime
        }


class SpecimenReport(models.Model):
    class Meta:
        db_table = 'specimenreport'

    sepcimenreportid = models.AutoField(primary_key=True)
    specimenid = models.IntegerField()
    specimenreportpath = models.CharField(max_length=256, help_text=u'')
    createtime = models.DateTimeField()

    def to_json(self):
        return {
            'sepcimenreportid': self.sepcimenreportid,
            'specimenid': self.specimenid,
            'specimenreportpath': self.specimenreportpath,
            'createtime': self.createtime
        }


class Polygon(object):
    def __init__(self, name, vectexs):
        self.vectexs = vectexs
        self.name = name
        self.path = mplPath.Path(self.vectexs)

    def isPoiWithinPolyon(self, point):
        return self.path.contains_point(point)


class Gate(object):
    def __init__(self, xaxis=None, yaxis=None, polygons=None):
        self.polygons = polygons
        self.xaxis = xaxis
        self.yaxis = yaxis

    def stat(self, points):
        result = {}
        result['stat'] = {}
        result['detail'] = {}
        for polygon in self.polygons:
            result['stat'][polygon.name] = 0
            result['detail'][polygon.name] = []

        count = 0
        for point in points:
            for polygon in self.polygons:
                if polygon.isPoiWithinPolyon(point):
                    #result['detail'][polygon.name].append(point)
                    result['stat'][polygon.name] = result['stat'][polygon.name] + 1
                    count = count + 1
                    break

        if count == 0:
          return result

        for key, item in result['stat'].items():
            result['stat'][key] = float(result['stat'][key]) / float(count)
        return result

    def load(self, json):
        self.polygons=[]
        for gate_polygon in json['gate']:
            polygon = Polygon(gate_polygon['name'], gate_polygon['data'])
            self.polygons.append(polygon)
        self.xaxis = json['xaxis']
        self.yaxis = json['yaxis']
