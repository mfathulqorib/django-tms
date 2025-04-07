# 🚚 Transport Management System

## 📄 Overview
The Transport Management System is a web-based application built with Django to simplify logistics and delivery management. It features role-based access control for administrators and regular users, supporting warehouse management, delivery order tracking, and history monitoring.

## ⚙️ Features

### 👤 User Roles
- **Admin Users:**
  - Register and manage warehouses.
  - Create and view delivery orders.
  - View delivery order history.
- **Regular Users:**
  - View delivery orders.
  - View delivery order history.

### 🔐 Authentication
- Secure login system with role-based access control.

### 📦 Delivery Order Management
Admin users can create delivery orders with:
- Assigned delivery personnel
- Destination warehouses
- Estimated time of arrival (ETA)
- Notes or additional delivery information

### 🏢 Warehouse Management (Admin Only)
- Add, edit, and delete warehouse data.

## 🧪 Test Credentials
To test the application, you can log in with:
- **Username:** `admin`  
- **Password:** `admin1234`

## 🛠️ Technology Stack
- **Backend:** Python, Django  
- **Frontend:** HTML, Tailwind CSS, JavaScript  
- **Database:** PostgreSQL or SQLite

## 🧩 Dependencies
- Django
- Other dependencies listed in `requirements.txt`

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mfathulqorib/django-tms.git
   cd django-tms
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional if using the test account):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## 💡 Usage Example
 1.	Log in using the admin credentials provided above.
 2.	Navigate to the Warehouse section to register warehouse locations.
 3.	Go to the Delivery Order section to create a new delivery order by selecting destinations and assigning a delivery person.
 4.	View delivery order history to track completed deliveries.

## 📧 Contact

For any inquiries or support, please contact mfathulqorib97@gmail.com