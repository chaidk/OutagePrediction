import numpy as np
import pandas as pd
import os
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 1800)
pd.set_option('expand_frame_repr', False)
def getData():
    pass
def save(data):#保存 打开文件
    data.to_excel('userInformation\data.xls', 'sheet1')
    os.system('userInformation\data.xls')
def user_gds(roudName):#供电所线路用户表
    df = pd.read_excel('userInformation\用户信息统计表.xls', '供电所线路用户', header=2)
    df = df.reset_index()
    for index in df.index:
        if str(df.loc[index]['线路名称']).find(roudName)>=0:
            if df.loc[index]['数据属性']=='整路数据':
                rst = df.loc[index][['运行维护单位','变电站名称','线路名称','小区名称','煤改电村名称','高户名称','高户户数','低户户数','居民户数','煤改电户数','煤改气户数']]
    return rst
def own(roudName):#局属小区
    df = pd.read_excel('userInformation\用户信息统计表.xls', '局属小区', header=1, index_col=0)
    df = df.reset_index(drop=True)
    df.fillna('-', inplace = True)
    rst = pd.DataFrame(columns=df.columns, index=None)
    for index in df.index:
        if str(df.loc[index]['线路名']).find(roudName)>=0:
            rst = rst.append(df.loc[index], ignore_index=True)
    if rst.empty:
        return 0
    rst.set_index('线路名', inplace = True)
    return rst
def userGDS(roudName):#供电所线路用户表
    df = pd.read_excel('userInformation\用户信息统计表.xls', '供电所线路用户', header=2, index_col=0)
    df = df.reset_index(drop=True)
    df.fillna('-', inplace = True)
    rst = pd.DataFrame(columns=df.columns, index=None)
    for index in df.index:
        if str(df.loc[index]['线路名称']).find(roudName)>=0:
            rst = rst.append(df.loc[index], ignore_index=True)
    if rst.empty:
        return 0
    rst.set_index('线路名称', inplace = True)
    return rst



if __name__ == "__main__":

    #data = user_gds('精化')
    #save(data)
    data1 = own('林校南')
    #save(data)
    data2 = userGDS('林校南')
    #print(data)
    #save(data)
    #save(pd.concat([data1,data2], axis=0))

    print(data1)
    print(data2)

    input('-------')