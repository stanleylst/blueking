# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1494400852.819276
_enable_loop = True
_template_filename = '/Users/stanley/Documents/\xe9\xa9\xac\xe5\x93\xa5\xe6\x95\x99\xe8\x82\xb2/\xe8\x93\x9d\xe9\xb2\xb8\xe5\xb9\xb3\xe5\x8f\xb0\xe5\x90\x88\xe4\xbd\x9c/blueking/framework/templates/home_application/home.html'
_template_uri = '/home_application/home.html'
_source_encoding = 'utf-8'
_exports = [u'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        BK_PAAS_HOST = context.get('BK_PAAS_HOST', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        BK_PAAS_HOST = context.get('BK_PAAS_HOST', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\t<div>\n\t\t<!-- \u84dd\u9cb8\u667a\u4e91\u5f00\u53d1\u6846\u67b6\u8bf4\u660e  Start -->\n\t\t<div>\n\t\t\t<h3>\u84dd\u9cb8\u667a\u4e91\u5f00\u53d1\u6846\u67b6<small>\u52a9\u529b\u4f60\u7684\u81ea\u52a8\u5316</small></h3>\n\t\t</div>\n\t\t<hr>\n\t\t<div class="mt30">\n\t\t\t<p>\u60a8\u73b0\u5728\u6253\u5f00\u7684\u5e94\u7528\u662f\u7531\u84dd\u9cb8\u667a\u4e91\u793a\u4f8b\u4ee3\u7801\u751f\u6210\u7684\uff0c\u8be5\u793a\u4f8b\u4ee3\u7801\u79f0\u4e3a\u201cAPP\u5f00\u53d1\u6846\u67b6\u201d\u3002</p>\n\t\t\t<p>\u84dd\u9cb8\u667a\u4e91\u96c6\u6210\u5e73\u53f0\uff08PaaS\uff09\u63d0\u4f9b\u4e86\u5b8c\u5584\u7684\u524d\u540e\u53f0\u5f00\u53d1\u6846\u67b6\u3001\u8c03\u5ea6\u5f15\u64ce\u3001\u516c\u5171\u7ec4\u4ef6\u7b49\u6a21\u5757\uff0c\u5e2e\u52a9\u4e1a\u52a1\u7684\u4ea7\u54c1\u548c\u6280\u672f\u4eba\u5458\u5feb\u901f\u6784\u5efa\u4f4e\u6210\u672c\u3001\u514d\u8fd0\u7ef4\u7684\u652f\u6491\u5de5\u5177\u548c\u8fd0\u8425\u7cfb\u7edf\u3002</p>\n\t\t\t<p>\u82e5\u60f3\u4f53\u9a8c\u5feb\u901f\u5f00\u53d1\u5e94\u7528\u7684\u529f\u80fd\uff0c\u8bf7\u524d\u5f80<a href="')
        __M_writer(unicode(BK_PAAS_HOST))
        __M_writer(u'" target="_blank">\u201c\u5f00\u53d1\u8005\u4e2d\u5fc3\u201d</a>\u3002</p>\n\t\t</div>\n\t\t<!-- \u84dd\u9cb8\u667a\u4e91\u5f00\u53d1\u6846\u67b6\u8bf4\u660e  End -->\n\t</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"35": 1, "40": 18, "46": 3, "53": 3, "54": 13, "55": 13, "27": 0, "61": 55}, "uri": "/home_application/home.html", "filename": "/Users/stanley/Documents/\u9a6c\u54e5\u6559\u80b2/\u84dd\u9cb8\u5e73\u53f0\u5408\u4f5c/blueking/framework/templates/home_application/home.html"}
__M_END_METADATA
"""
