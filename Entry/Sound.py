class EntrySound:
    def __init__(self, object_id):
        self.base = f"Entry.container.getObject('{object_id}').entity.soundManager"

    def playSound(self, sound_name):
        return f"{self.base}.playSound('{sound_name}');"

    def stopSound(self):
        return f"{self.base}.stopSound();"
