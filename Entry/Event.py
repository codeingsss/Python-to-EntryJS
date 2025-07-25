class EntryEvent:
    @staticmethod
    def on_start(callback_body):
        return f"Entry.addEventListener('start', function() {{\n{callback_body}\n}});"

    @staticmethod
    def on_key_press(key_code, callback_body):
        return (
            "Entry.addEventListener('keyPress', function(e) {\n"
            f"    if (e.keyCode === {key_code}) {{\n{callback_body}\n    }}\n}});"
        )

    @staticmethod
    def on_message(msg, callback_body):
        return (
            f"Entry.addEventListener('receiveMessage_{msg}', function() {{\n"
            f"{callback_body}\n}});"
        )
