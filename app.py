import streamlit as st
from deep_translator import GoogleTranslator

# 1. إعدادات الصفحة والعنوان
st.set_page_config(page_title="HASSAN NASSER Translator", page_icon="🏗️", layout="wide")

st.title("🏗️ مترجم المهندس HASSAN NASSER الذكي")
st.markdown("### أداة الترجمة الفورية وتعديل القاموس يدوياً من الشاشة")
st.write("---")

# 2. 🧠 تهيئة الذاكرة التخزينية المؤقتة للموقع (لحفظ كلماتك الجديدة)
if "my_dict" not in st.session_state:
    # الكلمات الافتراضية المعتمدة في البداية
    st.session_state.my_dict = {
        "handover": "تسليم المواد لشركة دايسون",
        "scrap": "المخلفات والسكراب التالف",
        "variance": "الفروقات بين الجرد والواقع"
    }

# 3. تصميم واجهة الموقع (تقسيم الشاشة إلى جزأين)
col_left, col_right = st.columns([2, 1])

# 👈 الجزء الأيسر: محرك المترجم الأساسي
with col_left:
    st.subheader("🌐 قسم الترجمة الفورية")
    
    # اختيار اللغات
    languages_dict = {"العربية": "ar", "الإنجليزية (English)": "en", "الروسية (Русский)": "ru"}
    c1, c2 = st.columns(2)
    with c1:
        source_lang = st.selectbox("من لغة:", list(languages_dict.keys()), index=1)
    with c2:
        target_lang = st.selectbox("إلى لغة:", list(languages_dict.keys()), index=0)
        
    # صندوق كتابة النص المراد ترجمته
    text_to_translate = st.text_area("اكتب النص هنا للفحص والترجمة:", height=100)
    
    if st.button("✨ ترجم الآن", type="primary"):
        if text_to_translate.strip() != "":
            cleaned_text = text_to_translate.strip().lower()
            
            # فحص هل الكلمة موجودة في القاموس الذي عدلته بيدك؟
            if source_lang == "الإنجليزية (English)" and target_lang == "العربية" and cleaned_text in st.session_state.my_dict:
                st.info("💡 تم استخدام التعديل اليدوي الخاص بك من الشاشة:")
                st.subheader(st.session_state.my_dict[cleaned_text])
            else:
                # ترجمة طبيعية عبر الإنترنت
                translated = GoogleTranslator(source=languages_dict[source_lang], target=languages_dict[target_lang]).translate(text_to_translate)
                st.success("📝 النتيجة:")
                st.subheader(translated)

# 👉 الجزء الأيمن: لوحة التعديل وإضافة الكلمات يدوياً
with col_right:
    st.subheader("📝 تعديل وإضافة كلمات يدوياً")
    st.write("يمكنك إدخال أي مصطلح هنا لتعديل ترجمته فوراً:")
    
    # خانات إدخال يدوية تظهر للمستخدم على الشاشة
    new_word = st.text_input("1. اكتب الكلمة بالإنجليزية:", placeholder="مثال: fabrication")
    new_translation = st.text_input("2. اكتب الترجمة العربية المعتمدة:", placeholder="مثال: تصنيع موقعي")
    
    # زر الحفظ
    if st.button("📥 حفظ الكلمة في القاموس"):
        if new_word.strip() != "" and new_translation.strip() != "":
            word_key = new_word.strip().lower()
            # إضافة الكلمة والترجمة يدوياً للذاكرة
            st.session_state.my_dict[word_key] = new_translation.strip()
            st.success(f"✅ تم حفظ الكلمة '{new_word}' بنجاح!")
        else:
            st.error("⚠️ يرجى ملء الخانتين أولاً قبل الحفظ.")
            
    # عرض الكلمات المضافة حالياً للتأكد منها
    st.write("---")
    with st.expander("📖 كلمات قاموسك الحالي"):
        for w, t in st.session_state.my_dict.items():
            st.write(f"🔹 **{w}** : {t}")
            
