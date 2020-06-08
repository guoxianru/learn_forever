# -*- coding: utf-8 -*-
# -*- author: GXR -*-

# # 查看当前JS使用引擎
# import execjs
# print(execjs.get())

# # 手动设置JS使用引擎：长期使用
# import os
# os.environ["EXECJS_RUNTIME"] = "Node"

# # 手动设置JS使用引擎：临时使用
# import execjs.runtime_names
# node = execjs.get(execjs.runtime_names.Node)

# # 直接运行JS代码
# import execjs
# e = execjs.eval("a = new Array(1,2,3)")
# print(e)

# # 调用编译JS代码
# import execjs
# js_text = "function hello(str,int){ return str+int;}"
# ctx = execjs.compile(js_text)
# a = ctx.call("hello", "world", 1)
# print(a)
