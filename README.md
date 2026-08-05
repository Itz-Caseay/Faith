# 🚀 Prince - Cyber Security Portfolio

![Portfolio](https://img.shields.io/badge/Portfolio-Cyber_Security-blue?style=for-the-badge&logo=cyberdefenders)
![Django](https://img.shields.io/badge/Django-4.x-green?style=for-the-badge&logo=django)
![Responsive](https://img.shields.io/badge/Responsive-All_Devices-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=opensourceinitiative)

A modern, fully responsive **Cyber Security Portfolio Website** built with **Django**.

It features a stunning network-themed background with animated topology, glass-morphism UI, neon gradients, responsive layouts, and a fully functional contact system.

---

## 📸 Screenshots

<div align="center">

| Desktop View | Mobile View | Smart Watch |
|---|---|---|
| ![Desktop](https://via.placeholder.com/300x200/0a0e1a/00d4ff?text=Desktop+View) | ![Mobile](https://via.placeholder.com/200x300/0a0e1a/00d4ff?text=Mobile+View) | ![Watch](https://via.placeholder.com/150x150/0a0e1a/00d4ff?text=Watch) |

</div>

---

## ✨ Features

### 🎨 Design Features

- **Network Topology Background** — Live animated network visualization with nodes and connections.
- **Glass-morphism UI** — Modern frosted-glass effects with backdrop blur.
- **Neon Gradients** — Dynamic cyan-to-purple gradient effects.
- **Animated Elements** — Floating particles, data packets, and pulsing nodes.
- **Matrix Rain** — Subtle binary code animation in the background.
- **Fully Responsive** — Designed to work from smartwatches to 4K displays.

### 🛠️ Functionality

- **Contact Form** — Fully functional Django contact form with CSRF protection.
- **Message System** — Success and error messages with animations.
- **Email Integration** — Optional email notifications for contact submissions.
- **Admin Dashboard** — Easy management of contact messages.
- **Download CV** — One-click CV download functionality.
- **Social Links** — Integrated social media profiles.

---

## 📱 Responsive Breakpoints

- **Desktop:** Full experience with all animations.
- **Tablet (≤ 900px):** Optimized tablet layout.
- **Mobile (≤ 600px):** Mobile-first design with touch optimization.
- **Smart Watch (< 380px):** Minimal interface for tiny displays.
- **Landscape:** Optimized for landscape orientation.

---

## 🚀 Technologies Used

| Technology | Purpose |
|---|---|
| Django 4.x | Backend |
| HTML5 | Page structure |
| CSS3 | Styling and animations |
| JavaScript | Optional interactions |
| Custom SVG | Icons |
| SQLite | Default database |
| PostgreSQL | Production database option |
| Gunicorn | Production WSGI server |

---

## 📋 Prerequisites

Make sure you have the following installed:

- Python 3.8+
- Django 4.x
- pip
- Git

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/prince-portfolio.git
cd prince-portfolio
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Optional Email Settings
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
CONTACT_EMAIL=admin@yourdomain.com
```

> ⚠️ **Security Warning:** Never commit your real `.env`, secret key, email password, or other credentials to GitHub.

Add `.env` to your `.gitignore` file:

```gitignore
.env
venv/
__pycache__/
*.pyc
db.sqlite3
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Collect Static Files

```bash
python manage.py collectstatic
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Then open the local development server shown in your terminal, normally:

```text
http://localhost:8000
```

---

## 📁 Project Structure

```text
prince-portfolio/
├── base/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── portfolio/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
│   ├── assets/
│   │   ├── icons/
│   │   ├── me.png
│   │   └── logo.png
│   ├── scripts/
│   │   └── script.js
│   └── styles/
│
├── templates/
│   └── index.html
│
├── .env
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📝 Usage

### Contact Form

Visitors can submit:

- Full Name
- Phone Number (optional)
- Email Address (optional)
- Message

After submission:

1. The message is validated.
2. The message is saved to the database.
3. A success or error notification is displayed.
4. An optional email notification can be sent to the administrator.

### Admin Dashboard

Access the Django administration panel at:

```text
/admin/
```

Depending on the configured admin functionality, administrators can:

- View contact messages.
- Mark messages as read.
- Filter messages by date or status.
- Search through messages.
- Manage stored contact information.

---

## 🎨 Customization

### Colors

Modify the CSS variables:

```css
:root {
    --primary: #00d4ff;
    --secondary: #7b2ffc;
    --accent: #ff6b9d;
    --dark: #0a0e1a;
}
```

### Content

Edit `templates/index.html` to customize:

- Hero section
- Name and professional title
- Biography
- Skills
- Experience
- Projects
- Statistics
- Social links
- Contact information

Replace:

```text
static/assets/me.png
```

with your own profile image.

### Background Animations

Example:

```css
.network-grid {
    animation: gridShift 30s linear infinite;
}

.packet-1 {
    animation: packetFlow1 12s linear infinite;
}
```

Adjust animation durations to make effects faster or slower.

---

## 📱 Responsive Design

| Device | Resolution | Breakpoint |
|---|---:|---:|
| 4K Desktop | 2560 × 1440+ | > 900px |
| Laptop | 1366 × 768 | > 900px |
| Tablet | 768 × 1024 | 600px – 900px |
| Mobile | 375 × 812 | 380px – 600px |
| Smart Watch | 280 × 280 | < 380px |

### Touch Optimization

- 44px minimum touch targets.
- Mobile-friendly typography.
- Proper spacing between interactive elements.
- Touch-friendly buttons and links.
- Responsive navigation.

---

## 🔒 Security Features

The application takes advantage of Django's built-in security mechanisms, including:

- CSRF protection on forms.
- Parameterized database access through the Django ORM.
- Template auto-escaping to reduce XSS risk.
- Secure password hashing.
- Environment variables for sensitive configuration.

> Security also depends on correct production configuration, dependency updates, HTTPS, secure cookies, proper host settings, and keeping `DEBUG=False` in production.

---

## 🚀 Deployment

The project can be deployed to platforms that support Python/Django applications.

### Render

Example `render.yaml`:

```yaml
services:
  - type: web
    name: prince-portfolio
    env: python
    buildCommand: |
      pip install -r requirements.txt
      python manage.py collectstatic --noinput
      python manage.py migrate
    startCommand: gunicorn portfolio.wsgi:application
```

Configure your production environment variables through the hosting dashboard rather than committing them to the repository.

### Heroku

Create a `Procfile` containing:

```text
web: gunicorn portfolio.wsgi:application
```

Then deploy using your configured Heroku application and run migrations in the production environment.

### PythonAnywhere

General deployment steps:

1. Upload or clone the project.
2. Create and configure a virtual environment.
3. Install `requirements.txt`.
4. Configure the WSGI application.
5. Configure environment variables.
6. Run database migrations.
7. Configure static files.
8. Reload the web application.

---

## 🤝 Contributing

Contributions are welcome.

### 1. Fork the Repository

Create your own fork of the project.

### 2. Create a Feature Branch

```bash
git checkout -b feature/AmazingFeature
```

### 3. Commit Your Changes

```bash
git commit -m "Add AmazingFeature"
```

### 4. Push the Branch

```bash
git push origin feature/AmazingFeature
```

### 5. Open a Pull Request

Submit a pull request describing your changes.

---

## 📄 License

Distributed under the **MIT License**.

See the `LICENSE` file for more information.

---

## 👤 Author

**Prince Faith**

- **LinkedIn:** `@princefaith`
- **Facebook:** `@princefaith`
- **WhatsApp:** `+237 677 563 929`
- **Telegram:** `@princefaith`

---

## 🙏 Acknowledgments

Special thanks to:

- The Django Framework community
- Font Awesome
- Open-source contributors
- Developers and security researchers who continue to support the open-source ecosystem

---

## 📞 Contact

For inquiries, collaborations, projects, or professional opportunities, please use the website's contact form or reach out through the listed social channels.

---

<div align="center">

### ⭐ Support the Project

If you find this project useful, consider giving the repository a **⭐ Star**.

**Made with ❤️ by Prince Faith**

</div>
