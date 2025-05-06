# import re
# import yt_dlp
# import os
# import requests
# from dotenv import load_dotenv
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.vectorstores import FAISS
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.schema import Document
# from langchain.chat_models import ChatOpenAI
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import RetrievalQA
# from langchain.agents import initialize_agent, AgentType, Tool
# from langchain_core.messages import HumanMessage
# from langchain_community.tools import YouTubeSearchTool

# load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")
# api_key = os.getenv('IDEOGRAM')

# # Download audio
# def download_audio(youtube_url, output_path):
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'outtmpl': output_path,
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#         'quiet': True
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([youtube_url])

# # Extract YouTube links from search text
# def extract_youtube_links(text):
#     pattern = r'(https?://[^\s]+)'
#     return re.findall(pattern, text)

# # Convert audio to text (fake placeholder, adjust for real Whisper later)
# def transcribe_audio_openai(file_path):
#     return "This is a fake transcription for demo."

# # Split text into chunks
# def split_text(text, chunk_size=500, chunk_overlap=100):
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap,
#         length_function=len
#     )
#     return splitter.split_text(text)

# # Process videos
# def process_videos_and_store(links,user_id):
#     all_documents = []
#     for idx, url in enumerate(links):
#         output_mp3 = f"video_{idx}"
#         download_audio(url, output_mp3)
#         full_text = transcribe_audio_openai(f'{output_mp3}.mp3')
#         chunks = split_text(full_text)
#         for chunk_id, chunk_text in enumerate(chunks):
#             doc = Document(
#                 page_content=chunk_text,
#                 metadata={"source": url, "video_name": output_mp3, "chunk_id": chunk_id}
#             )
#             all_documents.append(doc)
#             all_documents = [Document(page_content=d.page_content.lower(), metadata=d.metadata) for d in all_documents]


#     if all_documents:
#         embeddings = OpenAIEmbeddings()
#         vectorstore = FAISS.from_documents(all_documents, embeddings)
#         # vectorstore.save_local("faiss_index")
#         vectorstore.save_local(f"faiss_index_user_{user_id}")


# # Setup LangChain agent
# embeddings = OpenAIEmbeddings()
# # vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
# # retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})


# # qa_chain = RetrievalQA.from_chain_type(
# #     llm=ChatOpenAI(model_name="gpt-4.1", openai_api_key=openai_api_key, temperature=0),
# #     retriever=retriever,
# #     chain_type="map_reduce"
# # )

# # def learning_function(query):
# #     return qa_chain.run(query)

# # memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


# # agent = initialize_agent(
# #     tools=[Tool(name="LearningTool", func=learning_function, description="QA from docs")],
# #     llm=ChatOpenAI(model_name="gpt-4.1", openai_api_key=openai_api_key, temperature=0),
# #     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
# #     memory=memory,
# #     verbose=True,
# #     handle_parsing_errors=True
# # )

# # ———————————————————————————
# # تابع التلخيص من قاعدة المعرفة
# # def summarize_function(vectorstore):
# #     docs = vectorstore.similarity_search("", k=1000)
# #     text = " ".join([doc.page_content for doc in docs])
# #     prompt = f"Summarize the following content in bullet points:\n\n{text}"
    
# #     llm = ChatOpenAI(model_name="gpt-4.1", openai_api_key=openai_api_key)
# #     response = llm.invoke([HumanMessage(content=prompt)])
    
# #     return response.content

# # # تابع إنشاء خريطة ذهنية
# # def mindmap_image_function(query: str) -> str:
# #     try:
# #         short_text = summarize_function(query)
# #         prompt = f"A mind map with only main topics: {short_text}. Clear readable text, minimal connections, compact design."

# #         endpoint = "https://api.ideogram.ai/generate"
# #         headers = {
# #             "Api-Key": api_key,
# #             "Content-Type": "application/json"
# #         }
# #         payload = {
# #             "image_request": {
# #                 "prompt": prompt,
# #                 "model": "V_2",
# #                 "aspect_ratio": "ASPECT_1_1",
# #                 "magic_prompt_option": "AUTO"
# #             }
# #         }

# #         response = requests.post(endpoint, headers=headers, json=payload)

# #         if response.status_code == 200:
# #             image_url = response.json()["data"][0]["url"]
# #             return f"🖼️ Mindmap image generated! View here: {image_url}"
# #         else:
# #             return f"❌ Error generating mindmap image: {response.text}"
# #     except Exception as e:
# #         return f"❌ Error generating mindmap image: {str(e)}"

# # # تابع إنشاء الاختبار
# # def generate_quiz_from_text(vectorstore):
# #     all_docs = vectorstore.similarity_search("", k=1000)
# #     full_text = " ".join([doc.page_content for doc in all_docs])

# #     quiz_prompt = f"""
# # You are a smart teacher. Create 10 multiple-choice and true/false questions, each with 4 options:

# # {full_text}

# # Format them like this:  
# # 1- Question?
# # a) Option1
# # b) Option2
# # c) Option3
# # d) Option4
# # """
# #     llm = ChatOpenAI(model_name="gpt-4.1", openai_api_key=openai_api_key, temperature=0)
# #     return llm.predict(quiz_prompt)

# # ———————————————————————————
# # تحديث الأدوات في الوكيل (Agent) لتشمل التلخيص والاختبار والخريطة الذهنية
# # tools = [
# #     Tool(name="LearningTool", func=learning_function, description="Answer from video documents."),
# #     Tool(name="SummarizeTool", func=summarize_function, description="Summarize content in bullet points."),
# #     Tool(name="MindMapImageTool", func=mindmap_image_function, description="Create a mind map from summarized content."),
# #     Tool(name="QuizTool", func=generate_quiz_from_text, description="Generate a quiz based on the documents."),
# # ]

# # إعادة تهيئة الوكيل بعد تحديث الأدوات



# user_agents = {}  # حفظ الـ agent لكل مستخدم

# def get_agent_for_session(user_id):
#     # تحميل أو إنشاء FAISS خاص بالمستخدم
#     faiss_path = f"faiss_index_user_{user_id}"
#     if os.path.exists(faiss_path):
#         vectorstore = FAISS.load_local(faiss_path, embeddings, allow_dangerous_deserialization=True)
#     else:
#         # مبدئيًا ننشئ فارغ (أو ضع هنا data init لو تحب)
#         vectorstore = FAISS.from_texts([], embeddings)
#         vectorstore.save_local(faiss_path)

#     retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})

#     memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
#     llm = ChatOpenAI(model_name="gpt-4.1", openai_api_key=openai_api_key, temperature=0)

#     qa_chain = RetrievalQA.from_chain_type(
#         llm=llm,
#         retriever=retriever,
#         chain_type="map_reduce"
#     )
#     def learning_function(query):
#         return qa_chain.run(query)
    


#     def summarize_function(vectorstore):
#         docs = vectorstore.similarity_search("", k=1000)
#         text = " ".join([doc.page_content for doc in docs])
#         prompt = f"Summarize the following content in bullet points:\n\n{text}"
        
#         llm = ChatOpenAI(model_name="gpt-4.1", openai_api_key=openai_api_key)
#         response = llm.invoke([HumanMessage(content=prompt)])
        
#         return response.content

#     # تابع إنشاء خريطة ذهنية
#     def mindmap_image_function(query: str) -> str:
#         try:
#             short_text = summarize_function(query)
#             prompt = f"A mind map with only main topics: {short_text}. Clear readable text, minimal connections, compact design."

#             endpoint = "https://api.ideogram.ai/generate"
#             headers = {
#                 "Api-Key": api_key,
#                 "Content-Type": "application/json"
#             }
#             payload = {
#                 "image_request": {
#                     "prompt": prompt,
#                     "model": "V_2",
#                     "aspect_ratio": "ASPECT_1_1",
#                     "magic_prompt_option": "AUTO"
#                 }
#             }

#             response = requests.post(endpoint, headers=headers, json=payload)

#             if response.status_code == 200:
#                 image_url = response.json()["data"][0]["url"]
#                 return f"🖼️ Mindmap image generated! View here: {image_url}"
#             else:
#                 return f"❌ Error generating mindmap image: {response.text}"
#         except Exception as e:
#             return f"❌ Error generating mindmap image: {str(e)}"

#     # تابع إنشاء الاختبار
#     def generate_quiz_from_text(vectorstore):
#         all_docs = vectorstore.similarity_search("", k=1000)
#         full_text = " ".join([doc.page_content for doc in all_docs])

#         quiz_prompt = f"""
#     You are a smart teacher. Create 10 multiple-choice and true/false questions, each with 4 options:

#     {full_text}

#     Format them like this:  
#     1- Question?
#     a) Option1
#     b) Option2
#     c) Option3
#     d) Option4
#     """
#         llm = ChatOpenAI(model_name="gpt-4.1", openai_api_key=openai_api_key, temperature=0)
#         return llm.predict(quiz_prompt)









    
#     tools = [
#         Tool(name="LearningTool", func=learning_function, description="Answer from video documents."),
#         Tool(name="SummarizeTool", func=summarize_function, description="Summarize content in bullet points."),
#         Tool(name="MindMapImageTool", func=mindmap_image_function, description="Create a mind map from summarized content."),
#         Tool(name="QuizTool", func=generate_quiz_from_text, description="Generate a quiz based on the documents."),
#     ]

#     agent = initialize_agent(
#         tools=tools,
#         llm=llm,
#         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#         memory=memory,
#         verbose=True,
#         handle_parsing_errors=True
#     )
#     return agent, vectorstore ,retriever





# # user_agents = {}

# # def get_agent_for_session(user_id):
# #     if user_id not in user_agents:
# #         memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
# #         llm = ChatOpenAI(model_name="gpt-4.1", openai_api_key=openai_api_key)
# #         agent = initialize_agent(
# #             tools=tools,  # تأكد تعرف الأدوات هنا
# #             llm=llm,
# #             agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
# #             memory=memory,
# #             verbose=True,
# #             handle_parsing_errors=True
# #         )
# #         user_agents[user_id] = agent
# #     return user_agents[user_id]


# # agent = initialize_agent(
# #     tools=tools,
# #     llm=ChatOpenAI(model_name="gpt-4.1", openai_api_key=openai_api_key, temperature=0),
# #     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
# #     memory=memory,
# #     verbose=True,
# #     handle_parsing_errors=True
# # )








# import re
# import yt_dlp
# import os
# import requests
# from dotenv import load_dotenv
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import FAISS
# from langchain_openai import OpenAIEmbeddings
# from langchain.schema import Document
# from langchain_community.chat_models import ChatOpenAI
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import RetrievalQA
# from langchain.agents import initialize_agent, AgentType, Tool
# from langchain_core.messages import HumanMessage
# from openai import OpenAI


# load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")
# api_key = os.getenv('IDEOGRAM')
# embeddings = OpenAIEmbeddings()

# def download_audio(youtube_url, output_path):
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'outtmpl': output_path,
#         'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
#         'quiet': True
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([youtube_url])

# def extract_youtube_links(text):
#     pattern = r'(https?://[^\s]+)'
#     return re.findall(pattern, text)
# client = OpenAI(api_key=openai_api_key)
# def transcribe_audio_openai(file_path):
#     with open(file_path, "rb") as audio_file:
#         response = client.audio.transcriptions.create(
#             model="whisper-1",
#             file=audio_file,
#             response_format="text"  # Return plain text only
#         )
#     return response


# def split_text(text, chunk_size=500, chunk_overlap=100):
#     splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, length_function=len)
#     return splitter.split_text(text)

# def process_videos_and_store(links, user_id):
#     all_documents = []
#     for idx, url in enumerate(links):
#         output_mp3 = f"video_{idx}"
#         # تحقق: إذا ملف محلي mp3 جاهز، مباشرة نستخدمه
#         if os.path.isfile(url) and url.endswith('.mp3'):
#             full_text = transcribe_audio_openai(url)
#         else:
#             download_audio(url, output_mp3)  # ينزل mp3 من YouTube
#             full_text = transcribe_audio_openai(f'{output_mp3}.mp3')

#         chunks = split_text(full_text)
#         for chunk_id, chunk_text in enumerate(chunks):
#             doc = Document(page_content=chunk_text.lower(), metadata={"source": url, "video_name": output_mp3, "chunk_id": chunk_id})
#             all_documents.append(doc)

#     if all_documents:
#         vectorstore = FAISS.from_documents(all_documents, embeddings)
#         vectorstore.save_local(f"faiss_index_user_{user_id}")


# def is_valid_duration(url):
#     try:
#         with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
#             info_dict = ydl.extract_info(url, download=False)
#             duration_seconds = info_dict.get('duration', 0)
#             return duration_seconds <= 1800  # 30 minutes
#     except Exception as e:
#         print(f"Error checking duration for {url}: {e}")
#         return False

# def save_chat_history(user_id, sender, message):
#     with open(f'chat_history_{user_id}.txt', 'a') as f:
#         f.write(f"{sender}: {message}\n")


# last_quiz = {"questions": "", "answers": ""}  # ضعها هنا في الأعلى لتكون global

# def get_agent_for_session(user_id):
#     faiss_path = f"faiss_index_user_{user_id}"
#     if os.path.exists(faiss_path):
#         vectorstore = FAISS.load_local(faiss_path, embeddings, allow_dangerous_deserialization=True)
#     else:
#         vectorstore = FAISS.from_texts([], embeddings)
#         vectorstore.save_local(faiss_path)

#     retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})
#     llm = ChatOpenAI(model_name="gpt-4.1", openai_api_key=openai_api_key, temperature=0)
#     memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
#     qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="map_reduce", memory=memory)

#     def learning_function(query):
#         return qa_chain.run(query)

#     def summarize_function(_):
#         docs = vectorstore.similarity_search("", k=1000)
#         text = " ".join([doc.page_content for doc in docs])
#         prompt = f"Summarize the following content in bullet points:\n\n{text}"
#         response = llm.invoke([HumanMessage(content=prompt)])
#         return response.content

#     def mindmap_full_ideas_function(_):
#         docs = vectorstore.similarity_search("", k=1000)
#         text = " ".join([doc.page_content for doc in docs])
#         prompt = f"Create a mind map with only the main topics from the following text. Keep it clear and minimal:\n\n{text}"
#         response = llm.invoke([HumanMessage(content=prompt)])
#         return response.content

#     def mindmap_image_function(_):
#         short_text = mindmap_full_ideas_function(None)
#         prompt = f"A mind map with only main topics: {short_text}. Clear readable text, minimal connections, compact design."
#         endpoint = "https://api.ideogram.ai/generate"
#         headers = {"Api-Key": api_key, "Content-Type": "application/json"}
#         payload = {"image_request": {"prompt": prompt, "model": "V_2", "aspect_ratio": "ASPECT_1_1", "magic_prompt_option": "AUTO"}}
#         response = requests.post(endpoint, headers=headers, json=payload)
#         if response.status_code == 200:
#             return f"🖼️ Mindmap image generated! View here: {response.json()['data'][0]['url']}"
#         return f"❌ Error generating mindmap image: {response.text}"

#     def generate_quiz_from_text(_):
#         global last_quiz
#         all_docs = vectorstore.similarity_search("", k=1000)
#         full_text = " ".join([doc.page_content for doc in all_docs])

#         quiz_prompt = f"""
#         You are a smart teacher. Create 10 multiple-choice and true/false questions, each with 4 options. Format:
#         1- Question?
#         a) Option1
#         b) Option2
#         c) Option3
#         d) Option4
#         """

#         response = llm.predict(quiz_prompt)
#         memory.chat_memory.add_user_message("Generated Quiz")
#         memory.chat_memory.add_ai_message(response)
#         return response

#     def get_quiz_answers(_):
#         ai_messages = [msg.content for msg in memory.chat_memory.messages if msg.type == 'ai']
#         if ai_messages:
#             return f"✅ Here’s the last quiz:\n\n{ai_messages[-1]}"
#         return "❌ No quiz has been generated yet."

#     tools = [
#         Tool(
#         name="LearningTool",
#         func=learning_function,
#         description="I want a response from the discussion only. If the question is not related to the discussion, say I am sorry, this is outside the discussion."
#     ),
#     Tool(
#         name="QuizTool",
#         func=generate_quiz_from_text,
#         description="Use this tool when the user requests a test, such as Test me or Give me a test only about the document, do not write the question and answers outside the document."
#     ),
#     Tool(name="MindMapImageTool", 
#         func=mindmap_image_function, 
#         description="Create a visual mind map that contains the main points."),

#     Tool(name="SummarizeTool", 
#         func=summarize_function, 
#         description="Summarize into bullet points."),
    
#     Tool(name="mindmap_full_ideas_function", 
#         func=mindmap_full_ideas_function, 
#         description="mindmap text ."),
#         Tool(name="QuizAnswerTool", func=get_quiz_answers, description="Get last quiz questions and answers.")
#     ]

#     agent = initialize_agent(
#         tools=tools,
#         llm=llm,
#         agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
#         memory=memory,
#         verbose=True,
#         handle_parsing_errors=True
#     )
#     return agent, memory






import re
import yt_dlp
import os
import requests
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import RetrievalQA
from langchain.agents import initialize_agent, AgentType, Tool
from langchain_core.messages import HumanMessage
from openai import OpenAI
import openai
import base64



load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
api_key = os.getenv('IDEOGRAM')
embeddings = OpenAIEmbeddings()

def download_audio(youtube_url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'cookies': '/home/ubuntu/cookies.txt',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

def extract_youtube_links(text):
    pattern = r'(https?://[^\s]+)'
    return re.findall(pattern, text)
client = OpenAI(api_key=openai_api_key)
def transcribe_audio_openai(file_path):
    with open(file_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"  # Return plain text only
        )
    return response


def split_text(text, chunk_size=500, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, length_function=len)
    return splitter.split_text(text)

def process_videos_and_store(links, user_id):
    all_documents = []
    for idx, url in enumerate(links):
        output_mp3 = f"video_{idx}"
        if os.path.isfile(url) and url.endswith('.mp3'):
            full_text = transcribe_audio_openai(url)
        else:
            download_audio(url, output_mp3) 
            full_text = transcribe_audio_openai(f'{output_mp3}.mp3')

        chunks = split_text(full_text)
        for chunk_id, chunk_text in enumerate(chunks):
            doc = Document(page_content=chunk_text.lower(), metadata={"source": url, "video_name": output_mp3, "chunk_id": chunk_id})
            all_documents.append(doc)

    if all_documents:
        vectorstore = FAISS.from_documents(all_documents, embeddings)
        vectorstore.save_local(f"faiss_index_user_{user_id}")


def is_valid_duration(url):
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            duration_seconds = info_dict.get('duration', 0)
            return duration_seconds <= 1800  # 30 minutes
    except Exception as e:
        print(f"Error checking duration for {url}: {e}")
        return False

def save_chat_history(user_id, sender, message):
    with open(f'chat_history_{user_id}.txt', 'a') as f:
        f.write(f"{sender}: {message}\n")




def generate_speech(text, voice='alloy', model='gpt-4o-mini-tts'):
    response = openai.audio.speech.create(
        model=model,
        voice=voice,
        input=text
    )
    audio_content = response.content
    audio_base64 = base64.b64encode(audio_content).decode('utf-8')
    return audio_base64



quiz_data = {}
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
def get_agent_for_session(user_id):
    faiss_path = f"faiss_index_user_{user_id}"
    if os.path.exists(faiss_path):
        vectorstore = FAISS.load_local(faiss_path, embeddings, allow_dangerous_deserialization=True)
    else:
        vectorstore = FAISS.from_texts([], embeddings)
        vectorstore.save_local(faiss_path)

    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})
    llm = ChatOpenAI(model_name="gpt-4.1", openai_api_key=openai_api_key, temperature=0)
    
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="map_reduce", memory=memory)

    def learning_function(query):
        return qa_chain.run(query)

    def summarize_function(_):
        docs = vectorstore.similarity_search("", k=10)
        text = " ".join([doc.page_content for doc in docs])
        prompt = (
        "Please create a small and very small the simple main  mind map from the following text. \n\n"
        f"{text}"
    )
        response = llm.invoke([HumanMessage(content=prompt)])
        return response.content



    def generate_title_with_ai(ـ):
        
        summary = summarize_function(None)
        prompt = f"Generate a short, catchy, and relevant title for the following summary:\n\n{summary}\n\nTitle:"

        response = client.chat.completions.create(
            model="gpt-4o",  # أو gpt-4 إذا عندك وصول
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes concise, relevant titles."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=20,
            temperature=0.5,
        )
        title = response.choices[0].message.content.strip()
        return title


    # def mindmap_full_ideas_function(_):
    #     docs = vectorstore.similarity_search("", k=1000)
    #     text = " ".join([doc.page_content for doc in docs])
    #     prompt = f"Create a mind map with only the main topics from the following text. Keep it clear and minimal:\n\n{text}"
    #     response = llm.invoke([HumanMessage(content=prompt)])
    #     return response.content

    def mindmap_image_function(_):
        short_text = generate_title_with_ai(None)
        prompt = f"Draw very small maind map aboute : \n\n{short_text}."

        endpoint = "https://api.ideogram.ai/v1/ideogram-v3/generate"
        headers = {"Api-Key": api_key}
        
        files = {
            'prompt': (None, prompt),
            'rendering_speed': (None, 'QUALITY'),
            # 'resolution': (None, '1024x1024'),
            'aspect_ratio': (None, '16x9'),
            'style_type': (None, 'GENERAL')

        }

        response = requests.post(endpoint, headers=headers, files=files)

        if response.status_code == 200:
            data = response.json()
            image_url = data['data'][0]['url']
            return f"🖼️ Mindmap image generated! View here: {image_url}"
        else:
            return f"❌ Error generating mindmap image: {response.text}"

    def generate_quiz_from_text(_):
        global quiz_data
        all_docs = vectorstore.similarity_search("", k=1000)
        full_text = " ".join([doc.page_content for doc in all_docs])

        quiz_prompt = f"""
        You are a smart teacher. Based on the following content, create 10 multiple-choice and true/false questions.
        For EACH question, provide:
        1. The question
        2. Four answer options (a, b, c, d)
        3. The correct answer letter
        
        Content: {full_text}
        \n
        Format your response exactly like this:
        1- Question 1?
        a) Option1
        b) Option2
        c) Option3
        d) Option4
        Answer: b
        \n
        2- Question 2?
        a) Option1
        b) Option2
        c) Option3
        d) Option4
        Answer: c
        \n
        Continue with all 10 questions.
        """

        response = llm.invoke([HumanMessage(content=quiz_prompt)])
        
        quiz_text = response.content
        
        if user_id not in quiz_data:
            quiz_data[user_id] = {}
        quiz_data[user_id]["full_quiz"] = quiz_text
        
        user_quiz = re.sub(r'Answer: [a-d](\n|$)', r'\1', quiz_text)
        
        # memory.chat_memory.add_user_message("Generate Quiz")
        # memory.chat_memory.add_ai_message(user_quiz)
        
        return user_quiz

    def get_quiz_answers(_):
        global quiz_data
        if user_id in quiz_data and "full_quiz" in quiz_data[user_id]:
            return f"✅ Here are the questions with answers:\n\n{quiz_data[user_id]['full_quiz']}"
        return "❌ No quiz has been generated yet. Please generate a quiz first."

    tools = [
        Tool(
        name="LearningTool",
        func=learning_function,
        description=(
        "Use this tool to answer all questions."
        "Search for the answers only in the provided documents."
        "DO NOT answer based on your own knowledge or assumptions. "
        "If the answer is not found in the documents, say 'I couldn’t find that information in the provided videos and stop.'"
    )
    ),
    Tool(
        name="QuizTool",
        func=generate_quiz_from_text,
        description="Use this tool when the user requests a test, such as Test me or Give me a test only about the document, do not write the question and answers outside the document."
    ),
    Tool(name="MindMapImageTool", 
        func=mindmap_image_function, 
        description="Create a visual that contains the main points."),

    Tool(name="SummarizeTool", 
        func=summarize_function, 
        description="If the user wants a summary, return clean formatted summary without extra wrapping."),
    
    # Tool(name="mindmap_full_ideas_function", 
    #     func=mindmap_full_ideas_function, 
    #     description="mindmap text ."),
        Tool(name="QuizAnswerTool", 
            func=get_quiz_answers, 
            description=(
            "Get the latest quiz questions and answers. "
            "If you need answers, send them to the user. "
            "If the user I need answer, correct him. "
            "How many questions did he get out of the total."
        ))
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True
    )
    return agent, memory












# def get_agent_for_session(user_id):
#     faiss_path = f"faiss_index_user_{user_id}"
#     if os.path.exists(faiss_path):
#         vectorstore = FAISS.load_local(faiss_path, embeddings, allow_dangerous_deserialization=True)
#     else:
#         vectorstore = FAISS.from_texts([], embeddings)
#         vectorstore.save_local(faiss_path)
#     retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 2})
#     llm = ChatOpenAI(model_name="gpt-4.1", openai_api_key=openai_api_key, temperature=0)
#     memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
#     qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="map_reduce", memory=memory)
    

#     def learning_function(query):
#         return qa_chain.run(query)

#     def summarize_function(_):
#         docs = vectorstore.similarity_search("", k=1000)
#         text = " ".join([doc.page_content for doc in docs])
#         prompt = f"Summarize the following content in bullet points:\n\n{text}"
#         response = llm.invoke([HumanMessage(content=prompt)])
#         return response.content
    
#     def mindmap_full_ideas_function(_):
#         # استخراج كل المستندات
#         docs = vectorstore.similarity_search("", k=1000)
#         text = " ".join([doc.page_content for doc in docs])
        
#         # تجهيز الـ prompt لخريطة المفاهيم
#         prompt = f"Create a mind map with only the main topics from the following text. Keep it clear and minimal:\n\n{text}"
        
#         # إرسال الطلب للنموذج
#         response = llm.invoke([HumanMessage(content=prompt)])
        
#         # إرجاع النتيجة
#         return response.content


#     def mindmap_image_function(_):
#         short_text = mindmap_full_ideas_function(None)
#         prompt = f"A mind map with only main topics: {short_text}. Clear readable text, minimal connections, compact design."
#         endpoint = "https://api.ideogram.ai/generate"
#         headers = {"Api-Key": api_key, "Content-Type": "application/json"}
#         payload = {"image_request": {"prompt": prompt, "model": "V_2", "aspect_ratio": "ASPECT_1_1", "magic_prompt_option": "AUTO"}}
#         response = requests.post(endpoint, headers=headers, json=payload)
#         if response.status_code == 200:
#             return f"🖼️ Mindmap image generated! View here: {response.json()['data'][0]['url']}"
#         return f"❌ Error generating mindmap image: {response.text}"
#     last_quiz = {"questions": "", "answers": ""}
#     last_quiz = {"questions": "", "answers": ""}
    

#     def generate_quiz_from_text(_):
#         """Used to generate 10 multiple-choice questions from all knowledge base data"""

#         # Retrieve all documents (some versions need search(""))
#         all_docs = vectorstore.similarity_search("", k=1000)

#         # Combine all texts
#         full_text = " ".join([doc.page_content for doc in all_docs])

#         # Request GPT-4o to generate 10 multiple-choice questions
#         quiz_prompt = f"""
#     You are a smart teacher. Create 10 multiple-choice and true/false questions, each with 4 options, a form of true/false and multiple choice, and let the user choose how many questions they want:

#     {full_text}

#     Please be very precise and only take important questions.  
#     Format them like this:  
#     1- Question?
#     a) Option1
#     b) Option2
#     c) Option3
#     d) Option4

#     Then the second question and so on...
#     """
#         llm = ChatOpenAI(model_name="gpt-4.1", openai_api_key=openai_api_key, temperature=0)
#         response = llm.predict(quiz_prompt)
#         last_quiz["questions"] = response
#         return response

#     def get_quiz_answers(_):
#         if last_quiz["questions"]:
#             return f"✅ Here are the last quiz questions and answers:\n\n{last_quiz['questions']}"
#         return "❌ No quiz has been generated yet."
            



#     tools = [
#     Tool(
#         name="LearningTool",
#         func=learning_function,
#         description="I want a response from the discussion only. If the question is not related to the discussion, say I am sorry, this is outside the discussion."
#     ),
#     Tool(
#         name="QuizTool",
#         func=generate_quiz_from_text,
#         description="Use this tool when the user requests a test, such as Test me or Give me a test only about the document, do not write the question and answers outside the document."
#     ),
#     Tool(name="MindMapImageTool", 
#         func=mindmap_image_function, 
#         description="Create a visual mind map that contains the main points."),

#     Tool(name="SummarizeTool", 
#         func=summarize_function, 
#         description="Summarize into bullet points."),
    
#     Tool(name="mindmap_full_ideas_function", 
#         func=mindmap_full_ideas_function, 
#         description="mindmap text ."),

#         Tool(
#         name="QuizAnswerTool",
#         func=get_quiz_answers,
#         description="Show the last quiz questions and correct answers when the user asks.")

#     ]

#     agent = initialize_agent(tools=tools,
#                             llm=llm, 
#                             agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, 
#                             memory=memory, 
#                             verbose=True, 
#                             handle_parsing_errors=True)
#     return agent , memory
