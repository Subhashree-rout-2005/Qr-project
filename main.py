import tkinter as tk
from tkinter import ttk, messagebox
from analyzer import analyze_url


def check_url():
    url = url_entry.get().strip()

    if not url:
        messagebox.showerror(
            "Error",
            "Please enter a URL."
        )
        return

    result = analyze_url(url)

    output.delete("1.0", tk.END)

    output.insert(
        tk.END,
        f"Verdict: {result['verdict']}\n"
    )

    output.insert(
        tk.END,
        f"Risk Score: {result['score']}/100\n\n"
    )

    output.insert(
        tk.END,
        "Reasons:\n"
    )

    for reason in result["reasons"]:
        output.insert(
            tk.END,
            f"• {reason}\n"
        )


root = tk.Tk()
root.title("URL Safety Checker")
root.geometry("700x500")

title = ttk.Label(
    root,
    text="URL Safety Analyzer",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)

url_entry = ttk.Entry(root, width=80)
url_entry.pack(pady=10)

check_btn = ttk.Button(
    root,
    text="Analyze URL",
    command=check_url
)

check_btn.pack(pady=10)

output = tk.Text(
    root,
    height=15,
    width=80
)

output.pack(pady=10)

root.mainloop() 