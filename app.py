import streamlit as st
from deep_translator import GoogleTranslator

# 1. إعدادات الصفحة
st.set_page_config(page_title="HASSAN NASSER Translator", page_icon="🏗️", layout="centered")

st.title("🏗️ مترجم المهندس HASSAN NASSER الذكي")
st.markdown("### أداة تفاعلية مدعومة بقاموس المصطلحات الهندسية لمشروع الضبعة")
st.write("---")

# 2. 🔑 قاموس المصطلحات الخاص بك (تستطيع إضافة أي كلمة ومعناها هنا)
# اكتب الكلمة بالإنجليزية وبحروف صغيرة على اليسار، وترجمتها العربية الدقيقة على اليمين
custom_glossary = {
    "handover": "تسليم العهدة / المواد لشركة دايسون",
    "fabrication": "أعمال التصنيع والتشكيل الموقعي",
    "scrap": "المخلفات / السكراب التالف",
    "doosan": "شركة دوسان للصناعات الثقيلة",
    "daesun": "شركة دايسون للمقاولات",
    "variance": "الفروقات بين الجرد والواقع",
    "incoming": "المواد الواردة حديثاً للموقع"
}

# 3. قائمة اللغات
languages_dict = {
    "العربية": "ar",
    "الإنجليزية (English)": "en",
    "الروسية (Русский)": "ru",
    "الكورية (한국어)": "ko",
    "الصينية (中文)": "zh"
}

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1)
with col2:
    target_lang = st.selectbox("إلى لغة:", list(languages_dict.keys()), index=0)

st.write("---")

text_to_translate = st.text_area("اكتب أو الصق النص هنا:", placeholder="Type your text here...")

if st.button("✨ ترجم الآن", type="primary"):
    if text_to_translate.strip() == "":
        st.warning("⚠️ من فضلك اكتب نصاً أولاً.")
    else:
        with st.spinner("جاري فحص القاموس والترجمة..."):
            try:
                # تحويل النص المكتوب لحروف صغيرة لفحصه في قاموسك المخصص
                cleaned_text = text_to_translate.strip().lower()
                
                # اختبار: هل الكلمة موجودة في قاموس حسن ناصر؟
                if source_lang == "الإنجليزية (English)" and target_lang == "العربية" and cleaned_text in custom_glossary:
                    translated = custom_glossary[cleaned_text]
                    st.info("💡 تم استخدام الترجمة المعتمدة من قاموس المهندس حسن المخصص للموقع:")
                else:
                    # إذا لم تكن في القاموس، تترجم طبيعي عبر جوجل
                    translated = GoogleTranslator(
                        source=languages_dict[source_lang], 
                        target=languages_dict[target_lang]
                    ).translate(text_to_translate)
                
                st.success("📝 النص المترجم:")
                st.subheader(translated)
                
            except Exception as e:
                st.error(f"حدث خطأ أثناء الترجمة: {e}")

# 4. عرض القاموس الحالي في أسفل الصفحة للمراجعة
with st.expander("📖 استعراض كلمات قاموس الموقع الحالي"):
    st.write("هذه الكلمات تترجم تلقائياً حسب معانيها المعتمدة في الموقع:")
    for word, translation in custom_glossary.items():
        st.write(f"🔹 **{word}** ──> {translation}")
