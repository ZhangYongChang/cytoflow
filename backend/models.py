from django.db import models

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
            'bedno': self.bedno,
            'doctor': self.doctor,
            'specimentype': self.specimentype,
            'caseno': self.caseno,
            'collecttime': self.collecttime,
            'recvtime': self.recvtime
        }
