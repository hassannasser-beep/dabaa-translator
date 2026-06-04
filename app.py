import streamlit as st
import requests

# 1. إعدادات الصفحة والعنوان باسمك
st.set_page_config(page_title="HASSAN NASSER AI Translator", page_icon="🤖", layout="centered")

st.title("🤖 مترجم  HASSAN NASSER بذكاء Gemini")
st.markdown("### أداة سريعة ومباشرة لترجمة المصطلحات الهندسية والمحادثات")
st.write("---")

# 2. قائمة اللغات المتاحة
languages_dict = {
    "العربية": "Arabic", "الإنجليزية (English)": "English", 
    "الروسية (Русский)": "Russian", "الكورية (한국어)": "Korean", "الصينية (中文)": "Chinese"
}

# 🔑 ضع مفتاح جيميناي الخاص بك هنا بين علامات الاقتباس (المفتاح السري الذي يبدأ بـ AIzaSy)
GEMINI_API_KEY = "AQ.Ab8RN6Kw65ub_b94LxuWmQHARAoRKPfefdT5_HS0VkOVy-ZPEA"

# 3. تصميم واجهة الاختيار (قوائم جاهزة)
col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1) # الافتراضي إنجليزي
with col2:
    target_lang = st.selectbox("إلى لغة:", list(languages_dict.keys()), index=0) # الافتراضي عربي

st.write("---")

# 4. صندوق إدخال النص وزر الترجمة
text_to_translate = st.text_area("اكتب أو الصق النص هنا:", placeholder="Type your text or engineering terms here...")

if st.button("✨ ترجم الآن عبر الذكاء الاصطناعي", type="primary"):
    if text_to_translate.strip() == "":
        st.warning("⚠️ من فضلك اكتب نصاً أولاً ليتمكن البرنامج من ترجمته.")
    elif GEMINI_API_KEY == "ضع_هنا_مفتاح_جيميني_السري_API_KEY" or GEMINI_API_KEY.strip() == "":
        st.error("❌ يرجى وضع الـ API KEY الخاص بك في السطر رقم 20 داخل الكود أولاً لكي يشتغل المترجم.")
    else:
        with st.spinner("جاري الترجمة الذكية عبر سيرفر Gemini..."):
            try:
                # تجهيز الطلب المباشر لسيرفر جوجل جيميناي بدون مكتبات وسيطة
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
                
                prompt = f"You are an expert engineer and professional translator. Translate this text from {languages_dict[source_lang]} to {languages_dict[target_lang]}. Provide ONLY the clear translation without any extra comments, introduction or notes:\n\n{text_to_translate}"
                
                payload = {
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }]
                }
                
                # إرسال الطلب
                response = requests.post(url, json=payload)
                response_json = response.json()
                
                # استخراج النص المترجم من الإجابة
                translated_text = response_json['candidates'][0]['content']['parts'][0]['text']
                
                # عرض النتيجة فوراً على الشاشة
                st.success("📝 الترجمة الاحترافية:")
                st.subheader(translated_text.strip())
                
            except Exception as e:
                st.error("حدث خطأ أثناء الاتصال بـ Gemini. تأكد من صلاحية الـ API KEY الخاص بك وأنه مكتوب بشكل صحيح.")
