# AI Complaint Management System

An intelligent Complaint Management System built with Django that helps organizations efficiently manage, track, and resolve customer complaints. The system incorporates AI-powered sentiment analysis to automatically identify and prioritize urgent complaints, improving response times and customer satisfaction.

---

## Features

### Customer Features
- User Registration & Authentication
- Submit Complaints
- Edit Submitted Complaints
- Track Complaint Status
- View Personal Complaint Dashboard
- Complaint History Management

### Admin/Staff Features
- View All Complaints
- Manage Complaint Status
- Update Complaint Progress
- Monitor Customer Issues
- Complaint Analytics Dashboard
- Priority-Based Complaint Handling

### AI-Powered Features
- Sentiment Analysis using TextBlob
- Automatic Priority Assignment
- Detection of Negative Customer Feedback
- High-Priority Escalation for Critical Complaints

---

## Complaint Workflow

```text
Pending
   ↓
In Progress
   ↓
Resolved
```

The system allows staff members to manage complaints through different stages until resolution.

---

## Complaint Categories

- Technical Support
- Billing & Payments
- Account Issues
- General Feedback

---

## Technology Stack

### Backend
- Django
- Python

### Database
- SQLite (Development)
- PostgreSQL/MySQL (Production Ready)

### AI/NLP
- TextBlob
- Natural Language Processing (NLP)

### Frontend
- HTML
- CSS
- Bootstrap

---

## AI Sentiment Analysis

When a customer submits a complaint, the system analyzes the complaint text using TextBlob.

### Example

**Customer Complaint:**
> "I am extremely frustrated with your service. Nothing is working."

**System Result:**
- Sentiment: Negative
- Priority: High
- Immediate Escalation

This helps support teams quickly identify dissatisfied customers and address urgent issues.

---

## Suitable Industries

This system can be adapted for various businesses and organizations, including:

### SaaS & Technology Companies
- Software bug reports
- Technical support requests
- Account access issues

### E-Commerce Platforms
- Order complaints
- Refund requests
- Delivery issues

### Telecommunications Providers
- Service outages
- Network issues
- Billing disputes

### Educational Institutions
- Student grievances
- Portal access issues
- Fee-related complaints

### Property Management
- Maintenance requests
- Tenant complaints
- Service tracking

### Banking & Financial Services
- Transaction disputes
- Account-related complaints
- Payment issues

---

## Project Structure

```text
Complaint_System/
│
├── complaint/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── migrations/
│
├── Complaint_System/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/AI-Complaint-Management-System.git
cd AI-Complaint-Management-System
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run Development Server

```bash
python manage.py runserver
```

### 7. Open Browser

```text
http://127.0.0.1:8000/
```

---

## Future Improvements

- Email Notifications
- Complaint Assignment to Staff
- AI Complaint Classification
- Complaint Analytics Dashboard
- REST API Integration
- Real-Time Chat Support
- PDF Report Generation
- Complaint Resolution Time Tracking

---

## Learning Outcomes

This project demonstrates:

- Django Web Development
- Authentication & Authorization
- CRUD Operations
- Database Management
- Natural Language Processing (NLP)
- Sentiment Analysis
- Role-Based Access Control
- Software Engineering Best Practices

---

## Author

**Ahsan Hussain**

BS Software Engineering  
University of Management and Technology (UMT)  
Lahore, Pakistan

LinkedIn:
https://www.linkedin.com/in/ahsan-hussain-dev

---

## License

This project is developed for educational and portfolio purposes.
