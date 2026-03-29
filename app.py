import os
from datetime import datetime

from flask import Flask, render_template


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key")
    app.config["JSON_AS_ASCII"] = False

    site_config = {
        "brand_name": "Embedded Atelier",
        "tagline": "Arduino / ESP32 專案開發與 IoT 原型製作",
        "contact_email": "we25266855@gmail.com",
        "line_id": "we252668",
        "github_username": "jason55-wq",
        "github_profile_url": "https://github.com/jason55-wq",
    }

    services = [
        {
            "title": "Arduino 專案開發",
            "summary": "從需求拆解、感測器整合到韌體撰寫，協助完成可展示、可驗證的嵌入式原型。",
            "features": ["感測器與模組整合", "控制流程設計", "原型驗證與除錯"],
        },
        {
            "title": "ESP32 / IoT 整合",
            "summary": "建立具備 Wi-Fi 連線能力的 IoT 裝置，串接雲端服務、Webhook 或內部系統。",
            "features": ["Wi-Fi 連線與通訊", "遠端資料上傳", "IoT 情境原型"],
        },
        {
            "title": "裝置資料監測",
            "summary": "協助將設備狀態轉成可觀察資料，讓測試、展示與後續維護更加清楚。",
            "features": ["資料採集規劃", "狀態監測流程", "展示用資料輸出"],
        },
        {
            "title": "MVP 技術驗證",
            "summary": "以最小可行產品方式快速驗證方向，幫助你在投入大量開發前先確認可行性。",
            "features": ["需求聚焦", "原型實作", "MVP 驗證"],
        },
    ]

    about_points = [
        "聚焦 Arduino、ESP32 與 IoT 類型專案，重視可以實際運作與驗證的結果。",
        "偏好清楚的模組拆分、穩定的整合流程，以及方便展示的成果交付方式。",
        "開發內容可搭配 GitHub 展示，方便後續協作、追蹤與持續迭代。",
    ]

    def render_page(template_name: str, **context):
        """Render a page with shared site content."""
        return render_template(
            template_name,
            site=site_config,
            services=services,
            about_points=about_points,
            current_year=datetime.now().year,
            **context,
        )

    @app.after_request
    def apply_utf8_charset(response):
        """Ensure text responses explicitly declare UTF-8."""
        if response.mimetype.startswith("text/"):
            response.headers["Content-Type"] = f"{response.mimetype}; charset=utf-8"
        return response

    @app.route("/")
    def home():
        return render_page("home.html", page_title="首頁")

    @app.route("/services")
    def services_page():
        return render_page("services.html", page_title="服務項目")

    @app.route("/portfolio")
    def portfolio_page():
        return render_page("portfolio.html", page_title="GitHub 作品")

    @app.route("/about")
    def about_page():
        return render_page("about.html", page_title="關於我")

    @app.route("/contact")
    def contact_page():
        return render_page("contact.html", page_title="聯絡我")

    @app.errorhandler(404)
    def not_found(error):
        return render_page("404.html", page_title="找不到頁面"), 404

    @app.errorhandler(500)
    def server_error(error):
        return render_page("500.html", page_title="伺服器錯誤"), 500

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
