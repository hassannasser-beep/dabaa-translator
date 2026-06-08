import streamlit as st
from deep_translator import GoogleTranslator

# 1. إعدادات الصفحة والعنوان
st.set_page_config(page_title="HASSAN NASSER", page_icon="🤖", layout="wide")

st.title("🤖 HASSAN NASSER")
st.markdown("### SMART AI TRANSLATOR | المترجم الذكي المطور (متعدد المترادفات)")
st.write("---")

# اللغات المعتمدة
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

# قاعدة بيانات موسعة للمصطلحات التخصصية التي تعطى أكثر من معنى في السياق الواحد
multi_meaning_db = {
    "slab": {
        "engineering": "بلاطة خرسانية / سقف / فرش خرساني مسلح",
        "legal": "عنصر إنشائي خاضع للمعاينة والاستلام تعاقدياً",
        "general": "شريحة / لوح سميك"
    },
    "lean concrete": {
        "engineering": "خرسانة عادية / خرسانة نظافة / فرشية عمية (ضعيفة)",
        "legal": "طبقة التأسيس غير المسلحة أسفل القواعد المعتمدة",
        "general": "خرسانة فقيرة الإسمنت"
    },
    "shop drawings": {
        "engineering": "رسومات تنفيذية / مخططات ورشة / لوحات تشغيلية للموقع",
        "legal": "المخططات التفصيلية الواجب اعتمادها قبل بدء التنفيذ",
        "general": "رسومات المتجر"
    },
    "as-built drawings": {
        "engineering": "مخططات الواقع الفعلي / رسومات كما نُفذ / لوحات مطابقة الطبيعة",
        "legal": "الرسومات النهائية والمستند التعاقدي بعد إتمام الأعمال",
        "general": "رسومات كما بنيت"
    },
    "shuttering": {
        "engineering": "شدّة خشبية / طوبار / قالب صب / كوفراج",
        "legal": "الهيكل المؤقت الحاضن للخرسانة لحين جفافها تعاقدياً",
        "general": "إغلاق / نوافذ"
    },
    "curing": {
        "engineering": "رش المياه / معالجة الخرسانة / ترطيب / إنضاج الخرسانة",
        "legal": "فترة الحماية والترطيب الإلزامية للمنشأ الخرساني",
        "general": "علاج / شفاء"
    },
    "honeycombing": {
        "engineering": "تعشيش الخرسانة / فراغات حصوية / تزهير وتجويف الخرسانة",
        "legal": "عيوب مصنعية ناتجة عن سوء الدمك تستوجب الإصلاح الفني",
        "general": "تعتشيق النحل"
    },
    "bill of quantities": {
        "engineering": "جدول الكميات والمواصفات (BOQ) / مقايسة الأعمال",
        "legal": "وثيقة التسعير الأساسية وحجر الزاوية في التعاقد",
        "general": "فاتورة الكميات"
    }
}

# دالة ذكية لتوليد الصياغات مع إعطاء مرونة وخيارات متعددة داخل السياق
def generate_all_styles(base_text, text_lower, to_lang):
    
    # قاموس دقيق جداً لاستبدال العبارات الركيكة بعبارات احترافية تحتوي على بدائل
    eng_phrases = {
        "من أجل ضمان": "لضمان [تحقيق / تأكيد] الموثوقية الفنية في", 
        "يجب أن يدفع الانتباه": "يتعين [الالتزام الصارم بـ / مراعاة] ضوابط", 
        "الخرسانة الذاتي": "الخرسانة ذاتية الدمك (SCC)", 
        "أشغال خفية": "الأعمال [المخفية / المستترة / غير الظاهرة]", 
        "قوة التصميم": "المقاومة التصميمية [المستهدفة] للخرسانة", 
        "إلى آلات المعاينة": "في محاضر الفحص والمعاينة المعتمدة موقعياً", 
        "رصد مستمر": "إجراء [المراقبة الدائمة / المتابعة المستمرة] لـ", 
        "تصل الخرسانة": "تأكيد وصول وتوريد الخرسانة إلى", 
        "رب العمل": "المالك / صاحب العمل (Employer)", 
        "فسخ": "إجراءات [إنهاء التعاقد / سحب الأعمال]", 
        "طرد": "سحب الأعمال وطرد المقاول تدابيرياً",
        "المهندس": "استشاري المشروع / المهندس المشرف (The Engineer)", 
        "برنامج مراقبة الجودة": "خطة ضبط وتأكيد الجودة المعتمدة"
    }
    
    legal_phrases = {
        "من أجل ضمان": "بغرض تأكيد الامتثال والوفاء بـ", 
        "يجب أن يدفع الانتباه": "يتعين قانوناً ولائحياً التركيز والإيعاز بـ", 
        "قوة التصميم": "مقاومة الخرسانة المستهدفة تعاقدياً", 
        "رب العمل": "صاحب العمل تعاقدياً / المالك", 
        "فسخ": "فسخ التعاقد بموجب أحكام الشروط العامة (FIDIC)"
    }

    # تحقق أولاً إذا كانت الكلمة موجودة في قاموس تعدد المعاني المخصص
    word_key = text_lower.strip()
    if word_key in multi_meaning_db:
        db_entry = multi_meaning_db[word_key]
        if to_lang == "ar":
            return base_text, db_entry["engineering"], db_entry["legal"], f"🔬 [مترادفات أكاديمية]: {db_entry['engineering']}", None, None, None

    # الصياغة العامة
    form_general = base_text

    # الصياغة الهندسية (تطبيق الفلتر الذكي لإعطاء المترادفات بين أقواس)
    form_engineering = base_text
    if to_lang == "ar":
        for key, val in eng_phrases.items():
            form_engineering = form_engineering.replace(key, val)
    else:
        form_engineering = f"[Technical/Field Options]: {base_text}"

    # الصياغة القانونية
    form_legal = base_text
    if to_lang == "ar":
        for key, val in legal_phrases.items():
            form_legal = form_legal.replace(key, val)
        if "المقاول" in form_legal:
            form_legal = form_legal.replace("المقاول", "يلتزم الطرف الثاني (المقاول) بـ")
    else:
        form_legal = f"[Contractual/Statutory]: {base_text}"

    # فحص بقية السياقات بالكلمات المفتاحية
    form_scientific = f"🔬 [أكاديمي/مختبري]: {base_text}" if any(w in text_lower for w in ["ذرة", "خرسانة", "تفاعل", "concrete", "atom", "chemical", "test"]) else None
    form_political = f"🏛️ [دبلوماسي/رسمي]: {base_text}" if any(w in text_lower for w in ["دولة", "رئيس", "وزير", "president", "minister", "government"]) else None
    form_economic = f"📊 [مالي/تجاري]: {base_text}" if any(w in text_lower for w in ["مال", "بنوك", "دولار", "سعر", "money", "price", "bank", "boq"]) else None
    form_religious = f"🌙 [سياق روحي]: {base_text}" if any(w in text_lower for w in ["الله", "رب", "صلاة", "god", "lord", "pray"]) else None

    return form_general, form_engineering, form_legal, form_scientific, form_political, form_economic, form_religious

# ==========================================
# 📥 واجهة المستخدم
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
# 📊 عرض النتائج
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
            
            st.success("🎯 تم توليد معاني متعددة وبدائل سياقية لتقليل نسبة الخطأ إلى 0%:")
            st.write("---")
            
            st.subheader("🛠️ الصياغات المفتوحة على خيارات متعددة:")
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.markdown("### 💬 صياغة عامة مب
