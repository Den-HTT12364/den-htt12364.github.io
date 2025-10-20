import tkinter as tk
from tkinter import ttk, messagebox

def convert_urls():
    github_urls = input_text.get("1.0", tk.END).strip().splitlines()
    if not github_urls:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "กรุณาป้อนลิงก์ GitHub อย่างน้อย 1 ลิงก์")
        return

    converted = []
    for url in github_urls:
        url = url.strip()
        if "github.com" in url and "/blob/" in url:
            pages_url = url.replace(
                "https://github.com/Den-HTT12364/den-htt12364.github.io/blob/main/",
                "https://den-htt12364.github.io/"
            )
            converted.append(pages_url)
        else:
            converted.append(f"[ไม่ใช่ blob URL] {url}")

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "\n".join(converted))

def copy_all():
    links = output_text.get("1.0", tk.END).strip()
    if links:
        root.clipboard_clear()
        root.clipboard_append(links)
        root.update()
        messagebox.showinfo("สำเร็จ", "คัดลอกลิงก์ทั้งหมดไป Clipboard แล้ว!")
    else:
        messagebox.showwarning("แจ้งเตือน", "ยังไม่มีลิงก์ให้คัดลอก")

# --- GUI ---
root = tk.Tk()
root.title("GitHub Blob → GitHub Pages URLs")
root.geometry("800x500")

# Input
ttk.Label(root, text="ป้อนลิงก์ GitHub (blob) หลายลิงก์ ต่อบรรทัด:").pack(pady=5)
input_text = tk.Text(root, height=10, width=95)
input_text.pack(pady=5)

# Buttons
frm_btn = ttk.Frame(root)
frm_btn.pack(pady=10)
ttk.Button(frm_btn, text="แปลงเป็น GitHub Pages URLs", command=convert_urls).pack(side="left", padx=5)
ttk.Button(frm_btn, text="Copy All", command=copy_all).pack(side="left", padx=5)

# Output
ttk.Label(root, text="GitHub Pages URLs ที่ได้:").pack(pady=5)
output_text = tk.Text(root, height=10, width=95)
output_text.pack(pady=5)

root.mainloop()
