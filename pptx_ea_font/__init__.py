# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2019-11-11 17:42:18
# @Last Modified by:   Bi Ying
# @Last Modified time: 2022-10-12 12:34:07
from pptx.oxml.ns import qn


def set_font(run, font_name):
    run.font.name = font_name
    if run.font._rPr.find(qn("a:ea")) is not None:
        run.font._rPr.find(qn("a:ea")).set("typeface", run.font.name)
    else:
        element = run.font._rPr.makeelement(qn("a:ea"))
        element.set("typeface", run.font.name)
        run.font._rPr.insert(0, element)
