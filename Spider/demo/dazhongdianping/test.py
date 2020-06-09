# -*- coding: utf-8 -*-
# -*- author: GXR -*-
address_true = [
    '&#xf889;', '&#xea50;', '&#xf7b1;', '&#xec98;', '&#xf898;', '&#xf28e;', '照相', '&#xf7f4;', '&#xf3a8;',
    '&#xf40b;', '胡', '&#xf4e3;', '&#xed40;', '&#xe15e;', '&#xe9c9;', '&#xea01;', '&#xe616;', '&#xe1f8;',
    '涮(', '&#xf889;', '&#xe3ae;', '&#xf898;', '&#xe71f;', '&#xe479;', '&#xe616;', '&#xe479;', '&#xe25e;',
    '1', '&#xe6c2;', '&#xe9c9;', '左转', '&#xea01;', '&#xe616;', '&#xe1f8;', '涮) '
]
address_list = [
    ['王', 'unif889'], ['井', 'uniea50'], ['大', 'unif7b1'], ['街', 'uniec98'], ['中', 'unif898'],
    ['国', 'unif28e'], ['馆', 'unif7f4'], ['对', 'unif3a8'], ['面', 'unif40b'], ['同', 'unif4e3'],
    ['2', 'unied40'], ['8', 'unie15e'], ['米', 'unie9c9'], ['京', 'uniea01'], ['门', 'unie616'],
    ['九', 'unie1f8'], ['王', 'unif889'], ['府', 'unie3ae'], ['中', 'unif898'], ['环', 'unie71f'],
    ['南', 'unie479'], ['门', 'unie616'], ['南', 'unie479'], ['行', 'unie25e'], ['5', 'unie6c2'],
    ['米', 'unie9c9'], ['京', 'uniea01'], ['门', 'unie616'], ['九', 'unie1f8']
]
for i in range(len(address_true)):
    for k in address_list:
        if k[1][-4:] == address_true[i][-5:-1]:
            print(address_true[i])
            address_true[i] = k[0]
            print(address_true[i])
print(address_true)
