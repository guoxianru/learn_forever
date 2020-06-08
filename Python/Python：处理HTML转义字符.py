# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import html

text = "&lt;abc&gt;"

print(html.unescape(text))

print(html.escape(text))
