import tkinter as tk
from tkinter import ttk, messagebox

def convert_url():
    github_url = entry.get().strip()
    if not github_url:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "กรุณาป้อนลิงก์ GitHub")
        return
    
    # แปลงจาก blob เป็น GitHub Pages
    if "github.com" in github_url and "/blob/" in github_url:
        pages_url = github_url.replace(
            "https://github.com/Den-HTT12364/den-htt12364.github.io/blob/main/",
            "https://den-htt12364.github.io/"
        )
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, pages_url)
    else:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "ลิงก์ไม่ใช่ GitHub blob ที่ถูกต้อง")

def copy_link():
    link = result_text.get("1.0", tk.END).strip()
    if link:
        root.clipboard_clear()
        root.clipboard_append(link)
        root.update()
        messagebox.showinfo("สำเร็จ", "คัดลอกลิงก์ GitHub Pages ไป Clipboard แล้ว!")
    else:
        messagebox.showwarning("แจ้งเตือน", "ยังไม่มีลิงก์ให้คัดลอก")

# --- GUI ---
root = tk.Tk()
root.title("GitHub Blob → GitHub Pages URL")
root.geometry("700x300")

ttk.Label(root, text="ป้อนลิงก์ GitHub (blob) ที่นี่:").pack(pady=10)
entry = ttk.Entry(root, width=80)
entry.pack(pady=5)

frm_btn = ttk.Frame(root)
frm_btn.pack(pady=10)

ttk.Button(frm_btn, text="แปลงเป็น GitHub Pages URL", command=convert_url).pack(side="left", padx=5)
ttk.Button(frm_btn, text="Copy Link", command=copy_link).pack(side="left", padx=5)

ttk.Label(root, text="GitHub Pages URL ที่ได้:").pack(pady=5)
result_text = tk.Text(root, height=2, width=80)
result_text.pack(pady=5)

root.mainloop()
