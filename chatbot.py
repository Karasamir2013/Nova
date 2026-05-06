import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_nova():
    """Main chatbot function that allows you to have a conversation with Nova"""
    print("=" * 50)
    print("Welcome to Nova - Your AI Chatbot!")
    print("=" * 50)
    print("Type 'quit' or 'exit' to end the conversation")
    print("=" * 50)
    
    # Store conversation history
    messages = []
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Check if user wants to exit
        if user_input.lower() in ['quit', 'exit']:
            print("\nNova: Goodbye! Thanks for chatting with me!")
            break
        
        # Skip empty inputs
        if not user_input:
            continue
        
        # Add user message to history
        messages.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            # Get response from OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            
            # Extract the assistant's response
            assistant_message = response.choices[0].message.content
            
            # Add assistant message to history
            messages.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            # Display the response
            print(f"\nNova: {assistant_message}")
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Make sure you have set your OPENAI_API_KEY environment variable")
            break

if __name__ == "__main__":
    chat_with_nova()
