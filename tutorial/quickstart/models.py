# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from neo4django.db import models

class Person(models.NodeModel):
    name = models.StringProperty()
    #age = models.IntegerProperty()
    friends = models.Relationship('self',rel_type='friends_with')