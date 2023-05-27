import tkinter as tk
from translate import Translator


def translate_text():
    text = input_text.get("1.0", "end-1c")  # 获取输入文本框的内容
    translator = Translator(from_lang=input_lang.get(), to_lang=output_lang.get())
    translation = translator.translate(text)  # 进行翻译
    output_text.delete("1.0", tk.END)  # 清空输出文本框
    output_text.insert(tk.END, translation)  # 在输出文本框中显示翻译结果


# 创建主窗口
window = tk.Tk()
window.title("翻译窗口By:n-Jack(UI摆烂了)")
window.attributes('-topmost', True)  # 窗口置顶

# 默认文字
default_font = ("Sans-Serif", 11)
window.option_add("*Font", default_font)

# 创建输入语言选项框
input_lang_label = tk.Label(window, text="输入语言:")
input_lang_label.pack()
input_lang = tk.StringVar(window)
input_lang.set("zh-CN")  # 默认为中文
input_lang_dropdown = tk.OptionMenu(window, input_lang, "zh-CN", "en", "ja", "ru", "fr")
input_lang_dropdown.pack()

# 创建输入文本框
input_text_label = tk.Label(window, text="输入文本:")
input_text_label.pack()
input_text = tk.Text(window, height=10, width=30)
input_text.pack()

# 创建输出语言选项框
output_lang_label = tk.Label(window, text="输出语言:")
output_lang_label.pack()
output_lang = tk.StringVar(window)
output_lang.set("en")  # 默认输出为英语
output_lang_dropdown = tk.OptionMenu(window, output_lang, "zh-CN", "en", "ja", "ru", "fr")
output_lang_dropdown.pack()

# 创建翻译按钮
translate_button = tk.Button(window, text="翻译", command=translate_text)
translate_button.pack()

# 创建输出文本框
output_text_label = tk.Label(window, text="翻译结果:")
output_text_label.pack()
output_text = tk.Text(window, height=10, width=30)
output_text.pack()

# 设置窗口样式
window.geometry("300x530")  # 设置窗口大小
window.resizable(True, True)  # 禁止调整窗口大小
window.wm_attributes("-alpha", 0.92)  # 窗口背景不透明度

# 运行主循环
window.mainloop()
