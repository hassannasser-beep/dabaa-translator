import streamlit as st
from deep_translator import GoogleTranslator

# 1. إعدادات الصفحة والعنوان الرسمي باسمك الحصري
st.set_page_config(page_title="HASSAN NASSER", page_icon="🤖", layout="wide")

st.title("🤖 HASSAN NASSER")
st.markdown("### SMART AI TRANSLATOR | المترجم الذكي متعدد السياقات")
st.write("---")

# اللغات الثمانية المعتمدة في النظام
languages_dict = {
    "العربية": "ar", 
    "الإنجليزية (English)": "en", 
    "الروسية (Русский)": "ru", 
    "الصينية (中文)": "zh", 
    "الألمانية (Deutsch)": "de", 
    "الإسبانية (Español)": "es", 
    "البرتغالية (Português)": "pt", 
    "الكورية (한국어)": "ko"
}

# دالة ذكية لتوليد الصياغات بناءً على قاموس استبدال هندسي وقواعد لغوية حقيقية
def generate_all_styles(base_text, to_lang):
    # القاموس الهندسي الاحترافي الخاص بك لتعديل الصياغة الهندسية فوراً إذا كانت الترجمة للعربية
    eng_replacements = {
        "من أجل ضمان": "لضمان تحقيق الموثوقية الفنية في", "يجب أن يدفع الانتباه": "يتعين الالتزام الصارم بـ", 
        "الخرسانة الذاتي": "الخرسانة ذاتية الدمك (SCC)", "أشغال خفية": "الأعمال المخفية والمستترة", 
        "قوة التصميم": "المقاومة التصميمية للخرسانة", "إلى آلات المعاينة": "في محاضر المعاينة المعتمدة موقعياً", 
        "رصد مستمر": "إجراء المراقبة والمتابعة المستمرة لـ", "تصل الخرسانة": "تأكيد وصول الخرسانة إلى", 
        "رب العمل": "المالك (Employer)", "فسخ": "إنهاء سحب الأعمال", "طرد": "سحب الأعمال وطرد المقاول تدابيرياً",
        "المهندس": "استشاري المشروع (The Engineer)", "برنامج مراقبة الجودة": "خطة ضبط الجودة المعتمدة",
        "بلاطة": "بلاطة خرسانية / سقف", "خرسانة ضعيفة": "خرسانة عادية / خرسانة نظافة",
        "رسومات المتجر": "الرسومات التنفيذية للموقع (Shop Drawings)"
    }
    
    # قاموس الصياغة القانونية الصارمة (FIDIC)
    legal_replacements = {
        "من أجل ضمان": "بغرض تأكيد الامتثال والوفاء بـ", "يجب أن يدفع الانتباه": "يتعين قانوناً التركيز والإيعاز بـ", 
        "قوة التصميم": "مقاومة الخرسانة المستهدفة تعاقدياً", "رب العمل": "صاحب العمل / المالك تعاقدياً", 
        "فسخ": "فسخ التعاقد بموجب الشروط العامة", "طرد": "إجراءات مصادرة الموقع وسحب الأعمال"
    }

    # 1. الصياغة العامة (الأصلية)
    form_general = base_text

    # 2. الصياغة الهندسية الموقعية
    form_engineering = base_text
    if to_lang == "ar":
        for key, val in eng_replacements.items():
            form_engineering = form_engineering.replace(key, val)
    else:
        form_engineering = f"[Technical/Engineering]: {base_text}"

    # 3. الصياغة القانونية
    form_legal = base_text
    if to_lang == "ar":
        for key, val in legal_replacements.items():
            form_legal = form_legal.replace(key, val)
        if "المقاول" in form_legal:
            form_legal = form_legal.replace("المقاول", "يتعين على المقاول")
    else:
        form_legal = f"[Contractual/Legal]: Subject to the terms, {base_text[0].lower() + base_text[1:] if len(base_text)>1 else base_text}"

    # الكلمات المفتاحية الذكية لفحص بقية السياقات منعاً للكلام العشوائي (الذي ليس له أساس)
    text_lower = base_text.lower()
    
    # 4. الصياغة العلمية الأكاديمية
    scientific_keywords = ["ذرة", "خرسانة", "تفاعل", "مادة", "تحليل", "طب", "خلية", "concrete", "atom", "cell", "acid", "chemical", "test", "analysis", "system"]
    if any(word in text_lower for word in scientific_keywords):
        form_scientific = f"🔬 [أكاديمي/مختبري]: {base_text}" if to_lang == "ar" else f"🔬 [Academic/Scientific]: {base_text}"
    else:
        form_scientific = None

    # 5. الصياغة السياسية
    political_keywords = ["دولة", "رئيس", "حكومة", "وزير", "سفارة", "اتفاقية", "سياسة", "president", "minister", "government", "state", "policy", "treaty", "official"]
    if any(word in text_lower for word in political_keywords):
        form_political = f"🏛️ [دبلوماسي/رسمي]: {base_text}" if to_lang == "ar" else f"🏛️ [Diplomatic/Political]: {base_text}"
    else:
        form_political = None

    # 6. الصياغة الاقتصادية
    economic_keywords = ["مال", "بنوك", "دولار", "سعر", "أسهم", "شراء", "فاتورة", "تمويل", "money", "price", "bank", "stock", "invoice", "finance", "market", "boq", "quantities"]
    if any(word in text_lower for word in economic_keywords):
        form_economic = f"📊 [مالي/تجاري]: {base_text}" if to_lang == "ar" else f"📊 [Financial/Economic]: {base_text}"
    else:
        form_economic = None

    # 7. الصياغة الدينية
    religious_keywords = ["الله", "رب", "صلاة", "مقدس", "كنيسة", "مسجد", "آية", "قرآن", "god", "lord", "pray", "holy", "church", "mosque", "scripture", "bless"]
    if any(word in text_lower for word in religious_keywords):
        form_religious = f"🌙 [سياق روحي/عقائدي]: {base_text}" if to_lang == "ar" else f"🌙 [Spiritual/Religious]: {base_text}"
    else:
        form_religious = None

    return form_general, form_engineering, form_legal, form_scientific, form_political, form_economic, form_religious

# ==========================================
# 📥 واجهة المستخدم (Inputs)
# ==========================================
with st.form(key="smart_translator_form", clear_on_submit=False):
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1, key="src_lang")
    with col_l2:
        target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0, key="tgt_lang")
    
    st.write("---")
    
    text_to_translate = st.text_area(
        "أدخل النص أو الكلمة (سيقوم النظام بفرز الصياغات الحقيقية فقط):", 
        placeholder="Type or paste your text here...",
        height=150,
        key="input_text"
    )
    
    btn_process = st.form_submit_button("🚀 TRANSLATE | تشغيل الترجمة السياقية الفورية", use_container_width=True)

st.write("---")

# ==========================================
# 📊 عرض النتائج (Outputs)
# ==========================================
if btn_process and text_to_translate.strip():
    cleaned_text = text_to_translate.strip()
    
    lang_from = languages_dict[source_lang]
    lang_to = languages_dict[target_lang]
    
    with st.spinner("جاري الترجمة والفرز السياقي الذكي..."):
        try:
            # استخدام محرك ترجمة مستقر جداً ومجاني وبدون حظر
            base_translation = GoogleTranslator(source=lang_from, target=lang_to).translate(cleaned_text)
            
            # توليد الصياغات السبعة المحدثة
            f_general, f_engineering, f_legal, f_scientific, f_political, f_economic, f_religious = generate_all_styles(base_translation, lang_to)
            
            st.success("🔍 تم تحليل النص وتوليد الصياغات المطابقة بنجاح:")
            st.write("---")
            
            # عرض الصياغات الأساسية الثلاثة (تظهر دائماً لأنها تناسب أي نص)
            st.subheader("🛠️ الصياغات الأساسية الدائمة:")
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.markdown("### 💬 صياغة عامة")
                st.warning(f_general)
            with col_b:
                st.markdown("### 👷 صياغة هندسية موقعية")
                st.info(f_engineering)
            with col_c:
                st.markdown("### 📜 صياغة تعاقدية قانونية")
                st.success(f_legal)
                
            st.write("---")
            
            # عرض الصياغات التخصصية (تظهر فقط إذا كان لها أساس في النص الأصلي)
            st.subheader("🎯 الصياغات التخصصية المستهدفة (إن وجدت):")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🧬 الصياغة العلمية")
                if f_scientific: st.info(f_scientific)
                else: st.caption("_لا توجد أبعاد علمية أو أكاديمية لهذا النص_")
                    
                st.markdown("### 📊 الصياغة الاقتصادية")
                if f_economic: st.warning(f_economic)
                else: st.caption("_لا توجد أبعاد مالية أو تجارية لهذا النص_")

            with col2:
                st.markdown("### 🏛️ الصياغة السياسية")
                if f_political: st.code(f_political, language="")
                else: st.caption("_لا توجد أبعاد سياسية أو دبلوماسية لهذا النص_")
                    
                st.markdown("### 🌙 الصياغة الدينية")
                if f_religious: st.markdown(f"> **{f_religious}**")
                else: st.caption("_لا توجد أبعاد دينية أو روحية لهذا النص_")

        except Exception as e:
            st.error(f"❌ عذراً، حدث خطأ أثناء المعالجة: {e}")

elif btn_process:
    st.warning("⚠️ من فضلك اكتب أو ألصق نصاً أولاً ليتمكن النظام من معالجته.")
