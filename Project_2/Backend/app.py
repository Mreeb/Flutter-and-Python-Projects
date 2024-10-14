from fastapi import FastAPI, Form
import ollama

app = FastAPI()

# Define the system message globally
system_message = {
    'role': 'system',
    'content': '''You are an assistant for Zong Network customer support.
      You will only assist with Zong-related questions and should not provide answers to any other topics.
        If a user asks a question that doesn\'t relate to your purpose, you are to simply respond 
        "Sorry I can\'t entertain this request; I can only provide answers to Zong-related queries".'''
}

# Variable to hold the loaded model
model_instance = None

@app.on_event("startup")
async def load_model():
    """Load the Llama 3.2 model when the FastAPI server starts."""
    global model_instance
    # Load the model only once on startup
    model_instance = 'llama3.2'  # This represents your model instance.
    print("Llama 3.2 model loaded successfully!")

@app.post("/ask-question/")
async def ask_question(question: str = Form(...)):
    # Define the user message with the input from the form
    user_message = {
        'role': 'user',
        'content': question
    }

    # Use the loaded model instance with both system and user messages
    response = ollama.chat(
        model=model_instance,  # Use the model instance loaded on startup
        messages=[system_message, user_message]
    )
    
    # Return the assistant's response
    return {"response": response['message']['content']}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)





# import ollama

# system_message = {
#     'role': 'system',
#     'content': 'You are an assistant for Zong Network customer support. You will only assist with Zong-related questions and should not provide answers to any other topics if a user asks a question that doesnt relate to your purpose you are to simply respond "Sorry I cant entertain this request i can only provide answers to zong related quries".'
# }

# user_input = input("Enter your Question: ")

# user_message = {
#     'role': 'user',
#     'content': user_input
# }

# response = ollama.chat(
#     model='llama3.2', 
#     messages=[system_message, user_message]
# )

# print(response['message']['content'])
