# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
#CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。
#主要财务指标
# "code":"550017",
# "name":"信诚添金分级债券",
# "netincome":"--",
# "assincome":"0.2151",
# "netassrate":"--",
# "netgrowrate":"-0.8900",
# "tonetgrora":"29.3700",
# "time":"20160630"
class FundFinance(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    netincome = models.FloatField()
    assincome = models.FloatField()
    netassrate = models.FloatField()
    netgrowrate = models.FloatField()
    tonetgrora = models.FloatField()
    time = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

# 基金规模
# "code":"560003",
# "name":"益民创新优势混合",
# "fundshare":"986,718,250.3100",
# "netfunval":"844,465,274.72",
# "tolassfund":"853,366,706.31",
# "time":"20161231"
class FundScale(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    fundshare = models.FloatField()
    netfunval = models.FloatField()
    tolassfund = models.FloatField()
    time = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

# 资产配置
# "code":"560003",
# "name":"益民创新优势混合",
# "totalass":"853,366,720.00",
# "stockinv":"689,494,020.00",
# "stockrat":"80.800",
# "bondcurr":"84,010,584.00",
# "bcrate":"9.840",
# "time":"20161231"
class FundConfig(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    totalass = models.FloatField()
    stockinv = models.FloatField()
    stockrat = models.FloatField()
    bondcurr = models.FloatField()
    bcrate = models.FloatField()
    time = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name