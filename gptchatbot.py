import openai

openai.api_key = "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"
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model ="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}])

    
    return response.choices[0].message.content.strip()
if __name__=="__main":
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break

        response = chat_with_gpt(user_input)
        print("chatbot",response)