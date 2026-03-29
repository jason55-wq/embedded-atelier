import os
from datetime import datetime

from flask import Flask, flash, redirect, render_template, request, url_for


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key")
    app.config["JSON_AS_ASCII"] = False

    site_config = {
        "brand_name": "Embedded Atelier",
        "tagline": "Arduino / ESP32 控制系統與作品開發工作室",
        "contact_email": "we25266855@gmail.com",
        "line_id": "we252668",
    }

    services = [
        {
            "title": "Arduino 控制系統開發",
            "summary": "從需求分析、電路規劃到程式撰寫，協助完成可落地的控制系統原型與成品。",
            "features": ["客製邏輯控制", "設備流程整合", "原型驗證"],
        },
        {
            "title": "ESP32 / IoT 整合",
            "summary": "串接 Wi-Fi、藍牙與雲端服務，建立遠端監控、資料回傳與裝置連線能力。",
            "features": ["無線通訊", "雲端資料串接", "遠端控制介面"],
        },
        {
            "title": "感測器與自動控制應用",
            "summary": "整合溫濕度、光學、距離、流量等感測器，打造穩定的自動控制流程。",
            "features": ["感測器校正", "資料判斷邏輯", "警示與自動化"],
        },
        {
            "title": "客製化作品開發",
            "summary": "針對展示裝置、教學設備與小型商用系統，提供外觀與功能兼顧的客製方案。",
            "features": ["展示互動裝置", "教學模組", "小量製作規劃"],
        },
    ]

    products = [
        {
            "name": "智慧溫室控制器",
            "description": "整合溫濕度、土壤濕度與繼電器輸出，可自動控制風扇與灌溉。",
            "tags": ["Arduino", "Sensor", "Automation"],
            "price": "NT$ 4,800 起",
        },
        {
            "name": "ESP32 遠端監測模組",
            "description": "透過 Wi-Fi 回傳設備狀態，適合小型工位、展示系統與教學專案。",
            "tags": ["ESP32", "IoT", "Dashboard"],
            "price": "NT$ 3,200 起",
        },
        {
            "name": "互動式展示按鈕面板",
            "description": "適用於展場、教具或產品展示，可客製按鍵、燈號與觸發流程。",
            "tags": ["Interface", "Exhibit", "Embedded"],
            "price": "NT$ 2,600 起",
        },
        {
            "name": "自動補水控制盒",
            "description": "針對水箱液位與泵浦控制設計，提供穩定的自動補水邏輯。",
            "tags": ["Control", "Pump", "Relay"],
            "price": "NT$ 5,500 起",
        },
        {
            "name": "教學用感測器實驗套件",
            "description": "提供多種感測模組與示範程式，方便教學、社團與自學應用。",
            "tags": ["Education", "Arduino", "Kit"],
            "price": "NT$ 1,980 起",
        },
        {
            "name": "小型設備警示模組",
            "description": "結合蜂鳴器、警示燈與事件判斷邏輯，適合設備異常提示用途。",
            "tags": ["Alert", "Embedded", "Safety"],
            "price": "報價洽詢",
        },
    ]

    about_points = [
        "專注於 Arduino、ESP32 與嵌入式控制系統實作，重視功能穩定與維護性。",
        "可協助從概念驗證、電控整合到作品製作，適合接案開發與展示型系統需求。",
        "同時提供可販售成品與客製化方案，讓網站兼具官方展示與商業接洽用途。",
    ]

    featured_items = products[:3]

    def render_page(template_name: str, **context):
        """Render a page with shared site content."""
        return render_template(
            template_name,
            site=site_config,
            services=services,
            products=products,
            featured_items=featured_items,
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
        return render_page("portfolio.html", page_title="作品 / 商品")

    @app.route("/about")
    def about_page():
        return render_page("about.html", page_title="關於我")

    @app.route("/contact", methods=["GET", "POST"])
    def contact_page():
        form_data = {"name": "", "email": "", "subject": "", "message": ""}

        if request.method == "POST":
            form_data = {
                "name": request.form.get("name", "").strip(),
                "email": request.form.get("email", "").strip(),
                "subject": request.form.get("subject", "").strip(),
                "message": request.form.get("message", "").strip(),
            }

            missing_fields = [label for key, label in {
                "name": "姓名",
                "email": "Email",
                "subject": "主旨",
                "message": "需求內容",
            }.items() if not form_data[key]]

            if missing_fields:
                flash(f"請完整填寫欄位：{'、'.join(missing_fields)}", "error")
                return render_page("contact.html", page_title="聯絡我", form_data=form_data), 400

            # Placeholder: this is the extension point for future email or Discord webhook integration.
            app.logger.info("New contact request received: %s", form_data)
            flash("表單已成功送出，我會盡快與你聯繫。", "success")
            return redirect(url_for("contact_page"))

        return render_page("contact.html", page_title="聯絡我", form_data=form_data)

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
