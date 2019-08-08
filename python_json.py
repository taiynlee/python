# -*- coding: utf-8 -*-
"""
Created on Tue May  1 18:35:49 2018

@author: Tommy_Lee
"""

import json

Employee={
"employee_1":{
"姓名": "林小寶",
"年齡": 25,
"地址": "台北市復興南路199號",
"電話":
{
"公司": "0287436472",
"住家": "876894373"
}},
"employee_2":{
"姓名": "江美麗",
"年齡": 35,
"地址": "台北市敦化南路19號",
"電話":
{
"公司": "9876398472",
"住家": "876683944"
}}}

"""
有中文字要ensure_ascii=False, indent=2
"""
company_employee=json.dumps(Employee,ensure_ascii=False, indent=2)
print(company_employee)
company2=json.loads(company_employee)
print(company2)
print(company2.keys())
print(company2.values())