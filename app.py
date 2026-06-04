import streamlit as st
import requests

# 1. إعدادات الصفحة والعنوان باسمك
st.set_page_config(page_title="HASSAN NASSER AI Translator", page_icon="🤖", layout="centered")

st.title("🤖 مترجم المهندس HASSAN NASSER بذكاء Gemini الشامل")
st.markdown("### أداة ذكية وسريعة تعرض لك كافة خيارات الترجمة المتاحة للمصطلحات")
st.write("---")

# 2. قائمة اللغات المتاحة
languages_dict = {
    "العربية": "Arabic", "الإنجليزية (English)": "English", 
    "الروسية (Русский)": "Russian", "الكورية (한국어)": "Korean", "الصينية (中文)": "Chinese"
}

# 🔑 تم دمج مفتاحك الجديد من نوع AQ هنا مباشرة
GEMINI_API_KEY = "AQ.Ab8RN6Ju1TteQTKBNmvIWB9qbFFVstmyWc935_YLqmyIAuPlIw"

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
        with st.spinner("جاري الاتصال الآمن بسيرفر Gemini واستخراج الخيارات..."):
            try:
                # الرابط المباشر بدون دمج المفتاح فيه لحمايته
                url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
                
                # 🔒 الطريقة الصحيحة والآمنة لإرسال مفاتيح AQ الجديدة عبر الـ Bearer Token
                headers = {
                    "Authorization": f"Bearer {GEMINI_API_KEY}",
                    "Content-Type": "application/json"
                }
                
                # الأمر الموجه للذكاء الاصطناعي ليعطي أكثر من ترجمة
                prompt = (
                    f"You are an expert engineer and professional polyglot translator. "
                    f"Translate the following text/term from {languages_dict[source_lang]} to {languages_dict[target_lang]}. "
                    f"If the word or phrase has multiple possible translations, meanings, or contexts (e.g., technical, engineering, general, site jargon), "
                    f"provide ALL the valid translations formatted as clear, numbered bullet points in {languages_dict[target_lang]}. "
                    f"Briefly mention the context or usage for each option if applicable. Do not write intros or outros. "
                    f"Text to translate:\n\n{text_to_translate}"
                )
                
                payload = {
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }]
                }
                
                # إرسال الطلب مع الرؤوس المشفرة لحل مشكلة الـ AQ Key
                response = requests.post(url, json=payload, headers=headers)
                response_json = response.json()
                
                # استخراج النص وعرضه
                if 'candidates' in response_json:
                    translated_text = response_json['candidates'][0]['content']['parts'][0]['text']
                    st.success("📝 خيارات الترجمة المتاحة:")
                    st.markdown(translated_text.strip())
                else:
                    # حل بديل إذا طلب السيرفر الرأس الآخر المخصص للمفاتيح المطورة
                    headers_backup = {
                        "x-goog-api-key": GEMINI_API_KEY,
                        "Content-Type": "application/json"
                    }
                    response_backup = requests.post(url, json=payload, headers=headers_backup)
                    response_json_backup = response_backup.json()
                    
                    if 'candidates' in response_json_backup:
                        translated_text = response_json_backup['candidates'][0]['content']['parts'][0]['text']
                        st.success("📝 خيارات الترجمة المتاحة:")
                        st.markdown(translated_text.strip())
                    else:
                        st.error("❌ واجه السيرفر مشكلة في تفعيل المفتاح، يرجى التأكد من أن المفتاح نشط في حسابك.")
                
            except Exception as e:
                st.error(f"حدث خطأ أثناء الاتصال بـ Gemini: {e}")
