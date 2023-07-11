a="Hello World"
#in(존재여부)
print("el" in a)
#slice
print(a[1:3])
#리스트 슬라이스
b=['h','e','l','l','o']
print(b[2:4])

#in은 true/faulse find는 인덱스를 출력해줌
str='abbbbde'
c=str.find('b')
if c==-1:
    print('없음')
else:
    print(c)

str_text='abbbde'
ind=str_text.find('b')
if ind==-1:
    print('없음')
else:
    print(str_text)
    while ind!=-1:
        print(str_text,ind)
        str_text=str_text[ind+1:]
        ind=str_text.find('b')
        if ind==-1:
            break
