import os
import openai

# Set your OpenAI GPT-3 API key
openai.api_key = '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'

#what is the weather?
def ask_gpt(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # You can choose a different engine based on your preference and usage
        prompt=prompt,
        max_tokens=150  # You can adjust this based on the desired response length
    )
    return response.choices[0].text.strip()


def main():
    print("Welcome to GPT-3 Console Chat!")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        prompt = f"You: {user_input}\nGPT-3:"
        response = ask_gpt(prompt)
        print(response)


if __name__ == "__main__":
    main()



