# Code OS – Invoice Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?logo=mongodb&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

> A web-based invoice management system built with Flask and MongoDB for businesses, enabling seamless creation, tracking, and management of invoices with company branding.

---

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About the Project

The **Code OS Invoice Management System** is a Flask-powered web application designed to help small and medium-sized businesses manage their invoicing process efficiently. Users can set up their company profile with branding (logo and digital signature), then create professional invoices with dynamic line items — all persisted to MongoDB Atlas in the cloud.

The system is actively under development, with a working invoicing core and several additional modules (dashboard analytics, reports, client management) planned for future releases.

---

## Features

### Implemented

- **Company profile setup** — register your business name, email, phone, address, tax ID, and financial year dates
- **Logo and signature upload** — upload a company logo and digital signature with live image preview; stored as base64 in the database
- **Invoice creation** — create invoices with client billing details, invoice number, issue date, and due date
- **Dynamic line items** — add or remove item rows on the fly with description, quantity, and price fields
- **Real-time calculations** — item totals (quantity x price) update automatically as you type
- **Cloud database** — all data is persisted to MongoDB Atlas for reliable, scalable storage

### Planned

- [ ] Dashboard with invoice analytics and summaries
- [ ] View and search existing invoices
- [ ] Edit and delete invoices
- [ ] Track payment status (paid / unpaid / pending)
- [ ] Download invoices as PDF
- [ ] Client management and frequent customer categorization
- [ ] Reports and sales insights
- [ ] Settings and user preferences

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Backend logic |
| **Flask** | Web framework and routing |
| **MongoDB Atlas** | Cloud database (via PyMongo) |
| **Jinja2** | Server-side HTML templating |
| **HTML5** | Page structure |
| **CSS3** | Styling and responsive layout |
| **JavaScript** | Frontend interactivity and calculations |

---

## Getting Started

### Prerequisites

- Python 3.x
- pip
- A [MongoDB Atlas](https://www.mongodb.com/atlas) account (or a local MongoDB instance)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sakibumumuni/code_os_invoice.git
   cd code_os_invoice
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask pymongo python-dotenv
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:
   ```
   MONGO_URL='your_mongodb_atlas_connection_string'
   ```

5. **Run the application**
   ```bash
   python app/main.py
   ```

6. Open your browser and navigate to `http://127.0.0.1:5000`

---

## Usage

1. **Set up your company profile** — on the landing page, enter your company details, upload your logo and digital signature, and submit
2. **Create an invoice** — you'll be redirected to the invoice creation page where your company logo is displayed automatically
3. **Add client details** — fill in the client's name, email, and address
4. **Add line items** — enter item descriptions, quantities, and prices; totals calculate in real time
5. **Submit** — the invoice is saved to the database

---

## Project Structure

```
code_os_invoice/
├── app/
│   ├── main.py                  # Flask application and routes
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css        # Application styling
│   │   └── js/
│   │       └── main.js          # Frontend logic and calculations
│   └── templates/
│       ├── base.html            # Company profile setup page
│       ├── createinvoice.html   # Invoice creation form
│       ├── dashboard.html       # Dashboard (planned)
│       ├── invoicedatabase.html # Invoice database view (planned)
│       ├── client.html          # Client management (planned)
│       ├── report.html          # Reports (planned)
│       └── settings.html        # Settings (planned)
├── .env                         # Environment variables (not tracked in git)
├── .gitignore
└── README.md
```

---

## Roadmap

| Phase | Milestone | Status |
|-------|-----------|--------|
| 1 | Company profile setup and logo upload | Done |
| 2 | Invoice creation with dynamic line items | Done |
| 3 | Dashboard with analytics and summaries | In progress |
| 4 | Invoice database — view, search, edit, delete | Planned |
| 5 | PDF export and download | Planned |
| 6 | Payment status tracking | Planned |
| 7 | Client management and reporting | Planned |
| 8 | User authentication and settings | Planned |

---

## Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

## Contact

**Code OS Development Team**

- Email: codeos285@gmail.com
- GitHub: [sakibumumuni](https://github.com/sakibumumuni)
- Project Link: [github.com/sakibumumuni/code_os_invoice](https://github.com/sakibumumuni/code_os_invoice)
