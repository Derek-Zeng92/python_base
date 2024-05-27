
import requests # 下载网页
import bs4 # beautifulSoup，解析网页

headers={
    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding':'gzip, deflate, br, zstd',
    # 'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    # 'Connection':'keep-alive',
    # 'Cache-Control':'no-cache',
    # 'Host':'www.douban.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

def download_page(url):
    '''
    下载指定页面及其所有分页
    :param url:
    :return:
    '''

    page_obj =requests.get(url,headers=headers)
    bs4_obj=bs4.BeautifulSoup(page_obj.text,'lxml')

    url_set=set()
    bs4_page_obj_list=[bs4_obj] # 把刚才下载的第一一页，先放进去 统一提取所有数据
    paginator_ele = bs4_obj.find('div',attrs={'class':'paginator'})
    if paginator_ele: # 如有有分页拿到所有分页
        for a_ele in paginator_ele.find_all('a'):
            url_set.add(a_ele.attrs.get('href'))

        for url in url_set:
            print(f'下载分页：{url}')
            page_obj=requests.get(url,headers=headers)
            bs4_page_obj=bs4.BeautifulSoup(page_obj.text,'lxml')
            bs4_page_obj_list.append(bs4_page_obj) # 先暂存

    return bs4_page_obj_list

all_bs4_page_list=download_page('https://www.douban.com/group/topic/254968751/?_i=5585752RutQKYR')

def fetch_replys(page_obj_list):
    reply_list=[]
    for bs4_obj in page_obj_list:
        comment_eles=bs4_obj.find_all('div',attrs={'class':'reply-doc'})
        for ele in comment_eles:
            comment_ele=ele.find('p',attrs={'class':'reply-content'})
            reply_list.append(comment_ele.text)
            print(comment_ele.text)
    print(len(reply_list))
fetch_replys(all_bs4_page_list)