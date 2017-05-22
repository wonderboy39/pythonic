import django
from subprocess import call

def get_version() :
    print("--------version--------")
    print(" django version : " + django.get_version())
    print("-----------------------")
    call(["ls", "-l"])

get_version()
