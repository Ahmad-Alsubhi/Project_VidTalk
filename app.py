# from flask import Flask, render_template, request, jsonify
# from core import process_videos_and_store, agent, extract_youtube_links
# import re
# import yt_dlp

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/start', methods=['POST'])
# def start():
#     data = request.json
#     mode = data.get('mode')
#     input_value = data.get('input')

#     links = []
#     if mode == 'topic':
#         from langchain_community.tools import YouTubeSearchTool
#         search_tool = YouTubeSearchTool()
#         results = search_tool.run(f'{input_value},2')
#         links = extract_youtube_links(results)
#     elif mode == 'playlist':
#         ydl_opts = {'quiet': True, 'extract_flat': True, 'force_generic_extractor': True}
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info_dict = ydl.extract_info(input_value, download=False)
#             entries = info_dict.get('entries', [])
#             links = [entry['url'] for entry in entries if 'url' in entry]

#     if not links:
#         return jsonify({'status': '❌ No links found.'})

#     process_videos_and_store(links)
#     return jsonify({'status': '✅ Processing complete! You can start chatting now.'})

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.json['message']
#     try:
#         response = agent.run(user_message)
#     except Exception as e:
#         response = f"❌ Error: {str(e)}"
#     return jsonify({'reply': response})

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, jsonify, session
# from flask_session import Session
# from core import process_videos_and_store, extract_youtube_links, get_agent_for_session
# import re
# import yt_dlp
# import uuid

# app = Flask(__name__)
# app.secret_key = 'supersecret'  # غيّره بمفتاحك السري الحقيقي!
# app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)

# @app.route('/')
# def index():
#     if 'user_id' not in session:
#         session['user_id'] = str(uuid.uuid4())  # توليد UUID لكل مستخدم
#     return render_template('index.html')

# @app.route('/start', methods=['POST'])
# def start():
#     data = request.json
#     mode = data.get('mode')
#     input_value = data.get('input')

#     links = []
#     if mode == 'topic':
#         from langchain_community.tools import YouTubeSearchTool
#         search_tool = YouTubeSearchTool()
#         results = search_tool.run(f'{input_value},2')
#         links = extract_youtube_links(results)
#     elif mode == 'playlist':
#         ydl_opts = {'quiet': True, 'extract_flat': True, 'force_generic_extractor': True}
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info_dict = ydl.extract_info(input_value, download=False)
#             entries = info_dict.get('entries', [])
#             links = [entry['url'] for entry in entries if 'url' in entry]

#     if not links:
#         return jsonify({'status': '❌ No links found.'})

#     process_videos_and_store(links)
#     return jsonify({'status': '✅ Processing complete! You can start chatting now.'})

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.json['message']
#     user_id = session['user_id']
    
#     # جلب agent المخصص لهذا المستخدم
#     agent = get_agent_for_session(user_id)
    
#     try:
#         response = agent.run(user_message)
#     except Exception as e:
#         response = f"❌ Error: {str(e)}"
#     return jsonify({'reply': response})

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, jsonify, session
# from flask_session import Session
# from core import process_videos_and_store, extract_youtube_links, get_agent_for_session
# import yt_dlp
# import uuid

# app = Flask(__name__)
# app.secret_key = 'supersecret'
# app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)

# @app.route('/')
# def index():
#     if 'user_id' not in session:
#         session['user_id'] = str(uuid.uuid4())
#     return render_template('index.html')

# @app.route('/start', methods=['POST'])
# def start():
#     data = request.json
#     mode = data.get('mode')
#     input_value = data.get('input')
#     user_id = session['user_id']

#     links = []
#     if mode == 'topic':
#         from langchain_community.tools import YouTubeSearchTool
#         search_tool = YouTubeSearchTool()
#         results = search_tool.run(f'{input_value},2')
#         links = extract_youtube_links(results)
#     elif mode == 'playlist':
#         ydl_opts = {'quiet': True, 'extract_flat': True, 'force_generic_extractor': True}
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info_dict = ydl.extract_info(input_value, download=False)
#             entries = info_dict.get('entries', [])
#             links = [entry['url'] for entry in entries if 'url' in entry]

#     if not links:
#         return jsonify({'status': '❌ No links found.'})

#     process_videos_and_store(links, user_id)
#     return jsonify({'status': '✅ Processing complete! You can start chatting now.'})

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.json['message']
#     user_id = session['user_id']

#     agent, _, _ = get_agent_for_session(user_id)

#     try:
#         response = agent.run(user_message)
#     except Exception as e:
#         response = f"❌ Error: {str(e)}"
#     return jsonify({'reply': response})

# if __name__ == '__main__':
#     app.run(debug=True)








# from flask import Flask, render_template, request, jsonify, session
# from flask_session import Session
# from core import process_videos_and_store, extract_youtube_links, get_agent_for_session
# import yt_dlp
# import uuid

# app = Flask(__name__)
# app.secret_key = 'supersecret'
# app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)

# @app.route('/')
# def index():
#     if 'user_id' not in session:
#         session['user_id'] = str(uuid.uuid4())
#     return render_template('index.html')

# @app.route('/start', methods=['POST'])
# def start():
#     data = request.json
#     mode = data.get('mode')
#     input_value = data.get('input')
#     user_id = session['user_id']
#     links = []
#     if mode == 'topic':
#         from langchain_community.tools import YouTubeSearchTool
#         search_tool = YouTubeSearchTool()
#         results = search_tool.run(f'{input_value},2')
#         links = extract_youtube_links(results)
#     elif mode == 'playlist':
#         if not input_value.startswith("http"):
#             return jsonify({'status': '❌ Invalid playlist URL.'})
#         ydl_opts = {'quiet': True, 'extract_flat': True, 'force_generic_extractor': True}
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info_dict = ydl.extract_info(input_value, download=False)
#             entries = info_dict.get('entries', [])
#             links = [entry['url'] for entry in entries if 'url' in entry]

#     if not links:
#         return jsonify({'status': '❌ No links found.'})

#     process_videos_and_store(links, user_id)
#     return jsonify({'status': '✅ Processing complete! You can start chatting now.'})

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.json['message']
#     user_id = session['user_id']
#     agent = get_agent_for_session(user_id)
#     try:
#         response = agent.run(user_message)
#     except Exception as e:
#         response = f"❌ Error: {str(e)}"
#     return jsonify({'reply': response})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)





# from flask import Flask, render_template, request, jsonify, session
# from flask_session import Session
# from core import process_videos_and_store, extract_youtube_links, is_valid_duration,get_agent_for_session
# import yt_dlp
# import uuid

# app = Flask(__name__)
# app.secret_key = 'supersecret'
# app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)

# @app.route('/')
# def index():
#     if 'user_id' not in session:
#         session['user_id'] = str(uuid.uuid4())
#     return render_template('index.html')

# @app.route('/start', methods=['POST'])
# def start():
#     data = request.json
#     mode = data.get('mode')
#     input_value = data.get('input')
#     user_id = session['user_id']
#     links = []

#     if mode == 'topic':
#         from langchain_community.tools import YouTubeSearchTool
#         search_tool = YouTubeSearchTool()
#         results = search_tool.run(f'{input_value},2')
#         raw_links = extract_youtube_links(results)
#         for url in raw_links:
#             if len(links) >= 5:
#                 break
#             if is_valid_duration(url):
#                 links.append(url)

#     elif mode == 'playlist':
#         if not input_value.startswith("http"):
#             return jsonify({'status': '❌ Invalid playlist URL.'})
#         ydl_opts = {'quiet': True, 'extract_flat': True, 'force_generic_extractor': True}
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info_dict = ydl.extract_info(input_value, download=False)
#             all_links = [entry['url'] for entry in info_dict.get('entries', []) if 'url' in entry]
#         for url in all_links:
#             if len(links) >= 5:
#                 break
#             if is_valid_duration(url):
#                 links.append(url)

#     elif mode == 'single_url':
#         if not input_value.startswith("http"):
#             return jsonify({'status': '❌ Invalid video URL.'})
#         if is_valid_duration(input_value):
#             links.append(input_value)
#         else:
#             return jsonify({'status': '❌ Video exceeds 30 minutes.'})

#     elif mode == 'upload':
#         file = request.files.get('file')
#         if not file:
#             return jsonify({'status': '❌ No file uploaded.'})
#         file_path = f"./uploads/{file.filename}"
#         file.save(file_path)
#         links.append(file_path)

#     if not links:
#         return jsonify({'status': '❌ No suitable links found.'})

#     process_videos_and_store(links, user_id)
#     return jsonify({'status': '✅ Processing complete! You can start chatting now.'})

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.json['message']
#     user_id = session['user_id']
#     agent, _, _ = get_agent_for_session(user_id)
#     try:
#         response = agent.run(user_message)
#     except Exception as e:
#         response = f"❌ Error: {str(e)}"
#     return jsonify({'reply': response})

# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask, render_template, request, jsonify, session
# from flask_session import Session
# from core import process_videos_and_store, extract_youtube_links, is_valid_duration, get_agent_for_session, save_chat_history
# import yt_dlp
# import uuid
# import os

# app = Flask(__name__)
# app.secret_key = 'supersecret'
# app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)

# UPLOAD_FOLDER = './uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route('/')
# def index():
#     if 'user_id' not in session:
#         session['user_id'] = str(uuid.uuid4())
#     return render_template('index.html')

# @app.route('/start', methods=['POST'])
# def start():
#     mode = request.form.get('mode')
#     input_value = request.form.get('input')
#     user_id = session['user_id']
#     links = []

#     if mode == 'upload':
#         file = request.files.get('file')
#         if not file:
#             return jsonify({'status': '❌ No file uploaded.'})
#         upload_dir = './uploads'
#         os.makedirs(upload_dir, exist_ok=True)
#         file_path = os.path.join(upload_dir, file.filename)
#         file.save(file_path)
#         links.append(file_path)

#     else:
#         if mode == 'topic':
#             from langchain_community.tools import YouTubeSearchTool
#             search_tool = YouTubeSearchTool()
#             results = search_tool.run(f'{input_value},6')
#             raw_links = extract_youtube_links(results)
#             for url in raw_links:
#                 if len(links) >= 3:
#                     break
#                 if is_valid_duration(url):
#                     links.append(url)

#         elif mode == 'playlist':
#             if not input_value.startswith("http"):
#                 return jsonify({'status': '❌ Invalid playlist URL.'})
#             ydl_opts = {'quiet': True, 'extract_flat': True, 'force_generic_extractor': True}
#             with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#                 info_dict = ydl.extract_info(input_value, download=False)
#                 all_links = [entry['url'] for entry in info_dict.get('entries', []) if 'url' in entry]
#             for url in all_links:
#                 if is_valid_duration(url):
#                     links.append(url)

#         elif mode == 'single_url':
#             if not input_value.startswith("http"):
#                 return jsonify({'status': '❌ Invalid video URL.'})
#             if is_valid_duration(input_value):
#                 links.append(input_value)
#             else:
#                 return jsonify({'status': '❌ Video exceeds 30 minutes.'})

#     if not links:
#         return jsonify({'status': '❌ No suitable links found.'})

#     process_videos_and_store(links, user_id)
#     return jsonify({'status': '✅ Processing complete! You can start chatting now.'})

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.json['message']
#     user_id = session['user_id']
#     agent, _ = get_agent_for_session(user_id)

    
#     # 🟡 خزّن رسالة المستخدم
#     save_chat_history(user_id, "User", user_message)
    
#     try:
#         response = agent.run(user_message)
#     except Exception as e:
#         response = f"❌ Error: {str(e)}"
    
#     # 🟡 خزّن رد البوت
#     save_chat_history(user_id, "Bot", response)
    
#     return jsonify({'reply': response})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)






# from flask import Flask, render_template, request, jsonify, session, Response
# from flask_session import Session
# from core import process_videos_and_store, extract_youtube_links, is_valid_duration, get_agent_for_session, save_chat_history
# import yt_dlp
# import uuid
# import os
# import time
# import json
# import threading
# from flask_socketio import SocketIO  # تأكد من تثبيت: pip install flask-socketio

# app = Flask(__name__)
# app.secret_key = 'supersecret'
# app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)
# socketio = SocketIO(app, cors_allowed_origins="*")

# UPLOAD_FOLDER = './uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # قاموس لتخزين تقدم المعالجة لكل مستخدم
# progress_data = {}

# @app.route('/')
# def index():
#     if 'user_id' not in session:
#         session['user_id'] = str(uuid.uuid4())
#     return render_template('index.html')

# def update_progress(user_id, message, percentage):
#     """تحديث حالة تقدم المعالجة وإرسالها عبر Socket.IO"""
#     progress_data[user_id] = {"message": message, "percentage": percentage}
#     socketio.emit('progress_update', 
#                   {'message': message, 'percentage': percentage}, 
#                   room=user_id)

# def process_with_progress(links, user_id):
#     """وظيفة لمعالجة الروابط مع إرسال تحديثات التقدم"""
#     total_links = len(links)
    
#     # إعداد المجلد
#     update_progress(user_id, "التحضير للمعالجة...", 5)
#     time.sleep(0.5)  # لإظهار التقدم بشكل أفضل
    
#     all_documents = []
#     for idx, url in enumerate(links):
#         # تحديث التقدم للرابط الحالي
#         progress_percentage = int(5 + (idx / total_links) * 80)
#         update_progress(user_id, f"معالجة الفيديو {idx+1} من {total_links}...", progress_percentage)
        
#         output_mp3 = f"video_{idx}"
#         # تحقق: إذا ملف محلي mp3 جاهز، مباشرة نستخدمه
#         if os.path.isfile(url) and url.endswith('.mp3'):
#             update_progress(user_id, f"تحويل الصوت للنص... ({idx+1}/{total_links})", progress_percentage + 5)
#             full_text = process_videos_and_store.transcribe_audio_openai(url)
#         else:
#             # تنزيل الفيديو
#             update_progress(user_id, f"تنزيل الفيديو {idx+1} من {total_links}...", progress_percentage)
#             process_videos_and_store.download_audio(url, output_mp3)
            
#             # تحويل الصوت إلى نص
#             update_progress(user_id, f"تحويل الصوت للنص... ({idx+1}/{total_links})", progress_percentage + 5)
#             full_text = process_videos_and_store.transcribe_audio_openai(f'{output_mp3}.mp3')
        
#         # تقسيم النص إلى أجزاء
#         update_progress(user_id, f"تقسيم المحتوى... ({idx+1}/{total_links})", progress_percentage + 10)
#         chunks = process_videos_and_store.split_text(full_text)
        
#         for chunk_id, chunk_text in enumerate(chunks):
#             doc = process_videos_and_store.Document(
#                 page_content=chunk_text.lower(), 
#                 metadata={"source": url, "video_name": output_mp3, "chunk_id": chunk_id}
#             )
#             all_documents.append(doc)
    
#     # إنشاء متجر الفهرس
#     update_progress(user_id, "بناء قاعدة المعرفة...", 90)
#     if all_documents:
#         vectorstore = process_videos_and_store.FAISS.from_documents(all_documents, process_videos_and_store.embeddings)
#         vectorstore.save_local(f"faiss_index_user_{user_id}")
    
#     # اكتمال المعالجة
#     update_progress(user_id, "اكتملت المعالجة! يمكنك بدء المحادثة الآن.", 100)

# @app.route('/start', methods=['POST'])
# def start():
#     mode = request.form.get('mode')
#     input_value = request.form.get('input')
#     user_id = session['user_id']
#     links = []

#     # إعادة تعيين التقدم
#     update_progress(user_id, "بدء المعالجة...", 0)

#     if mode == 'upload':
#         file = request.files.get('file')
#         if not file:
#             return jsonify({'status': '❌ No file uploaded.'})
#         upload_dir = './uploads'
#         os.makedirs(upload_dir, exist_ok=True)
#         file_path = os.path.join(upload_dir, file.filename)
#         file.save(file_path)
#         links.append(file_path)

#     else:
#         if mode == 'topic':
#             update_progress(user_id, "البحث عن فيديوهات مناسبة...", 10)
#             from langchain_community.tools import YouTubeSearchTool
#             search_tool = YouTubeSearchTool()
#             results = search_tool.run(f'{input_value},6')
#             raw_links = extract_youtube_links(results)
#             for url in raw_links:
#                 if len(links) >= 3:
#                     break
#                 update_progress(user_id, f"التحقق من مدة الفيديو: {url}", 15 + len(links) * 5)
#                 if is_valid_duration(url):
#                     links.append(url)

#         elif mode == 'playlist':
#             if not input_value.startswith("http"):
#                 return jsonify({'status': '❌ Invalid playlist URL.'})
#             update_progress(user_id, "استخراج روابط قائمة التشغيل...", 10)
#             ydl_opts = {'quiet': True, 'extract_flat': True, 'force_generic_extractor': True}
#             with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#                 info_dict = ydl.extract_info(input_value, download=False)
#                 all_links = [entry['url'] for entry in info_dict.get('entries', []) if 'url' in entry]
            
#             for i, url in enumerate(all_links):
#                 update_progress(user_id, f"التحقق من مدة الفيديو {i+1}/{len(all_links)}", 15 + (i/len(all_links)) * 15)
#                 if is_valid_duration(url):
#                     links.append(url)

#         elif mode == 'single_url':
#             if not input_value.startswith("http"):
#                 return jsonify({'status': '❌ Invalid video URL.'})
#             update_progress(user_id, "التحقق من مدة الفيديو...", 10)
#             if is_valid_duration(input_value):
#                 links.append(input_value)
#             else:
#                 update_progress(user_id, "❌ الفيديو يتجاوز 30 دقيقة.", 0)
#                 return jsonify({'status': '❌ Video exceeds 30 minutes.'})

#     if not links:
#         update_progress(user_id, "❌ لم يتم العثور على روابط مناسبة.", 0)
#         return jsonify({'status': '❌ No suitable links found.'})

#     # معالجة الروابط في خيط منفصل
#     thread = threading.Thread(target=process_with_progress, args=(links, user_id))
#     thread.daemon = True
#     thread.start()
    
#     return jsonify({'status': '✅ Processing started! Check progress indicator.'})

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.json['message']
#     user_id = session['user_id']
    
#     # إعداد رسالة التقدم للعمليات مثل إنشاء الاختبار أو المخطط الذهني
#     if "quiz" in user_message.lower() or "test" in user_message.lower():
#         update_progress(user_id, "جاري إنشاء الاختبار...", 0)
#     elif "mind map" in user_message.lower() or "mindmap" in user_message.lower():
#         update_progress(user_id, "جاري إنشاء المخطط الذهني...", 0)
    
#     agent, _ = get_agent_for_session(user_id)
    
#     # خزّن رسالة المستخدم
#     save_chat_history(user_id, "User", user_message)
    
#     try:
#         response = agent.run(user_message)
        
#         # اكتمال العملية
#         if "quiz" in user_message.lower() or "test" in user_message.lower():
#             update_progress(user_id, "تم إنشاء الاختبار بنجاح!", 100)
#         elif "mind map" in user_message.lower() or "mindmap" in user_message.lower():
#             update_progress(user_id, "تم إنشاء المخطط الذهني بنجاح!", 100)
#     except Exception as e:
#         response = f"❌ Error: {str(e)}"
#         update_progress(user_id, f"حدث خطأ: {str(e)}", 0)
    
#     # خزّن رد البوت
#     save_chat_history(user_id, "Bot", response)
    
#     return jsonify({'reply': response})

# @socketio.on('connect')
# def handle_connect():
#     user_id = session.get('user_id')
#     if user_id:
#         socketio.emit('connected', {'message': 'تم الاتصال بالخادم'}, room=request.sid)
#         # إضافة المستخدم إلى غرفة فريدة
#         socketio.server.enter_room(request.sid, user_id)

# @app.route('/progress')
# def progress():
#     user_id = session.get('user_id')
#     if user_id in progress_data:
#         return jsonify(progress_data[user_id])
#     return jsonify({"message": "لا توجد عملية قيد التنفيذ", "percentage": 0})

# if __name__ == '__main__':
#     socketio.run(app, host='0.0.0.0', port=5000, debug=True)




# from flask import Flask, render_template, request, jsonify, session
# from flask_session import Session
# from core import process_videos_and_store, extract_youtube_links, is_valid_duration, get_agent_for_session, save_chat_history, download_audio,generate_speech
# import yt_dlp
# import uuid
# import os
# import time
# import threading
# import datetime

# app = Flask(__name__)
# app.secret_key = 'supersecret'
# app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)

# UPLOAD_FOLDER = './uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # Global dictionary to store processing progress
# processing_status = {}

# def process_with_progress(links, user_id):
#     """Process videos with progress tracking and timing"""
#     start_time = time.time()
    
#     # Initialize progress status
#     processing_status[user_id] = {
#         'total': len(links),
#         'completed': 0,
#         'current_file': '',
#         'start_time': start_time,
#         'estimated_completion': None
#     }
    
#     all_files = []
#     for i, url in enumerate(links):
#         # Update current file being processed
#         processing_status[user_id]['current_file'] = url if url.startswith('http') else os.path.basename(url)
        
#         # Process file or URL
#         if url.startswith('http'):
#             # For YouTube URLs
#             output_mp3 = f'./uploads/{user_id}_{i}'
#             download_audio(url, output_mp3)  # استدعاء دالة download_audio من ملف core
#             all_files.append(f"{output_mp3}.mp3")
#         else:
#             # For uploaded files
#             all_files.append(url)
        
#         # Update progress
#         processing_status[user_id]['completed'] += 1
        
#         # Calculate estimated completion time
#         elapsed = time.time() - start_time
#         avg_time_per_file = elapsed / processing_status[user_id]['completed']
#         remaining_files = processing_status[user_id]['total'] - processing_status[user_id]['completed']
#         estimated_remaining_seconds = avg_time_per_file * remaining_files
        
#         if remaining_files > 0:
#             completion_time = datetime.datetime.now() + datetime.timedelta(seconds=estimated_remaining_seconds)
#             processing_status[user_id]['estimated_completion'] = completion_time.strftime('%H:%M:%S')
    
#     # معالجة جميع الملفات مرة واحدة بعد الانتهاء من التحميل
#     process_videos_and_store(all_files, user_id)
    
#     # Processing complete
#     end_time = time.time()
#     total_time = end_time - start_time
#     processing_status[user_id]['status'] = 'complete'
#     processing_status[user_id]['total_time'] = f"{total_time:.2f} seconds"

# @app.route('/')
# def index():
#     if 'user_id' not in session:
#         session['user_id'] = str(uuid.uuid4())
#     return render_template('index.html')

# @app.route('/start', methods=['POST'])
# def start():
#     mode = request.form.get('mode')
#     input_value = request.form.get('input')
#     user_id = session['user_id']
#     links = []

#     if mode == 'upload':
#         file = request.files.get('file')
#         if not file:
#             return jsonify({'status': '❌ No file uploaded.'})
#         upload_dir = './uploads'
#         os.makedirs(upload_dir, exist_ok=True)
#         file_path = os.path.join(upload_dir, file.filename)
#         file.save(file_path)
#         links.append(file_path)

#     else:
#         if mode == 'topic':
#             from langchain_community.tools import YouTubeSearchTool
#             search_tool = YouTubeSearchTool()
#             results = search_tool.run(f'{input_value},6')
#             raw_links = extract_youtube_links(results)
#             for url in raw_links:
#                 if len(links) >= 3:
#                     break
#                 if is_valid_duration(url):
#                     links.append(url)

#         elif mode == 'playlist':
#             if not input_value.startswith("http"):
#                 return jsonify({'status': '❌ Invalid playlist URL.'})
#             ydl_opts = {'quiet': True, 'extract_flat': True, 'force_generic_extractor': True}
#             with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#                 info_dict = ydl.extract_info(input_value, download=False)
#                 all_links = [entry['url'] for entry in info_dict.get('entries', []) if 'url' in entry]
#             for url in all_links:
#                 if is_valid_duration(url):
#                     links.append(url)

#         elif mode == 'single_url':
#             if not input_value.startswith("http"):
#                 return jsonify({'status': '❌ Invalid video URL.'})
#             if is_valid_duration(input_value):
#                 links.append(input_value)
#             else:
#                 return jsonify({'status': '❌ Video exceeds 30 minutes.'})

#     if not links:
#         return jsonify({'status': '❌ No suitable links found.'})

#     # Start processing in a background thread
#     processing_thread = threading.Thread(target=process_with_progress, args=(links, user_id))
#     processing_thread.daemon = True
#     processing_thread.start()
    
#     return jsonify({
#         'status': '✅ Processing started! You will see progress updates.',
#         'totalFiles': len(links)
#     })

# @app.route('/progress', methods=['GET'])
# def get_progress():
#     """Endpoint to get current processing progress"""
#     user_id = session.get('user_id')
#     if not user_id or user_id not in processing_status:
#         return jsonify({
#             'status': 'unknown',
#             'progress': 0,
#             'message': 'No processing in progress'
#         })
    
#     status = processing_status[user_id]
#     progress_percent = (status['completed'] / status['total']) * 100 if status['total'] > 0 else 0
    
#     return jsonify({
#         'status': 'processing' if status.get('status') != 'complete' else 'complete',
#         'progress': progress_percent,
#         'currentFile': status['current_file'],
#         'completedFiles': status['completed'],
#         'totalFiles': status['total'],
#         'estimatedCompletion': status.get('estimated_completion'),
#         'elapsedTime': f"{time.time() - status['start_time']:.2f} seconds",
#         'totalTime': status.get('total_time')
#     })

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.json['message']
#     user_id = session['user_id']
#     agent, _ = get_agent_for_session(user_id)

#     # 🟡 خزّن رسالة المستخدم في السجل (قاعدة البيانات أو ملف خارجي)
#     save_chat_history(user_id, "User", user_message)
    
#     try:
#         # ✅ لا تمرر memory هنا لأن الـ agent أصلاً مربوط بها عند إنشائه
#         response = agent.run(user_message)
#     except Exception as e:
#         response = f"❌ Error: {str(e)}"
    
#     # 🟡 خزّن رد البوت في السجل
#     save_chat_history(user_id, "Bot", response)
    
#     return jsonify({'reply': response})
# @app.route('/speak', methods=['POST'])
# def speak():
#     text = request.json['text']
#     audio_base64 = generate_speech(text)
#     return jsonify({'audio': audio_base64})


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)






































from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
from core import process_videos_and_store, extract_youtube_links, is_valid_duration, get_agent_for_session, save_chat_history, download_audio,generate_speech
import yt_dlp
import uuid
import os
import time
import threading
import datetime

app = Flask(__name__)
app.secret_key = 'supersecret'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Global dictionary to store processing progress
processing_status = {}

def process_with_progress(links, user_id):
    """Process videos with progress tracking and timing"""
    start_time = time.time()
    
    # Initialize progress status
    processing_status[user_id] = {
        'total': len(links),
        'completed': 0,
        'current_file': '',
        'start_time': start_time,
        'estimated_completion': None
    }
    
    all_files = []
    for i, url in enumerate(links):
        # Update current file being processed
        processing_status[user_id]['current_file'] = url if url.startswith('http') else os.path.basename(url)
        
        # Process file or URL
        if url.startswith('http'):
            # For YouTube URLs
            output_mp3 = f'./uploads/{user_id}_{i}'
            download_audio(url, output_mp3)  # استدعاء دالة download_audio من ملف core
            all_files.append(f"{output_mp3}.mp3")
        else:
            # For uploaded files
            all_files.append(url)
        
        # Update progress
        processing_status[user_id]['completed'] += 1
        
        # Calculate estimated completion time
        elapsed = time.time() - start_time
        avg_time_per_file = elapsed / processing_status[user_id]['completed']
        remaining_files = processing_status[user_id]['total'] - processing_status[user_id]['completed']
        estimated_remaining_seconds = avg_time_per_file * remaining_files
        
        if remaining_files > 0:
            completion_time = datetime.datetime.now() + datetime.timedelta(seconds=estimated_remaining_seconds)
            processing_status[user_id]['estimated_completion'] = completion_time.strftime('%H:%M:%S')
    
    # معالجة جميع الملفات مرة واحدة بعد الانتهاء من التحميل
    process_videos_and_store(all_files, user_id)
    
    # Processing complete
    end_time = time.time()
    total_time = end_time - start_time
    processing_status[user_id]['status'] = 'complete'
    processing_status[user_id]['total_time'] = f"{total_time:.2f} seconds"

@app.route('/')
def index():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    mode = request.form.get('mode')
    input_value = request.form.get('input')
    user_id = session['user_id']
    links = []

    if mode == 'upload':
        file = request.files.get('file')
        if not file:
            return jsonify({'status': '❌ No file uploaded.'})
        upload_dir = './uploads'
        os.makedirs(upload_dir, exist_ok=True)
        file_path = os.path.join(upload_dir, file.filename)
        file.save(file_path)
        links.append(file_path)

    else:
        if mode == 'topic':
            from langchain_community.tools import YouTubeSearchTool
            search_tool = YouTubeSearchTool()
            results = search_tool.run(f'{input_value},6')
            raw_links = extract_youtube_links(results)
            for url in raw_links:
                if len(links) >= 3:
                    break
                if is_valid_duration(url):
                    links.append(url)

        elif mode == 'playlist':
            if not input_value.startswith("http"):
                return jsonify({'status': '❌ Invalid playlist URL.'})
            ydl_opts = {'quiet': True, 'extract_flat': True, 'force_generic_extractor': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(input_value, download=False)
                all_links = [entry['url'] for entry in info_dict.get('entries', []) if 'url' in entry]
            for url in all_links:
                if is_valid_duration(url):
                    links.append(url)

        elif mode == 'single_url':
            if not input_value.startswith("http"):
                return jsonify({'status': '❌ Invalid video URL.'})
            if is_valid_duration(input_value):
                links.append(input_value)
            else:
                return jsonify({'status': '❌ Video exceeds 30 minutes.'})

    if not links:
        return jsonify({'status': '❌ No suitable links found.'})

    # Start processing in a background thread
    processing_thread = threading.Thread(target=process_with_progress, args=(links, user_id))
    processing_thread.daemon = True
    processing_thread.start()
    
    return jsonify({
        'status': '✅ Processing started! You will see progress updates.',
        'totalFiles': len(links)
    })

@app.route('/progress', methods=['GET'])
def get_progress():
    """Endpoint to get current processing progress"""
    user_id = session.get('user_id')
    if not user_id or user_id not in processing_status:
        return jsonify({
            'status': 'unknown',
            'progress': 0,
            'message': 'No processing in progress'
        })
    
    status = processing_status[user_id]
    progress_percent = (status['completed'] / status['total']) * 100 if status['total'] > 0 else 0
    
    return jsonify({
        'status': 'processing' if status.get('status') != 'complete' else 'complete',
        'progress': progress_percent,
        'currentFile': status['current_file'],
        'completedFiles': status['completed'],
        'totalFiles': status['total'],
        'estimatedCompletion': status.get('estimated_completion'),
        'elapsedTime': f"{time.time() - status['start_time']:.2f} seconds",
        'totalTime': status.get('total_time')
    })

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    user_id = session['user_id']
    agent, _ = get_agent_for_session(user_id)

    # 🟡 خزّن رسالة المستخدم في السجل (قاعدة البيانات أو ملف خارجي)
    save_chat_history(user_id, "User", user_message)
    
    try:
        # ✅ لا تمرر memory هنا لأن الـ agent أصلاً مربوط بها عند إنشائه
        response = agent.run(user_message)
    except Exception as e:
        print(f"❌ Error extracting playlist: {str(e)}")
        return jsonify({'status': f'❌ Error extracting playlist: {str(e)}'})

    
    # 🟡 خزّن رد البوت في السجل
    save_chat_history(user_id, "Bot", response)
    
    return jsonify({'reply': response})
@app.route('/speak', methods=['POST'])
def speak():
    text = request.json['text']
    audio_base64 = generate_speech(text)
    return jsonify({'audio': audio_base64})


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)