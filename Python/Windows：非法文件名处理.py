# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

import os
import re


def clean_field(file_name):
    c_str = r"[\/\\\:\*\?\"\<\>\|]"
    clean_name = re.sub(c_str, "-", file_name)
    try:
        open(clean_name + ".txt", "w+")
        os.remove(clean_name + ".txt")
        return clean_name
    except:
        pass


print(clean_field(":.txt"))
