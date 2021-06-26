import requests
import re
import time
import json
import pandas as pd

headers = {
    'referer': 'https://detail.tmall.com/item.htm?id=535651561398&spm=a1z09.2.0.0.47632e8d8Yllvg&_u=p3qpi1dc3df0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'cookie': 't=fa0c081e55baeee248405486e1dea6f4; _tb_token_=e15e56b585038; cookie2=1e63abc08aea3af6d504a9ec6456bc72; cna=LhhFGGT46iYCAd9oJKLqK75u; xlly_s=1; dnk=tb910937679; uc1=cookie14=Uoe0azUEaEkI5g%3D%3D&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=URm48syIYn73; uc3=id2=Vy0RpYbwy8lQtA%3D%3D&nk2=F5RMGLZB8aVcjqM%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&vt3=F8dCufwnjf0WjrucHcA%3D; tracknick=tb910937679; lid=tb910937679; _l_g_=Ug%3D%3D; uc4=nk4=0%40FY4HXZ%2FSHXr%2FSqjl1xrfe0NSRTQnbw%3D%3D&id4=0%40VXqfvNjTE1%2BMjjUlVD0hxyKfw0ax; unb=4120446380; lgc=tb910937679; cookie1=ACO%2FjY1lB9iFHuJCu6BbSfr7lyTRzUuejdY2faLIJJI%3D; login=true; cookie17=Vy0RpYbwy8lQtA%3D%3D; _nk_=tb910937679; sgcookie=E100aetb3N2YMeGp1vlxKQZ%2F560hIRWW4uhYXMsBJsn2m%2BFwsyYQvT%2BjYZ2vFE%2Be7pGYKIfjVshv59rRlgAmjw9b8Q%3D%3D; sg=90f; csg=c557052f; tfstk=c37GBu43VG-1u-KhVPT1wXNXEzjGZPywQZ7O8wkRyAzhD_bFiBoE4EIbtpWGkm1..; l=eBP3LuQ4OC-14SgfBO5Churza779fIOb8sPzaNbMiInca1zFwUc1RNQV8EhBkdtj_tCfletruwYsJRHX-BzdgZqhuJ1REpZZexvO.; isg=BJ6eLmGpTXdqE5kTZVIt_d517zTgX2LZu67ApkgmaeH2az9FsO7c6exNZ3_n01rx'
}
pat = re.compile('"rateContent":"(.*?)","fromMall"')
texts = []

print('程序开始运行：')
for i in range(1,4):
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=535651561398&spuId=651248066&sellerId=1049653664&order=3&currentPage='+ str(i) +'&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvj9vcvOIvUpCkvvvvvjiWP2dWQjl8R2Lh6j1VPmPWQjDnRFLpljrWn2cwljnmRL9CvvpvvhCvdvhvmpmvqKK1vvm6%2B4QCvvyv9PfsWQvv%2Bq4%2BvpvLCO2wzFQvvCOTEBY7rX63rqwT88QCvvyv9bKTgpvvHXJ%2BvpvEvvhOVoWvvCbTRvhvCvvvphvUvpCW9bFsG10xdBkKDVQEfaoK5d8raAitD40Od3ODN%2BBl5d8re161D70fdiTinh4DKfWcWsySp903%2B2e3rABCIE7reuTZfvDrs8TJ%2Bulsbd9Cvm9vvhCvvvvvvvvvBZZvvUCDvvCHBpvvv79vvhxHvvvC4vvvBZZvvvHIkvhvC9hvpyP9l89Cvv9vvhh6Mlld%2FpvCvvOvChCvvvvRvpvhvv2MMs9CvvpvvhCvi9hvCvvvpZoVvpvhvUCvp8QCvvyv9EKf%2Fvvv3PevvpvJfHlizGcw7Di4JGPNoIdvSGRj%2FkWU4w5C3q6qZ6uUdvhvmpmC4edovvvBLTQCvvyvvpgPv9vv5O8%2BvpvEvvmlrPyvv2vRdvhvmpmvmvyHvvm1MOvCvv147zpv3Y147Ddh%2BaG%3D&needFold=0&_ksTS=1606306775735_4719&callback=jsonp4720'
    data = requests.get(url, headers = headers).text
    txt = pat.findall(data)
    texts.extend(txt)
    print('...')
    time.sleep(3)
print('程序结束运行。')
df = pd.DataFrame()
df['评论'] = texts
df.to_excel('原始数据集.xlsx')