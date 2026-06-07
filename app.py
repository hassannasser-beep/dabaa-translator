import streamlit as st
import requests
import urllib.parse

# 1. إعدادات الصفحة والعنوان باسمك
st.set_page_config(page_title=" HASSAN NASSER ", page_icon="🤖", layout="centered")

st.title(" HN TRANSLATOR ")
st.markdown("### نظام ترجمة متطور للمصطلحات الهندسية والنصوص والفقرات الكاملة")
st.write("---")

# 2. قائمة اللغات المتاحة
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

# 3. تصميم واجهة الاختيار
col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1)
with col2:
    target_lang = st.selectbox("إلى لغة:", list(languages_dict.keys()), index=0)

st.write("---")

# 4. صندوق إدخال النص (يتسع للمقالات والفقرات الكبيرة)
text_to_translate = st.text_area(
    "اكتب أو الصق النص أو الفقرة الكاملة هنا:", 
    placeholder="Type or paste your full text, sentences, or engineering paragraphs here...",
    height=250
)

if st.button("✨ ترجم النص الآن", type="primary"):
    if not text_to_translate.strip():
        st.warning("⚠️ من فضلك اكتب أو الصق نصاً أولاً ليتمكن البرنامج من ترجمته.")
    else:
        with st.spinner("جاري معالجة وترجمة النص الكامل..."):
            try:
                encoded_text = urllib.parse.quote(text_to_translate.strip())
                lang_pair = f"{languages_dict[source_lang]}|{languages_dict[target_lang]}"
                url = f"https://api.mymemory.translated.net/get?q={encoded_text}&langpair={lang_pair}"
                
                response = requests.get(url)
                response_json = response.json()
                
                if 'responseData' in response_json:
                    translated_text = response_json['responseData']['translatedText']
                    st.success("📝 النص المترجم:")
                    st.info(translated_text.strip())
                    
                    matches = response_json.get('matches', [])
                    word_count = len(text_to_translate.strip().split())
                    if word_count <= 4 and len(matches) > 1:
                        st.write("---")
                        st.markdown("💡 **صياغات أو خيارات بديلة متوفرة للمصطلح:**")
                        seen = {translated_text.strip().lower()}
                        count = 1
                        for match in matches:
                            alt_text = match.get('translation', '').strip()
                            if alt_text and alt_text.lower() not in seen:
                                st.write(f"{count}. {alt_text}")
                                seen.add(alt_text.lower())
                                count += 1
                else:
                    st.error("❌ واجه النظام مشكلة مؤقتة في معالجة السيرفر، يرجى إعادة المحاولة.")
            except Exception as e:
                st.error(f"حدث خطأ أثناء الاتصال بسيرفر الترجمة: {e}")
