#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
source = {
    "username" : "fuyongde",
    "password" : "password"
}

json_str = json.dumps(source)

print("原文：", source)

print("JSON:", json_str)