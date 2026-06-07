import streamlit as st
import requests
import urllib.parse

# 1. إعدادات الصفحة والعنوان باسمك
st.set_page_config(page_title="HASSAN NASSER", page_icon="🤖", layout="centered")

st.title("🤖  HN TRANSLATOR  ")
st.markdown("### نظام ترجمة متطور للمصطلحات الهندسية والنصوص والفقرات الكاملة")
st.write("---")

# 2. قائمة اللغات المتاحة (تمت إضافة الألمانية والبرتغالية والإسبانية مع الاختصارات العالمية)
languages_dict = {
    "العربية": "ar", 
    "الإنجليزية (English)": "en", 
    "الألمانية (Deutsch)": "de",
    "الإسبانية (Español)": "es",
    "البرتغالية (Português)": "pt",
    "الروسية (Русский)": "ru", 
    "الكورية (한국어)": "ko", 
    "الصينية (中文)": "zh"
}

# 3. تصميم واجهة الاختيار (قوائم جاهزة بجانب بعضها)
col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1) # الافتراضي إنجليزي
with col2:
    target_lang = st.selectbox("إلى لغة:", list(languages_dict.keys()), index=0) # الافتراضي عربي

st.write("---")

# 4. صندوق إدخال النص (يتسع للمقالات والفقرات الكبيرة)
text_to_translate = st.text_area(
    "اكتب أو الصق النص أو الفقرة الكاملة هنا:", 
    placeholder="Type or paste your full text, sentences, or engineering paragraphs here...",
    height=250
)

if st.button("✨ ترجم النص الآن", type="primary"):
    # فحص إذا كان النص فارغاً
    if not text_to_translate.strip():
        st.warning("⚠️ من فضلك اكتب أو الصق نصاً أولاً ليتمكن البرنامج من ترجمته.")
        st.stop()
        
    with st.spinner("جاري معالجة وترجمة النص الكامل..."):
        try:
            # ترميز النص بأمان للتعامل مع المسافات والأسطر الجديدة في النصوص الطويلة
            encoded_text = urllib.parse.quote(text_to_translate.strip())
            
            # إعداد تركيب اللغات المطلوبة للطلب
            lang_pair = f"{languages_dict[source_lang]}|{languages_dict[target_lang]}"
            url = f"https://api.mymemory.translated.net/get?q={encoded_text}&langpair={lang_pair}"
            
            # إرسال الطلب للمحرك المستقر
            response = requests.get(url)
            response_json = response.json()
            
            if 'responseData' not in response_json:
                st.error("❌ واجه النظام مشكلة مؤقتة في معالجة السيرفر، يرجى إعادة المحاولة.")
                st.stop()
                
            translated_text = response_json['responseData']['translatedText']
            
            #
