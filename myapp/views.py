import time
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import ResumeForm
import random

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Registration successful. Please login.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return render(request, 'thankyou.html')

def dashboard(request):
    return render(request, 'dashboard.html')


def load_questions_for_round(round_number):
    start = round_number * 5
    end = start + 15
    return QUESTIONS[start:end]

QUESTIONS = [
    {"question": "What is 2 + 2?", "options": ['2', '3', '4', '5'], "answer": "4"},
    {"question": "What is 5 * 6?", "options": ['11', '30', '20', '60'], "answer": "30"},
    {"question": "What is the capital of India?", "options": ['Delhi', 'Mumbai', 'Kolkata', 'Chennai'], "answer": "Delhi"},
    {"question": "What is 10 / 2?", "options": ['2', '5', '10', '20'], "answer": "5"},
    {"question": "What comes after 15?", "options": ['14', '15', '16', '17'], "answer": "16"},
    {"question": "What is the square of 3?", "options": ['3', '6', '9', '12'], "answer": "9"},
    {"question": "What is the largest ocean?", "options": ['Indian', 'Arctic', 'Atlantic', 'Pacific'], "answer": "Pacific"},
    {"question": "How many legs do spiders have?", "options": ['6', '8', '10', '12'], "answer": "8"},
    {"question": "Which planet is red?", "options": ['Earth', 'Mars', 'Venus', 'Jupiter'], "answer": "Mars"},
    {"question": "Which gas do we breathe in?", "options": ['Oxygen', 'Carbon Dioxide', 'Hydrogen', 'Nitrogen'], "answer": "Oxygen"},
    {"question": "Who wrote 'Ramayana'?", "options": ['Valmiki', 'Tulsidas', 'Kalidas', 'Chanakya'], "answer": "Valmiki"},
    {"question": "12 * 12 = ?", "options": ['122', '132', '144', '154'], "answer": "144"},
    {"question": "How many continents?", "options": ['5', '6', '7', '8'], "answer": "7"},
    {"question": "Which animal is fastest?", "options": ['Tiger', 'Leopard', 'Cheetah', 'Lion'], "answer": "Cheetah"},
    {"question": "What is H2O?", "options": ['Hydrogen', 'Oxygen', 'Water', 'Salt'], "answer": "Water"},
]

QUESTIONS_PER_TEST = 15

def aptitude_test(request):
    if request.method == "POST":
        score = int(request.POST.get("score", 0))
        question_index = int(request.POST.get("question_index", 0))
        selected_answer = request.POST.get("answer")

        # Retrieve questions from session
        question_set = request.session.get("question_set", [])
        current_questions = [QUESTIONS[i] for i in question_set]

        current_question = current_questions[question_index]
        if selected_answer == current_question["answer"]:
            score += 1

        question_index += 1

        if question_index >= len(current_questions):
            return render(request, "aptitude_result.html", {
                "final_score": score,
                "total": len(current_questions),
                "title": "Aptitude Round"
            })

        question = current_questions[question_index]

    else:
        # First attempt: shuffle and store question indexes
        question_index = 0
        score = 0
        all_indexes = list(range(len(QUESTIONS)))
        random.shuffle(all_indexes)
        selected_indexes = all_indexes[:QUESTIONS_PER_TEST]
        request.session["question_set"] = selected_indexes
        current_questions = [QUESTIONS[i] for i in selected_indexes]
        question = current_questions[question_index]

    return render(request, "aptitude_test.html", {
        "score": score,
        "question_index": question_index,
        "question": question,
        "is_last_question": (question_index == QUESTIONS_PER_TEST - 1),
        "title": "Aptitude Round"
    })

TECHNICAL_QUESTIONS = [
    {"question": "What is the output of print(2 ** 3)?", "options": ['6', '8', '9', '5'], "answer": "8"},
    {"question": "Which data type is immutable in Python?", "options": ['List', 'Set', 'Dictionary', 'Tuple'], "answer": "Tuple"},
    {"question": "What does HTML stand for?", "options": ['Hyper Trainer Marking Language', 'Hyper Text Markup Language', 'Hyper Text Marketing Language', 'High Text Machine Language'], "answer": "Hyper Text Markup Language"},
    {"question": "What does RAM stand for?", "options": ['Read Access Memory', 'Random Access Memory', 'Run Access Memory', 'Rapid Access Machine'], "answer": "Random Access Memory"},
    {"question": "Which keyword is used to define a function in Python?", "options": ['function', 'def', 'define', 'func'], "answer": "def"},

    {"question": "Which tag is used to insert a line break in HTML?", "options": ['<p>', '<break>', '<br>', '<lb>'], "answer": "<br>"},
    {"question": "Which sorting algorithm is best on average?", "options": ['Bubble Sort', 'Merge Sort', 'Selection Sort', 'Insertion Sort'], "answer": "Merge Sort"},
    {"question": "Which protocol is used for sending emails?", "options": ['FTP', 'SMTP', 'HTTP', 'TCP'], "answer": "SMTP"},
    {"question": "Which command is used to initialize a Git repository?", "options": ['git start', 'git init', 'git create', 'git new'], "answer": "git init"},
    {"question": "What is the extension of a Python file?", "options": ['.pt', '.p', '.py', '.pyth'], "answer": ".py"},

    {"question": "What does CSS stand for?", "options": ['Creative Style Sheets', 'Cascading Style Sheets', 'Computer Style Sheets', 'Colorful Style Sheets'], "answer": "Cascading Style Sheets"},
    {"question": "Which operator is used for equality check in Python?", "options": ['=', '==', '!=', '<>'], "answer": "=="},
    {"question": "Which keyword is used for a loop in Python?", "options": ['loop', 'iterate', 'for', 'foreach'], "answer": "for"},
    {"question": "Which language runs in the browser?", "options": ['Java', 'Python', 'C++', 'JavaScript'], "answer": "JavaScript"},
    {"question": "What does CPU stand for?", "options": ['Central Process Unit', 'Central Processing Unit', 'Computer Personal Unit', 'Central Processor Utility'], "answer": "Central Processing Unit"},
]


TECHNICAL_QUESTIONS_PER_TEST = 15

def technical_test(request):
    if request.method == "POST":
        score = int(request.POST.get("score", 0))
        question_index = int(request.POST.get("question_index", 0))
        selected_answer = request.POST.get("answer")

        # Get the stored random question indices
        question_set = request.session.get("technical_question_set", [])
        current_questions = [TECHNICAL_QUESTIONS[i] for i in question_set]

        current_question = current_questions[question_index]
        if selected_answer == current_question["answer"]:
            score += 1

        question_index += 1

        if question_index >= len(current_questions):
            return render(request, "technical_result.html", {
                "final_score": score,
                "total": len(current_questions),
                "title": "Technical Round"
            })
 
        question = current_questions[question_index]

    else:
        # First visit: shuffle questions and store in session
        question_index = 0
        score = 0
        all_indexes = list(range(len(TECHNICAL_QUESTIONS)))
        random.shuffle(all_indexes)
        selected_indexes = all_indexes[:TECHNICAL_QUESTIONS_PER_TEST]
        request.session["technical_question_set"] = selected_indexes
        current_questions = [TECHNICAL_QUESTIONS[i] for i in selected_indexes]
        question = current_questions[question_index]

    return render(request, "technical_test.html", {
        "score": score,
        "question_index": question_index,
        "question": question,
        "is_last_question": (question_index == TECHNICAL_QUESTIONS_PER_TEST - 1),
        "title": "Technical Round"
    })


CODING_QUESTIONS = {
    "arrays": [
        {
            "question": "Find the maximum subarray sum.",
            "difficulty": "easy",
            "test_cases": [
                {"input": "[-2,1,-3,4,-1,2,1,-5,4]", "expected": "6"},
                {"input": "[1,2,3,4,-10]", "expected": "10"}
            ]
        },
        {
            "question": "Rotate an array by k steps.",
            "difficulty": "medium",
            "test_cases": [
                {"input": "[1,2,3,4,5], k=2", "expected": "[4,5,1,2,3]"},
                {"input": "[0,1,2], k=4", "expected": "[2,0,1]"}
            ]
        }
    ],
    "linkedlist": [
        {
            "question": "Reverse a linked list.",
            "difficulty": "easy",
            "test_cases": [
                {"input": "1->2->3->4->5", "expected": "5->4->3->2->1"},
                {"input": "1->2", "expected": "2->1"}
            ]
        }
    ],
    # Add more topics: "trees", "strings", "dp"
}

LANGUAGES = ["python", "c", "cpp", "java"]

def coding_test_intro(request):
    if request.method == "POST":
        # Save selections to session
        request.session["coding_topic"] = request.POST.get("topic")
        request.session["coding_lang"] = request.POST.get("language")
        request.session["coding_round"] = 0
        request.session["coding_score"] = 0
        return redirect("coding_test")  
    return render(request, "coding_test_intro.html", {
        "topics": CODING_QUESTIONS.keys(),
        "languages": LANGUAGES
    })

@csrf_exempt
def coding_test(request):
    topic = request.session.get("coding_topic")
    lang = request.session.get("coding_lang")
    round_number = request.session.get("coding_round", 0)
    score = request.session.get("coding_score", 0)

    if topic not in CODING_QUESTIONS or round_number >= 3:
        return redirect("coding_result")

    question = random.choice(CODING_QUESTIONS[topic])
    request.session["current_question"] = question

    if request.method == "POST":
        submitted_code = request.POST.get("code")
        passed = 0
        for test in question["test_cases"]:
            if test["expected"] in submitted_code:  # Simulate test pass (placeholder)
                passed += 1
        request.session["coding_score"] = score + passed * 5
        request.session["coding_round"] = round_number + 1
        if request.session["coding_round"] >= 3:
            return redirect("coding_result")
        return redirect("coding_test")

    # ✅ This is where you return data to the coding_test.html template
    return render(request, "coding_test.html", {
        "question": question,
        "round_number": round_number + 1,
        "lang": lang,
        "time_limit": 30 * 60  # 30 minutes in seconds
    })


def coding_result(request):
    return render(request, "coding_result.html", {
        "score": request.session.get("coding_score", 0),
        "total": 30
    })

HR_QUESTIONS ={
  "TCS": [
    "Tell me about yourself.",
    "Why do you want to join TCS?",
    "Are you willing to relocate anywhere in India?",
    "What are your strengths and weaknesses?",
    "Describe a situation where you worked under pressure.",
    "How do you handle conflicts in a team?",
    "What do you know about TCS?",
    "Where do you see yourself in 5 years?",
    "Are you open to working night shifts?",
    "What is your expectation from this job?"
  ],
  "Infosys": [
    "Introduce yourself.",
    "Why do you want to work at Infosys?",
    "How do you keep yourself updated with technology?",
    "Tell me about a time you failed and how you handled it.",
    "What is your biggest achievement?",
    "Describe a time you had to lead a team.",
    "How do you handle criticism?",
    "What will you do if you are stuck in a task?",
    "Are you willing to sign a service agreement?",
    "What values do you think Infosys looks for in an employee?"
  ],
  "Wipro": [
    "Tell me about a time when you took initiative.",
    "Why Wipro?",
    "What makes you a good fit for this role?",
    "How do you handle pressure and deadlines?",
    "Describe a situation where you helped a teammate.",
    "What motivates you to perform well?",
    "Are you comfortable working in a diverse environment?",
    "How would you handle a disagreement with your manager?",
    "Are you flexible with work timings and shifts?",
    "What are your expectations from Wipro?"
  ],
  "Accenture": [
    "Why do you want to work at Accenture?",
    "How do you prioritize your work?",
    "Describe a project where you had to meet a tight deadline.",
    "How do you contribute to team success?",
    "What do you know about Accenture's values?",
    "How do you handle multitasking?",
    "Have you ever disagreed with your team? How did you handle it?",
    "Describe a time when you had to learn something new quickly.",
    "What is your understanding of client-centric work?",
    "Do you have any leadership experience?"
  ],
  "Cognizant": [
    "Tell me about a situation when you had to adapt quickly.",
    "Why should we hire you?",
    "Are you aware of Cognizant’s work culture?",
    "How do you react to negative feedback?",
    "Have you ever worked on a team project? Describe your role.",
    "What is your biggest strength, and how will it help you here?",
    "How do you stay organized?",
    "What do you know about Cognizant's digital initiatives?",
    "What are your career goals?",
    "How would you handle a disagreement with a client?"
  ],
  "Capgemini": [
    "What do you know about Capgemini?",
    "Why do you want to join Capgemini?",
    "How do you manage your time and meet deadlines?",
    "Have you worked in a diverse team before?",
    "How do you approach problem-solving?",
    "Tell me about a time you failed. What did you learn?",
    "Are you ready to travel for projects?",
    "What are your salary expectations?",
    "How would you contribute to Capgemini’s mission?",
    "What are the three qualities a good team member must have?"
  ],
  "IBM": [
    "Describe yourself in three words.",
    "What do you know about IBM’s core business areas?",
    "Have you taken part in any leadership activities?",
    "Describe an innovative idea you implemented.",
    "What would you do if you were assigned an unfamiliar task?",
    "How do you deal with pressure in work situations?",
    "What are your hobbies and how do they relate to your career?",
    "Why do you want to be part of IBM?",
    "How would you explain a technical concept to a non-technical person?",
    "What’s one challenge you’ve overcome in life?"
  ],
  "HCL Technologies": [
    "What makes you unique from other candidates?",
    "How do you keep up with technological advancements?",
    "Describe a situation where you took ownership of a task.",
    "How would you handle working with a difficult teammate?",
    "What do you know about HCL’s company values?",
    "What is your approach to handling constructive feedback?",
    "Have you ever made a mistake? What did you learn?",
    "What is your greatest strength that fits this role?",
    "Why do you want to work in the IT industry?",
    "Are you ready to commit to a long-term opportunity?"
  ],
  "Tech Mahindra": [
    "Describe a project you’re proud of.",
    "What do you know about Tech Mahindra?",
    "Have you handled a conflict in a team before?",
    "What would your friends say about you?",
    "What motivates you to work hard?",
    "Are you comfortable with frequent changes in project needs?",
    "How do you deal with failure?",
    "What are your short-term and long-term career plans?",
    "Are you open to upskilling and certifications?",
    "Do you have any questions for us?"
  ],
  "L&T Infotech": [
    "Tell me something not in your resume.",
    "How do you manage both work and stress?",
    "Why do you want to join LTI?",
    "What skills do you bring to this job?",
    "Have you ever worked under a tough deadline?",
    "What are your personal values and how do they align with LTI?",
    "Are you okay with contractual employment or training bonds?",
    "What do you know about our recent projects or clients?",
    "How do you improve your communication skills?",
    "Describe a time you made a decision without complete information."
  ]
}


def hr_company_select(request):
    if request.method == "POST":
        company = request.POST.get("company")
        return redirect(f"/hr/questions/{company}/")
    return render(request, "hr_company_select.html", {
        "companies": HR_QUESTIONS.keys()
    })

def hr_questions(request, company):
    questions = HR_QUESTIONS.get(company, [])
    return render(request, "hr_questions.html", {
        "company": company,
        "questions": questions
    })

def resume_checker(request):
    result = None
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            job_title = form.cleaned_data['job_title']
            resume = request.FILES['resume_file']
            content = resume.read().decode(errors="ignore").lower()

            # Simple keyword matching logic (you can replace with ML model)
            keywords = {
                "Data Analyst": ["excel", "sql", "data", "analysis", "tableau"],
                "Software Engineer": ["python", "java", "code", "development", "algorithm"],
                "Project Manager": ["project", "manage", "timeline", "budget", "stakeholders"],
                "Machine Learning Engineer": ["model", "python", "ml", "training", "data"]
            }

            match_count = sum(word in content for word in keywords[job_title])
            result = "Fit for the job" if match_count >= 2 else "Not a good fit"

            return render(request, "resume_result.html", {
                "result": result,
                "job_title": job_title
            })
    else:
        form = ResumeForm()
    return render(request, "resume_checker.html", {"form": form})