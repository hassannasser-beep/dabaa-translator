import streamlit as st
import requests
import re

# 1. Page Configuration
st.set_page_config(page_title="HASSAN NASSER", page_icon="🏗️", layout="wide")

# 2. Adaptive CSS (Supports Light & Dark Themes)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght=400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; max-width: 1000px; }

/* Hero Banner */
.hero {
    background: #1a1a2e;
    border-radius: 14px;
    padding: 2rem 2rem 1.5rem;
    margin-bottom: 1.5rem;
}
.hero-name { font-size: 30px; font-weight: 600; color: #ffffff; letter-spacing: -0.5px; }
.hero-name span { color: #5DCAA5; }
.hero-sub { font-size: 13px; color: rgba(255,255,255,0.45); margin-top: 6px; letter-spacing: 0.04em; }
.hero-pills { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 12px; }
.pill { display: inline-block; border-radius: 20px; padding: 4px 12px; font-size: 11px; font-weight: 500; letter-spacing: 0.04em; }
.pill-active { background: #5DCAA5; color: #04342C; }
.pill-muted { background: rgba(255,255,255,0.07); border: 0.5px solid rgba(255,255,255,0.12); color: rgba(255,255,255,0.5); }
.lang-bar { display: flex; gap: 6px; margin-top: 14px; align-items: center; }
.ldot { width: 8px; height: 8px; border-radius: 50%; background: #5DCAA5; display: inline-block; }
.lang-bar-txt { font-size: 11px; color: rgba(255,255,255,0.35); margin-left: 4px; }

/* Dynamic Context Cards */
.rcard { 
    border-radius: 12px; 
    padding: 1.5rem; 
    border: 0.5px solid rgba(128, 128, 128, 0.2); 
    background: var(--background-color, #fff);
    margin-top: 1rem;
}
.rcard-eng { border-top: 4px solid #1D9E75; }
.rcard-leg { border-top: 4px solid #534AB7; }
.rcard-med { border-top: 4px solid #00B4D8; }
.rcard-lit { border-top: 4px solid #E63946; }
.rcard-sci { border-top: 4px solid #FFB703; }
.rcard-pol { border-top: 4px solid #6C757D; }
.rcard-dir { border-top: 4px solid #D85A30; }

.rlabel { font-size: 11px; font-weight: 600; letter-spacing: 0.08em; margin-bottom: 10px; }
.rlabel-e { color: #1D9E75; }
.rlabel-l { color: #534AB7; }
.rlabel-m { color: #00B4D8; }
.rlabel-lit { color: #E63946; }
.rlabel-s { color: #FFB703; }
.rlabel-p { color: #6C757D; }
.rlabel-g { color: #D85A30; }
.rtext { font-size: 16px; line-height: 1.8; color: var(--text-color, #1f2937); direction: auto; }

/* Slang Detector Table */
.slang-wrap { border-radius: 12px; overflow: hidden; border: 0.5px solid #9FE1CB; margin-top: 1.5rem; }
.slang-head { background: #085041; padding: 12px 16px; }
.slang-head-txt { font-size: 11px; font-weight: 600; color: #9FE1CB; letter-spacing: 0.06em; }
.slang-table { width: 100%; border-collapse: collapse; background: var(--background-color, #fff); }
.slang-table th { font-size: 10px; font-weight: 600; color: #6b7280; letter-spacing: 0.06em; padding: 8px 14px; border-bottom: 0.5px solid rgba(128, 128, 128, 0.2); text-align: left; }
.slang-table td { font-size: 13px; padding: 10px 14px; border-bottom: 0.5px solid rgba(128, 128, 128, 0.1); vertical-align: top; color: var(--text-color, #1f2937); }
.slang-table tr:last-child td { border-bottom: none; }
.term-cell { font-weight: 600; color: #1D9E75; }
.site-cell { font-weight: 500; color: #534AB7; }

/* Spellcheck Alert Box */
.dym-box { background: #FAEEDA; border-left: 3px solid #BA7517; border-radius: 0 8px 8px 0; padding: 10px 14px; font-size: 13px; color: #412402; margin-bottom: 1rem; }

/* Input Adjustments */
div.stButton > button {
    background: #1a1a2e !important; color: white !important; border: none !important;
    border-radius: 8px !important; font-weight: 500 !important;
    font-size: 15px !important; padding: 0.65rem 2rem !important; width: 100% !important;
}
div.stButton > button:hover { background: #0f0f1e !important; }
textarea { border-radius: 8px !important; border: 0.5px solid #d1d5db !important; font-size: 14px !important; }
</style>
""", unsafe_allow_html=True)

# 3. Hero Layout (تم إرجاع العناوين الأصلية كما طلبت)
st.markdown("""
<div class="hero">
    <div class="hero-name">HASSAN <span>NASSER</span></div>
    <div class="hero-sub">ENGINEERING · LEGAL · CONTRACTUAL TRANSLATIONS</div>
    <div class="hero-pills">
        <span class="pill pill-active">Context Classifier</span>
        <span class="pill pill-muted">Smart Translator</span>
        <span class="pill pill-muted">Site Slang Detector</span>
    </div>
    <div class="lang-bar">
        <span class="ldot"></span><span class="ldot"></span><span class="ldot"></span>
        <span class="ldot"></span><span class="ldot"></span><span class="ldot"></span>
        <span class="ldot"></span><span class="ldot"></span>
        <span class="lang-bar-txt">8 languages</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Databases and Mappings
languages_dict = {
    "العربية": "ar", "English": "en", "Русский": "ru", "中文": "zh",
    "Deutsch": "de", "Español": "es", "Português": "pt", "한국어": "ko"
}

# قاموس داخلي موسع للكلمات الفردية متعددة المعاني (مثل charge وغيرها) لضمان إظهار كافة المعاني الممكنة حسب السياق
ADVANCED_LEXICON = {
    "charge": [
        {"context": "⚡ Electrical Engineering", "meaning": "شحنة كهربائية / يشحن بطارية"},
        {"context": "⚖️ Legal & Contractual", "meaning": "تهمة رسمية / ادعاء جنائي / رهن تعاقدي لضمان مالي"},
        {"context": "💰 Financial & Accounts", "meaning": "رسوم مالية / تكلفة / مصاريف إضافية"},
        {"context": "👔 Management & Site", "meaning": "في عهدة / تحت مسؤولية وإشراف (In charge of)"},
        {"context": "🩺 Medical & Clinical", "meaning": "جرعة علاجية مكثفة مفاجئة"},
        {"context": "🏛️ Political & Official", "meaning": "تكليف بمهام دبلوماسية أو منصب رسمي مؤقت"}
    ],
    "tender": [
        {"context": "🏗️ Engineering & Procurement", "meaning": "عطاء / مناقصة مشروع / مستندات التسعير والمزايدة"},
        {"context": "⚖️ Legal & FIDIC", "meaning": "عرض رسمي للوفاء بالتزام تعاقدي"},
        {"context": "💰 Financial", "meaning": "عملة قانونية سائلة للمدفوعات"},
        {"context": "💬 General / Literary", "meaning": "رقيق / حنون / حساس"}
    ],
    "plant": [
        {"context": "🏗️ Heavy Engineering", "meaning": "معدات وآليات الموقع الثقيلة (آلات الصب، الحفارات)"},
        {"context": "🏭 Technical / Industrial", "meaning": "محطة توليد أو معالجة / مصنع إنتاجي ضخم"},
        {"context": "🔬 Scientific / Biology", "meaning": "نبات / كائن حي نباتي"}
    ]
}

site_slang_db = {
    "slab": {"academic": "بلاطة", "slang": "سقف / فرش خرساني", "desc": "الأسقف والمسطحات الخرسانية المسلحة في الموقع."},
    "lean concrete": {"academic": "خرسانة عجيفة / ضعيفة", "slang": "خرسانة نظافة", "desc": "طبقة خرسانية غير مسلحة أسفل القواعد."},
    "shop drawings": {"academic": "رسومات المتجر", "slang": "الرسومات التنفيذية للموقع", "desc": "المخططات التفصيلية للتنفيذ الفعلي."},
    "as-built drawings": {"academic": "رسومات كما بنيت", "slang": "مخططات الواقع الفعلي", "desc": "الرسومات النهائية التي تعكس ما نُفِّذ على أرض الواقع."},
    "bill of quantities": {"academic": "فاتورة الكميات", "slang": "جدول الكميات BOQ", "desc": "الوثيقة التعاقدية الأساسية لتسعير خامات المشروع."},
    "shuttering": {"academic": "إغلاق", "slang": "الشدّة الخشبية / الطوبار", "desc": "الهيكل المؤقت لصب الخرسانة."},
    "scaffolding": {"academic": "أشغال السقالة", "slang": "السقالات الإنشائية", "desc": "الهياكل المعدنية للعمل على الارتفاعات."},
    "curing": {"academic": "شفاء / علاج", "slang": "معالجة الخرسانة بالمياه", "desc": "رش الخرسانة بعد الصب لاكتساب المقاومة."},
    "honeycombing": {"academic": "تعتشيق النحل", "slang": "تعشيش الخرسانة", "desc": "فراغات حصوية تظهر بعد فك الخشب."},
    "kick-off meeting": {"academic": "اجتماع ركلة البداية", "slang": "الاجتماع التحضيري للمشروع", "desc": "أول اجتماع رسمي للمالك والاستشاري والمقاول."},
    "variation order": {"academic": "ترتيب الاختلاف", "slang": "أمر تغيير / ملحق تعاقدي (VO)", "desc": "أمر رسمي لتعديل بند خارج نطاق التعاقد."}
}

# 5. Core Utility Functions
def fetch_ai_translation(text, from_lang, to_lang):
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {"client": "gtx", "sl": from_lang, "tl": to_lang, "dt": "t", "q": text.strip()}
        r = requests.get(url, params=params).json()
        return "".join([p[0] for p in r[0] if p[0]])
    except Exception:
        return text

def fetch_all_dictionary_meanings(word):
    """دالة ذكية تبحث عن كافة المعاني المحتملة للكلمة من مصادر متعددة"""
    w_clean = word.strip().lower()
    if w_clean in ADVANCED_LEXICON:
        return ADVANCED_LEXICON[w_clean]
    
    # محاولة جلب معاني إضافية من API عام خارجي في حالة توفره للكلمات الأخرى
    try:
        res = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{w_clean}", timeout=3)
        if res.status_code == 200:
            data = res.json()
            meanings_list = []
            for meaning in data[0].get('meanings', []):
                part = meaning.get('partOfSpeech', 'general')
                defs = [d.get('definition', '') for d in meaning.get('definitions', [])[:2]]
                meanings_list.append({
                    "context": f"💬 Context as {part.title()}",
                    "meaning": "; ".join(defs)
                })
            if meanings_list:
                return meanings_list
    except Exception:
        pass
        
    return None

def calculate_distance(s1, s2):
    if len(s1) < len(s2): return calculate_distance(s2, s1)
    if len(s2) == 0: return len(s1)
    prev = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        cur = [i + 1]
        for j, c2 in enumerate(s2):
            cur.append(min(prev[j+1]+1, cur[j]+1, prev[j]+(c1!=c2)))
        prev = cur
    return prev[-1]

def check_do_you_mean(text):
    clean_text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    words = clean_text.lower().split()
    sug = []
    for w in words:
        if len(w) < 3 or w.isupper() or w in site_slang_db: continue
        for k in site_slang_db:
            d = calculate_distance(w, k)
            if d == 1 or (len(k) > 6 and d == 2):
                if k not in sug: sug.append(k)
    return sug

def detect_site_slang(text):
    tl = text.lower()
    return [{"term": k.title(), "academic": v["academic"], "slang": v["slang"], "desc": v["desc"]}
            for k, v in site_slang_db.items() if k in tl]

def classify_and_build_formula(base, text, to_lang):
    tl_text = text.lower()
    
    keywords = {
        "legal": ['shall', 'contract', 'employer', 'contractor', 'agreement', 'clause', 'liability', 'المقاول', 'صاحب العمل', 'العقد', 'شروط', 'يلتزم', 'المحكمة'],
        "engineering": ['concrete', 'slab', 'drawing', 'beam', 'specification', 'site', 'foundation', 'خرسانة', 'الموقع', 'رسومات', 'تسليح', 'مخططات', 'بند', 'عمود'],
        "medical": ['patient', 'clinical', 'diagnosis', 'treatment', 'symptoms', 'disease', 'doctor', 'hospital', 'المريض', 'تشخيص', 'أعراض', 'علاج', 'سريري', 'جرعة'],
        "literary": ['metaphor', 'poem', 'novel', 'soul', 'heart', 'beauty', 'shadow', 'whisper', 'شعر', 'رواية', 'بلاغة', 'روح', 'قصيدة', 'نثر', 'وجدان'],
        "scientific": ['laboratory', 'experiment', 'hypothesis', 'molecule', 'quantum', 'chemical', 'data', 'مختبر', 'جزيء', 'معادلة', 'فرضية', 'تحليل', 'فيزياء'],
        "political": ['government', 'election', 'minister', 'diplomatic', 'treaty', 'parliament', 'policy', 'الحكومة', 'انتخابات', 'وزير', 'دبلوماسي', 'معاهدة', 'سياسة']
    }

    scores = {k: sum(1 for word in v if word in tl_text) for k, v in keywords.items()}
    max_context = max(scores, key=scores.get)
    
    if scores[max_context] == 0:
        max_context = "direct"

    if to_lang != "ar":
        prefix_mapping = {
            "legal": "[Legal & Contractual Formulation]\nIt is strictly stipulated that " + base[0].lower() + base[1:],
            "engineering": "[Technical Engineering Formulation]\n" + base,
            "medical": "[Clinical Medical Formulation]\n" + base,
            "literary": "[Literary & Aesthetic Formulation]\n" + base,
            "scientific": "[Academic Scientific Formulation]\n" + base,
            "political": "[Official Political & Diplomatic Formulation]\n" + base,
            "direct": base
        }
        return max_context, prefix_mapping[max_context]

    if max_context == "legal":
        replacements = {"يجب": "يلتزم الطرف الثاني بـ", "المقاول": "يتعين على المقاول", "رب العمل": "صاحب العمل تعاقدياً"}
        for k, v in replacements.items(): base = base.replace(k, v)
    elif max_context == "engineering":
        replacements = {"من أجل ضمان": "لضمان الموثوقية الفنية في", "رب العمل": "المالك (Employer)", "المهندس": "استشاري المشروع"}
        for k, v in replacements.items(): base = base.replace(k, v)
    elif max_context == "medical":
        replacements = {"مرض": "اعتلال صحي", "موت": "وفاة سريرية", "دواء": "العقار العلاجي قيد الوصف"}
        for k, v in replacements.items(): base = base.replace(k, v)
    elif max_context == "literary":
        replacements = {"جميل": "آسرٌ يخلب الألباب", "حزين": "مثقلٌ بأعباء الشجن", "قال": "أردفَ قائلاً بنبرةٍ وجدانية"}
        for k, v in replacements.items(): base = base.replace(k, v)
    elif max_context == "scientific":
        replacements = {"نتيجة": "المخرجات التجريبية الرصدية", "تغيير": "تحول تفاعلي ديناميكي"}
        for k, v in replacements.items(): base = base.replace(k, v)
    elif max_context == "political":
        replacements = {"اتفاق": "معاهدة دبلوماسية رفيعة المستوى", "رفض": "أعربت الجهات السيادية عن تحفظها على"}
        for k, v in replacements.items(): base = base.replace(k, v)

    return max_context, base

# 6. Interactive Interface
col1, col2 = st.columns(2)
with col1:
    src = st.selectbox("FROM", list(languages_dict.keys()), index=1)
with col2:
    tgt = st.selectbox("INTO", list(languages_dict.keys()), index=0)

text_input = st.text_area("", placeholder="اكتب أو الصق النص هنا — تقارير هندسية، بنود تعاقدية، تقارير طبية، نصوص أدبية وسياسية...", height=140)
btn = st.button("🌐  Translate & Refine", use_container_width=True)

st.divider()

# 7. Processing Engine
if btn and text_input.strip():
    text = text_input.strip()
    fl = languages_dict[src]
    tl = languages_dict[tgt]

    sug = check_do_you_mean(text)
    if sug:
        fmt = ", ".join([f"<strong>{s.title()}</strong>" for s in sug])
        st.markdown(f'<div class="dym-box">💡 <b>Did you mean:</b> {fmt}?</div>', unsafe_allow_html=True)

    with st.spinner("Analyzing context and translating..."):
        # التحقق مما إذا كان المدخل كلمة واحدة فقط لإظهار القاموس الشامل لكافة المعاني الممكنة
        is_single = len(text.split()) == 1

        if is_single:
            base = fetch_ai_translation(text, fl, tl)
            all_meanings = fetch_all_dictionary_meanings(text)
            
            st.markdown(f"### 🗄️ Comprehensive Contextual Lexicon for: `{text}`")
            
            if all_meanings:
                # إنشاء جدول ديناميكي يحتوي على كافة المعاني المتاحة دون الاقتصار على ثلاثة فقط
                markdown_table = "| Field / Context | All Possible Meanings & Variations |\n|:---|:---|\n"
                for m in all_meanings:
                    markdown_table += f"| {m['context']} | {m['meaning']} |\n"
                st.markdown(markdown_table)
            else:
                # في حال لم تكن الكلمة مسجلة في القاموس المتعدد، نعرض الترجمة الافتراضية المباشرة
                st.markdown(f"""
| Field / Context | Meaning |
|:---|:---|
| 💬 General Translation | {base} |
""")
        else:
            # إذا كان النص جملة كاملة، يتم تفعيل كاشف السياق التلقائي وعرض بطاقة واحدة ذكية ومناسبة للمجال
            base = fetch_ai_translation(text, fl, tl)
            context_type, formulated_text = classify_and_build_formula(base, text, tl)

            if context_type == "engineering":
                st.markdown(f'<div class="rcard rcard-eng"><div class="rlabel rlabel-e">🏗️ DETECTED CONTEXT: ENGINEERING & TECHNICAL</div><div class="rtext">{formulated_text}</div></div>', unsafe_allow_html=True)
            elif context_type == "legal":
                st.markdown(f'<div class="rcard rcard-leg"><div class="rlabel rlabel-l">⚖️ DETECTED CONTEXT: LEGAL & CONTRACTUAL</div><div class="rtext">{formulated_text}</div></div>', unsafe_allow_html=True)
            elif context_type == "medical":
                st.markdown(f'<div class="rcard rcard-med"><div class="rlabel rlabel-m">🩺 DETECTED CONTEXT: MEDICAL & CLINICAL</div><div class="rtext">{formulated_text}</div></div>', unsafe_allow_html=True)
            elif context_type == "literary":
                st.markdown(f'<div class="rcard rcard-lit"><div class="rlabel rlabel-lit">✍️ DETECTED CONTEXT: LITERARY & AESTHETIC</div><div class="rtext">{formulated_text}</div></div>', unsafe_allow_html=True)
            elif context_type == "scientific":
                st.markdown(f'<div class="rcard rcard-sci"><div class="rlabel rlabel-s">🔬 DETECTED CONTEXT: SCIENTIFIC & ACADEMIC</div><div class="rtext">{formulated_text}</div></div>', unsafe_allow_html=True)
            elif context_type == "political":
                st.markdown(f'<div class="rcard rcard-pol"><div class="rlabel rlabel-p">🏛️ DETECTED CONTEXT: POLITICAL & DIPLOMATIC</div><div class="rtext">{formulated_text}</div></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="rcard rcard-dir"><div class="rlabel rlabel-g">💬 DETECTED CONTEXT: DIRECT & GENERAL</div><div class="rtext">{formulated_text}</div></div>', unsafe_allow_html=True)

            # كاشف المصطلحات الدارجة في الموقع
            detected = detect_site_slang(text)
            if detected:
                rows = "".join([f"""
                <tr>
                  <td class="term-cell">{d['term']}</td>
                  <td>{d['academic']}</td>
                  <td class="site-cell">{d['slang']}</td>
                  <td style="font-size:12px;color:#6b7280">{d['desc']}</td>
                </tr>""" for d in detected])
                st.markdown(f"""
<div class="slang-wrap">
  <div class="slang-head"><span class="slang-head-txt">🔍 SITE SLANG DETECTOR — {len(detected)} TERM(S) FOUND</span></div>
  <table class="slang-table">
    <thead><tr><th>TERM</th><th>STANDARD</th><th>ON-SITE</th><th>NOTE</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
</div>""", unsafe_allow_html=True)

elif btn:
    st.warning("⚠️ Please enter some text first.")
