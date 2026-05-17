# Z FIT BY ZAINAB 🏋️

> *Where strength meets style. Build the body — and life — you deserve.*

---

## 📌 Project Purpose

**Z Fit by Zainab** is a multi-page gym website built as a Python Flask web application. It serves as the online presence for a fitness center located in Karachi, Pakistan.

The purpose of this project is to:
- Showcase the gym's facilities, classes, and unique offerings
- Introduce the professional coaching team
- Present membership pricing plans to potential members
- Provide a clean, modern, and mobile-friendly frontend experience

This is a **server-rendered web app** — Flask handles routing and passes dynamic data (team members, plans, highlights) into Jinja2 HTML templates, which are styled with a single custom CSS file.

---

## 📸 Pages & Routes

| Page | Route | What It Shows |
|---|---|---|
| **Home** | `/` | Hero banner, gym highlights, class list, call-to-action |
| **About** | `/about` | Coach team profiles and list of facilities |
| **Membership** | `/membership` | Pricing plans (Starter / Elite / VIP) and services |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask |
| Templating | Jinja2 |
| Frontend | HTML5, CSS3 |
| Fonts | Google Fonts (Bebas Neue, Outfit) |

---

## 📁 Project Structure

```
zfit/
├── app.py                  # Flask app — all routes and data
├── static/
│   ├── css/
│   │   └── style.css       # All custom styles
│   └── images/             # Image assets
└── templates/
    ├── base.html           # Shared layout: navbar + footer
    ├── home.html           # Home page template
    ├── about.html          # About page template
    └── membership.html     # Membership page template
```

---

## 🚀 Running the Project Locally

Follow these steps to run Z Fit on your own machine.

### ✅ Prerequisites

Make sure you have the following installed:
- **Python 3.7+** → [Download here](https://www.python.org/downloads/)
- **pip** (comes with Python)

Check your versions:
```bash
python --version
pip --version
```

---

### 📥 Step 1 — Get the Code

**Option A: Clone from GitHub**
```bash
git clone https://github.com/your-username/zfit-by-zainab.git
cd zfit-by-zainab
```

**Option B: Download ZIP**

Download and unzip the project, then open a terminal inside the `zfit/` folder.

---

### 🐍 Step 2 — Create a Virtual Environment (Recommended)

A virtual environment keeps your project dependencies isolated.

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

You should see `(venv)` appear in your terminal prompt.

---

### 📦 Step 3 — Install Dependencies

```bash
pip install flask
```

---

### ▶️ Step 4 — Run the App

```bash
python app.py
```

You should see output like:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

---

### 🌐 Step 5 — Open in Browser

Visit the following URL in your browser:
```
http://127.0.0.1:5000
```

Navigate between pages using the navbar:
- `http://127.0.0.1:5000/` — Home
- `http://127.0.0.1:5000/about` — About
- `http://127.0.0.1:5000/membership` — Membership

---

### 🛑 Stopping the Server

Press `CTRL + C` in the terminal to stop the Flask server.

---

## ❗ Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'flask'` | Run `pip install flask` |
| Port 5000 already in use | Change the port: `app.run(port=5001)` in `app.py` |
| Page not found (404) | Make sure you're running `app.py` from inside the `zfit/` folder |
| Styles not loading | Ensure `static/css/style.css` exists and the server is running |

---

## 💳 Membership Plans

| Plan | Price | Highlights |
|---|---|---|
| **Starter** | Rs 4,999/month | Gym floor, 2 classes/week, locker room |
| **Elite** ⭐ | Rs 8,999/month | Unlimited classes, 1 PT session, nutrition consult |
| **VIP** | Rs 14,999/month | 4 PT sessions, custom meal plan, guest passes |

---

## 👥 The Team

- **Zainab Javed** — Founder & Head Coach
- **Sara Ahmed** — Nutrition Specialist
- **Ali Raza** — Strength Coach
- **Hira Baig** — Yoga & Mindfulness Instructor

---

## 📍 Contact

- 📍 Block 5, Clifton, Karachi
- 📞 +92 300 1234567
- ✉️ hello@zfitbyzainab.com

---

## 📄 License

© 2025 **Z FIT BY ZAINAB**. All rights reserved. Created by ZAINAB JAVED.
