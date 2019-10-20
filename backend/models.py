from django.db import models
from backend.poiwithinpolygon import isPoiWithinPoly
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
    gates = models.CharField(max_length=256, help_text=u'门')
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


class Polygon(object):
    def __init__(self, name, vectexs):
        self.vectexs = vectexs
        self.name = name

    def isPoiWithinPolyon(self, point):
        return isPoiWithinPoly(point, self.vectexs)


class PolygonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Polygon):
            return {'name': obj.name, 'vectexs': json.dumps(obj.vectexs)}
        return json.JSONEncoder.default(self, obj)


class Gate(object):
    def __init__(self, xaxis, yaxis, polygons=None):
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
                if isPoiWithinPoly(point, polygon.vectexs):
                    result['detail'][polygon.name].append(point)
                    result['stat'][
                        polygon.name] = result['stat'][polygon.name] + 1
                    count = count + 1

        for item, key in result['stat']:
            result['stat'][key] = float(result['stat'][key]) / float(count)
        return result


class GateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Gate):
            return {
                'xaxis': obj.xaxis,
                'yaxis': obj.yaxis,
                'polygons': json.dumps(obj.polygons, cls=PolygonEncoder)
            }
        return json.JSONEncoder.default(self, obj)
