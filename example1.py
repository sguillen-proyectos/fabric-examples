#!/usr/bin/python

# How to execute me
# fab -H example.com host_type -f example1.py -u username
# fab -H example.com hello_world:name=foo,lastname=bar
# echo "name=foo,lastname=bar" >> example1.params && fab -H example.com hello_world:$(cat example1.params)

from fabric.api import run

def host_type():
    run('uname -s')

def hello_world(name='joe', lastname='doe'):
    print('hello world from fabric!')
    print('nice to meet you %s %s' % (name, lastname))
