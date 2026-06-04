import streamlit as st
from deep_translator import GoogleTranslator

# 1. إعدادات الصفحة والعنوان
st.set_page_config(page_title="HASSAN NASSER Translator", page_icon="🏗️", layout="wide")

st.title("🏗️ مترجم المهندس HASSAN NASSER الذكي والأمن")
st.markdown("### نظام الترجمة الفورية وإدارة القواميس المخصصة لجميع اللغات")
st.write("---")

# 2. قائمة اللغات المدعومة
languages_dict = {
    "العربية": "ar",
    "الإنجليزية (English)": "en",
    "الروسية (Русский)": "ru",
    "الكورية (한국어)": "ko",
    "الصينية (中文)": "zh"
}

# 3. 🔒 إعداد كلمة المرور الافتراضية للمسؤول (حسن ناصر)
ADMIN_PASSWORD = "1992002"  # يمكنك تغيير "1234" لأي كلمة سر قوية تريدها

# 4. 🧠 تهيئة الذاكرة التخزينية المؤقتة للقاموس الشامل
if "global_dict" not in st.session_state:
    # القاموس الافتراضي (يدعم تحديد لغة المصدر والهدف والكلمة والترجمة)
    st.session_state.global_dict = [

# 5. تصميم واجهة الموقع (تقسيم الشاشة)
col_left, col_right = st.columns([2, 1])

# 👈 الجزء الأيسر: محرك المترجم الأساسي (متاح لجميع المستخدمين)
with col_left:
    st.subheader("🌐 قسم الترجمة الفورية الذكي")
    
    c1, c2 = st.columns(2)
    with c1:
        source_lang = st.selectbox("من لغة:", list(languages_dict.keys()), index=1)
    with c2:
        target_lang = st.selectbox("إلى لغة:", list(languages_dict.keys()), index=0)
        
    text_to_translate = st.text_area("اكتب النص أو الكلمة هنا للفحص والترجمة:", height=100)
    
    if st.button("✨ ترجم الآن", type="primary"):
        if text_to_translate.strip() != "":
            src_code = languages_dict[source_lang]
            tgt_code = languages_dict[target_lang]
            search_word = text_to_translate.strip().lower()
            
            # فحص هل الكلمة مطابقة في القاموس المخصص بناءً على اللغات المختارة؟
            found_translation = None
            for item in st.session_state.global_dict:
                if item["from_lang"] == src_code and item["to_lang"] == tgt_code and item["word"] == search_word:
                    found_translation = item["translation"]
                    break
            
            if found_translation:
                st.info("💡 تم استخدام الترجمة المعتمدة الخاصة بالمهندس حسن مسبقاً:")
                st.subheader(found_translation)
            else:
                # إذا لم تكن موجودة، يتم استخدام مترجم جوجل
                with st.spinner("جاري الترجمة عبر السيرفر العالمي..."):
                    try:
                        translated = GoogleTranslator(source=src_code, target=tgt_code).translate(text_to_translate)
                        st.success("📝 النتيجة:")
                        st.subheader(translated)
                    except Exception as e:
                        st.error(f"حدث خطأ أثناء الترجمة: {e}")

# 👉 الجزء الأيمن: لوحة التحكم المحمية بكلمة مرور (لحسن ناصر فقط)
with col_right:
    st.subheader("🔒 لوحة الإدارة والتعديل اليدوي")
    
    # خانة إدخال كلمة المرور للأمان
    password_input = st.text_input("أدخل كلمة مرور المسؤول لرؤية أدوات التعديل:", type="password")
    
    if password_input == ADMIN_PASSWORD:
        st.success("🔓 مرحباً مهندس حسن! تم تفعيل صلاحيات التعديل والمسح.")
        st.write("---")
        st.markdown("#### 📥 إضافة مصطلح جديد بكل اللغات")
        
        # اختيار لغات الكلمة الجديدة
        add_src = st.selectbox("لغة الكلمة الأصلية:", list(languages_dict.keys()), key="add_src")
        add_tgt = st.selectbox("لغة الترجمة المعتمدة:", list(languages_dict.keys()), key="add_tgt")
        
        word_in = st.text_input("الكلمة الأصلية:")
        trans_in = st.text_input("الترجمة الصحيحة:")
        
        if st.button("📥 حفظ في النظام"):
            if word_in.strip() != "" and trans_in.strip() != "":
                # إضافة الكلمة للقاموس العام ببياناتها الكاملة
                st.session_state.global_dict.append({
                    "from_lang": languages_dict[add_src],
                    "to_lang": languages_dict[add_tgt],
                    "word": word_in.strip().lower(),
                    "translation": trans_in.strip()
                })
                st.success("✅ تم الحفظ بنجاح!")
                st.rerun()  # إعادة تحديث الشاشة لرؤية النتيجة فوراً
            else:
                st.error("⚠️ يرجى ملء البيانات أولاً.")
                
        st.write("---")
        st.markdown("#### 🗑️ إدارة ومسح الكلمات الحالية")
        
        # عرض الكلمات مع زر مسح بجانب كل كلمة
        for index, item in enumerate(st.session_state.global_dict):
            # جلب أسماء اللغات للعرض بشكل مقروء
            f_name = [k for k, v in languages_dict.items() if v == item["from_lang"]][0]
            t_name = [k for k, v in languages_dict.items() if v == item["to_lang"]][0]
            
            # إنشاء سطر يحتوي على الكلمة وزر المسح بجانبها
            c_word, c_btn = st.columns([3, 1])
            c_word.write(f"🔹 **{item['word']}** ({f_name}) ➔ {item['translation']} ({t_name})")
            
            # زر المسح يأخذ كود تعريفي فريد يعتمد على رقمه الترتيبي (index)
            if c_btn.button("🗑️ مسح", key=f"del_{index}"):
                st.session_state.global_dict.pop(index)
                st.success("تم مسح الكلمة!")
                st.rerun()
                
    elif password_input != "":
        st.error("❌ كلمة المرور خاطئة! لا تمتلك صلاحيات التعديل.")
    else:
        st.info("💡 هذه اللوحة مخصصة للمسؤول فقط لتعديل ومسح الكلمات. بقية المستخدمين سيظهر لهم القاموس الصحيح والمترجم الفوري فقط.")
        
    # عرض القاموس الحالي للقراءة فقط للباقيين إذا لم يدخلوا كلمة السر
    if password_input != ADMIN_PASSWORD:
        st.write("---")
        with st.expander("📖 استعراض القاموس المعتمد الحالي في الموقع"):
            for item in st.session_state.global_dict:
                f_name = [k for k, v in languages_dict.items() if v == item["from_lang"]][0]
                t_name = [k for k, v in languages_dict.items() if v == item["to_lang"]][0]
                st.write(f"🔹 **{item['word']}** ({f_name}) ➔ {item['translation']} ({t_name})")
