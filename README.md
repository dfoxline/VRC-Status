# VRChat Status Monitor (Python Version)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[**中文**](#zh) | [**English**](#en) | [**日本語**](#ja)

---

<a id="zh"></a>
## 🇨🇳 简体中文

### 项目简介
这是一个基于 Python 开发的 VRChat 服务器状态实时监控工具。它拥有现代化的 GUI 界面，旨在让玩家无需打开浏览器即可一眼掌握 VRChat 的运行状态。

### 核心特性
* **实时更新**：直接对接 VRChat 官方 API，数据权威准确。
* **现代 UI**：基于 `CustomTkinter` 设计，支持深色模式，视觉体验极佳。
* **智能提醒**：根据服务器负载情况（正常、维护、故障）动态切换状态颜色。
* **悬浮置顶**：窗口可始终保持在最前方，方便在等待进图时监控状态。
* **自动刷新**：后台每 60 秒自动获取最新数据，无需手动操作。

### 运行环境
1.  安装 Python 3.8 或更高版本。
2.  安装依赖库：
    ```bash
    pip install requests customtkinter
    ```
3.  运行程序：
    ```bash
    python vrchat_status.py
    ```

---

<a id="en"></a>
## 🇺🇸 English

### Overview
A Python-based desktop widget for real-time monitoring of VRChat server status. Featuring a modern GUI, it allows players to track server health at a glance without opening a browser.

### Key Features
* **Real-time Data**: Directly consumes the official VRChat Status API for maximum accuracy.
* **Modern UI**: Built with `CustomTkinter`, offering a sleek dark-themed interface.
* **Status Indicators**: Dynamic color coding (Normal, Maintenance, Outage) for instant status recognition.
* **Always on Top**: Keeps the widget visible while you work or wait for the game to load.
* **Auto-Refresh**: Background updates every 60 seconds, ensuring you're always informed.

### Quick Start
1.  Ensure Python 3.8+ is installed.
2.  Install dependencies:
    ```bash
    pip install requests customtkinter
    ```
3.  Launch the app:
    ```bash
    python vrchat_status.py
    ```

---

<a id="ja"></a>
## 🇯🇵 日本語

### プロジェクト概要
Python で開発された VRChat サーバーステータス監視ツールです。モダンな GUI を採用し、ブラウザを開くことなく VRChat の稼働状況をデスクトップ上で瞬時に確認できます。

### 主な機能
* **リアルタイム更新**: VRChat 公式 API と直接連携し、正確なデータを取得。
* **モダンな UI**: `CustomTkinter` を使用した洗練されたダークモードデザイン。
* **ステータス表示**: サーバーの状態（正常、メンテナンス、障害）に合わせて色が動的に変化。
* **最前面表示**: 常に手前に表示可能。ログイン待ちや作業中の監視に最適です。
* **自動更新**: 60 秒ごとにバックグラウンドで自動更新されるため、操作は不要です。

### セットアップ
1.  Python 3.8 以上をインストールしてください。
2.  必要なライブラリをインストールします：
    ```bash
    pip install requests customtkinter
    ```
3.  プログラムを実行します：
    ```bash
    python vrchat_status.py
    ```

---

### 🛠️ Tech Stack / 使用技術
* **Language**: [Python](https://www.python.org/)
* **UI Framework**: [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* **Networking**: [Requests](https://requests.readthedocs.io/)

### 📝 License
This project is licensed under the **MIT License**.
