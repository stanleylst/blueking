# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1494401038.085806
_enable_loop = True
_template_filename = u'/Users/stanley/Documents/magedu/blueking/blueking/framework/templates/base.html'
_template_uri = u'/base.html'
_source_encoding = 'utf-8'
_exports = [u'content', u'head']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        APP_PATH = context.get('APP_PATH', UNDEFINED)
        def head():
            return render_head(context._locals(__M_locals))
        BK_PLAT_HOST = context.get('BK_PLAT_HOST', UNDEFINED)
        STATIC_VERSION = context.get('STATIC_VERSION', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        APP_ID = context.get('APP_ID', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        LOGOUT_URL = context.get('LOGOUT_URL', UNDEFINED)
        NOW = context.get('NOW', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n  <head>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head'):
            context['self'].head(**pageargs)
        

        __M_writer(u'\n  </head>\n\n  <body>\n  \t<div>\n\t    <!--\u9876\u90e8\u5bfc\u822a Start-->\n\t\t<nav class="navbar navbar-default king-horizontal-nav2" role="navigation">\n\t\t    <div class="container" style="width: 100%;">\n\t\t        <div class="navbar-header col-md-4 col-sm-4 col-xs-4 logo">\n\t\t            <a class="navbar-brand" href="')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'">\n\t\t                \u84dd\u9cb8\u667a\u4e91\u5f00\u53d1\u6846\u67b6\n\t\t            </a>\n\t\t        </div>\n\t\t        <div class="collapse navbar-collapse navbar-responsive-collapse" id="king-example-navbar-collapse-2">\n\t\t            <ul class="nav navbar-nav">\n\t\t\t\t\t\t')

        home = dev_guide = contactus = ''
        relative_path = APP_PATH
        if relative_path == SITE_URL or relative_path.startswith(SITE_URL + "?"):
                home = 'king-navbar-active'
        elif relative_path.startswith(SITE_URL + "dev-guide/"):
                dev_guide = 'king-navbar-active'
        elif relative_path.startswith(SITE_URL + "contactus/"):
                contactus = 'king-navbar-active'
                                                        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['home','relative_path','contactus','dev_guide'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\t\t                <li class="')
        __M_writer(unicode(home))
        __M_writer(u'"><a href="')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'"><span>\u9996\u9875</span></a></li>\n\t\t                <li class="')
        __M_writer(unicode(dev_guide))
        __M_writer(u'"><a href="')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'dev-guide/"><span>\u5f00\u53d1\u6307\u5f15</span></a></li>\n\t\t                <li class="')
        __M_writer(unicode(contactus))
        __M_writer(u'"><a href="')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'contactus/"><span>\u8054\u7cfb\u6211\u4eec</span></a></li>\n\t\t            </ul>\n\t\t            <ul class="nav navbar-nav navbar-right">\n\t\t\t\t\t\t<a href="###" class="avatar">\n\t\t\t                <img src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'img/getheadimg.jpg" width="40" alt="Avatar" class="avatar-img">\n')
        if request.user.is_superuser:
            __M_writer(u'                                <i class="crown"></i>\n')
        __M_writer(u'                            <span>')
        __M_writer(unicode(request.user.username))
        __M_writer(u'</span>\n\t\t\t            </a>\n\t\t\t\t\t\t<!--\u9000\u51fa\u767b\u5f55-->\n\t\t\t\t        <a id="logout" href="')
        __M_writer(unicode(LOGOUT_URL))
        __M_writer(u'">\u6ce8\u9500</a>\n\t\t            </ul>\n\t\t        </div>\n\t\t    </div>\n\t\t</nav>\n\t\t<!--\u9876\u90e8\u5bfc\u822a End-->\n  \t</div>\n    <!-- \u56fa\u5b9a\u5bbd\u5ea6\u5c45\u4e2d start -->\n    <div class="container page_index">\n    \t<div class="">\n        \t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n    \t</div>\n    </div>\n    <!-- \u56fa\u5b9a\u5bbd\u5ea6\u8868\u5355\u5c45\u4e2d end -->\n    <!-- \u5c3e\u90e8\u58f0\u660e start -->\n      <div class="foot" id="footer">\n        <ul class="links ft">\n            <li>\n                <a href="###" id="contact_us" class="link">QQ\u54a8\u8be2</a>\n                <script src="//wp.qiye.qq.com/loader/4.0.0.js" charset="utf-8"></script>\n                <script type="text/javascript">\n                   try{\n                      __WPA.create({\n                          nameAccount:"800802001",\n                          customEle: document.getElementById(\'contact_us\')\n                      })\n                   }catch(err){}\n                </script>\n                | <a href="http://bbs.bk.tencent.com/forum.php" target="_blank" hotrep="hp.footer.feedback" class="link">\u84dd\u9cb8\u8bba\u575b</a>\n                | <a href="http://bk.tencent.com/" target="_blank" hotrep="hp.footer.feedback" class="link">\u84dd\u9cb8\u5b98\u7f51</a>\n                | <a href="')
        __M_writer(unicode(BK_PLAT_HOST))
        __M_writer(u'" target="_blank" hotrep="hp.footer.feedback" class="link">\u84dd\u9cb8\u667a\u4e91\u5de5\u4f5c\u53f0</a>\n            </li>\n            <li><p class="copyright">Copyright \xa9 2012-')
        __M_writer(unicode(NOW.year))
        __M_writer(u' Tencent BlueKing. All Rights Reserved.</p> </li>\n          <li><p class="copyright">\u84dd\u9cb8\u667a\u4e91 \u7248\u6743\u6240\u6709</p> </li>\n        </ul>\n      </div>\n      <!-- \u5c3e\u90e8\u58f0\u660e end -->\n\n    <!-- jquery js  -->\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/jquery-1.10.2.min.js" type="text/javascript"></script>\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/jquery.json-2.3.min.js" type="text/javascript"></script>\n    <!-- bootstrap js  -->\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/bootstrap-3.3.4/js/bootstrap.min.js" type="text/javascript"></script>\n    <!--\u914d\u7f6ejs  \u52ff\u5220-->\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/settings.js?v=')
        __M_writer(unicode(STATIC_VERSION))
        __M_writer(u'" type="text/javascript"></script>\n    ')
        __M_writer(unicode(self.body()))
        __M_writer(u'\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_VERSION = context.get('STATIC_VERSION', UNDEFINED)
        def head():
            return render_head(context)
        APP_ID = context.get('APP_ID', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n        <title>\u5f00\u53d1\u6846\u67b6|\u84dd\u9cb8\u667a\u4e91\u793e\u533a\u7248</title>\n        <meta name="description" content=""/>\n        <meta name="author" content=""/>\n        <link rel="shortcut icon" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'favicon.ico" type="image/x-icon">\n        <!-- bootstrap css -->\n\t\t    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/bootstrap-3.3.4/css/bootstrap.min.css" rel="stylesheet">\n\t\t    <!-- \u7981\u6b62bootstrap \u54cd\u5e94\u5f0f \uff08app\u6839\u636e\u81ea\u8eab\u9700\u6c42\u542f\u7528\u6216\u7981\u6b62bootstrap\u54cd\u5e94\u5f0f\uff09 -->\n\t\t    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/bootstrap-3.3.4/css/bootstrap_noresponsive.css" rel="stylesheet">\n\t\t    <!--\u81ea\u5b9a\u4e49css-->\n\t\t    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/base.css?v=')
        __M_writer(unicode(STATIC_VERSION))
        __M_writer(u'" rel="stylesheet">\n        <!-- \u8fd9\u4e2a\u662f\u5168\u5c40\u914d\u7f6e\uff0c\u5982\u679c\u9700\u8981\u5728js\u4e2d\u4f7f\u7528app_id\u548csite_url,\u5219\u8fd9\u4e2ajavascript\u7247\u6bb5\u4e00\u5b9a\u8981\u4fdd\u7559 -->\n        <script type="text/javascript">\n\t    \t  var app_id = "')
        __M_writer(unicode(APP_ID))
        __M_writer(u'";\n\t\t\t    var site_url = "')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'";\t  // app\u7684url\u524d\u7f00,\u5728ajax\u8c03\u7528\u7684\u65f6\u5019\uff0c\u5e94\u8be5\u52a0\u4e0a\u8be5\u524d\u7f00\n\t\t\t    var static_url = "')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'"; // \u9759\u6001\u8d44\u6e90\u524d\u7f00\n\t      </script>\n        <style>\n          /*\u5982\u679c\u4f60\u9700\u8981\u7ed9\u4f60\u7684\u5e94\u7528\u56fa\u5b9a\u9ad8\u5ea6\u548c\u5bbd\u5ea6\uff0c\u8bf7\u5728\u8fd9\u91cc\u4fee\u6539*/\n    \t\t\tbody {min-width:1200px;}\n    \t\t</style>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 11, "129": 11, "130": 13, "131": 13, "132": 15, "133": 15, "134": 15, "135": 15, "136": 18, "137": 18, "138": 19, "139": 19, "140": 20, "141": 20, "16": 0, "147": 141, "35": 1, "40": 26, "41": 35, "42": 35, "43": 41, "56": 50, "57": 51, "58": 51, "59": 51, "60": 51, "61": 52, "62": 52, "63": 52, "64": 52, "65": 53, "66": 53, "67": 53, "68": 53, "69": 57, "70": 57, "71": 58, "72": 59, "73": 61, "74": 61, "75": 61, "76": 64, "77": 64, "82": 74, "83": 94, "84": 94, "85": 96, "86": 96, "87": 103, "88": 103, "89": 104, "90": 104, "91": 106, "92": 106, "93": 108, "94": 108, "95": 108, "96": 108, "97": 109, "98": 109, "104": 74, "115": 4, "125": 4, "126": 9, "127": 9}, "uri": "/base.html", "filename": "/Users/stanley/Documents/magedu/blueking/blueking/framework/templates/base.html"}
__M_END_METADATA
"""
