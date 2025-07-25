import os

def Compile(js_code: str, plugin_name="JavaScript"):
    js_name = input("자바스크립트 파일 이름 입력(확장자 제외) : ")
    plugin_dir = os.path.join("Output", plugin_name)
    os.makedirs(plugin_dir, exist_ok=True)

    js_path = os.path.join(plugin_dir, f"{js_name}.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_code)

    print(f"[✓] 자바스크립트가 만들어졌습니다: {js_path}")
