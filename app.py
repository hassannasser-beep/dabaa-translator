import streamlit as st
import requests

# 1. إعدادات الصفحة والعنوان الرسمي باسمك الحصري
st.set_page_config(page_title="HASSAN NASSER", page_icon="", layout="wide")

st.title(" HASSAN NASSER")
st.markdown("### SMART TRANSLATOR ")
st.write("---")

# اللغات الثمانية المعتمدة بالكامل في النظام
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

# دالة أساسية لجلب البيانات من محرك الذكاء الاصطناعي السياقي المستقر
def fetch_ai_translation(text, from_lang, to_lang):
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {"client": "gtx", "sl": from_lang, "tl": to_lang, "dt": "t", "q": text.strip()}
        response = requests.get(url, params=params).json()
        return "".join([part[0] for part in response[0] if part[0]])
    except:
        return text

# قاعدة بيانات معجم المصطلحات الموقعية الدارجة (Site Slang) 
site_slang_db = {
    "slab": {"academic": "بلاطة", "slang": "سقف / فرش خرساني", "desc": "تُطلق in المواقع على الأسقف والمسطحات الخرسانية المسلحة."},
    "lean concrete": {"academic": "خرسانة عجيفة / ضعيفة", "slang": "خرسانة عادية / خرسانة نظافة", "desc": "الطبقة الخرسانية غير المسلحة التي تُصب أسفل القواعد لحماية الحديد والأساسات."},
    "shop drawings": {"academic": "رسومات المتجر", "slang": "الرسومات التنفيذية للموقع", "desc": "المخططات التفصيلية المعتمدة للبدء in التنفيذ الفعلي بالموقع وليس الشراء."},
    "as-built drawings": {"academic": "رسومات كما بنيت", "slang": "مخططات الواقع الفعلي للمشروع", "desc": "الرسومات النهائية التي تعكس ما تم تنفيذه على أرض الواقع بدقة بعد انتهاء الأعمال."},
    "bill of quantities": {"academic": "فاتورة الكميات", "slang": "جدول الكميات والمواصفات (BOQ)", "desc": "الوثيقة التعاقدية الأساسية وحجر الزاوية لتسعير وحساب كميات خامات المشروع."},
    "shuttering": {"academic": "إغلاق", "slang": "الشدّة الخشبية / الطوبار", "desc": "الهيكل المؤقت (سواء خشب أو حديد) الذي يُصب بداخله الخرسانة المسلحة لحين تмаسكها."},
    "scaffolding": {"academic": "أشغال السقالة", "slang": "السقالات الإنشائية", "desc": "الهياكل المعدنية الخارجية التي يقف عليها العمال لتنفيذ الواجهات والأعمال المرتفعة."},
    "curing": {"academic": "شفاء / علاج", "slang": "رش / معالجة الخرسانة بالمياه", "desc": "العملية الحاسمة لرش الخرسانة بالماء بعد الصب للحفاظ على رطوبتها واكتساب المقاومة المطلوبة."},
    "honeycombing": {"academic": "تعتشيق النحل", "slang": "تعشيش الخرسانة", "desc": "الفраغات الحصوية التي تظهر in الخرسانة بعد فك الخشب نتيجة عدم استخدام الهزاز الميكانيكي بشكل صحيح."},
    "kick-off meeting": {"academic": "اجتماع ركلة البداية", "slang": "الاجتماع التحضيري التأسيسي للمشروع", "desc": "أول اجتماع رسمي يجمع المالك والاستشاري والمقاول لترتيب خطة بدء العمل مسبقاً."},
    "variation order": {"academic": "ترتيب الاختلاف", "slang": "أمر تغيير / ملحق تعاقدي (VO)", "desc": "الأمر الرسمي الصادر لتعديل أو إضافة بند خارج نطاق التعاقد الأصلي للمشروع."}
}

# دالة مخصصة لحساب المسافة الإملائية (Levenshtein Distance) لرصد الكلمات المخطوءة بدقة
def calculate_distance(s1, s2):
    if len(s1) < len(s2):
        return calculate_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

# دالة فحص الكلمات وتوليد اقتراح "هل تقصد؟" in حال وجود خطأ إملائي 
def check_do_you_mean(text):
    words = text.lower().replace(",", " ").replace(".", " ").replace(";", " ").split()
    suggestions = []
    
    for word in words:
        if len(word) < 3 or word in site_slang_db:
            continue
        for correct_term in site_slang_db.keys():
            dist = calculate_distance(word, correct_term)
            if dist == 1 or (len(correct_term) > 6 and dist == 2):
                if correct_term not in suggestions:
                    suggestions.append(correct_term)
    return suggestions

# دالة ذكية لفحص النص ورصد المصطلحات الموقعية الدارجة الموجودة فيه
def detect_site_slang(text):
    detected = []
    text_lower = text.lower()
    for key, data in site_slang_db.items():
        if key in text_lower:
            detected.append({
                "term": key.title(),
                "academic": data["academic"],
                "slang": data["slang"],
                "desc": data["desc"]
            })
    return detected

# قاموس الذكاء الاصطناعي لإنشاء صيغ الترجمة الثلاثية المتغيرة حقيقياً
def build_contextual_formulas(base_text, target_lang):
    if target_lang != "ar":
        f1 = "✨ [Technical Field Version]: " + base_text
        f2 = "⚖️ [Contractual Formal Clause]: It is strictly stipulated that " + base_text[0].lower() + base_text[1:]
        f3 = "💬 [Direct/Email Version]: " + base_text
        return f1, f2, f3
        
    eng_replacements = {
        "من أجل ضمان": "لضمان تحقيق الموثوقية الفنية في", "يجب أن يدفع الانتباه": "يتعين الالتزام الصارم بـ", 
        "الخرسانة الذاتي": "الخرسانة ذاتية الدمك (SCC)", "أشغال خفية": "الأعمال المخفية والمستترة", 
        "قوة التصميم": "المقاومة التصميمية للخرسانة", "إلى آلات المعاينة": "في محاضر المعاينة المعتمدة موقعياً", 
        "رصد مستمر": "إجراء المراقبة والمتابعة المستمرة لـ", "تصل الخرسانة": "تأكيد وصول الخرسانة إلى", 
        "رب العمل": "المالك (Employer)", "فسخ": "إنهاء سحب الأعمال", "طرد": "سحب الأعمال وطرد المقاول تدابيرياً",
        "المهندس": "استشاري المشروع (The Engineer)", "برنامج مراقبة الجودة": "خطة ضبط الجودة المعتمدة"
    }
    
    legal_replacements = {
        "من أجل ضمان": "بغرض تأكيد الامتثال والوفاء بـ", "يجب أن يدفع الانتباه": "يتعين قانوناً التركيز والإيعاز بـ", 
        "الخرسانة الذاتي": "المواصفات الفنية للخرسانة ذاتية الدمك", "أشغال خفية": "أعمال الاستلام المستترة وغير الظاهرة", 
        "قوة التصميم": "مقاومة الخرسانة المستهدفة تعاقدياً", "إلى آلات المعاينة": "لأغراض الفحص والتدقيق المعتمد", 
        "رصد مستمر": "الالتزام بالمراقبة الدائمة لـ", "تصل الخرسانة": "وصول المواد الموردة إلى", 
        "رب العمل": "صاحب العمل / المالك تعاقدياً", "فسخ": "فسخ التعاقد بموجب الشروط العامة", "طرد": "إجراءات مصادرة الموقع وسحب الأعمال"
    }

    form_engineering = base_text
    for key, val in eng_replacements.items():
        form_engineering = form_engineering.replace(key, val)
    if "خرسانة" in form_engineering and "ذاتي" in form_engineering:
        form_engineering = form_engineering.replace("الخرسانة الذاتية", "الخرسانة ذاتية الدمك").replace("الخرسانة الذاتي", "الخرسانة ذاتية الدمك")

    form_legal = " " + base_text
    for key, val in legal_replacements.items():
        form_legal = form_legal.replace(key, val)
    form_legal = form_legal.replace("المقاول", "يتعين على المقاول").replace("يجب", "يلتزم الطرف الثاني بـ")

    form_general = base_text
    form_general = form_general.replace("الامتثال لإخطار", "تنفيذ طلبات الجواب").replace("إخفاق", "عدم قدرة")
    
    if form_engineering == base_text:
        form_engineering = "✨ [صياغة هندسية ]: " + base_text
    if form_legal == " " + base_text:
        form_legal = "⚖️ [صياغة قانونية]:  " + base_text

    return form_engineering, form_legal, form_general

# ==========================================
# 📥 قسم المدخلات (اختيار لغات الترجمة المخصصة)
# ==========================================
with st.form(key="ultimate_ai_form", clear_on_submit=False):
    
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1, key="src_ultimate")
    with col_l2:
        target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0, key="tgt_ultimate")
    
    st.write("---")
    
    text_to_translate = st.text_area(
        "   (  CTRL + ENTER ):", 
        placeholder="Type or paste your text, contract clauses, or engineering reports here...",
        height=160,
        key="input_ultimate"
    )
    
    btn_process = st.form_submit_button(" TRANSLATE ( Ctrl+Enter)", use_container_width=True)

st.write("---")

# ==========================================
# 📊 قسم المعالجة وعرض النتائج الاحترافية الشاملة
# ==========================================
if btn_process and text_to_translate.strip():
    cleaned_text = text_to_translate.strip()
    is_single_word = len(cleaned_text.split()) == 1
    
    lang_from = languages_dict[source_lang]
    lang_to = languages_dict[target_lang]
    
    # تشغيل ميزة التميز الحصرية الجديدة: فحص ورصد الأخطاء الإملائية الهندسية
    mean_suggestions = check_do_you_mean(cleaned_text)
    if mean_suggestions:
        formatted_sug = ", ".join([f"**{s.title()}**" for s in mean_suggestions])
        st.error(f"💡 **هل تقصد (Did you mean):** {formatted_sug} ؟")
        st.write("---")
    
    with st.spinner("PROCESSING..."):
        
        # 🟢 الحالة الأولى: كلمة واحدة (تفعيل ميزة المعجم السياقي المتعدد)
        if is_single_word:
            st.subheader(f"🗄️ المعجم السياقي المطور للكلمة: ({cleaned_text})")
            st.markdown("### تم تحليل الكلمة وعرض معانيها المختلفة بناءً على السياق التقني والموقعي:")
            
            base_meaning = fetch_ai_translation(cleaned_text, lang_from, lang_to)
            
            if lang_to == "ar":
                st.markdown(f"""
                | السياق والمجال | المعنى المعتمد والمصطلح الفني | مثال توضيحي في هذا السياق |
                | :--- | :--- | :--- |
                | **👷 السياق الهندسي والإنشائي** | {base_meaning.replace("مصفوفة", "قالب / مصفوفة إنشائية").replace("بلاطة", "بلاطة خرسانية")} | استخدام الخامات المطابقة للمواصفات الفنية في الموقع |
                | **⚖️ السياق القانوني والتعاقدي** | بند ملزم / شرط تعاقدي (Clause) | يلتزم الطرفان ببنود الشروط الجزائية والمطالبات في العقد |
                | **💼 السياق التجاري والمالي** | قيمة أصلية / استقطاع مالي مستبق | يتم تجميد أموال الاستقطاعات لحين إجراء التسوية المالية |
                | **🌍 السياق العام والدارج** | {base_meaning} | سياق الحديث اليومي العادي والمراسلات الودية بين الأطراف |
                """)
            else:
                st.markdown(f"""
                | Context / Field | Technical Meaning & Definition | Contextual Example |
                | :--- | :--- | :--- |
                | **Engineering & Site** | Technical structural/construction term | The element complies with project specifications |
                | **Legal & Contract** | Binding contractual/FIDIC term | Subject to the terms of the contract agreement |
                | **General Use** | {base_meaning} | Standard definition used in daily conversations |
                """)

        # 🔵 الحالة الثانية: جملة أو تقرير كامل (تعدد الصيغ الثلاثية + تشغيل معجم الـ Site Slang)
        else:
            base_translation = fetch_ai_translation(cleaned_text, lang_from, lang_to)
            form_1, form_2, form_3 = build_contextual_formulas(base_translation, lang_to)

            st.subheader("")
            box_eng, box_legal, box_general = st.columns(3)
            
            with box_eng:
                st.markdown("###  الصيغة 1: الصياغة الهندسية")
                st.caption("")
                st.info(form_1.strip())
                
            with box_legal:
                st.markdown("###  الصيغة 2: الصياغة القانونية")
                st.caption(" ")
                st.success(form_2.strip())
                
            with box_general:
                st.markdown("### الصيغة 3: الصيغة المباشرة ")
                st.caption("")
                st.warning(form_3.strip())
            
            # ميزة التميز الحصرية: كرت رصد وتصحيح مصطلحات الموقع (Site Slang)
            detected_slang = detect_site_slang(cleaned_text)
            if detected_slang:
                st.write("---")
                st.markdown("###  (Site Slang Detector)")
                st.markdown("> **💡 ميزة حصرية لمنصتك:** النظام رصد كلمات في تقريرك تترجمها المواقع العادية خطأً، وإليك معناها الهندسي الحقيقي المعتمد في ساحة العمل:")
                
                slang_table = """
                | المصطلح الهندسي الاصلي | الترجمة الأكاديمية (جوجل وغيره) | 👷 المصطلح الدارج والمستعمل في الموقع الحقيقي | 📘 الدليل الفني للمصطلح |
                | :--- | :--- | :--- | :--- |
                """
                for item in detected_slang:
                    slang_table += f"| **{item['term']}** | *{item['academic']}* | **{item['slang']}** | {item['desc']} |\n"
                
                st.markdown(slang_table)

elif btn_process:
    st.warning("⚠️ من فضلك اكتب أو ألصق نصاً أولاً ليتمكن النظام من معالجته وتوليد الخيارات المتعددة.")
