# Placement Preparation Platform

## Project Overview

The Placement Preparation Platform is a web-based application developed using Django to help students prepare for campus placements. It provides structured resources for coding practice, aptitude preparation, and interview questions in an easy-to-use interface.

## Features

*  Coding practice questions
*  Aptitude preparation
*  Interview questions and tips
*  Simple and user-friendly interface
*  Organized learning modules

## Technologies Used

* Frontend: HTML, CSS
* Backend: Django (Python)
* Programming Language: Python

## Project Structure

Placement_Preparation_Platform/
│── manage.py
│── app/
│── templates/
│── static/
│── db.sqlite3
│── requirements.txt
│── README.md

## Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/Bhagi-24/Placement_Preparation_Platform.git
cd Placement_Preparation_Platform
```

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate it:

* Windows:

```
venv\\Scripts\\activate
```

* Mac/Linux:

```
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Apply Migrations

```
python manage.py migrate
```

### 5. Run the Server

```
python manage.py runserver
```

### 6. Open in Browser

```
http://127.0.0.1:8000/
```

## How to Run the Project

Anyone can run this project locally by following the above steps. No additional configuration is required.

## Future Enhancements

* Add user authentication system
* Include mock tests and scoring
* Improve UI/UX design
* Add real-time coding editor

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is open-source and available for learning purposes.

## Author

Bhargavi Lankapalli

## Acknowledgements

Thanks to all resources and inspirations that helped in building this project.
