# [Project Title]

# STFRY Academy

# [Project Description]

STFRY Academy is a full-featured, Django-based academy management system designed to centralize the administration of academic institutions. The platform
streamlines the management of students/users, faculties, lessons, classrooms, dormitories and course enrollments through a secure role-based architecture.
Educational institutions can manage their academic structure, student records, dormitories, classrooms and enrollment processes from a single system.

The system provides a dual-interface environment, consisting of an administrative management panel for CRUD operations and a user-facing interface for browsing
academic information. This system enables efficient academic organization, enrollment tracking and information access within a unified platform.

This system is built around a modular multi-app architecture and role-based authorization and access control. The platform separates administrative operations
from the public-facing academic interface, providing a secure, scalable and maintainable system for academy management.

# [Features]

- User Authentication (Secure login and logout system.)
- Administrative User Provisioning (Self-signup is disabled by design. Following institutional standards, user accounts are securely created and managed exclusively by the administration.)
- Role-based Access Control (Distinct permission levels for Admin, Teacher and Student.)
- Academic Management (CRUD) (Management of faculties, lessons, classrooms and student/user profiles.)
- Dormitory Management (CRUD)
- Enrollment Management System (CRUD) (Dynamic course assignment and student-to-class registration.)
- AJAX-based Dynamic CRUD Operations (management panel)
- Classroom and Dorm Detail Views
- User Directory and Listing pages
- Security Measures and User Authorization

# [Tech Stack]

- Python 3 for Backend
- Django Framework for Backend Development
- SQLite for Database
- JavaScript (AJAX / Fetch API) for Frontend Logic
- HTML5 / CSS3 & Bootstrap Framework for Frontend UI

# [Installation Guide]

# 1. Clone the repository:
```
git clone <repo-url>
```

# 2. Create virtual environment:
```
python -m venv academy
```

# 3. Activate environment:
Windows;
```
academy\Scripts\Activate.bat
```
macOS;
```
source academy/bin/activate
```
Linux;
```
source academy/bin/activate
```

# 4. Install dependencies:
```
pip install -r requirements.txt
```

# 5. Run migrations:
```
python manage.py migrate
```

# 6. Create superuser:
```
python manage.py createsuperuser
```

# 7. Run server:
```
python manage.py runserver
```

# [Project Structure]

# Basic;

```
apps/
│
├── academics/    # faculties, lessons, classes
├── accounts/     # authentication, roles, and user profiles
├── dorms/        # dorm management, dormitory building
├── enrollments/  # tracks student and class enrollment relationships
├── management/   # AJAX-powered administrative CRUD panel & management base layouts
└── core/         # user base templates, static assets, and public homepage
```

# Full;

```
stfry_academy
│   db.sqlite3
│   manage.py
│
├───apps
│   │   __init__.py
│   │
│   ├───academics
│   │   │   admin.py
│   │   │   apps.py
│   │   │   models.py
│   │   │   tests.py
│   │   │   urls.py
│   │   │   views.py
│   │   │   __init__.py
│   │   │
│   │   ├───migrations
│   │   │       0001_initial.py
│   │   │       0002_alter_faculty_options.py
│   │   │       __init__.py
│   │   │
│   │   ├───templates
│   │       └───academics
│   │               classes.html
│   │               classroom_detail.html
│   │               faculties.html
│   │               lessons.html
│   │
│   ├───accounts
│   │   │   admin.py
│   │   │   apps.py
│   │   │   forms.py
│   │   │   models.py
│   │   │   tests.py
│   │   │   urls.py
│   │   │   views.py
│   │   │   __init__.py
│   │   │
│   │   ├───migrations
│   │   │       0001_initial.py
│   │   │       __init__.py
│   │   │
│   │   ├───templates
│   │       └───accounts
│   │               dashboard.html
│   │               login.html
│   │               user_list.html
│   │
│   ├───core
│   │   │   admin.py
│   │   │   apps.py
│   │   │   models.py
│   │   │   tests.py
│   │   │   urls.py
│   │   │   views.py
│   │   │   __init__.py
│   │   │
│   │   ├───migrations
│   │   │       __init__.py
│   │   │
│   │   ├───static
│   │   │   └───core
│   │   │       └───css
│   │   │               home.css
│   │   │
│   │   ├───templates
│   │       │   base.html
│   │       │
│   │       └───core
│   │               home.html
│   │
│   ├───dorms
│   │   │   admin.py
│   │   │   apps.py
│   │   │   models.py
│   │   │   tests.py
│   │   │   urls.py
│   │   │   views.py
│   │   │   __init__.py
│   │   │
│   │   ├───migrations
│   │   │       0001_initial.py
│   │   │       __init__.py
│   │   │
│   │   ├───templates
│   │       └───dorms
│   │               dorms.html
│   │               dorm_detail.html
│   │
│   ├───enrollments
│   │   │   admin.py
│   │   │   apps.py
│   │   │   models.py
│   │   │   tests.py
│   │   │   views.py
│   │   │   __init__.py
│   │   │
│   │   ├───migrations
│   │           0001_initial.py
│   │           __init__.py
│   │
│   ├───management
│       │   admin.py
│       │   apps.py
│       │   models.py
│       │   tests.py
│       │   urls.py
│       │   views.py
│       │   __init__.py
│       │
│       ├───migrations
│       │       __init__.py
│       │
│       ├───templates
│           │   base_management.html
│           │
│           └───management
│                   classes.html
│                   dashboard_management.html
│                   dorms.html
│                   enrollments.html
│                   faculties.html
│                   lessons.html
│                   users.html
│
└───stfry_academy
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py
```

# [Architecture Explanation]

# 1. Project Architecture

Multi-app Django MVT (Model-View-Template) Architecture

User (Browser)
|
v
URLs (routing)
|
v
Views (logic)
|
v
Models (database)
|
v
Templates (UI)

[ User / Browser ] 
       │  ^
       │  │ (HTTP Request / AJAX Fetch)
       v  │
  [ URLs Routing ]
       │
       v
   [ Views (logic)] <────────> [ Django ORM / Models ] <───> [ SQLite DB ]
       │
       v
 [ Templates / UI ] (Rendered with Bootstrap)

# 2. App Separation Strategy

accounts -> custom authentication system and user profiles
academics -> academic structure (faculty, lesson, class)
dorms -> dormitory system
enrollments -> relationship system acts as a specialized bridge application handling relational data between users and classes (user <-> class)
management -> admin CRUD panel and administrative views (AJAX-based)
core -> shared UI + homepage

Each app is responsible for a single domain to ensure modularity and maintainability.

# 3. Database Design Logic

User Model extends Django's native AbstractUser to support custom roles (admin, teacher, student).

Dorm -> User (One-to-Many relationship representing students assigned to specific dorms.)
Faculty -> Lesson (One-to-Many relationship structuring course catalogs under faculties.)
Lesson -> Classroom (One-to-Many relationship where each lesson can have multiple classrooms.)
Classroom <-> User (Many-to-Many relationship via Enrollment model to manage class rosters.)

Core Models
User
- Extends Django AbstractUser
- Stores authentication data and role information
- Roles: Admin, Teacher, Student
Faculty
- Represents an academic faculty/department
- Contains faculty name and related metadata
Lesson
- Represents a course offered by a faculty
- Belongs to a Faculty
Classroom
- Represents a specific class section
- Associated with a Lesson
Dorm
- Represents a dormitory building
- Stores dorm information and assigned students
Enrollment
- Junction model implementing the many-to-many relationship between Students and Classrooms
- Tracks student course registrations and enrollment records

# 4. Design Choices

- Bootstrap framework utilized as the primary frontend foundation, providing a fully responsive and mobile-friendly interface while enabling rapid UI development
- AJAX (Asynchronous JavaScript and XML) is used in management panel to improve UX and CRUD operations seamlessly and without page reloads
- Separation between management and user-facing pages
- Django ORM used instead of raw SQL for maintainability and to help prevent SQL Injection and other common database-related vulnerabilities
- Role-based Access Control implemented via custom decorator

# [Screenshots]

Additional screenshots can be found in the `screenshots/` directory.

# [Future Improvements]

- Email notifications
- Course scheduling system
- Student grade management
- REST API support
- PostgreSQL deployment configuration