# 파이썬 To **엔트리JS** 번역기
파이썬 파일을 **엔트리JS**로 바꿔주는 프로그램

# 만들게된 이유
엔트리JS로 오브젝트를 움직이고, 회전시키고 동작 시키는것은 너무 어렵습니다. 그리고
파이썬으로 엔트리 프로젝트를 구현하는 **엔트리 파이썬**이 있지만 다른 파이썬 모듈을 사용할수 없기때문에
이것을 만들었습니다.

# 설치 방법
**Entry**폴더를 자신의 프로젝트에 옮깁니다
프로젝트 폴더에(Entry폴더 밖에) 파이썬 파일을 만든 뒤 다음 코드를 작성합니다

```python
#Entry폴더에서 파일들을 import합니다
import Entry.Object
import Entry.EntryCompiler
import Entry.Event

#code 리스트를 만듭니다
code = []

#클래스를 찍어냅니다
EntryOBJ = Entry.Object.EntryObject()
code.append(EntryOBJ.SetId("오브젝트 아이디를 넣으세요"))

#시작하기를 눌렀을때 실행되게 합니다.(이걸로 코딩한 후 불러오고 엔트리 온라인에 올리면 유저들을 사용할수 없습니다)
start = Entry.Event.EntryEvent.on_start("\n".join(code))
Entry.EntryCompiler.Compile(start)


```

# 코딩 방식
코드를 저장할 리스트에 코드를 **append**헤줍니다 EntryCompiler로 컴파일 해줍니다.

**예시**
```python
code.append(EntryOBJ.setPos(10,10))
```
이런 방식으로 코드를 작성하면 됩니다

# JS 파일 만들기
코드 작성한 파일을 실행하고 파일 이름을 입력해줍니다

# 함수 목록
Entry 폴더 안에 .py파일을 열어 함수를 확인합니다

# 오브젝트 아이디 확입법
```javascript
Entry.container.objects_ 
```
이 코드를 콘솔에 입력하고 확인합니다.
