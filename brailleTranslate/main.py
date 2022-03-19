from unicode import *
from braille import *

if __name__ == "__main__":
    dot_text = "⠥⠠⠘⠒⠀⠫⠶⠉⠢⠠⠪⠓⠣⠕⠂"
    plain_text = ""
    chojong = {}  # 지금 자음이 초성인지 종성인지 구분하기 위해 사용. /i: "초성"/i: "종성"/
    
    dtl = list(dot_text)  # 점자 문자열 처리를 쉽게 하기 위해 리스트로 바꿈.
    while dtl:
        try:
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
                if yakeo[dtl[0]][-1] in ("ㄱ", "ㄴ", "ㄹ", "ㅇ", "ㅆ"):
                    chojong[len(plain_text) - 1] = "종성"
                dtl.pop(0)
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
        except:
            pass
    
    print(list(plain_text))
    print(chojong)
    
    ptl = list(plain_text)  # 만들어진 한글 문자열의 후처리를 위해 리스트로 바꿈.
    i = 0  # ptl에 접근하기 위함.
    k = 0  # 인덱스값이 계속 변하는 ptl이기 때문에, 초기 ptl의 인덱스로 접근하기 위한 변수.
    while i < len(ptl):
        try:
            if ptl[i] in ("ㄴ", "ㄷ", "ㅁ", "ㅂ", "ㅈ", "ㅋ", "ㅌ", "ㅍ", "ㅎ", "ㄸ", "ㅃ", "ㅉ") and ptl[i + 1] == "ㅏ" and ptl[i + 2] in joongsung.values():
                del ptl[i + 1]
                k = k + 1
                continue
            
            if ptl[i] in joongsung.values():  # 모음이 나왔는데
                if i == 0:  # 그냥 시작부터 바로 모음이면
                    ptl.insert(i, "ㅇ")  # ㅇ 추가
                    i = i + 1
                elif ptl[i - 1] == " ":  # 앞에가 띄어쓰기면
                    ptl.insert(i, "ㅇ")  # ㅇ 추가
                    i = i + 1
                elif ptl[i - 1] in joongsung.values():  # i - 1이 모음이면
                    ptl.insert(i, "ㅇ")  # ㅇ 추가
                    i = i + 1
                else:  # 모음이 안나왔으로 i - 1은 초성 or 종성 or 약자 셋 중 한개인데
                    if k - 1 in chojong.keys():  # k - 1이 chojong의 키인데
                        if chojong[k - 1] != "초성":  # 그게 초성이 아니면
                            ptl.insert(i, "ㅇ")  # ㅇ 추가
                            i = i + 1
                    else:  # k - 1이 chojong의 키가 아니라는 것은 i - 1이 약자라는 뜻이고
                        if ptl[i - 1] not in chosung.values():  # 그게 초성이 아니면
                            ptl.insert(i, "ㅇ")  # ㅇ 추가
                            i = i + 1

        except:
            pass

        finally:
            i = i + 1
            k = k + 1
    plain_text = "".join(ptl)
    
    print(plain_text)
    print(join_jamos(plain_text))
            
"""
⠊⠗⠚⠒⠑⠟⠈⠍⠁ - 대한민국 ㅇ

⠨⠣⠽⠠⠾ - 자외선 ㅇ

⠘⠗⠫⠀⠈⠥⠙⠣⠌⠊ - 배가 고팠다 ㅇ

⠥⠠⠘⠒⠀⠫⠶⠉⠢⠠⠪⠓⠣⠕⠂ - 오빤 강남스타일 ㅇ

⠁⠝⠀⠈⠪⠸⠎⠕⠀⠠⠕⠂⠨⠝⠐⠥⠀⠕⠂⠎⠉⠌⠠⠪⠃⠉⠕⠊ - 그런데 그것이 실제로 일어났습니다 ㅇ

⠨⠟⠨⠎⠃⠀⠘⠶⠑⠡ - 진접 방면 ㅇ

⠣⠘⠎⠨⠕⠫⠀⠘⠶⠝⠀⠊⠮⠎⠫⠠⠱⠌⠊ - 아버지가 방에 들어가셨다 ㅇ

⠚⠉⠮⠝⠠⠎⠀⠘⠕⠫⠀⠉⠗⠐⠱⠀⠧⠬ - 하늘에서 비가 내려 와요 ㅇ

⠕⠨⠝⠒⠀⠈⠧⠗⠒⠰⠣⠒⠴⠵⠊⠝⠀⠇⠐⠣⠶⠠⠊⠣⠍⠗⠒⠀⠨⠎⠘⠎⠐⠱⠌⠉⠵⠊⠝ - 이젠 괜찮은데 사랑따윈 저버렸는데 ㅇ

⠚⠡⠨⠗⠀⠠⠕⠫⠁⠵⠀⠥⠚⠍⠕⠃⠉⠕⠊ - 현재 시각은 오후입니다 ㅇ

⠕⠰⠾⠕⠠⠕⠃⠕⠉⠡⠀⠇⠢⠏⠂⠀⠠⠕⠃⠩⠁⠕⠂⠀⠥⠚⠍⠀⠱⠊⠞⠃⠠⠕⠀⠇⠢⠠⠕⠃⠥⠘⠛ - 이천이십이년 삼월 십육일 오후 여덟시 삼십오분 ㅇ

⠚⠍⠰⠾⠨⠹⠀⠠⠕⠫⠁⠨⠶⠗⠟⠺⠀⠘⠕⠩⠂⠵⠀⠈⠍⠠⠕⠃⠙⠎⠠⠝⠒⠓⠪⠐⠮⠀⠉⠎⠢⠉⠵⠊ - 후천적 시각장애인의 비율은 구십퍼센트를 넘는다 ㅇ

⠋⠥⠊⠪⠨⠻⠐⠳⠮⠀⠠⠕⠂⠚⠗⠶⠚⠒⠊ - 코드졍렬을 실행한다 ㅇ
------------------------------------------------------------------------------------------------------------------------------
ㄼ, ㅀ, ㄶ 등등 겹받침 안되는건 unicode.py에 join_jamos()를 수정해야 한다.
근데 저건 나도 어디서 뜯어온거라 수정이 가능할지 어떨지는 모르겠다.

숫자 - 처리 해야함.
영어 - 처리 해야함.
문장부호 - 처리 할필요 없다고 생각하나, 문장부호가 들어간 점자를 다른식으로 해석해서 이상하게 나올 가능성이 큼. 그래서 처리 하긴 해야할듯?
"""