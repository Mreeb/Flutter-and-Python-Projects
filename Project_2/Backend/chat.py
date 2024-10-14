import ollama



system_message = {
    'role': 'system',
    'content': 'You are My mental Health Companion, A therapist, your name is Therape. you are to provide '
}

user_input = input("Enter your Question: ")

user_message = {
    'role': 'user',
    'content': user_input
}

response = ollama.chat(
    model='llama3.2', 
    messages=[system_message, user_message]
)

print(response['message']['content'])
