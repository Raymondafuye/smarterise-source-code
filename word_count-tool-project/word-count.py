# def count_words():
#     text = input("Enter your word ")
#     words = text.split()
#     word_count = {}
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count

# print(count_words()) 

def quiz_application():
    quiz = [

        {
            "question": "what is the capital of France",
            "options": ["paris", "london", "Berlin", "NIGERIA"],
            "answer": "paris"
        }
    ]

    score = 0
    for q in quiz:
        print(f"Question: {q['question']}")
        for idx, option in enumerate(q['options'], start=1):
            print(f"{idx}, {option}")

        answer = input("your answer: ")
        if answer == q['answer']:
            score += 1
    print(f"your score is {score}/{len(quiz)}")

quiz_application()