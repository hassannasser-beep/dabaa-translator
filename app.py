import streamlit as st
import requests

st.set_page_config(page_title="HASSAN NASSER", page_icon="🏗️", layout="wide")

# ========== CSS مخصص للتصميم الجديد ==========
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* إخفاء عناصر Streamlit الافتراضية */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 1000px; }

/* الهيدر */
.hn-header {
    border-bottom: 0.5px solid #e5e7eb;
    padding-bottom: 1.2rem;
    margin-bottom: 1.5rem;
}
.hn-badge {
    display: inline-block;
    background: #E1F5EE;
    color: #0F6E56;
    font-size: 11px;
    font-weight: 600;
    padding: 3px 12px;
    border-radius: 20px;
    letter-spacing: 0.06em;
    margin-bottom: 0.5rem;
}
.hn-title {
    font-size: 26px;
    font-weight: 600;
    color: #111827;
    margin: 0;
}
.hn-sub {
    font-size: 14px;
    color: #6b7280;
    margin-top: 4px;
}

/* بطاقات النتائج */
.result-card {
    background: #ffffff;
    border: 0.5px solid #e5e7eb;
    border-radius: 12px;
    padding: 1.1rem 1.3rem;
    height: 100%;
}
.result-card.eng  { border-top: 3px solid #1D9E75; }
.result-card.legal { border-top: 3px solid #534AB7; }
.result-card.direct { border-top: 3px solid #BA7517; }

.result-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.06em;
    margin-bottom: 0.6rem;
}
.result-label.e { color: #0F6E56; }
.result-label.l { color: #534AB7; }
.result-label.g { color: #BA7517; }

.result-text {
    font-size: 14px;
    line-height: 1.75;
    color: #1f2937;
    direction: auto;
}

/* بطاقة Site Slang */
.slang-wrap {
    background: #E1F5EE;
    border: 0.5px solid #9FE1CB;
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin-top: 1rem;
}
.slang-title {
    font-size: 12px;
    font-weight: 600;
    color: #0F6E56;
    margin-bottom: 0.75rem;
}
.slang-item {
    background: #fff;
    border: 0.5px solid #9FE1CB;
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 8px;
}
.slang-term { font-size: 13px; font-weight: 600; color: #111827; }
.slang-grid { display: flex; gap: 20px; margin-top: 6px; flex-wrap: wrap; }
.slang-col span { font-size: 11px; color: #6b7280; display: block; }
.slang-val { font-size: 12px; color: #111827; font-weight: 500; }
.slang-desc { font-size: 12px; color: #6b7280; margin-top: 6px; line-height: 1.5; }

/* تنبيه هل تقصد */
.dym-box {
    background: #FAEEDA;
    border: 0.5px solid #FAC775;
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 13px;
    color: #633806;
    margin-bottom: 1rem;
}

/* زر الترجمة */
div.stButton > button {
    background: #0F6E56 !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 500 !important;
    font-size: 15px !important;
    padding: 0.6rem 2rem !important;
    width: 100% !important;
    transition: background 0.15s !important;
}
div.stButton > button:hover {
    background: #085041 !important;
}

/* حقل النص */
textarea {
    border-radius: 8px !important;
    border: 0.5px solid #d1d5db !important;
    font-size: 14px !important;
}
</style>
""", unsafe_allow_html=True)

# ========== الهيدر ==========
st.markdown("""
<div class="hn-header">
    <div class="hn-badge">SMART TRANSLATOR</div>
    <h1 class="hn-title">HASSAN NASSER</h1>
    <p class="hn-sub">Engineering · Legal · Contractual Translations — 8 Languages</p>
</div>
""", unsafe_allow_html=True)

# ========== البيانات ==========
languages_dict = {
    "العربية": "ar",
    "English": "en",
    "Русский": "ru",
    "中文": "zh",
    "Deutsch": "de",
    "Español": "es",
    "Português": "pt",
    "한국어": "ko"
}

site_slang_db = {
    "slab": {"academic": "بلاطة", "slang": "سقف / فرش خرساني", "desc": "تُطلق في المواقع على الأسقف والمسطحات الخرسانية المسلحة."},
    "lean concrete": {"academic": "خرسانة عجيفة / ضعيفة", "slang": "خرسانة عادية / خرسانة نظافة", "desc": "الطبقة الخرسانية غير المسلحة التي تُصب أسفل القواعد."},
    "shop drawings": {"academic": "رسومات المتجر", "slang": "الرسومات التنفيذية للموقع", "desc": "المخططات التفصيلية المعتمدة للبدء في التنفيذ الفعلي."},
    "as-built drawings": {"academic": "رسومات كما بنيت", "slang": "مخططات الواقع الفعلي للمشروع", "desc": "الرسومات النهائية التي تعكس ما تم تنفيذه على أرض الواقع."},
    "bill of quantities": {"academic": "فاتورة الكميات", "slang": "جدول الكميات والمواصفات (BOQ)", "desc": "الوثيقة التعاقدية الأساسية لتسعير وحساب كميات خامات المشروع."},
    "shuttering": {"academic": "إغلاق", "slang": "الشدّة الخشبية / الطوبار", "desc": "الهيكل المؤقت الذي يُصب بداخله الخرسانة لحين تماسكها."},
    "scaffolding": {"academic": "أشغال السقالة", "slang": "السقالات الإنشائية", "desc": "الهياكل المعدنية الخارجية التي يقف عليها العمال."},
    "curing": {"academic": "شفاء / علاج", "slang": "رش / معالجة الخرسانة بالمياه", "desc": "عملية رش الخرسانة بالماء بعد الصب للحفاظ على رطوبتها."},
    "honeycombing": {"academic": "تعتشيق النحل", "slang": "تعشيش الخرسانة", "desc": "الفراغات الحصوية التي تظهر في الخرسانة بعد فك الخشب."},
    "kick-off meeting": {"academic": "اجتماع ركلة البداية", "slang": "الاجتماع التحضيري التأسيسي للمشروع", "desc": "أول اجتماع رسمي يجمع المالك والاستشاري والمقاول."},
    "variation order": {"academic": "ترتيب الاختلاف", "slang": "أمر تغيير / ملحق تعاقدي (VO)", "desc": "الأمر الرسمي الصادر لتعديل أو إضافة بند خارج نطاق التعاقد."}
}

# ========== الدوال ==========
def fetch_ai_translation(text, from_lang, to_lang):
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {"client": "gtx", "sl": from_lang, "tl": to_lang, "dt": "t", "q": text.strip()}
        response = requests.get(url, params=params).json()
        return "".join([part[0] for part in response[0] if part[0]])
    except:
        return text

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

def build_contextual_formulas(base_text, target_lang):
    if target_lang != "ar":
        f1 = "[Engineering]: " + base_text
        f2 = "[Legal/Contractual]: It is strictly stipulated that " + base_text[0].lower() + base_text[1:]
        f3 = base_text
        return f1, f2, f3

    eng_replacements = {
        "من أجل ضمان": "لضمان تحقيق الموثوقية الفنية في",
        "يجب أن يدفع الانتباه": "يتعين الالتزام الصارم بـ",
        "رب العمل": "المالك (Employer)",
        "المهندس": "استشاري المشروع (The Engineer)",
    }
    legal_replacements = {
        "من أجل ضمان": "بغرض تأكيد الامتثال والوفاء بـ",
        "يجب": "يلتزم الطرف الثاني بـ",
        "المقاول": "يتعين على المقاول",
        "رب العمل": "صاحب العمل / المالك تعاقدياً",
    }

    f1 = base_text
    for k, v in eng_replacements.items():
        f1 = f1.replace(k, v)

    f2 = base_text
    for k, v in legal_replacements.items():
        f2 = f2.replace(k, v)

    f3 = base_text
    return f1, f2, f3

# ========== الواجهة ==========
col_l1, col_l2 = st.columns(2)
with col_l1:
    source_lang = st.selectbox("من لغة:", list(languages_dict.keys()), index=1)
with col_l2:
    target_lang = st.selectbox("إلى لغة:", list(languages_dict.keys()), index=0)

text_to_translate = st.text_area(
    "النص المراد ترجمته:",
    placeholder="اكتب أو الصق نصك هنا — تقارير هندسية، بنود تعاقدية، مراسلات...",
    height=150
)

btn_process = st.button("🌐 ترجم الآن", use_container_width=True)

st.divider()

# ========== المعالجة ==========
if btn_process and text_to_translate.strip():
    cleaned_text = text_to_translate.strip()
    lang_from = languages_dict[source_lang]
    lang_to = languages_dict[target_lang]

    # هل تقصد؟
    suggestions = check_do_you_mean(cleaned_text)
    if suggestions:
        formatted = ", ".join([f"<strong>{s.title()}</strong>" for s in suggestions])
        st.markdown(f'<div class="dym-box">💡 <b>هل تقصد (Did you mean):</b> {formatted} ؟</div>', unsafe_allow_html=True)

    with st.spinner("جارٍ الترجمة..."):
        is_single = len(cleaned_text.split()) == 1

        if is_single:
            base = fetch_ai_translation(cleaned_text, lang_from, lang_to)
            st.markdown(f"### 🗄️ المعجم السياقي للكلمة: `{cleaned_text}`")
            if lang_to == "ar":
                st.markdown(f"""
| السياق | المعنى المعتمد | مثال |
|:---|:---|:---|
| 👷 هندسي وإنشائي | {base} | مواصفات فنية في الموقع |
| ⚖️ قانوني وتعاقدي | بند ملزم / شرط تعاقدي (Clause) | الشروط الجزائية في العقد |
| 💼 تجاري ومالي | قيمة أصلية / استقطاع مالي | التسوية المالية النهائية |
| 🌍 عام ودارج | {base} | الحديث اليومي والمراسلات |
""")
            else:
                st.markdown(f"""
| Context | Meaning | Example |
|:---|:---|:---|
| Engineering | Technical/structural term | On-site specifications |
| Legal | Contractual/FIDIC clause | Penalty conditions |
| General | {base} | Daily correspondence |
""")
        else:
            base = fetch_ai_translation(cleaned_text, lang_from, lang_to)
            f1, f2, f3 = build_contextual_formulas(base, lang_to)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f"""
<div class="result-card eng">
    <div class="result-label e">🏗️ الصياغة الهندسية</div>
    <div class="result-text">{f1}</div>
</div>""", unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
<div class="result-card legal">
    <div class="result-label l">⚖️ الصياغة القانونية</div>
    <div class="result-text">{f2}</div>
</div>""", unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
<div class="result-card direct">
    <div class="result-label g">💬 الصيغة المباشرة</div>
    <div class="result-text">{f3}</div>
</div>""", unsafe_allow_html=True)

            # Site Slang
            detected = detect_site_slang(cleaned_text)
            if detected:
                items_html = ""
                for item in detected:
                    items_html += f"""
<div class="slang-item">
    <div class="slang-term">{item['term']}</div>
    <div class="slang-grid">
        <div class="slang-col"><span>الترجمة الأكاديمية</span><span class="slang-val">{item['academic']}</span></div>
        <div class="slang-col"><span>المصطلح الموقعي</span><span class="slang-val">{item['slang']}</span></div>
    </div>
    <div class="slang-desc">{item['desc']}</div>
</div>"""
                st.markdown(f"""
<div class="slang-wrap">
    <div class="slang-title">🔍 Site Slang Detector — تم رصد {len(detected)} مصطلح</div>
    {items_html}
</div>""", unsafe_allow_html=True)

elif btn_process:
    st.warning("⚠️ من فضلك اكتب نصاً أولاً.")
