import streamlit as st
from deep_translator import GoogleTranslator

# إعدادات الصفحة والعنوان
st.set_page_config(page_title="مترجم مشروع الضبعة الذكي", page_icon="🌐", layout="centered")

st.title("🌐 مترجم المشروع الذكي (El Dabaa Translator)")
st.markdown("### أداة سريعة لترجمة المصطلحات الهندسية والمحادثات اليومية")
st.write("---")

# تعريف اللغات المدعومة في المشروع
languages_dict = {
    "العربية": "ar",
    "الإنجليزية (English)": "en",
    "الروسية (Русский)": "ru",
    "الكورية (한국어)": "ko"
}

# تصميم واجهة الاختيار باستخدام القوائم الجاهزة بجانب بعضها
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1) # الافتراضي إنجليزي

with col2:
    target_lang = st.selectbox("إلى لغة:", list(languages_dict.keys()), index=0) # الافتراضي عربي

st.write("---")

# صندوق إدخال النص المراد ترجمته
text_to_translate = st.text_area("اكتب أو الصق النص هنا:", placeholder="Type your text here...")

# زر تشغيل الترجمة
if st.button("✨ ترجم الآن", type="primary"):
    if text_to_translate.strip() == "":
        st.warning("⚠️ من فضلك اكتب نصاً أولاً ليتمكن البرنامج من ترجمته.")
    else:
        with st.spinner("جاري الترجمة الفورية..."):
            try:
                # استدعاء محرك الترجمة الذكي
                translated = GoogleTranslator(
                    source=languages_dict[source_lang], 
                    target=languages_dict[target_lang]
                ).translate(text_to_translate)
                
                # عرض النتيجة داخل صندوق مجهز وجميل
                st.success("📝 النص المترجم:")
                st.subheader(translated)
                
            except Exception as e:
                st.error(f"حدث خطأ أثناء الاتصال بمحرك الترجمة: {e}")
