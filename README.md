# le-chat

### Inspiration
This idea of chat companion comes from Inworld and Character.AI, creating open-ended conversation with fictional characters or famous people.

### What it does
Create an account and login to chat with a cat. Who knows. Maybe this app will help cat owners understand their felines more better.

### How we built it
The text generation in response to the user prompt comes from Co:here. The generated text is outputted and also inserted into OpenAI for three images that go along with the cat's reply. The web app is built with Streamlit.

### Challenges we ran into
Keeping track of initializing values in session state or else the program will run into KeyErrors.
Making sure to reset the chat history to prevent bleeding over to another different account login
Picking the most effective initial prompt for Co:here
Accomplishments that we're proud of
Made a working chat bot in a web app.

### What we learned
Learned how to incorporate APIs such as Co:here into Streamlit setting up the API keys as environment variables (used Streamlit secrets management).

### What's next for Le Chat-GPT
Instead of clearing the chat history whenever the user logs out, store it in a database so each user will still keep their chat history and it would not interfere with the other accounts.
Have a loading animation or some indication that the program is still processing the user input
Maybe allow the chat bot to retain some information on what user has said earlier in the conversation
