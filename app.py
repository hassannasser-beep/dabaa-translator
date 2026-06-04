import streamlit as st
from deep_translator import GoogleTranslator

# 1. إعدادات الصفحة وتغيير اسم التبويب والأيقونة باسمك
st.set_page_config(page_title="HASSAN NASSER Translator", page_icon="🏗️", layout="centered")

# 2. العنوان الرئيسي للموقع باسمك الشخصي
st.title("🏗️ مترجم المهندس HASSAN NASSER الذكي")
st.markdown("### أداة تفاعلية لترجمة المصطلحات الهندسية والمحادثات في موقع الضبعة")
st.write("---")

# 3. تعريف اللغات المدعومة (مع إضافة اللغة الصينية "zh")
languages_dict = {
    "العربية": "ar",
    "الإنجليزية (English)": "en",
    "الروسية (Русский)": "ru",
    "الكورية (한국어)": "ko",
    "الصينية (中文)": "zh"
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
                
                # عرض النتيجة داخل صندوق مجهز وأنيق
                st.success("📝 النص المترجم:")
                st.subheader(translated)
                
            except Exception as e:
                st.error(f"حدث خطأ أثناء الاتصال بمحرك الترجمة: {e}")
