🛒 ShopX – Django Ecommerce Website (Server-Side Rendered)

ShopX is a full-featured ecommerce web application built using Django.
It provides a complete shopping experience with product browsing, cart management, checkout, order history, and a dedicated admin dashboard for managing products and users.

This project demonstrates real-world ecommerce logic, backend workflows, and Django best practices, using server-side rendered templates.

## 🚀 Preview
Here are some visuals from the project:

## 📸 Project Screenshots

### User Dashboard
![User Dashboard](screenshots/userdashboard.png)

### Carts
![Carts](screenshots/carts.png)

### Admin Dashboard
![Admin Dashboard](screenshots/admindashboard.png)

### Admin Can see users
![Users](screenshots/users.png)


✨ Key Features
👤 Customer

User registration & login (custom authentication, no Django default auth)

Browse products with:

🔍 Search (by name, description, category)

💰 Price filters

🗂️ Category filters

↕️ Sorting (Low → High / High → Low)

Product detail page with stock information

Session-based cart system (add, remove, adjust quantity)

Checkout with payment method selection (Card / UPI / Cash on Delivery)

Place orders

View order history

🛠️ Admin

Admin login (custom role-based access)

Admin dashboard

Add, edit, delete products

View all products

View all registered users

Stock management (auto-updated after orders)

🧠 Core Logic Highlights

Session-based authentication & role handling

Session-based cart system with stock validation

Order & OrderItem separation for clean order management

Context processor for global auth access, cart count, and recent orders

Cloudinary integration for product images

Clear separation of concerns:

Models → data

Views → backend logic

Templates → UI

⚠️ Frontend is rendered via Django templates; JavaScript is minimal or not used. All filtering, sorting, and cart operations are handled server-side.

🛠️ Tech Stack

Backend:

Python

Django

Django ORM

SQLite (default, can be replaced)

Frontend:

Django Templates (HTML)

CSS (styling only, no frontend logic)

Storage:

Cloudinary (for product images)

📂 Project Structure (Logic-Focused)
ecommerce/
│
├── ecommerce/
│   └── urls.py
│
├── myapp/
│   ├── models.py
│   ├── views.py
│   ├── context_processors.py
│   ├── urls.py
│   └── templates/
│
├── static/        # styling only (no logic)
├── manage.py
└── requirements.txt

🗃️ Database Models

Product

name, price, description, image (Cloudinary), category, stock

Customer

name, email, password (hashed)

Order

customer, total_price, payment_method, created_at

OrderItem

order, product, price, quantity

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/yash123-gif/Ecommerce-Project.git
cd shopx

2️⃣ Create Virtual Environment
python -m venv env
source env/bin/activate   # Windows: env\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Environment Variables

Create a .env file with Cloudinary credentials:

CLOUDINARY_CLOUD_NAME=your_name
CLOUDINARY_API_KEY=your_key
CLOUDINARY_API_SECRET=your_secret

5️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Start Server
python manage.py runserver


Open in browser: http://127.0.0.1:8000/

🔐 Admin Access

Admin login is custom handled (session-based, not Django superuser):

Email: admin@gmail.com
Password: 12345


🚀 Future Improvements

Payment gateway integration (Razorpay / Stripe)

Upgrade to Django authentication system

Wishlist feature

Product reviews & ratings

Pagination for products

REST API (Django REST Framework)

Optional React frontend for SPA experience

👨‍💻 Author

Yash Gupta
Python & Django Developer
Server-side rendered Full-Stack Projects

⭐ Support

If you like this project:

⭐ Star the repo

🍴 Fork it

🧠 Study it to learn real ecommerce backend logic