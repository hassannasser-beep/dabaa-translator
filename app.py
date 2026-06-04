import streamlit as st
import requests

# 1. إعدادات الصفحة والعنوان باسمك
st.set_page_config(page_title="HASSAN NASSER ", page_icon="🤖", layout="centered")

st.title("🤖 مترجم  HASSAN NASSER ")
st.markdown("### أداة ذكية تعرض لك كافة الترجمات والخيارات المتاحة للمصطلحات")
st.write("---")

# 2. قائمة اللغات المتاحة
languages_dict = {
    "العربية": "Arabic", "الإنجليزية (English)": "English", 
    "الروسية (Русский)": "Russian", "الكورية (한국어)": "Korean", "الصينية (中文)": "Chinese"
}

# 🔑 مفتاح جيميناي الخاص بك مدمج وجاهز للعمل
GEMINI_API_KEY = "AQ.Ab8RN6JVfs-u8JIsqBIALwH7TUycLgRP4uffYdy-FTmrmcre5w"

# 3. تصميم واجهة الاختيار (قوائم جاهزة)
col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1) # الافتراضي إنجليزي
with col2:
    target_lang = st.selectbox("إلى لغة:", list(languages_dict.keys()), index=0) # الافتراضي عربي

st.write("---")

# 4. صندوق إدخال النص وزر الترجمة
text_to_translate = st.text_area("اكتب أو الصق النص هنا:", placeholder="Type your text or engineering terms here...")

if st.button("✨ ترجم الآن واستعرض كافة الخيارات", type="primary"):
    if text_to_translate.strip() == "":
        st.warning("⚠️ من فضلك اكتب نصاً أولاً ليتمكن البرنامج من ترجمته.")
    else:
        with st.spinner("جاري استخراج كافة الترجمات الممكنة عبر Gemini..."):
            try:
                # تجهيز الطلب المباشر لسيرفر جوجل جيميناي
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
                
                # تعديل الأمر الموجه للذكاء الاصطناعي ليعطي أكثر من ترجمة وسياقها الهندسي أو العام
                prompt = (
                    f"You are an expert engineer and professional polyglot translator. "
                    f"Translate the following text/term from {languages_dict[source_lang]} to {languages_dict[target_lang]}. "
                    f"If the word or phrase has multiple possible translations, meanings, or contexts (e.g., technical, engineering, general, site jargon), "
                    f"provide ALL the valid translations formatted as a clear, numbered bullet points in {languages_dict[target_lang]}. "
                    f"Briefly mention the context or usage for each option if applicable. Do not write intros or outros. "
                    f"Text to translate:\n\n{text_to_translate}"
                )
                
                payload = {
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }]
                }
                
                # إرسال الطلب
                response = requests.post(url, json=payload)
                response_json = response.json()
                
                # استخراج النص المترجم الشامل من الإجابة
                translated_text = response_json['candidates'][0]['content']['parts'][0]['text']
                
                # عرض النتيجة فوراً على الشاشة
                st.success("📝 خيارات الترجمة المتاحة:")
                st.markdown(translated_text.strip())
                
            except Exception as e:
                st.error("حدث خطأ أثناء الاتصال بـ Gemini. تأكد من استقرار الإنترنت وصلاحية الـ API KEY.")
