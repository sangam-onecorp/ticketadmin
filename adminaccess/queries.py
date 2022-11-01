
from django.db import models
# Create your models here.
from django.db import connection, transaction, connections
import sys
import os
import datetime
import re
import time
import random
from datetime import datetime
from django.core.mail import EmailMultiAlternatives

# Helper Quries




def dictfetchall(cursor=''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor=''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))


def replace_null_with_empty_string_many(result):
    for dictionary in result:
        for i in dictionary:
            if dictionary[i] == 'NULL' or dictionary[i] == None or dictionary[i] == 'None' or dictionary[i] == 'null':
                dictionary[i] = ''
            elif type(dictionary[i]) == int:
                dictionary[i] = str(dictionary[i])
    return result


def replace_null_with_empty_string(dictionary):
    for i in dictionary:
        if dictionary[i] == 'NULL' or dictionary[i] == None or dictionary[i] == 'None' or dictionary[i] == 'null':
            dictionary[i] = ''
        elif type(dictionary[i]) == int:
            dictionary[i] = str(dictionary[i])
    return dictionary


def get_userinfo_by_UserToken_q(data):
    """Get User Information by UserToken to Check User_Role"""
    with connections['StockOne'].cursor() as cursor:
        resp = cursor.execute(""" SELECT ID,ID KeyIndex, UserLoginID, UserToken, UserName, FirstName, LastName, Email, Mobile, IsEmailVerified, IsMobileVerified, Location, UserRole, IsDeleted, CreatedAt, CreatedBy, UpdatedAt, UpdatedBy FROM StockOne.UserLogin where UserToken='{}'; """.format(data))
        if resp and cursor.rowcount:
            resp = dictfetchone(cursor)
        else:
            resp = None
    return resp



def carstock_allocatestatus_q(data):
    with connections["StockOne"].cursor() as cursor:
        resp = cursor.execute("""update StockOne.carstock set
        allocation_status = %s,
        UpdatedBy= %s,
        updated_at = %s
        where CarStockID=%s;""", data)
    return resp



def UserSignup_q(data):

    with connection.cursor() as cursor:
        resp = cursor.execute(""" insert into adminticket.usersignup ( UserName, FirstName, LastName, Phone, Password, Email, AccessLevel, Location, IsDeleted, CreatedAt, CreatedBy, UpdatedAt, UpdatedBy)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """, data)
        resp = cursor.lastrowid
        return resp

