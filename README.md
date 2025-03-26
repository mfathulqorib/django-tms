# 🚚 Transport Management System

## 📄 Overview
The Transport Management System is a web-based application built using the Django framework to streamline the management of transportation logistics. It provides features for user registration and authentication, warehouse location management, shipment route optimization, shipment log tracking, and the generation of delivery notes.

## ⚙️ Features
1. **🔑 User Registration and Authentication**
   - Secure user registration and login functionality.
   - Role-based access control for Admin and regular users.

2. **🏢 Warehouse Management (Admin Only)**
   - Admin users can add and manage warehouse locations.

3. **🛋️ Shipment Route Optimization**
   - Users can input one or more delivery destinations.
   - The system calculates and suggests the fastest route for delivery.

4. **📊 Shipment Log Management**
   - Users can create, edit, and delete shipment logs.

5. **📝 Delivery Note Generation**
   - Users can generate delivery notes using predefined templates.

## 📚 Technology Stack
- Python
- Django
- HTML, CSS, JavaScript (Frontend)
- PostgreSQL or SQLite (Database)

## 🔧 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/transport-management-system.git
   cd transport-management-system
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   npm install
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
7. Access the app at [http://localhost:8000](http://localhost:8000).

## 💡 Usage
1. Register or log in as a user.
2. Admin users can add warehouse locations.
3. Input delivery destinations to get the fastest route.
4. Manage shipment logs (create, edit, delete).
5. Generate delivery notes with predefined templates.

## 📞 Contact
For any inquiries, please contact [mfathulqorib97@gmail.com](mailto:mfathulqorib97@gmail.com).

---

Happy coding and safe deliveries! 🚚

