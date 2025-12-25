import customtkinter as ctk
import requests
import threading
import time
import webbrowser

# 设置外观模式 (System, Dark, Light)
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class VRCStatusWidget(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- 窗口配置 ---
        self.title("VRC Status")
        self.geometry("300x160")
        self.resizable(False, False)
        
        # 设置窗口置顶 (可选，如果不想一直置顶可以将 True 改为 False)
        self.attributes("-topmost", True)
        
        # 状态颜色映射
        self.status_colors = {
            "none": "#2CC069",      # 绿色 (正常)
            "minor": "#F1C40F",     # 黄色 (轻微)
            "major": "#E67E22",     # 橙色 (主要)
            "critical": "#E74C3C",  # 红色 (严重)
            "maintenance": "#3498DB" # 蓝色 (维护)
        }

        # --- UI 布局 ---
        self.grid_columnconfigure(0, weight=1)

        # 1. 标题
        self.lbl_title = ctk.CTkLabel(self, text="VRChat Server Status", font=("Arial", 16, "bold"))
        self.lbl_title.grid(row=0, column=0, pady=(15, 5), sticky="ew")

        # 2. 状态指示灯 (圆形)
        self.status_indicator = ctk.CTkButton(self, text="", width=20, height=20, corner_radius=10, 
                                              fg_color="gray", hover=False, state="disabled")
        self.status_indicator.grid(row=1, column=0, pady=5)

        # 3. 状态文字描述
        self.lbl_status_text = ctk.CTkLabel(self, text="正在获取...", font=("Arial", 14))
        self.lbl_status_text.grid(row=2, column=0, pady=5)

        # 4. 底部按钮栏
        self.frame_cmds = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_cmds.grid(row=3, column=0, pady=10)

        self.btn_refresh = ctk.CTkButton(self.frame_cmds, text="刷新", width=80, height=24, command=self.fetch_status)
        self.btn_refresh.pack(side="left", padx=5)

        self.btn_open_web = ctk.CTkButton(self.frame_cmds, text="网页详情", width=80, height=24, 
                                          fg_color="transparent", border_width=1, 
                                          command=lambda: webbrowser.open("https://status.vrchat.com/"))
        self.btn_open_web.pack(side="left", padx=5)

        # --- 启动逻辑 ---
        self.fetch_status()
        # 开启自动刷新计时器
        self.start_auto_refresh()

    def fetch_status(self):
        """在后台线程获取数据，避免卡顿界面"""
        threading.Thread(target=self._get_data_thread, daemon=True).start()

    def _get_data_thread(self):
        try:
            # 使用官方 API (比解析 HTML 更稳定)
            url = "https://status.vrchat.com/api/v2/summary.json"
            response = requests.get(url, timeout=5)
            data = response.json()

            # 解析数据
            status_indicator = data["status"]["indicator"] # none, minor, major, etc.
            status_description = data["status"]["description"]
            
            # 更新 UI (必须在主线程更新)
            self.after(0, lambda: self._update_ui(status_indicator, status_description))
            
        except Exception as e:
            print(f"Error: {e}")
            self.after(0, lambda: self._update_ui("error", "连接失败"))

    def _update_ui(self, indicator, description):
        color = self.status_colors.get(indicator, "gray")
        
        # 如果是 error
        if indicator == "error":
            color = "#7F8C8D"
        
        self.status_indicator.configure(fg_color=color)
        self.lbl_status_text.configure(text=description)

    def start_auto_refresh(self):
        """每 60 秒自动刷新一次"""
        self.fetch_status()
        self.after(60000, self.start_auto_refresh)

if __name__ == "__main__":
    app = VRCStatusWidget()
    app.mainloop()