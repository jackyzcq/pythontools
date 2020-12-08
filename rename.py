#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re

def multi_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def xlat(match):
        return adict[match.group(0)]
    return rx.sub(xlat, text)

def batrename(curdir, pairs):
    for fn in os.listdir(curdir):
        newfn = multi_replace(fn, pairs)
        if newfn != fn:
            print("Renames %s to %s in %s." % (fn, newfn, curdir))
            os.rename(os.path.join(curdir, fn), os.path.join(curdir, newfn))
        file = os.path.join(curdir, newfn)

        if os.path.isdir(file):
            batrename(file, pairs)
            continue

        text = open(file).read()
        newtext = multi_replace(text, pairs)
        if newtext != text:
            print("Renames %s." % (file,))
            open(file, 'w').write(newtext)

if __name__=="__main__":
    while True:
        oldname = raw_input("Old name: ")
        newname = raw_input("New name: ")
        if oldname and newname:
            batrename(os.path.abspath('.'), {oldname:newname})
        else: break

