'''
#目前可用的笔趣阁网站，其他可加：
想增加新网站爬取时，建议更改带有（选择）的函数
http://www.biquge.info/
https://www.biquge.com/
http://www.xbiquge.la/
'''

import requests
from bs4 import BeautifulSoup
import random
import time
import re

#可用的网站（此列表除了用来展示，无实际意义）
novel_net=['http://www.biquge.info/','https://www.biquge.com/','http://www.xbiquge.la/']

#可更改：希望延迟秒数范围beg<= ? <=end
beg = 0
end = 0

#可用的网站正则匹配
available_list=["http://www\.biquge\.info/[0-9\_]+/",
               "https://www\.biquge\.com/[0-9\_]+/",
               "http://www\.xbiquge\.la/[0-9]+/[0-9]+/"]

#头
myheaders={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}


#创建txt文件并打开
def create_file(path,name,code):
    #文件路径处理
    if(path==''): 
        full_path=name + ".txt"
    else: 
        full_path = path + "\\" + name + ".txt"
    try:
        fp = open(full_path,'w',encoding=code)
        return fp
    except:
        newpath=input("文件路径不正确,请重新输入文件路径")
        fp=create_file(newpath,name,code)
        return fp
#获取页面编码
def getcode(url):
    try:
        time.sleep(random.randint(int(beg),int(end)))
        r = requests.get(url,headers=myheaders,timeout=30)
        r.raise_for_status()
        return r.apparent_encoding
    except:
        print("获取页面编码失败,5秒后将重新获取")
        time.sleep(5)
        return ''
#获取页面
def gethtml(url, code="utf-8"):
    try:
        time.sleep(random.randint(int(beg),int(end)))
        r = requests.get(url,headers=myheaders)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        print("获取文章失败,5秒后将重新获取")
        time.sleep(5)
        return ''
        
#打印目录列表时获得目录章节名字（选择）
def get_chapter_name(li,choose):
    if(int(choose)<=3):
        i=li.find("a")
        return i.string
        
#下载范围   
def down_range(all_chapter,choose):
    print("本书一共有"+str(len(all_chapter))+"章节")
    count=1
    #打印目录列表
    for i in all_chapter:
        chapter_name=get_chapter_name(i,choose)
        print('{:<7}|{}'.format(count,chapter_name))
        count+=1
    while(1):
        start_range = input("请输入开始下载的序号（默认为1）")
        if(start_range == ''):
            start_range=1
        end_range = input("请输入结束下载的序号（默认为到所有）")
        if(end_range == ''):
            end_range=len(all_chapter)
        try: 
        #查看章节名
            if((see_down_range(all_chapter,start_range,end_range,choose))):
                all_chapter=all_chapter[int(start_range)-1:int(end_range)]
                return all_chapter
                break
        except:         
            print("输入错误,请重新输入")
#查看实际下载范围
def see_down_range(all_chapter,start_range,end_range,choose):
    try:            
        i=all_chapter[int(start_range)-1]
        j=all_chapter[int(end_range)-1]
        i2=get_chapter_name(i,choose)
        j2=get_chapter_name(j,choose)
        print('是否从{:<7}{}\n    到{:<7}{}'.format(start_range,i2,end_range,j2))
        ans=input("输入y为是,n为否")
        if(ans=="n")or(ans=="N"):
            return False
        else:
            return True
    except:
        print("输入错误")
        return False
#获得文章名字（选择）
def getname(soup,choose):
    if(int(choose)<=3):
        return soup.find("h1").string

#获得文章url列表（选择）
def get_all_url(soup,choose):
    if(choose==0)or(choose==2):
        return (soup.find_all("dd"))
    if(choose==1):
        url_list1=soup.find_all("dd")
        if(len(url_list1)>=24):
            url_list=url_list1[12:]
            return url_list
        if(len(url_list1)<24):
            url_list=url_list1[(len(url_list)/2-1):]
            return url_list
    if(choose==3):
        url_list1=soup.find_all("dd")
        url_list=url_list1[:-1]
        return url_list 
#获得每篇文章的url（选择）        
def get_each_url(url,i,choose):
    if(choose==0):
        j=i.find("a")
        return (url + j.get("href"))
    if(choose==1):
        j=i.find("a")
        return ("https://www.biquge.com" + j.get("href"))   
    if(choose==2):
        j=i.find("a")
        return ('http://www.xbiquge.la' + j.get("href"))  
    
#获取文章目录
def download(path,url,choose):
    code=getcode(url)
    while(code==''):
        code=getcode(url)
    text=gethtml(url,code)
    while(text==''):
        text=gethtml(url,code)  
    soup = BeautifulSoup(text, "html.parser")
    #获取书名
    name=getname(soup,choose)
    #获得该文件
    fp=create_file(path,name,code)
    #获得文章url
    all_chapter=get_all_url(soup,choose)
    all_chapter=down_range(all_chapter,choose)
    print("开始下载ww巴拉巴拉呜呜呜呜=v=")
    for i in all_chapter:
        each_url = get_each_url(url,i,choose)
        #章节名
        chapter_name = get_chapter_name(i,choose)
        #文章内容
        chapter=get_chapter(each_url,choose,code)
        fp.write("\n\n"+chapter_name+"\n")
        fp.write(chapter)
        print(chapter_name+"下载成功")
      
    fp.close()
#获取整块文章文本（选择）    
def get_chapter_all(text,choose):
    if(choose==0):
        return (re.findall('<!--go-->(.*?)<!--over-->',text,re.S))
    if(choose==1):
        return (re.findall('<script>readx\(\)\;<\/script>(.*?)<script>chaptererror\(\)\;<\/script>',text,re.S))
    if(choose==2):
        return (re.findall('<div id\=\"content\">(.*?)<br /><br /><p><a',text,re.S))
    if(choose==3):
        return (re.findall('txtrightshow\(\)\;</script></div>(.*?)<div id=\"navup\"></div>',text,re.S))    

#获取文章文本并筛选出标签杂质
def get_chapter(each_url,choose,code):
    text=gethtml(each_url,code)
    #重新获取
    while(text==""):
        text=gethtml(each_url,code)
#.就是任意字符，*就是前面字符有任意多个，参数有re.S，不会对\n进行中断
    try:
        correct = get_chapter_all(text,choose) 
        chapter = correct[0]
        #筛选这里写的不好，但我不知道该怎么写更好
        if(choose==1): chapter = re.sub('^\s+|\s+$','       ',chapter)
        if(choose==3):chapter = re.sub('</div>','',chapter)
        chapter = re.sub('<br />','',chapter)
        chapter = re.sub('<br/>','\n',chapter)
        chapter = re.sub('&nbsp;',' ',chapter)
        return chapter
    except:
        print("程序意外终止")
    
      
 #检查延迟秒数是否更改正确
def check_environment():
    if(beg<0)or(end<0)or(beg>end):
        print("请检查程序延迟秒数是否配置正确，请退出程序重新配置")
        input("任意键退出")
        exit(0)
    else:
        print("============欢迎使用============")
     
#判断链接是否正确输入并且找到对应接口   
def judge(html_url):
    for i in range(len(available_list)):
        if(len(re.findall(available_list[i],html_url))!=0):
            c=re.findall(available_list[i],html_url)
            return c[0],i
            break
    else:
        print("请检查是否输入正确的书籍链接，当前只能下载")
        print(novel_net)
        print('这些网站的书籍')
        return "",-1


def main():
    check_environment()
    while(True):
        html_url=input("请输入要爬取的书籍链接QAQ")
        shore=judge(html_url)
        if(shore[0]!=""):
            break
    path=input("保存的路径（可不填）")
    print("开始分析~~~~请稍等")
    download(path,shore[0],int(shore[1]))
    input("下载结束")
 
main()
