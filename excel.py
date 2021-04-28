# -*- coding: utf-8 -*-
"""
Created by Leon at 4/28/2021

"""
__author__ = "Leon"
__version__ = "0.0.1"
__email__ = "yang.li@zillnk.com"
import pandas as pd
import os


def show(p, filter=None):
    cnt = 0
    for root, dirs, files in os.walk(p):
        for f in files:
            filename = str(f)
            if not filter:
                print(os.path.join(root, filename))
            elif os.path.splitext(filename)[-1] == filter:  # string you want to rename
                try:
                    # os.rename(os.path.join(root , f), os.path.join(root , renames[f]))
                    # print("Renaming ",f,"to",renames[f])
                    #print(os.path.join(root, filename))
                    path = os.path.join(root, filename)
                    info = read_info(path)
                    if not info:
                        #print(path)
                        continue
                    else:
                        print(cnt, ':', info)
                        cnt = cnt + 1
                except FileNotFoundError as e:
                    print(str(e))

def read_sn(file):
    try:
        xls = pd.ExcelFile(file)
        if 'Prod Info' in xls.sheet_names:
            info = xls.parse('Prod Info', header=None)
            #return info.values[1, 1]
            d = {}
            for i in info.index:
                cell_name = info.values[i, 0]
                cell_value = info.values[i, 1]
                #d[cell_name] = cell_value
                if 'Serial Number' in cell_name:
                    return cell_value

            return None
        else:
            return None
    except:
        return None

def read_info(file):
    try:
        xls = pd.ExcelFile(file)
        if 'Prod Info' in xls.sheet_names:
            info = xls.parse('Prod Info', header=None)
            #return info.values[1, 1]
            d = {}
            for i in info.index:
                cell_name = info.values[i, 0]
                cell_value = info.values[i, 1]
                d[cell_name] = cell_value

            if 'Serial Number' in d and 'SW info' in d and 'Test Date' in d:
                #print(d['Serial Number'], ': ', d['SW info'])
                return d['Serial Number'] + ":" + d['SW info'] + ":" + d['Test Date']
        else:
            return None
    except:
        return None


path = r"\\172.16.1.11\\产品开发-公用\\test\\ORU1226 N77A\\2021"
show(p=path, filter='.xlsx')

file = r'\\172.16.1.11\产品开发-公用\test\ORU1226 N77A\2021\Z122601202102000014\20210416174240_TX & RX Cal\160_Z122601202102000014_result_20210416174519.xlsx'
#print(read_info(file))
#xls = pd.ExcelFile(file)

# for sheet in xls.sheet_names:
#     print(sheet)

# if 'Prod Info' in xls.sheet_names:
#     info = xls.parse('Prod Info', header=None)
#     print(info.values[1, 1])
#     #print(type(info))
