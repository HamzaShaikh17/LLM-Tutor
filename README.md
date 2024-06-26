# This directory contains working code for the given problem below

### Problem Statement 💡 :

Build a chatbot API that is able to ingest images or text by a user. The chatbot should be able to fetch accurate YouTube links and respond to the user while answering their query on the chat.

### Requirements ✅ :

1. The bot should be able to respond to both text and image based queries.
2. The bot should provide real youtube video links to clarify certain topics when needed - this should be done using APIs (and not generated by the LLM).
3. The bot should have a memory so a conversation can take place. (No requirements for the kind of memory - could be DB based or buffer based).
4. For the major LLMs used, consider using OpenAI models.
5. Consider using existing frameworks instead of building one yourself.
6. [Hint/Optional] The bot should follow an agent based infrastructure - where a base model has the ability to use “tools” that could include vision capabilities i.e. in this case, call the GPT-4V model and YouTube capabilities i.e. in this case, call YouTube search APIs - the params for which can be gathered directly from the base model or from a smaller model.

# Solution:

## This directory contains following modules

1. image_extract : extract image text data
2. mondoDB_query : update database after getting response from main api
3. yt_recommendation : recommend 5 relevant videos
4. main : generate response
5. .env :
  API_Key = "Your_key"
  You are supposed to create Youtube API instance. https://developers.google.com/youtube/v3/docs/search/list


   
