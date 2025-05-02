from tkinter import *
from tkinter import scrolledtext
import ollama
model_nm = "mistral"
ollama.pull(model_nm)
# 대화 기록(컨텍스트 유지)
messages=[]

def send_message(event=None):
    message = entry.get()
    if message:
        messages.append({"role": "user", "content": message})
        chat_window.config(state=NORMAL)
        chat_window.insert(END, f"\n😎 You:{message}\n")
        chat_window.config(state=DISABLED)
        entry.delete(0, END)
        chat_window.yview(END) # 자동 스크롤
        # ollama 에게 요청
        # 스트리밍 응답 받기
        res_stream = ollama.chat(model=model_nm, messages=messages
                                 , stream=True)
        ai_all_response = ""
        chat_window.config(state=NORMAL)
        chat_window.insert(END, f"\n🦙Ollama:\n")
        for part in res_stream:
            text = part["message"]["content"]
            if "\n\n" in text:  # 응답이 종료되었을 가능성이 있는 부분 감지
                break

            ai_all_response += text
        # 응답 내용을 출력
        chat_window.insert(END, f"{ai_all_response}\n")
        chat_window.config(state=DISABLED)

        messages.append({"role": "assistant", "content": ai_all_response}) #컨텍스트 저장

app = Tk()
app.title("Chat UI")
app.geometry("400x500")
# 채팅 창
chat_window = scrolledtext.ScrolledText(app, wrap=WORD, state=DISABLED
                                        ,height=20,width=50)
chat_window.pack(pady=10, padx=10, expand=True, fill=BOTH)
# 입력프레임
input_frame = Frame(app)
input_frame.pack(pady=10, padx=10, fill=X)
# input
entry = Entry(input_frame)
entry.pack(side=LEFT, padx=5, pady=5, expand=True, fill=X)
# btn
btn = Button(input_frame, text="Send", command=send_message)
btn.pack(side=RIGHT, padx=5, pady=5)
app.mainloop()