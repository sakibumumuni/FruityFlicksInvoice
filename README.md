# 🍓 Fruity Flicks – Invoice Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![HTML](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

> A web-based invoice management system built with Flask for Fruity Flicks, enabling seamless creation, tracking, and management of invoices.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📌 About the Project

The Fruity Flicks Invoice Management System is a Flask-powered web application designed to help businesses manage their invoicing process efficiently. It allows users to [generate, download, view and search existing invoices, edit and delete invoices, track the payment status of invoices, categorize most frequent client groups to optimze sales, and save invoices in a database, all in one sysytem].
# Managing

---

## ✨ Features

- [ ] Generate invoices
- [ ] View and search existing invoices
- [ ] Edit and delete invoices
- [ ] Track payment status (paid / unpaid / pending)
- [ ] Download invoice as pdf
- [ ] Categorize most frequent client groups [to note target sales clientss]
- [ ] Save invoices in a single database

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend logic |
| Flask | Web framework |
| HTML5 | Page structure / Jinja2 templating |
| CSS3 | Styling and layout |
| JavaScript | Frontend interactivity |
|  SQLite3 / PostgreSQL / MongoDb] | Data storage |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip
- [virtualenv]

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/fruity-flicks-invoice.git
   cd fruity-flicks-invoice
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration (secret key, database URI, etc.)
   ```

5. **Initialize the database**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Run the application**
   ```bash
   flask run
   ```

7. Open your browser and navigate to `http://127.0.0.1:5000`

---

## 💻 Usage

1. Navigate to the **Invoices** section
2. Fill in client details, items, and amounts 
4. Click **New Invoice** to create an invoice (once created, the invoice is saved in a database/ MongoDb / postgreSQL or SQLite3)
5. Download invoice as a pdf
6. [View all issued invoices in a database, by clicking a daatabase button]
7. View a chart that has the most frequent customer groups.

---

## 📁 Project Structure

```
fruity-flicks-invoice/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── main.js
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── invoices/
│           ├── list.html
│           ├── create.html
│           └── detail.html
├── migrations/
├── .env.example
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

---

## 📸 Screenshots

<!-- Add screenshots of your application here once the UI is ready -->
| Dashboard | Invoice View |
|-----------|-------------|
| ![Dashboard](screenshots/dashboard.png) | ![Invoice](screenshots/invoice.png) |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📬 Contact

**Fruity Flicks Development Team**

- Email: [your-email@example.com]
- GitHub: [https://github.com/your-username]
- Project Link: [https://github.com/your-username/fruity-flicks-invoice]
