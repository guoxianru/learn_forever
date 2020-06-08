# -*- coding: utf-8 -*-
import re
import time

import scrapy

from ..items import TianyanchaItem


class ChaSpider(scrapy.Spider):
    name = 'cha'
    # allowed_domains = ['https://www.tianyancha.com']
    start_urls = ['https://www.tianyancha.com/search']

    def parse(self, response):
        all_strid = response.xpath('//*[@id="search-filter"]/div[2]/div/div[2]/div[1]/a/@href').extract()
        for strid in all_strid:
            for page in range(1, 6):
                url = 'https://www.tianyancha.com/search/p' + str(page) + '?' + strid[34:].strip()
                yield scrapy.Request(url, callback=self.parse_list)

    def parse_list(self, response):
        all_link = response.xpath('//*[@id="web-content"]/div/div[1]/div[2]/div[2]/div/div')
        for link in all_link:
            uuid = link.xpath(".//a/@href").extract_first()[35:]
            name = link.xpath(".//img/@alt").extract_first()
            href = link.xpath(".//a/@href").extract_first()
            yield scrapy.Request(url=href, callback=self.parse_detail,
                                 meta={'name': name, 'href': href, 'uuid': uuid})

    def parse_detail(self, response):

        time.sleep(2)
        item = TianyanchaItem()
        uuid = response.meta['uuid']
        name = response.meta['name']
        href = response.meta['href']

        data = re.sub('\n', '', response.text)

        # 联系方式
        lxfs = {}
        try:
            # 电话
            call_str = re.findall('>电话：(.*?)/span></div>', data, re.S)[0]
            call = [i for i in re.findall('>(.*?)<', call_str) if i != ''][0]
            lxfs.update({'电话': call})
            # 邮箱
            mail_str = re.findall('>邮箱：(.*?)/span></div>', data, re.S)[0]
            mail = [i for i in re.findall('>(.*?)<', mail_str) if i != ''][0]
            lxfs.update({'邮箱': mail})
            # 网址
            link_str = re.findall('>网址：(.*?)/span></div>', data, re.S)[0]
            link = [i for i in re.findall('>(.*?)<', link_str) if i != ''][0]
            lxfs.update({'网址': link})
            # 地址
            addr_str = re.findall('>地址：(.*?)/span></div>', data, re.S)[0]
            addr = [i for i in re.findall('>(.*?)<', addr_str) if i != ''][0]
            lxfs.update({'地址': addr})
            # 简介
            desc_str = re.findall('>简介：(.*?)/span></div>', data, re.S)[0]
            desc = [i for i in re.findall('>(.*?)<', desc_str) if i != ''][0]
            lxfs.update({'简介': desc})
        except:
            lxfs = {'联系方式': '无'}

        # 工商信息
        gsxx = {}
        try:
            # 法定代表人
            faren = re.findall(r'onclick="common.stopPropagation\(event\)">(.*?)</a>', data, re.S)[0]
            gsxx.update({'法定代表人': faren})
            # 注册资本
            zczb_str = re.findall(r'注册资本</td><td width="308px">(.*?)</td>', data, re.S)[0]
            zczb = [i for i in re.findall('>(.*?)<', zczb_str) if i != ''][0]
            gsxx.update({'注册资本': zczb})
            # 实缴资本
            sjzb_str = re.findall(r'实缴资本</td><td width=""(.*?)/td>', data, re.S)[0]
            sjzb = [i for i in re.findall('>(.*?)<', sjzb_str) if i != ''][0]
            gsxx.update({'实缴资本': sjzb})
            # 成立日期
            clsq_str = re.findall(r'成立日期</td><td width="308px"(.*?)/td>', data, re.S)[0]
            clsq = [i for i in re.findall('>(.*?)<', clsq_str) if i != ''][0]
            gsxx.update({'成立日期': clsq})
            # 经营状态
            jyzt_str = re.findall(r'经营状态</td><td width=""(.*?)/td>', data, re.S)[0]
            jyzt = [i for i in re.findall('>(.*?)<', jyzt_str) if i != ''][0]
            gsxx.update({'经营状态': jyzt})
            # 统一社会信用代码
            shxydm_str = re.findall(r'统一社会信用代码</td><td width="308px"(.*?)/td>', data, re.S)[0]
            shxydm = [i for i in re.findall('>(.*?)<', shxydm_str) if i != ''][0]
            gsxx.update({'统一社会信用代码': shxydm})
            # 工商注册号
            gszch_str = re.findall(r'工商注册号</td><td(.*?)/td>', data, re.S)[0]
            gszch = [i for i in re.findall('>(.*?)<', gszch_str) if i != ''][0]
            gsxx.update({'工商注册号': gszch})
            # 纳税人识别号
            nsrsbh_str = re.findall(r'纳税人识别号</td><td width="308px"(.*?)/td>', data, re.S)[0]
            nsrsbh = [i for i in re.findall('>(.*?)<', nsrsbh_str) if i != ''][0]
            gsxx.update({'纳税人识别号': nsrsbh})
            # 组织机构代码
            zzjgdm_str = re.findall(r'组织机构代码</td><td colspan="2"(.*?)/td>', data, re.S)[0]
            zzjgdm = [i for i in re.findall('>(.*?)<', zzjgdm_str) if i != ''][0]
            gsxx.update({'组织机构代码': zzjgdm})
            # 公司类型
            gslx_str = re.findall(r'公司类型</td><td width="308px"(.*?)/td>', data, re.S)[0]
            gslx = [i for i in re.findall('>(.*?)<', gslx_str) if i != ''][0]
            gsxx.update({'公司类型': gslx})
            # 行业
            hangye_str = re.findall(r'行业</td><td colspan="2"(.*?)/td>', data, re.S)[0]
            hangye = [i for i in re.findall('>(.*?)<', hangye_str) if i != ''][0]
            gsxx.update({'行业': hangye})
            # 核准日期
            hzrq_str = re.findall(r'核准日期</td><td(.*?)/td>', data, re.S)[0]
            hzrq = [i for i in re.findall('>(.*?)<', hzrq_str) if i != ''][0]
            gsxx.update({'核准日期': hzrq})
            # 登记机关
            djjg_str = re.findall(r'登记机关</td><td colspan="2"(.*?)/td>', data, re.S)[0]
            djjg = [i for i in re.findall('>(.*?)<', djjg_str) if i != ''][0]
            gsxx.update({'登记机关': djjg})
            # 营业期限
            yyqx_str = re.findall(r'营业期限</td><td width="308px"(.*?)/td>', data, re.S)[0]
            yyqx = [i for i in re.findall('>(.*?)<', yyqx_str) if i != ''][0]
            gsxx.update({'营业期限': yyqx})
            # 纳税人资质
            nsrzz_str = re.findall(r'纳税人资质</td><td colspan="2"(.*?)/td>', data, re.S)[0]
            nsrzz = [i for i in re.findall('>(.*?)<', nsrzz_str) if i != ''][0]
            gsxx.update({'纳税人资质': nsrzz})
            # 人员规模
            rygm_str = re.findall(r'人员规模</td><td width="308px"(.*?)/td>', data, re.S)[0]
            rygm = [i for i in re.findall('>(.*?)<', rygm_str) if i != ''][0]
            gsxx.update({'人员规模': rygm})
            # 参保人数
            cbrs_str = re.findall(r'参保人数</td><td colspan="2"(.*?)/td>', data, re.S)[0]
            cbrs = [i for i in re.findall('>(.*?)<', cbrs_str) if i != ''][0]
            gsxx.update({'参保人数': cbrs})
            # 曾用名
            cengym_str = re.findall(r'曾用名</td><td width="308px"(.*?)/td>', data, re.S)[0]
            cengym = [i for i in re.findall('>(.*?)<', cengym_str) if i != ''][0]
            gsxx.update({'曾用名': cengym})
            # 英文名称
            ywmc_str = re.findall(r'英文名称</td><td colspan="2"(.*?)/td>', data, re.S)[0]
            ywmc = [i for i in re.findall('>(.*?)<', ywmc_str) if i != ''][0]
            gsxx.update({'英文名称': ywmc})
            # 注册地址
            zcdz_str = re.findall(r'注册地址</td><td colspan="4"(.*?)/td>', data, re.S)[0]
            zcdz = [i for i in re.findall('>(.*?)<', zcdz_str) if i != ''][0]
            gsxx.update({'注册地址': zcdz})
            # 经营范围
            jyfw_str = re.findall(r'经营范围</td><td colspan="4"(.*?)/td>', data, re.S)[0]
            jyfw = [i for i in re.findall('>(.*?)<', jyfw_str) if i != ''][0]
            gsxx.update({'经营范围': jyfw})
        except:
            gsxx = {'工商信息': '无'}

        # 主要人员
        zyry = {}
        zyry_str = response.xpath('//*[@id="_container_staff"]/div/table/tbody/tr')
        if len(zyry_str) != 0:
            for ry in zyry_str:
                # 姓名
                xingming = ry.xpath("./td[2]/table//tr/td[2]/a/text()")[0].extract()
                # 职位
                zhiwei = ry.xpath("string(./td[3])")[0].extract()
                zyry.update({xingming: zhiwei})
        else:
            zyry = {'主要人员': '无'}

        # 股东信息
        gdxx = []
        gdxx_str = response.xpath('//*[@id="_container_holder"]/table/tbody/tr')
        if len(gdxx_str) != 0:
            for gd in gdxx_str:
                # 发起人
                try:
                    faqiren = gd.xpath("./td[2]/table//tr/td[2]/a/text()")[0].extract()
                except:
                    faqiren = gd.xpath('./td[2]/table//tr/td[2]/span/text()')[0].extract()
                # 持股比例
                cgbl = gd.xpath("./td[3]/div/div/span/text()")[0].extract()
                # 认缴出资额
                rjcze = gd.xpath("./td[4]/div/span/text()")[0].extract()
                gdxx.append(faqiren + ',' + cgbl + ',' + rjcze)
        else:
            gdxx = ['股东信息: 无']

        # 对外投资
        dwtz = []
        dwtz_str = response.xpath('//*[@id="_container_invest"]/table/tbody/tr')
        if len(dwtz_str) != 0:
            for qy in dwtz_str:
                # 被投资企业名称
                qymc = qy.xpath('./td[2]/table//tr/td[2]/div[1]/a/text()')[0].extract()
                # 法定代表人
                try:
                    qyfr = qy.xpath('string(./td[3])')[0].extract()
                except:
                    qyfr = qy.xpath('./td[3]/table//tr/td[2]/a/text()')[0].extract()
                else:
                    qyfr = qy.xpath('./td[3]/table//tr/td[2]/div[1]/a/text()')[0].extract()
                # 成立日期
                qyrq = qy.xpath('./td[4]/span/text()')[0].extract()
                # 投资数额
                qytz = qy.xpath('./td[5]/span/text()')[0].extract()
                # 投资比例
                qybl = qy.xpath('./td[6]/span/text()')[0].extract()
                # 经营状态
                qyzt = qy.xpath('./td[7]/span/text()')[0].extract()
                # 关联产品
                qycp = qy.xpath('string(./td[8])')[0].extract()
                # 关联机构
                qyjg = qy.xpath('string(./td[9])')[0].extract()
                dwtz.append(
                    qymc + ',' + qyfr + ',' + qyrq + ',' + qytz + ','
                    + qybl + ',' + qyzt + ',' + qycp + ',' + qyjg)
        else:
            dwtz = ['对外投资: 无']

        item['uuid'] = uuid
        item['name'] = name
        item['href'] = href
        item['lxfs'] = lxfs
        item['gsxx'] = gsxx
        item['zyry'] = zyry
        item['gdxx'] = gdxx
        item['dwtz'] = dwtz
        yield item
