class EntryObject:
    def __init__(self):
        self.id = None

    def SetId(self, id):
        self.id = id
        return ""
    @property
    def base(self):
        if not self.id:
            raise ValueError("오브젝트 ID가 설정되지 않았습니다. set_id()로 ID를 먼저 설정하세요.")
        return f"Entry.container.getObject('{self.id}').entity"

    def moveTo(self, x, y, duration=0):
        return f"{self.base}.moveTo({x}, {y}, {duration});"

    def setPos(self, x, y):
        return f"{self.base}.setX({x});\n{self.base}.setY({y});"

    def Say(self, message, duration=2000):
        return f"{self.base}.say('{message}', {duration});"

    def setRotation(self, angle):
        return f"{self.base}.setRotation({angle});"

    def Show(self):
        return f"{self.base}.setVisible(true);"

    def Hide(self):
        return f"{self.base}.setVisible(false);"
