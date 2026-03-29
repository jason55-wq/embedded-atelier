# 個人工作室官方網站 MVP

這是一個以 `Python + Flask` 建立的個人工作室官方網站專案，定位為可展示、可聯絡、可擴充的 MVP。網站主題聚焦於 Arduino 控制系統開發、ESP32 / IoT 整合、感測器應用，以及個人作品或成品販售。

## 1. 專案介紹

本專案適合作為個人技術工作室的官方網站起點，主要包含以下用途：

- 展示 Arduino / 嵌入式控制相關服務
- 展示可販售的作品或商品
- 提供客戶填寫聯絡表單與需求詢問
- 作為未來接案與作品展示的官網基礎

目前版本包含以下頁面：

- `Home` 首頁
- `Services` 服務項目
- `Portfolio / Products` 作品 / 商品頁
- `About` 關於我
- `Contact` 聯絡我

後端目前提供：

- Flask 頁面路由
- 聯絡表單 `POST` 處理
- 成功 / 錯誤訊息顯示
- 404 / 500 基本錯誤處理

## 2. 安裝方式

1. 進入專案資料夾：

```powershell
cd "c:\Users\ASUS\Desktop\html vscode"
```

2. 建立虛擬環境並啟用。

3. 安裝套件：

```powershell
pip install -r requirements.txt
```

## 3. 虛擬環境建立方式

Windows PowerShell：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS / Linux：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Flask 啟動方式

開發模式可直接使用：

```powershell
python app.py
```

或使用 Flask CLI：

```powershell
$env:FLASK_APP="app.py"
$env:FLASK_ENV="development"
flask run
```

啟動後可在瀏覽器開啟：

```text
http://127.0.0.1:5000
```

## 5. 專案資料夾結構說明

```text
.
|-- app.py
|-- requirements.txt
|-- README.md
|-- static/
|   |-- css/
|   |   `-- style.css
|   `-- js/
|       `-- main.js
`-- templates/
    |-- base.html
    |-- home.html
    |-- services.html
    |-- portfolio.html
    |-- about.html
    |-- contact.html
    |-- 404.html
    `-- 500.html
```

各目錄用途：

- `app.py`：Flask 主程式入口，包含路由、表單處理與錯誤處理
- `templates/`：Jinja2 模板頁面
- `static/css/`：網站共用樣式
- `static/js/`：導覽列互動與前端小型腳本

## 6. 後續部署到 Render 的基本說明

這個專案已適合部署到 Render 類型的 Python Web Service。

基本流程如下：

1. 將專案推送到 GitHub。
2. 到 Render 建立新的 `Web Service`。
3. 連接 GitHub repository。
4. 設定以下部署資訊：

```text
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

5. 若要正式上線，建議在 Render 環境變數中加入：

```text
SECRET_KEY=your-production-secret
```

## 補充說明

- 聯絡表單目前未接資料庫，送出後會由 Flask 接收並顯示成功訊息。
- `app.py` 中已保留註解位置，方便日後串接 Email 或 Discord webhook。
- 現在是 MVP 架構，後續可以再擴充商品詳情頁、案例管理或後台功能。
