import streamlit as st
import requests

# 1. إعدادات الصفحة والعنوان باسمك
st.set_page_config(page_title="HASSAN NASSER AI Translator", page_icon="🤖", layout="centered")

st.title("🤖 مترجم المهندس HASSAN NASSER الذكي الفوري")
st.markdown("### أداة سريعة ومباشرة لترجمة المصطلحات الهندسية والمحادثات بدون انقطاع")
st.write("---")

# 2. قائمة اللغات المتاحة (تم ضبط الاختصارات العالمية)
languages_dict = {
    "العربية": "ar", "الإنجليزية (English)": "en", 
    "الروسية (Русский)": "ru", "الكورية (한국어)": "ko", "الصينية (中文)": "zh"
}

# 3. تصميم واجهة الاختيار (قوائم جاهزة بجانب بعضها)
col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1) # الافتراضي إنجليزي
with col2:
    target_lang = st.selectbox("إلى لغة:", list(languages_dict.keys()), index=0) # الافتراضي عربي

st.write("---")

# 4. صندوق إدخال النص وزر الترجمة
text_to_translate = st.text_area("اكتب أو الصق النص هنا:", placeholder="Type your text or engineering terms here...")

if st.button("✨ ترجم الآن واستعرض الخيارات", type="primary"):
    if text_to_translate.strip() == "":
        st.warning("⚠️ من فضلك اكتب نصاً أولاً ليتمكن البرنامج من ترجمته.")
    else:
        with st.spinner("جاري الترجمة الفورية المستقرة..."):
            try:
                # إعداد تركيب اللغات المطلوبة للطلب
                lang_pair = f"{languages_dict[source_lang]}|{languages_dict[target_lang]}"
                url = f"https://api.mymemory.translated.net/get?q={text_to_translate.strip()}&langpair={lang_pair}"
                
                # إرسال الطلب للمحرك المجاني المستقر
                response = requests.get(url)
                response_json = response.json()
                
                if 'responseData' in response_json:
                    translated_text = response_json['responseData']['translatedText']
                    
                    # عرض الترجمة الأساسية الكبيرة
                    st.success("📝 الترجمة المعتمدة:")
                    st.subheader(translated_text.strip())
                    
                    # جلب واستعراض خيارات وترجمات بديلة ومتعددة للمصطلح إن وجدت
                    if 'matches' in response_json and len(response_json['matches']) > 1:
