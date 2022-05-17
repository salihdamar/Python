"""Çok Mesaj Geldiği için Böyle Bir Açıklama Yaptım.
for ile  ' l ' listesinin elemanlarını tek tek tarıyoruz. Aslında for döngüsü gibi gözüküyor ama  bu bir foreach döngüsüdür.

if ile aldığımız elemanlar hala liste halinde mi yoksa eleman halinde mi. isinstance bunu sorguluyor. Eğer hala liste halinde ise tekrar
elemanları listeden çıkarmak için if bloğu içerisinde tekrar flatten fonsiyonun çağırıyorum. Flatten fonksiyonu içerisinde Flatten fonsiyonunu
tekrar tekrar çağırıyoruz. taki elemanlar liste halinde değilde tek düz halde olsun. liste halinde değilse lnew.append(i) ile lnew listesine ekliyoruz.


l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

1- l[0]=[1,'a',['cat'],2]-->list tipinde ise liste tipinden çıkart
        -l=1
        -l='a'
        -l=['cat'] -->list tipinde ise liste tipinden çıkart
             - l='cat'
        -l=2
        
2- l[1]=[[[3]],'dog'] -->list tipinde ise liste tipinden çıkart
        -l=[[3]] -->list tipinde ise liste tipinden çıkart
            -l=[3] -->list tipinde ise liste tipinden çıkart
                -l=3
        -l='dog'

3- l[2]=4
4- l[3]=5
"""

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
lnew = []
def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            lnew.append(i)

flatten(l)
print(lnew)
