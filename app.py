import streamlit as st
from deep_translator import GoogleTranslator

# 1. إعدادات الصفحة والعنوان الرسمي
st.set_page_config(page_title="HASSAN NASSER", page_icon="🤖", layout="wide")

st.title("🤖 HASSAN NASSER")
st.markdown("### SMART AI TRANSLATOR | المترجم الذكي المطور (متعدد المترادفات)")
st.write("---")

# اللغات المعتمدة في النظام
languages_dict = {
    "العربية": "ar", 
    " can الإنجليزية (English)": "en", 
    "الروسية (Русский)": "ru", 
    "الصينية (中文)": "zh", 
    "الألمانية (Deutsch)": "de", 
    "الإسبانية (Español)": "es", 
    "البرتغالية (Português)": "pt", 
    "الكورية (한국어)": "ko"
}

# قاعدة بيانات موسعة للمصطلحات التخصصية (مختصرة لمنع بتر الكود)
multi_meaning_db = {
    "slab": {
        "engineering": "بلاطة خرسانية / سقف / فرش خرساني مسلح",
        "legal": "عنصر إنشائي خاضع للمعاينة والاستلام تعاقدياً"
    },
    "lean concrete": {
        "engineering": "خرسانة عادية / خرسانة نظافة / فرشية عمية (ضعيفة)",
        "legal": "طبقة التأسيس غير المسلحة أسفل القواعد المعتمدة"
    },
    "shop drawings": {
        "engineering": "رسومات تنفيذية / مخططات ورشة / لوحات تشغيلية للموقع",
        "legal": "المخططات التفصيلية الواجب اعتمادها قبل بدء التنفيذ"
    },
    "as-built drawings": {
        "engineering": "مخططات الواقع الفعلي / رسومات كما نُفذ / لوحات مطابقة الطبيعة",
        "legal": "الرسومات النهائية والمستند التعاقدي بعد إتمام الأعمال"
    }
}

# دالة ذكية لتوليد الصياغات مع إعطاء مرونة وخيارات متعددة داخل السياق
def generate_all_styles(base_text, text_lower, to_lang):
    eng_phrases = {
        "من أجل ضمان": "لضمان [تحقيق / تأكيد] الموثوقية الفنية في", 
        "يجب أن يدفع الانتباه": "يتعين [الالتزام الصارم بـ / مراعاة] ضوابط", 
        "الخرسانة الذاتي": "الخرسانة ذاتية الدمك (SCC)", 
        "أشغال خفية": "الأعمال [المخفية / المستترة / غير الظاهرة]", 
        "قوة التصميم": "المقاومة التصميمية [المستهدفة] للخرسانة", 
        "رب العمل": "المالك / صاحب العمل (Employer)", 
        "فسخ": "إجراءات [إنهاء التعاقد / سحب الأعمال]", 
        "المهندس": "استشاري المشروع / المهندس المشرف (The Engineer)"
    }
    
    legal_phrases = {
        "من أجل ضمان": "بغرض تأكيد الامتثال والوفاء بـ", 
        "يجب أن يدفع الانتباه": "يتعين قانوناً ولائحياً التركيز والإيعاز بـ", 
        "رب العمل": "صاحب العمل تعاقدياً / المالك", 
        "فسخ": "فسخ التعاقد بموجب أحكام الشروط العامة (FIDIC)"
    }

    word_key = text_lower.strip()
    if word_key in multi_meaning_db:
        db_entry = multi_meaning_db[word_key]
        if to_lang == "ar":
            return base_text, db_entry["engineering"], db_entry["legal"], f"🔬 [مترادفات أكاديمية]: {db_entry['engineering']}", None, None, None

    form_general = base_text

    form_engineering = base_text
    if to_lang == "ar":
        for key, val in eng_phrases.items():
            form_engineering = form_engineering.replace(key, val)
    else:
        form_engineering = f"[Technical/Field Options]: {base_text}"

    form_legal = base_text
    if to_lang == "ar":
        for key, val in legal_phrases.items():
            form_legal = form_legal.replace(key, val)
        if "المقاول" in form_legal:
            form_legal = form_legal.replace("المقاول", "يلتزم الطرف الثاني (المقاول) بـ")
    else:
        form_legal = f"[Contractual/Statutory]: {base_text}"

    form_scientific = f"🔬 [أكاديمي]: {base_text}" if any(w in text_lower for w in ["ذرة", "خرسانة", "تفاعل", "concrete", "atom", "test"]) else None
    form_political = f"🏛️ [رسمي]: {base_text}" if any(w in text_lower for w in ["دولة", "رئيس", "وزير", "president", "government"]) else None
    form_economic = f"📊 [مالي]: {base_text}" if any(w in text_lower for w in ["مال", "بنوك", "دولار", "money", "price", "boq"]) else None
    form_religious = f"🌙 [روحي]: {base_text}" if any(w in text_lower for w in ["الله", "رب", "صلاة", "god", "lord"]) else None

    return form_general, form_engineering, form_legal, form_scientific, form_political, form_economic, form_religious

# ==========================================
# 📥 واجهة المستخدم (Inputs)
# ==========================================
with st.form(key="advanced_translator_form", clear_on_submit=False):
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1, key="src_lang")
    with col_l2:
        target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0, key="tgt_lang")
    
    st.write("---")
    
    text_to_translate = st.text_area(
        "أدخل النص أو الكلمة (ستظهر البدائل والمترادفات لحمايتك من الخطأ):", 
        placeholder="Type or paste your text here...",
        height=150,
        key="input_text"
    )
    
    btn_process = st.form_submit_button("🚀 TRANSLATE | تشغيل الترجمة فائقة الدقة", use_container_width=True)

st.write("---")

# ==========================================
# 📊 عرض النتائج (Outputs)
# ==========================================
if btn_process and text_to_translate.strip():
    cleaned_text = text_to_translate.strip()
    text_lower = cleaned_text.lower()
    
    lang_from = languages_dict[source_lang]
    lang_to = languages_dict[target_lang]
    
    with st.spinner("جاري الترجمة واستخراج البدائل اللغوية..."):
        try:
            base_translation = GoogleTranslator(source=lang_from, target=lang_to).translate(cleaned_text)
            
            f_general, f_engineering, f_legal, f_scientific, f_political, f_economic, f_religious = generate_all_styles(base_translation, text_lower, lang_to)
            
            st.success("🎯 تم توليد معاني متعددة وبدائل سياقية لتقليل نسبة الخطأ:")
            st.write("---")
            
            st.subheader("🛠️ الصياغات المفتوحة على خيارات متعددة:")
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.markdown("### 💬 صياغة عامة مبسطة")
                st.warning(f_general)
            with col_b:
                st.markdown("### 👷 صياغة هندسية (مترادفات موقعية)")
                st.info(f_engineering)
            with col_c:
                st.markdown("### 📜 صياغة تعاقدية قانونية")
                st.success(f_legal)
                
            st.write("---")
            
            st.subheader("🎯 الصياغات التخصصية (تظهر إذا تضمنها النص):")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🧬 الصياغة العلمية")
                if f_scientific: st.info(f_scientific)
                else: st.caption("_لا توجد خيارات علمية حيوية لهذا النص_")
                    
                st.markdown("### 📊 الصياغة الاقتصادية")
                if f_economic: st.warning(f_economic)
                else: st.caption("_لا توجد أبعاد مالية أو حسابات كميات_")

            with col2:
                st.markdown("### 🏛️ الصياغة السياسية")
                if f_political: st.code(f_political, language="")
                else: st.caption("_لا توجد دلالات سياسية أو دولية_")
                    
                st.markdown("### 🌙 الصياغة الدينية")
                if f_religious: st.markdown(f"> **{f_religious}**")
                else: st.caption("_لا توجد دلالات لاهوتية أو دينية_")

        except Exception as e:
            st.error(f"❌ حدث خطأ أثناء المعالجة: {e}")

elif btn_process:
    st.warning("⚠️ من فضلك اكتب أو ألصق نصاً أولاً.")
