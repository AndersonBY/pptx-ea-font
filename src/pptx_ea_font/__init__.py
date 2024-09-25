from lxml import etree
from pptx.oxml.ns import qn
from pptx.text.text import _Run


def set_font(run: _Run, font_name: str):
    run.font.name = font_name
    namespaces = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}
    rPr = run.font._rPr

    # 保留现有的字体颜色属性
    color_element = rPr.find(qn("a:solidFill"), namespaces)

    # 查找并替换 a:cs 或 a:sym 标签
    cs_element = rPr.find(qn("a:cs"), namespaces)
    sym_element = rPr.find(qn("a:sym"), namespaces)

    if cs_element is not None:
        cs_element.tag = qn("a:ea")
        cs_element.set("typeface", font_name)
    elif sym_element is not None:
        sym_element.tag = qn("a:ea")
        sym_element.set("typeface", font_name)
    else:
        ea_element = rPr.find(qn("a:ea"), namespaces)
        if ea_element is not None:
            ea_element.set("typeface", font_name)
        else:
            element = etree.Element(qn("a:ea"), attrib={}, nsmap=rPr.nsmap)
            element.set("typeface", font_name)
            rPr.insert(0, element)  # 插入到首位

    # 如果存在字体颜色属性，将其重新插入
    if color_element is not None:
        rPr.insert(0, color_element)
