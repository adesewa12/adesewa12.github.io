#bot.py

from chatterbot import ChatBot

chatbot = ChatBot("Peanuts")

email_words= ["thanks", "sure", "i am done", "how can i reach adesewa", "no", "help"]

def email_process(query):
    """
    Share email with visitor
    """
    return "Email Adesewa for further inquiries adesewa.adesida@gmail.com"

def linkedin_process(query):
    """
    Share linkedin with visitor
    """
    return "Refer to Adesewa's LinkedIn for more updates, www.linkedin.com/in/adesewa-a-70606434"

exit_conditions = (":q", "quit", "exit")
print("\nWelcome to my website, Peanuts is here to help \n")

print(f"🥜 Hi I am Peanuts,how can I help you today? ")
while True:
    query = input(">")
    if query.lower() in exit_conditions:
        print(linkedin_process(query))
        break
    elif query.lower() in email_words:
        print(email_process(query))
    else:
        print(f"🥜{chatbot.get_response(query)}")


