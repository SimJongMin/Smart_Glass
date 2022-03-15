from unicode import *
from braille import *

if __name__ == "__main__":
    dot_text = "⠁⠝⠀⠈⠪⠸⠎⠕⠀⠠⠕⠂⠨⠝⠐⠥⠀⠕⠂⠎⠉⠌⠠⠪⠃⠉⠕⠊"
    plain_text = ""
    chojong = {}  # 지금 자음이 초성인지 종성인지 구분하기 위해 사용. /i: "초성"/i: "종성"/
    
    dtl = list(dot_text)  # 점자 문자열 처리를 쉽게 하기 위해 리스트로 바꿈.
    while dtl:
        if dtl[0] in space.keys():
            plain_text = plain_text + space[dtl[0]]
            dtl.pop(0)
            continue
        if len(dtl) >= 2: 
            if dtl[0] + dtl[1] in yakeo.keys():
                plain_text = plain_text + yakeo[dtl[0] + dtl[1]]
                dtl.pop(0)
                dtl.pop(0)
                continue
            elif dtl[0] + dtl[1] in chosung.keys():
                plain_text = plain_text + chosung[dtl[0] + dtl[1]]
                dtl.pop(0)
                dtl.pop(0)
                chojong[len(plain_text) - 1] = "초성"
                continue
            elif dtl[0] + dtl[1] in joongsung.keys():
                plain_text = plain_text + joongsung[dtl[0] + dtl[1]]
                dtl.pop(0)
                dtl.pop(0)
                continue
        if dtl[0] in yakeo.keys():
            plain_text = plain_text + yakeo[dtl[0]]
            if yakeo[dtl.pop(0)] == "ㅆ":
                chojong[len(plain_text) - 1] = "종성"
        elif dtl[0] in chosung.keys():
            plain_text = plain_text + chosung[dtl[0]]
            dtl.pop(0)
            chojong[len(plain_text) - 1] = "초성"
        elif dtl[0] in joongsung.keys():
            plain_text = plain_text + joongsung[dtl[0]]
            dtl.pop(0)
        elif dtl[0] in jongsung.keys():
            plain_text = plain_text + jongsung[dtl[0]]
            dtl.pop(0)
            chojong[len(plain_text) - 1] = "종성"
    
    print(list(plain_text))
    print(chojong)
    
    ptl = list(plain_text)  # 만들어진 한글 문자열의 후처리를 위해 리스트로 바꿈.
    for i in range(len(ptl)):
        if ptl[i] == "":
            continue
        try:
            if ptl[i] == "ㅇ":
                if chojong[i - 1] == "초성":
                    ptl[i] = ""
            if ptl[i] == "ㅏ":
                if ptl[i + 3] + ptl[i + 4] in joongsung.values():
                    if i + 1 not in chojong.keys() and ptl[i + 1] != " ":
                        print(i, ptl[i + 1], ptl[i + 2])
                        ptl[i + 1] = ""
                        ptl[i + 2] = ""
                            
                if ptl[i + 1] + ptl[i + 2] in joongsung.values():
                    ptl[i] = ""
                    ptl[i + 1] = ""
        except:
            pass
    plain_text = "".join(ptl)
    
    print(plain_text)
    print(join_jamos(plain_text))
            
"""
⠊⠗⠚⠒⠑⠟⠈⠍⠁: 대한민국
⠨⠣⠽⠠⠾: 자외선
⠘⠗⠫⠀⠈⠥⠙⠣⠌⠊⠲: 배가 고팠다
⠥⠠⠘⠒⠀⠫⠶⠉⠢⠠⠪⠓⠣⠕⠂: 오빤 강남스타일
⠁⠝⠀⠈⠪⠸⠎⠕⠀⠠⠕⠂⠨⠝⠐⠥⠀⠕⠂⠎⠉⠌⠠⠪⠃⠉⠕⠊: 그런데 그것이 실제로 일어났습니다

점자 2개를 먼저 보자. 왜냐하면 최대 2개까지 합처저서 점자를 이루기 때문이다.
만약 2개를 봤는데 있으면 그걸 쓰면 되는거고, 없으면 앞에거 1개만 보면 된다.
약어 >> 초성 >> 중성 >> 종성 순으로 보면 될 것 같긴 하다.

문장부호 X
숫자 X
영어 X
"""