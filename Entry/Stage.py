class EntryStage:
    def set_background(self, bg_id):
        return f"Entry.stage.setBackground('{bg_id}');"

    def get_size(self):
        return (
            "const width = Entry.stage.canvas.width;\n"
            "const height = Entry.stage.canvas.height;"
        )
