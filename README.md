# Embedded Atelier

這是一個以 `Flask` 製作的個人工作室網站專案，主題聚焦 Arduino、ESP32 與 IoT 原型開發。網站目前保留首頁、服務介紹、GitHub 作品展示、關於頁，以及已改為 LINE 聯絡資訊的聯絡頁。

## 目前聯絡方式

- LINE ID：`we252668`
- Email：`we25266855@gmail.com`

聯絡頁已移除網站表單，不再經由後端接收 `name`、`email`、`subject`、`message` 等欄位，也不再依賴 SMTP 寄信流程。

## 執行方式

1. 進入專案目錄

```powershell
cd "c:\Users\ASUS\Desktop\html vscode"
```

2. 安裝套件

```powershell
pip install -r requirements.txt
```

3. 啟動網站

```powershell
python app.py
```

4. 開啟瀏覽器前往

```text
http://127.0.0.1:5000
```

## 專案結構

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
