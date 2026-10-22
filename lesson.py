# print("Hello, World!")
# customer_age = 30
# _total = 1996
#2user = "Python" xeta verecek deyiseninn adi reqemle baslaya bilmez
#Dəyişən adları hərf ilə başlaya bilər;
#Dəyişən adı rəqəm ilə başlaya bilməz;
#Dəyişən adında _ ola bilər;
#Dəyişən adında boşluq ola bilməz;
#Dəyişən adları case sensitive-dir(böyük və kiçik hərf fərqlidir);
#Açar sözləri dəyişən adı kimi istifadə etmək olmaz.

pi=3.14
radius=5
area=pi*radius**2
a,b,c=5,10,15

# c=96 + 5j #96+5*i  complex type
# d=complex(96, 5)   complex type
# print(c, type(c))   complex type
# print(d, type(d))   complex type

# language = "Python"
# print(language * 3)

text = "  hello python  "
print(text.lower())       # "  hello python  "
print(text.upper())       # "  HELLO PYTHON  "
print(text.title())       # "  Hello Python  "
print(text.capitalize())  # "  hello python  "
print(text.strip())       # "hello python"
print(text.lstrip())      # "hello python  "
print(text.rstrip())      # "  hello python"
print(text.replace("python", "world"))  # "  hello world  "
print(text.count("o"))    # 2
print(text.find("python"))  # 8
print(text.startswith("  hello"))  # True
print(text.endswith("oiln  "))  # False

#len() ilə həm stringlərdə simvol sayını, həm də listdəki element sayını tapa bilərik:
#language="Python"
# ededler = [5, 96.5, 27, 9, 98]
#print("String-dəki simvol sayı:", len(language))
# print(ededler)
# print("List-dəki element sayı", len(ededler))
# len() ədədlər üçün işləmir. Yəni, ədəddəki rəqəm sayını len() ilə tapa bilmərik.
# year=1996    error
# print(len(year))    error

list1 = [5, 96.5, 27, 9, 98]
list1.append(100) #metodu ilə listə yeni element əlavə edə bilərik:extend-de icine metod elave olunur
list1.extend([101, 102]) #metodu ilə listə yeni elementlər əlavə edə bilərik:extend-de icine metod elave olunmur
list1.insert(5, 35) #metodu ilə listin istənilən indeksinə yeni element əlavə edə bilərik:
list1.remove(3) #metodu ilə listdən istənilən elementi silə bilərik:
list1.pop(2) #metodu ilə listdən istənilən indeksi silə bilərik:
list1.clear() #metodu ilə listin bütün elementlərini silə bilərik:
list1.index(5) #metodu ilə listdə istənilən elementin indeksini tapa bilərik:   
list1.count(2) #metodu ilə listdə istənilən elementin sayını tapa bilərik:
list1.sort() #metodu ilə listdəki elementləri kiçikdən böyüyə doğru sıralaya bilərik:
list1.reverse() #metodu ilə listdəki elementləri tərs qaydada sıralaya bilərik:
list1.copy() #metodu ilə listin surətini çıxara bilərik:

# Tuple-Mötərizə içində yazılırlar;indekslə mövcuddur;immutable-dır;
# Tərkibi dəyişdirilə bilməz(immutable). Bu xüsusiyyət tuple-ları digər tiplərdən ayıran əsas xüsusiyyətdir.
# Elementlər mötərizə içinə alınır. Bir tuple hər tipdə məlumatı daxilində saxlaya bilər.
# tuplenin icindeki melumati deyismek olmur ama arraydaki veyabasqa melumat tipindeki deyisenleri deyisilir
t=(96, [27, 7], True, 'Kiev')
# t[2]=1996-error
t[1][1]=1996 #bburda deyise bilirik cunki icindeki element listdir ve list mutable-dir
#Hər hansı bir elementin tuple içində olub olmadığını yoxlaya bilərik.
print(t)
print(1996 in t) #True
print(1998 in t) #False
t1=(96, 5, 27, 7, 9, 98)
print(len(t1)) #some tuple function
print(sum(t1)) #some tuple function
print(max(t1)) #some tuple function
print(min(t1)) #some tuple function
#index() funksiyası ilə biz axtardığımız hər hansı bir elementin indeksini tapa bilərik.Axtarılan element 
# tuple-ın daxilində varsa indeksini qaytarır, əks halda elementin olmadığına dair xəta verir.
print(t.index(96)) #0 olacaq cavab cunki 0ci indeksinde var
print(t.index(98.5)) #ValueError: tuple.index(x): x not in tuple
# tuple-lar mötərizə içində göstərilir. Lakin tək elementli tuple-da elementdən sonra vergül 
# qoymasaq bu tuple qəbul edilmir. Elementin tipi nədirsə elə o da qəbul edilir
t=(5)
print(type(t)) #<class 'int'>
t=(5,) #vergul elave etdik 
print(type(t)) #<class 'tuple'>
#Son olaraq bəzi üstünlüklərindən danışacağam: List-lərlə müqayisədə müəyyən əməliyyatlarda daha az yaddaş
#istifadə edə və daha sürətli ola bilər. Elementlərin dəyişdirilməməsi lazım olan yerlərdə istifadəsi 
#üstünlük yaradır.



#Set(Çoxluq)Set riyaziyyatdakı çoxluq anlayışına oxşayır. Əsas xüsusiyyətləri aşağıdakı kimidir:
#təkrar element saxlamır(təkrar element varsa avtomatik silinir);müxtəlif tipdə məlumat saxlaya bilərlər;
#indekslə işləmir;mutable-dır;elementlər sırasızdır.
s = {96, 'Kiev', 5.96, 96}
print(s) #cavab: {96, 5.96, 'Kiev'}-burda 96 bir defe yazilib cunku setde tekrarlanan elementler olmur
s.add("London") #metodu ilə set-ə yeni element əlavə edə bilərik:
s.update([27, "iyul"]) #metodu ilə set-ə yeni elementlər əlavə edə bilərik:
s.discard(27) # konkret 27 elementini silir.
s.remove(27) # konkret 27 elementini silir, amma element yoxdursa xəta verir.
s.pop() # set-dən bir elementi silir və həmin elementi qaytarır.
s.clear() # bütün elementləri silir.



A={27, 7, 2023, 9}
B={5, 96, 98, 27}
print("Birləşmə:", A.union(B)) #ansver: {5, 96, 98, 27, 7, 2023, 9}
print("Kəsişmə:", A.intersection(B)) #ansver: {27}
print("Fərq(A-da var, B-də yoxdur):", A.difference(B)) #ansver: {9, 2023, 7}


#Dictionary dictionary məlumatı {key:value} cütlüyü şəklində saxlayır.Dictionary daxilində hər key
# unikal olmalıdır. Eyni key yenidən yazılarsa, əvvəlki value son verilən value ilə əvəz olunur.
d = {
    "m": 5,
    "il": 1996,
    "bal": 96,
    "m": 55
}

print(d) #ansver: {'m': 55, 'il': 1996, 'bal': 96}
print(d['il'])  #ansver: 1996
print("m" in d) #ansver: True
d['m']=5.96 #deyeri deyisirik
print(d) #ansver: {'m': 5.96, 'il': 1996, 'bal': 96}
#print(d['s']) #ansver: KeyError: 's' - dictionaryde olmayan key-i cagirmaq error verir
#Daha təhlükəsiz variant isə get() istifadə etməkdir:
print(d.get('m', 'yoxdur')) #ansver: 5.96
print(d.get('s', 'yoxdur')) #ansver: yoxdur
#added new data
d.update({
    'month':'may',
    'language': 'python'
})
print(d) #ansver: {'m': 5.96, 'il': 1996, 'bal': 96, 'month': 'may', 'language': 'python'}
del d['month'] #metodu ilə dictionary-dən istənilən key-value cütlüyünü silə bilərik:
print("Açarlar:", d.keys()) #ansver: Açarlar: dict_keys(['m', 'il', 'bal', 'language'])
print("Dəyərlər:", d.values()) #ansver: Dəyərlər: dict_values([5.96, 1996, 96, 'python'])
print("Həm açarlar, həm dəyərlər:", d.items()) #ansver: Həm açarlar, həm dəyərlər: dict_items([('m', 5.96), ('il', 1996), ('bal', 96), ('language', 'python')])
#Son olaraq isə dictionary daxilində başqa dictionary saxlaya bilərik:
isciler = {
    "IT": {
        "Aysel": 2500,
        "Emin": 3000
    },
    "Data": {
        "Seymur": 4500
    }
}
print(isciler) #ansver: {'IT': {'Aysel': 2500, 'Emin': 3000}, 'Data': {'Seymur': 4500}}
print(isciler['IT']) #ansver: {'Aysel': 2500, 'Emin': 3000}

#Beləliklə, Python-da List, Tuple, Set və Dictionary məlumatları fərqli məqsədlər üçün saxlamağa və 
#idarə etməyə imkan verən əsas məlumat strukturlarıdır. Hansı strukturun seçilməsi isə məlumatların 
#sıralı olub-olmaması, dəyişdirilməsi, təkrarlanması və onlara necə müraciət edilməsi kimi tələblərdən 
#asılıdır. Bu strukturların xüsusiyyətlərini və fərqlərini düzgün anlamaq, sonrakı mərhələlərdə daha 
#səmərəli və oxunaqlı Python kodu yazmaq üçün vacib təməl yaradır.


#-----------if else elif-------------- Conditional Statements

bal=96
print("if-dən əvvəl")
if bal>=90:
    print("telebe kecdi")
print("if-dən sonra") #ansver: if-dən əvvəl telebe kecdi if-dən sonra

bal=86
if bal>50:
    print("telebe kecdi")
else:
    print("telebe kesildi") #ansver: telebe kecdi

s=96
if s>=90:
    print("telebe kecdi")
elif s>=80:
    print("telebe kecdi amma bali 80-90 araligindadir")
elif s>=70:
    print("telebe kecdi amma bali 70-80 araligindadir")
else:
    print("telebe kesildi")

salary = 590
year = 1996

if salary>= 500 and year >= 1995:
    print("Şərtlər ödənilir")

salary = 490
year = 1996

if salary>= 500 and year >= 1995:
    print("Şərtlər ödənilir")
    
else:
    print("Şərtlər ödənilmir")

age = 5
year = 1996

if age >= 18 or year >= 1995:
    print("Şərtlərdən ən azı biri ödənilir")

#not -> nəticəni əksinə çevirir. Yəni, True False olur, False True. Kod üstündə baxaq:
is_blocked = False
if not is_blocked:
    print("İstifadəçi sistemə daxil ola bilər")


#-----------------for and while loops-----------------  iterative Statements
month="may"
for element in month:
    print(element) #ansver: m a y

d = {
    "m": 96.5,
    "il": 1996,
    "bal": 96,
}

for key in d.keys():
    print(key) #ansver: m il bal

for value in d.values():
    print(value) #ansver: 96.5 1996 96

numbers = [5, 96.5, 27, 9, 98]
cem=0
for number in numbers:    
    cem+=number
print("Cəm:", cem) #ansver: Cəm: 235.5

#range() funksiyası ilə müəyyən bir aralıqda ədədlər yarada bilərik
for i in range(5):
    print(i) #ansver: 0 1 2 3 4

for i in range(5, 10): #given range(start, stop)
    print(i) #ansver: 5 6 7 8 9

for i in range(5, 10, 2): #given range(start, stop, step) 
    print(i) #ansver: 5 7 9

for i in range(10, 5, -1): #given range(start, stop, step)
    print(i) #ansver: 10 9 8 7 6

for i in range(5, 10):
    if i%2==0:
        print(i) #ansver: 6 8

names = ["May", "Python", "July", "Machine Learning"]
for index,name in enumerate(names):
    print(index,name) #ansver: 0 May 1 Python 2 July 3 Machine Learning
    print(f"{index} {name}") #ansver: 0 May 1 Python 2 July 3 Machine Learning--burada f-stringe cevirir her seyi reqem string seklinde gorseni
    print(len(names)) #ansver 4

for i in range(len(names)):
    print(i, names[i]) #ansver: 0 May 1 Python 2 July 3 Machine Learning


#zip() iki və ya daha çox ardıcıllığın uyğun mövqedəki elementlərini birləşdirir.
olkeler = [
    "Azərbaycan",
    "Ukrayna",
    "İspaniya",
    "İngiltərə",
    "Türkiyə",
]

paytaxtlar = [
    "Bakı",
    "Kiev",
    "Madrid",
    "London",
    "Ankara",
]

for olke,paytaxt in zip(olkeler,paytaxtlar):
    print(olke,paytaxt) #ansver: Azərbaycan Bakı Ukrayna Kiev İspaniya Madrid İngiltərə London Türkiyə Ankara

for sira,olke_paytaxt in enumerate(zip(olkeler,paytaxtlar)):
    print(sira,olke_paytaxt) #ansver: 0 ('Azərbaycan', 'Bakı') 1 ('Ukrayna', 'Kiev') 2 ('İspaniya', 'Madrid') 3 ('İngiltərə', 'London') 4 ('Türkiyə', 'Ankara')

for sira, melumat in enumerate(zip(olkeler, paytaxtlar)):    
    olke, paytaxt = melumat

#break dövrü dərhal dayandırır. Kobud şəkildə desək, kod break ifadəsini görən kimi prosesi dayandırır.
say = 1
while say <= 10:
    if say == 5:
        break
    print(say)
    say += 1

#continue dövrü tam dayandırmır. Sadəcə cari iterasiyanın qalan hissəsini ötürərək növbəti iterasiyaya 
#keçir. Yəni həmin addımı nəzərə almır, növbəti addıma keçir.
say = 0

while say < 5:
    say += 1

    if say == 3:
        continue

print(say) #ansver 1 2 4 5

#nested loop-İç-içə istədiyimiz qədər dövr yaza bilərik. Məsələn, əgər bir siyahının daxilində başqa 
#siyahılar varsa, hər səviyyə üçün ayrıca for dövründən istifadə edə bilərik.
for sinif in ["S", "M", "İ"]:
    
    for telebe in [5, 96, 7]:
        
        print(sinif, telebe) #ansver s5 s96 s7 M5 M96 M7 İ5 İ96 İ7



#--------------------Iterator and Comprehension------------
monthh="may"
iterator=iter(monthh)   
print(next(iterator)) #ansver: m
print(next(iterator)) #ansver: a    
print(next(iterator)) #ansver: y
#print(next(iterator)) #ansver: error


#Comprehension İndiyə qədər bir siyahının elementləri üzərində əməliyyat aparmaq üçün for dövründən 
#istifadə etdik. Bəzi hallarda isə bu prosesi daha qısa və oxunaqlı formada ifadə edə bilərik.
#Python bunu comprehension konstruksiyaları ilə təmin edir.
ededler = [5, 7, 96, 23, 4]
kvadratlar = []

for eded in ededler:
    kvadratlar.append(eded**2)
    print(kvadratlar) #ansver: [25, 49, 9216, 529, 16]
#Bunu comprehension üsulu ilə aşağıdakı kimi yaza bilərik:
kvadratlar = [eded ** 2 for eded in ededler]
print(kvadratlar)

kvadratlar=[i**2 for i in range(1,6) if i%2==0] #if ile filterleme
print(kvadratlar) #ansver: [1, 4, 9, 16, 25] 

netice=[i**2 if i%2==0 else i**3 for i in range(1,6)] #if else ile filterleme
print(netice) #ansver: [1, 4, 27, 16, 125]

tekler = {eded for eded in ededler if eded % 2 == 1}

seherler=["Bakı", "Gəncə", "Sumqayıt", "Şəki"]
seherler_dist={}

for seher in seherler:
    seherler_dist[seher]=len(seher)
print(seherler_dist) #ansver: {'Bakı': 3, 'Gəncə': 5, 'Sumqayıt': 7, 'Şəki': 4}

seherler_dist={seher:len(seher) for seher in seherler}
print(seherler_dist) #ansver: {'Bakı': 3, 'Gəncə': 5, 'Sumqayıt': 7, 'Şəki': 4}

numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
result=[]

for n1 in numbers1:
    for n2 in numbers2:
        result.append(n1*n2)
    print(result) #ansver: [10, 20, 30, 20, 40, 60, 30, 60, 90]
result=[n1*n2 for n1 in numbers1 for n2 in numbers2]    
print(result) #ansver: [10, 20, 30, 20, 40, 60, 30, 60, 90]

#Iterable bizim deyiseni teyin etdiyimiz bir arr veya obj ola biler Iterator ise iterable-in icindeki 
#elementleri teker teker goturmek ucun istifade olunan veya yaranan bir objedir.


#-------------------funksion------------------
#Python-da funksiya yaratmaq üçün def açar sözündən istifadə olunur.
def ilk_funksiya():
    print("May")

def bolenler(eded):
    b=[]
    for i in range(1, eded+1):
        if eded%i==0:
            b.append(i)

    return b

def orta_hesabla(siyahi):
    say = 0
    toplam = 0

    for eded in siyahi:
        say += 1
        toplam += eded

    orta = toplam / say

    return orta

ededler=[5, 96, 27, 7, 9]

ortalama=orta_hesabla(ededler)

print(ortalama)

def hasil(*args):
    netice = 1

    for eded in args:
        netice *= eded

    return netice
print(hasil(5, 96, 5))

#kwargs isə key-value formasında göndərilən arqumentləri qəbul edir.

def melumat(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
melumat(
    month="May",
    year=1996,
    day=5
) #ansver: month : May year : 1996 day : 5

def quvvet(x, a, b):
    q1 = x ** a
    q2 = x ** b

    return q1, q2
netice = quvvet(5, 2, 3)

n = 3

def hesabla(x):
    global n

    n += 1

    return x ** n

print(hesabla(5))

# yield istifadə olunan funksiya generator function adlanır. Belə funksiyanı çağırdıqda generator obyekti
# əldə edirik; funksiya dərhal bütün kodu icra etmir.böyük məlumatlarla işləyərkən yaddaşa qənaət etməyə 
# kömək edə bilər.return ilə bütün nəticəni bir dəfəyə ala bilərsən, yield ilə isə lazım olduqca bir-bir
# götürə bilərsən. yield xüsusilə böyük məlumatlarla işləyərkən yaddaşa qənaət edə bilər.

def test():
    print("Birinci")
    yield 10

    print("İkinci")
    yield 20

    print("Üçüncü")
    yield 30

it = test()

print(next(it))
print(next(it))
print(next(it))

#Biz funksiyaları belə çağırırıq: len(), quvvet() və s. Lakin bəzi funksiyalar konkret obyektə aid olur.
#Bunlara metod deyilir.Yəni, metod müəyyən obyektə bağlı olan funksiyadır.

siyahi = [5, 96, 98]
print(len(siyahi))  # funksiya  cavab: 3
siyahi.append(27)  # metod ansver: [5, 96, 98, 27]

#Bəzən bir funksiyanın öz daxilində yenidən özünü çağırmasına ehtiyac yaranır. Funksiyanın özünü 
#çağırmasına rekursiya (recursion) deyilir.Rekursiyanın mütləq dayanma şərti olmalıdır. Əks halda, 
#funksiya sonsuz şəkildə özünü çağırmağa çalışar.
def faktorial(n):
    if n==1:
        return 1

    return n*faktorial(n-1)  #burda funksiya ozunu cagirib
print(faktorial(5))

#Python-da Generator — dəyərləri hamısını birdən yaratmaq əvəzinə, bir-bir yaradan xüsusi obyekt növüdür.
# Bu, yaddaşa qənaət etməyə kömək edir və böyük məlumatlarla işləyərkən faydalıdır.

#next(it) — növbəti dəyəri götürür.

#Expression — Python-da hesablandıqda müəyyən bir dəyər verən kod ifadəsidir.
#  Məsələn, 5 + 3 ifadəsi 8 nəticəsini verir.Yadda saxlamaq üçün: Expression = ifadə, Result = nəticə.


# Proqram yazarkən hər funksiyanı sıfırdan özümüz yazmağa ehtiyac yoxdur. Python-da müxtəlif məqsədlər
#  üçün əvvəlcədən hazırlanmış çoxlu modullar mövcuddur. Məsələn, riyazi hesablamalar üçün lazım olan
# bəzi funksiyalar artıq Python-da hazır şəkildə mövcuddur. Tutaq ki, biz faktorial hesablamaq istəyirik.
# Bunun üçün ayrıca faktorial funksiyası yazmaq əvəzinə Python-un math modulunda olan hazır funksiyadan 
#istifadə edə bilərik. Bunun üçün əvvəlcə modulu proqramımıza import edirik:

import math
print(math.factorial(5)) #ansver: 120   

# import ilə from … import … arasındakı fərq--import math bütün modulu import edir, from math import 
# sqrt isə konkret sqrt funksiyasını import edir.  sqrt(her hansi bir funksiyadir)

#lambda Python-da qısa, adsız funksiya yaratmaq üçün istifadə olunur. Yəni adi def ilə funksiya yazmaq 
#əvəzinə, bəzi hallarda onu bir sətirdə yaza bilərik.qisa yazmaq ucun istifade olunur. 
kvadrat = lambda x: x ** 2
print(kvadrat(5))

ticket_price = lambda age: 5 if age < 18 else 10
print(ticket_price(15))  # 5
print(ticket_price(30))  # 10


#for dövründə hər addımı özün yazırsan, map() isə verdiyin funksiyanı elementlərə tətbiq edir.
#Python-da map() nəticəni dərhal siyahı kimi yaratmır; map obyekti qaytarır və nəticələri tələb olunduqca
#verir. list() yazdıqda isə nəticələr siyahıya yığılır.
def kvadrat(x):
    return x**2
netice = list(map(kvadrat, ededler))


ededler=[5, 3, 23, 21, 96]
cut_yoxla=lambda x: x%2==0 # hər element üçün True və ya False qaytarır.
cutler = list( filter(cut_yoxla, ededler))

#reduce map() hər elementə uyğun funksiyanı tətbiq edirdi. filter() şərtə uyğun elementləri seçirdi. 
#reduce() isə bütün elementləri ardıcıl şəkildə birləşdirərək tək bir nəticə yaradır.Qeyd: reduce istifadə 
#etmək üçün əvvəlcə onu import etmək lazımdır. functools modulundan import etməliyik.reduce() isə 
#elementləri bir-biri ilə birləşdirərək sonda tək bir nəticə əldə etmək üçün istifadə olunur.


#Machine Learning-də modelə əvvəlcə nümunə məlumatlar veririk. Model bu məlumatlardan uyğun xətti 
#tapmağa çalışır. Buna training (öyrətmə) deyilir.Sonra proqnozları həqiqi nəticələrlə müqayisə edir. Fərqə error (səhv) deyirik.
# Məsələn, həqiqi nəticə 5, modelin proqnozu isə 4 olsa:Error=5-4=1
#səhvi necə ölçürük? — MSE--Linear Regression üçün çox istifadə olunan ölçülərdən biri Mean Squared Error
#(MSE) — orta kvadratik səhvdir.

# Təlim məlumatları
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 6]

# 1. Ortalamaları hesablayırıq
x_orta = sum(x) / len(x)        #Bütün ədədləri toplayıb sayına bölür. Yəni ortalamanı hesablayır.  
y_orta = sum(y) / len(y)        #Bütün ədədləri toplayıb sayına bölür. Yəni ortalamanı hesablayır.

# 2. Xəttin meylini (w) tapırıq
surət = sum(
    (x[i] - x_orta) * (y[i] - y_orta)
    for i in range(len(x))    #Siyahıdakı elementləri indeksləri ilə bir-bir gəzərək hesablamalar aparır
)

mexrec = sum(
    (x[i] - x_orta) ** 2
    for i in range(len(x))
)

w = surət / mexrec    #Məlumatlara uyğun xəttin meylini hesablayır.

# 3. Başlanğıc sabitini (b) tapırıq 
b = y_orta - w * x_orta

# 4. Modelin nəticələrini göstəririk
print("w =", w)
print("b =", b)

# 5. Yeni proqnoz
yeni_saat = 6
proqnoz = w * yeni_saat + b   #Tapılmış xəttdən istifadə edərək yeni qiymət proqnozlaşdırır:

print("Proqnoz:", proqnoz)