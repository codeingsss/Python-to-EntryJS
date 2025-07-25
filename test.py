import Entry.Object
import Entry.EntryCompiler
import Entry.Event

#코드 리스트 생성
code = []
EntryOBJ = Entry.Object.EntryObject()

#오브젝트 설정
code.append(EntryOBJ.SetId(id="Object ID"))

#시작하기를 눌렀을때 시작
start = Entry.Event.EntryEvent.on_start("\n".join(code))
Entry.EntryCompiler.Compile(start)
