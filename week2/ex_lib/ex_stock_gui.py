from tkinter import *
from tkinter import messagebox, ttk
from week2.ex_db.DBManager import DBManager
import threading

db = DBManager()

def fetch_stock_date():
    """주식 종목명, 코드, 수집여부를 가져옴"""
    conn = db.get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT krx_code, krx_name, krx_yn FROM tb_ktx")
            return cursor.fetchall()
    except Exception as e:
        messagebox.showerror("db error", str(e))
        return []
def update_collect_yu():
    """선택한 주식의 수집 여부를 업데이트"""
    db.insert("UPDATE tb_krx SET krx_yn = :1 WHERE krx_code =:2",[flag,code])
def update_selected(event):
    """선택시 화면 표시"""
    selected_stock = stock_combobox.get()
    for stock in stock_list:
        if f"{stock[0]} - {stock[1]}" == selected_stock:
            collect_var.set(stock[2])
            break

def on_save():
    """선택 정보 저장"""
    selected_stock = stock_combobox.get()
    new_flag = collect_var.get()
    if not selected_stock:
        messagebox.showwarning("Warning","종목을 선택하세요")
        return
    stock_code = selected_stock.split(" - ")[0]
    update_collect_yu()
    messagebox.showwarning("success","데이터 저장됨.")
def load_data():
    """스레드를 사용하여 데이터를 비동기적으로 로드"""
    def task():
        stock_list = fetch_stock_date()
        stock_combobox['values'] = [f"{s[0]} - {s[1]}"for s in stock_list]
        thread = threading.Thread(target=task, daemon=True)
        thread.start()
app = Tk()
app.title("stock bbs manager")
app.geometry("400x200")
# 종목 Combobox
stock_list = []
stock_combobox = ttk.Combobox(app, state="readonly", width=30)
stock_combobox.grid(row=0, column=1, padx=10, pady=10)
stock_combobox.bind("<<ComboboxSelected>>", update_selected)
# 수집 여부 선택
collect_var = StringVar(value="N")
yes_bth = ttk.Radiobutton(app, text="Yes", variable=collect_var, value="Y")
no_bth = ttk.Radiobutton(app, text="No", variable=collect_var, value="N")
yes_bth.grid(row=1, column=1, padx=10, pady=5, sticky="w")
no_bth.grid(row=1,column=1, padx=10, pady=5, sticky="e")
# 저장 버튼
save_bth = ttk.Button(app, text="Save", command=on_save)
save_bth.grid(row=2, column=1, pady=10)
# 데이터 로드(스레드 사용)
load_data()
app.mainloop()