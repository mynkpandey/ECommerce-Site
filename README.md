# 🌟 ServiceHub: Premium Service Booking System

A state-of-the-art, full-stack service booking and management platform built with Django. Featuring a stunning **Glassmorphism UI**, real-time analytics, and role-based access control.

---

## ✨ Premium Features

### 🎨 Modern Glassmorphism UI
- **Aesthetic Excellence**: Built with a sleek dark theme, backdrop blurs, and vibrant gradients.
- **Dynamic Icons**: Integrated with FontAwesome for an intuitive visual experience.
- **Responsive Design**: Fully optimized for various screen sizes using Bootstrap 5.

### 📊 Advanced Admin Analytics
- **Visual Insights**: Real-time charts powered by **Chart.js** displaying platform health.
- **Revenue Tracking**: Live monitoring of platform earnings and booking distributions.
- **Exportable Reports**: One-click report generation for administrative oversight.

### 🍱 Category-Based Discovery
- **Smart Filtering**: Users can easily find services through a dynamic category system (Salon, Clinic, Repair, Tutor, etc.).
- **Rich Listings**: Detailed service cards with pricing, duration, and provider info.

### 🔐 Secure Multi-Role System
- **Users**: Browse, filter, and book appointments with secure simulated payments.
- **Providers**: Manage incoming requests through a dedicated glass-styled dashboard.
- **Admins**: Oversight of all platform metrics via an advanced analytics portal.

---

## 🛠 Tech Stack

- **Backend**: Python / Django 4.x
- **Frontend**: HTML5, Vanilla CSS (Glassmorphism), JavaScript
- **Visualization**: Chart.js
- **UI Framework**: Bootstrap 5
- **Icons**: FontAwesome 6
- **Typography**: Google Fonts (Outfit)
- **Database**: SQLite

---

## 🚀 Quick Start Instructions

1. **Install Dependencies**
   ```bash
   pip install django
   ```

2. **Run Databases Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **(Optional) Seed Realistic Data**
   The project comes with pre-configured categories and sample services for demo purposes.

4. **Launch Application**
   ```bash
   python manage.py runserver
   ```

---

## 🔑 Access Credentials (DEMO)

| Role | Username | Password |
| :--- | :--- | :--- |
| **Super Admin** | `admin` | `adminpassword` |
| **Service Provider** | `p_provider` | `providerpassword` |

---

## 📂 Project Structure
- `services/`: Category management and service discovery.
- `bookings/`: Core booking logic, payments, and analytics.
- `users/`: Role-based authentication and profile management.
- `templates/`: Premium glass-styled UI components.
