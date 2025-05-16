quiz_questions=[
    {
        "questions": "WHAT IS THE CAPITAL OF FRANCE?",
        "options": ["A.PARIS","B.POLAND","C.SYDNEY","D.BERTH"],
        "answer":"A"
    },
    {
        "questions":"WHICH LANGUAGE IS USED FOR WEB DEVELOPMENT?",
        "options":["A.PYTHON","B.JAVA","C.JAVA SCRIPT","D.C"],
        "answer":"C"
    },

    {
        "questions": "WHICH DATA STRUCTURE USES FIFO ORDER?",
        "options": ["A.STACK", "B.QUEUE", "C.TREE", "D.GRAPH"],
        "answer": "B"
    },

    {
        "questions": "WHICH LANGUAGE IS MOST COMMONLY USED FOR DATA ANALYSIS?",
        "options": ["A.C", "B.JAVA", "C.R", "D.HTML"],
        "answer": "C"
    },

    {
        "questions": "WHICH COMPONENT IS CONSIDERED THE 'BRAIN' OF THE COMPUTER?",
        "options": ["A.MONITOR", "B.RAM", "C.CPU", "D.HARD DISK"],
        "answer": "C"
    },

    {
        "questions": "WHAT DOES 'SQL' STAND FOR?",
        "options": ["A.STRUCTURED QUERY LANGUAGE", "B.SIMPLE QUERY LANGUAGE", "C.SYSTEM QUERY LANGUAGE", "D.SEQUENTIAL QUERY LANGUAGE"],
        "answer": "A"
    },

    {
        "questions": "WHICH SORTING ALGORITHM HAS THE BEST AVERAGE CASE TIME COMPLEXITY?",
        "options": ["A.BUBBLE SORT", "B.INSERTION SORT", "C.MERGE SORT", "D.SELECTION SORT"],
        "answer": "C"
    }
]


def quiz():
    score=0
    for question in quiz_questions:
        print(question["questions"])
        for option in question["options"]:
            print(option)
        user_chocice=input("Enter your answer(A/B/C/D):").strip().upper()
        if user_chocice==question["answer"]:
            print(f"{user_chocice} is correct..")
            score+=1
        else:
            print(f"{user_chocice} is wrong.The correct answer is {question['answer']}!")
    print(f"Final Score: {score}/{len(quiz_questions)}")
quiz()