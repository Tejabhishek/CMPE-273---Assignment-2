# -*- coding: utf-8 -*-

print "Loading Funcion..."

def handler(event, context):
    # Your code goes here!
    print "Hello World"
    print event
    #e = event.get('e')
    #pi = event.get('pi')
    #return e + pi
    return "OK"
