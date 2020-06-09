# -*- coding: utf-8 -*-
# -*- author: GXR -*-
import requests
import re
from lxml import etree

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
    'Cookie': 'TYCID=7abe93109bb011e9a20641c848bcf009; undefined=7abe93109bb011e9a20641c848bcf009; ssuid=5120513320; _ga=GA1.2.895057816.1562047464; _gid=GA1.2.494401681.1562047464; RTYCID=4c2d3b97771c45f5a88d7cc6360f6a8d; CT_TYCID=4ed79b6e147c43a39616b01d69a0fe74; aliyungf_tc=AQAAAGt3LB0cIgEA3Nj5cl8qpK3meB74; csrfToken=9VnHI3sYw6iD3d0zwrncyOll; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1562207900,1562222313,1562291658,1562313322; bannerFlag=true; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522Quiet.G%2522%252C%2522integrity%2522%253A%252214%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM4MzMwNjMzNyIsImlhdCI6MTU2MjMyNDcyOSwiZXhwIjoxNTkzODYwNzI5fQ.L_vEigjjY1w-h1fC8I_wZGXDBHM09F_QQwfC3IdrMxcNN515znN_OOGzSgsp2wQlrC6rqdWAAVrk3OGQ5SxmBw%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213383306337%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM4MzMwNjMzNyIsImlhdCI6MTU2MjMyNDcyOSwiZXhwIjoxNTkzODYwNzI5fQ.L_vEigjjY1w-h1fC8I_wZGXDBHM09F_QQwfC3IdrMxcNN515znN_OOGzSgsp2wQlrC6rqdWAAVrk3OGQ5SxmBw; cloud_token=d71b406a04304ded9136b1a504da909e; cloud_utm=62ecb2dad14f4ba9b1fe8cb65d098539; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1562324926',
}

# url = 'https://www.tianyancha.com/company/353800390'
# url = 'https://www.tianyancha.com/company/285490493'
# url = 'https://www.tianyancha.com/company/1150439899'
# url = 'https://www.tianyancha.com/company/3330338714'
# url = 'https://www.tianyancha.com/company/3069334211'
url = 'https://www.tianyancha.com/company/246162387'

response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
print('==========' + '%s' % response.status_code + '==========')
html = etree.HTML(response.text)
data = re.sub('\n', '', response.text)

# # 联系方式
# lxfs = {}
# try:
#     # 电话
#     call_str = re.findall('>电话：(.*?)/span></div>', data, re.S)[0]
#     call = [i for i in re.findall('>(.*?)<', call_str) if i != ''][0]
#     lxfs.update({'电话': call})
#     # 邮箱
#     mail_str = re.findall('>邮箱：(.*?)/span></div>', data, re.S)[0]
#     mail = [i for i in re.findall('>(.*?)<', mail_str) if i != ''][0]
#     lxfs.update({'邮箱': mail})
#     # 网址
#     link_str = re.findall('>网址：(.*?)/span></div>', data, re.S)[0]
#     link = [i for i in re.findall('>(.*?)<', link_str) if i != ''][0]
#     lxfs.update({'网址': link})
#     # 地址
#     addr_str = re.findall('>地址：(.*?)/span></div>', data, re.S)[0]
#     addr = [i for i in re.findall('>(.*?)<', addr_str) if i != ''][0]
#     lxfs.update({'地址': addr})
#     # 简介
#     desc_str = re.findall('>简介：(.*?)/span></div>', data, re.S)[0]
#     desc = [i for i in re.findall('>(.*?)<', desc_str) if i != ''][0]
#     lxfs.update({'简介': desc})
# except:
#     lxfs = {'联系方式': '无'}
# print(lxfs)

# # 工商信息
# gsxx = {}
# try:
#     # 法定代表人
#     faren = re.findall(r'onclick="common.stopPropagation\(event\)">(.*?)</a>', data, re.S)[0]
#     gsxx.update({'法定代表人': faren})
#     # 注册资本
#     zczb_str = re.findall(r'注册资本</td><td width="308px">(.*?)</td>', data, re.S)[0]
#     zczb = [i for i in re.findall('>(.*?)<', zczb_str) if i != ''][0]
#     gsxx.update({'注册资本': zczb})
#     # 实缴资本
#     sjzb_str = re.findall(r'实缴资本</td><td width=""(.*?)/td>', data, re.S)[0]
#     sjzb = [i for i in re.findall('>(.*?)<', sjzb_str) if i != ''][0]
#     gsxx.update({'实缴资本': sjzb})
#     # 成立日期
#     clsq_str = re.findall(r'成立日期</td><td width="308px"(.*?)/td>', data, re.S)[0]
#     clsq = [i for i in re.findall('>(.*?)<', clsq_str) if i != ''][0]
#     gsxx.update({'成立日期': clsq})
#     # 经营状态
#     jyzt_str = re.findall(r'经营状态</td><td width=""(.*?)/td>', data, re.S)[0]
#     jyzt = [i for i in re.findall('>(.*?)<', jyzt_str) if i != ''][0]
#     gsxx.update({'经营状态': jyzt})
#     # 统一社会信用代码
#     shxydm_str = re.findall(r'统一社会信用代码</td><td width="308px"(.*?)/td>', data, re.S)[0]
#     shxydm = [i for i in re.findall('>(.*?)<', shxydm_str) if i != ''][0]
#     gsxx.update({'统一社会信用代码': shxydm})
#     # 工商注册号
#     gszch_str = re.findall(r'工商注册号</td><td(.*?)/td>', data, re.S)[0]
#     gszch = [i for i in re.findall('>(.*?)<', gszch_str) if i != ''][0]
#     gsxx.update({'工商注册号': gszch})
#     # 纳税人识别号
#     nsrsbh_str = re.findall(r'纳税人识别号</td><td width="308px"(.*?)/td>', data, re.S)[0]
#     nsrsbh = [i for i in re.findall('>(.*?)<', nsrsbh_str) if i != ''][0]
#     gsxx.update({'纳税人识别号': nsrsbh})
#     # 组织机构代码
#     zzjgdm_str = re.findall(r'组织机构代码</td><td colspan="2"(.*?)/td>', data, re.S)[0]
#     zzjgdm = [i for i in re.findall('>(.*?)<', zzjgdm_str) if i != ''][0]
#     gsxx.update({'组织机构代码': zzjgdm})
#     # 公司类型
#     gslx_str = re.findall(r'公司类型</td><td width="308px"(.*?)/td>', data, re.S)[0]
#     gslx = [i for i in re.findall('>(.*?)<', gslx_str) if i != ''][0]
#     gsxx.update({'公司类型': gslx})
#     # 行业
#     hangye_str = re.findall(r'行业</td><td colspan="2"(.*?)/td>', data, re.S)[0]
#     hangye = [i for i in re.findall('>(.*?)<', hangye_str) if i != ''][0]
#     gsxx.update({'行业': hangye})
#     # 核准日期
#     hzrq_str = re.findall(r'核准日期</td><td(.*?)/td>', data, re.S)[0]
#     hzrq = [i for i in re.findall('>(.*?)<', hzrq_str) if i != ''][0]
#     gsxx.update({'核准日期': hzrq})
#     # 登记机关
#     djjg_str = re.findall(r'登记机关</td><td colspan="2"(.*?)/td>', data, re.S)[0]
#     djjg = [i for i in re.findall('>(.*?)<', djjg_str) if i != ''][0]
#     gsxx.update({'登记机关': djjg})
#     # 营业期限
#     yyqx_str = re.findall(r'营业期限</td><td width="308px"(.*?)/td>', data, re.S)[0]
#     yyqx = [i for i in re.findall('>(.*?)<', yyqx_str) if i != ''][0]
#     gsxx.update({'营业期限': yyqx})
#     # 纳税人资质
#     nsrzz_str = re.findall(r'纳税人资质</td><td colspan="2"(.*?)/td>', data, re.S)[0]
#     nsrzz = [i for i in re.findall('>(.*?)<', nsrzz_str) if i != ''][0]
#     gsxx.update({'纳税人资质': nsrzz})
#     # 人员规模
#     rygm_str = re.findall(r'人员规模</td><td width="308px"(.*?)/td>', data, re.S)[0]
#     rygm = [i for i in re.findall('>(.*?)<', rygm_str) if i != ''][0]
#     gsxx.update({'人员规模': rygm})
#     # 参保人数
#     cbrs_str = re.findall(r'参保人数</td><td colspan="2"(.*?)/td>', data, re.S)[0]
#     cbrs = [i for i in re.findall('>(.*?)<', cbrs_str) if i != ''][0]
#     gsxx.update({'参保人数': cbrs})
#     # 曾用名
#     cengym_str = re.findall(r'曾用名</td><td width="308px"(.*?)/td>', data, re.S)[0]
#     cengym = [i for i in re.findall('>(.*?)<', cengym_str) if i != ''][0]
#     gsxx.update({'曾用名': cengym})
#     # 英文名称
#     ywmc_str = re.findall(r'英文名称</td><td colspan="2"(.*?)/td>', data, re.S)[0]
#     ywmc = [i for i in re.findall('>(.*?)<', ywmc_str) if i != ''][0]
#     gsxx.update({'英文名称': ywmc})
#     # 注册地址
#     zcdz_str = re.findall(r'注册地址</td><td colspan="4"(.*?)/td>', data, re.S)[0]
#     zcdz = [i for i in re.findall('>(.*?)<', zcdz_str) if i != ''][0]
#     gsxx.update({'注册地址': zcdz})
#     # 经营范围
#     jyfw_str = re.findall(r'经营范围</td><td colspan="4"(.*?)/td>', data, re.S)[0]
#     jyfw = [i for i in re.findall('>(.*?)<', jyfw_str) if i != ''][0]
#     gsxx.update({'经营范围': jyfw})
# except:
#     gsxx = {'工商信息': '无'}
# print(gsxx)

# # 主要人员
# zyry = {}
# zyry_str = html.xpath('//*[@id="_container_staff"]/div/table/tbody/tr')
# if len(zyry_str) != 0:
#     for ry in zyry_str:
#         # 姓名
#         xingming = ry.xpath("./td[2]/table//tr/td[2]/a/text()")[0]
#         # 职位
#         zhiwei = ry.xpath("string(./td[3])")
#         zyry.update({xingming: zhiwei})
# else:
#     zyry = {'主要人员': '无'}
# print(zyry)

# # 股东信息
# gdxx = []
# gdxx_str = html.xpath('//*[@id="_container_holder"]/table/tbody/tr')
# if len(gdxx_str) != 0:
#     for gd in gdxx_str:
#         # 发起人
#         faqiren = gd.xpath("./td[2]/table/tbody/tr/td[2]/a/text()")[0]
#         # 持股比例
#         cgbl = gd.xpath("./td[3]/div/div/span/text()")[0]
#         # 认缴出资额
#         rjcze = gd.xpath("./td[4]/div/span/text()")[0]
#         gdxx.append(faqiren + ',' + cgbl + ',' + rjcze)
# else:
#     gdxx = ['股东信息: 无']
# print(gdxx)

# 对外投资
# dwtz = []
# dwtz_str = html.xpath('//*[@id="_container_invest"]/table/tbody/tr')
# if len(dwtz_str) != 0:
#     for qy in dwtz_str:
#         # 被投资企业名称
#         qymc = qy.xpath('./td[2]/table//tr/td[2]/div[1]/a/text()')[0]
#         # 法定代表人
#         try:
#             qyfr = qy.xpath('./td[3]/table//tr/td[2]/div[1]/a/text()')[0]
#         except:
#             qyfr = qy.xpath('./td[3]/table//tr/td[2]/a/text()')[0]
#         # 成立日期
#         qyrq = qy.xpath('./td[4]/span/text()')[0]
#         # 投资数额
#         qytz = qy.xpath('./td[5]/span/text()')[0]
#         # 投资比例
#         qybl = qy.xpath('./td[6]/span/text()')[0]
#         # 经营状态
#         qyzt = qy.xpath('./td[7]/span/text()')[0]
#         # 关联产品
#         qycp = qy.xpath('string(./td[8])')
#         # 关联机构
#         qyjg = qy.xpath('string(./td[9])')
#         dwtz.append(qymc + ',' + qyfr + ',' + qyrq + ',' + qytz + ',' + qybl + ',' + qyzt + ',' + qycp + ',' + qyjg)
# else:
#     dwtz = ['对外投资: 无']
# print(dwtz)
