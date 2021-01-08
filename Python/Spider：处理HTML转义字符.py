# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    处理HTML转义字符
"""

import html
import json

text = "&lt;abc&gt;"
print(html.unescape(text))
print(html.escape(text))

s = "&quot;\\u003Cimg src&#x3D;\\&quot;http:\\u002F\\u002Fp3-tt.byteimg.com\\u002Flarge\\u002Fpgc-image\\u002FS5MDUYI2Oowh2M?from&#x3D;pc\\&quot; img_width&#x3D;\\&quot;750\\&quot; img_height&#x3D;\\&quot;421\\&quot; alt&#x3D;\\&quot;佩洛西：若特朗普败选后不离开白宫 就用烟熏出去\\&quot; inline&#x3D;\\&quot;0\\&quot;\\u003E\\u003Cp\\u003E看看新闻Knews综合\\u003C\\u002Fp\\u003E\\u003Cp\\u003E2020-07-21 14:27\\u003C\\u002Fp\\u003E\\u003Cp\\u003E据路透社报道，当地时间7月20日，美国众议院议长佩洛西在接受美媒采访时称，如果特朗普在11月的大选中失利，他将不得不离开白宫,\\&quot;（如果败选后特朗普不愿离开白宫），那就不得不用烟（把他）熏出去。\\&quot;\\u003C\\u002Fp\\u003E\\u003Cimg src&#x3D;\\&quot;http:\\u002F\\u002Fp3-tt.byteimg.com\\u002Flarge\\u002Fpgc-image\\u002FS5MDUYqBaDJjAv?from&#x3D;pc\\&quot; img_width&#x3D;\\&quot;640\\&quot; img_height&#x3D;\\&quot;360\\&quot; alt&#x3D;\\&quot;佩洛西：若特朗普败选后不离开白宫 就用烟熏出去\\&quot; inline&#x3D;\\&quot;0\\&quot;\\u003E\\u003Cp\\u003E佩洛西在接受采访时称，如果特朗普在11月的大选中失利，他将不得不离开白宫。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E综合路透社、美国消费者新闻与商业频道（CNBC）报道，佩洛西称，\\&quot;（凡事）都有一个章程。\\&quot;CNBC解释称，佩洛西这里说的是美国总统选举和宪法机制中关于胜选者入主白宫的内容。\\&quot;这与白宫的某些居住者不想搬走无关，（如果败选后特朗普不愿离开白宫），那就不得不用烟（把他）熏出去。\\&quot;\\u003C\\u002Fp\\u003E\\u003Cimg src&#x3D;\\&quot;http:\\u002F\\u002Fp6-tt.byteimg.com\\u002Flarge\\u002Fpgc-image\\u002FS5GPSGR4B3qAir?from&#x3D;pc\\&quot; img_width&#x3D;\\&quot;640\\&quot; img_height&#x3D;\\&quot;360\\&quot; alt&#x3D;\\&quot;佩洛西：若特朗普败选后不离开白宫 就用烟熏出去\\&quot; inline&#x3D;\\&quot;0\\&quot;\\u003E\\u003Cp\\u003E福克斯新闻19日播出了特朗普的独家采访\\u003C\\u002Fp\\u003E\\u003Cp\\u003E特朗普会否接受大选结果并搬离白宫一直是美国关注焦点。佩洛西发表上述言论的前一天，美媒播出特朗普专访中，当被主持人问及是否能接受对手拜登在大选中获胜时，特朗普给出了模棱两可的回答，\\&quot;我得看看。听着，你……我得看看。不，我不会就这么说接受，我也不会说不接受。上次我也没有承诺。\\&quot;\\u003C\\u002Fp\\u003E\\u003Cimg src&#x3D;\\&quot;http:\\u002F\\u002Fp6-tt.byteimg.com\\u002Flarge\\u002Fpgc-image\\u002FS5MDUai4jbx7HJ?from&#x3D;pc\\&quot; img_width&#x3D;\\&quot;640\\&quot; img_height&#x3D;\\&quot;441\\&quot; alt&#x3D;\\&quot;佩洛西：若特朗普败选后不离开白宫 就用烟熏出去\\&quot; inline&#x3D;\\&quot;0\\&quot;\\u003E\\u003Cp\\u003E但他的\\&quot;老对手\\&quot;佩洛西对此态度则非常明确。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E在20日的采访中，佩洛西表示，不论是从选民选情还是从宪法制度，特朗普都将于明年1月离任，无论他是否接受这一结果。\\&quot;不管他是否知道（这一结果），他都将离开（白宫）。\\&quot;\\&quot;仅仅因为他可能不想搬出白宫，（这）并不意味着我们就不会为一位正式当选的美国总统举行就职典礼。\\&quot;\\u003C\\u002Fp\\u003E\\u003Cimg src&#x3D;\\&quot;http:\\u002F\\u002Fp3-tt.byteimg.com\\u002Flarge\\u002Fpgc-image\\u002FS5MDUbMAeZ65Pp?from&#x3D;pc\\&quot; img_width&#x3D;\\&quot;640\\&quot; img_height&#x3D;\\&quot;410\\&quot; alt&#x3D;\\&quot;佩洛西：若特朗普败选后不离开白宫 就用烟熏出去\\&quot; inline&#x3D;\\&quot;0\\&quot;\\u003E\\u003Cp\\u003E拜登\\u003C\\u002Fp\\u003E\\u003Cp\\u003E目前距离美国11月总统选举还有不到4个月时间，特朗普在全国和关键摇摆州民调中连续落后于民主党总统竞选人拜登。许多分析人士认为，新冠疫情已造成逾13.7万美国人死亡，重创美国经济，特朗普政府因疫情和种族关系应对方式饱受批评，这些对特朗普连任选情构成了不利影响。\\u003C\\u002Fp\\u003E\\u003Cp\\u003E（编辑：陈娴）\\u003C\\u002Fp\\u003E&quot;"
ss = json.loads(html.unescape(s))
print(ss)
print(type(ss))
