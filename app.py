import streamlit as st
import requests
import os

st.set_page_config(page_title="HASSAN NASSER", page_icon="🏗️", layout="wide")

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; max-width: 1100px; }

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
.ldot-off { background: rgba(255,255,255,0.18); }
.lang-bar-txt { font-size: 11px; color: rgba(255,255,255,0.35); margin-left: 4px; }

.rcard { border-radius: 12px; padding: 1.1rem 1.3rem; border: 0.5px solid #e5e7eb; background: #fff; }
.rcard-pol { border-top: 3px solid #E63946; }
.rcard-leg { border-top: 3px solid #534AB7; }
.rcard-eco { border-top: 3px solid #F4A261; }
.rcard-med { border-top: 3px solid #2A9D8F; }
.rcard-sci { border-top: 3px solid #264653; }
.rcard-gen { border-top: 3px solid #6B7280; }

.rlabel { font-size: 10px; font-weight: 600; letter-spacing: 0.08em; margin-bottom: 8px; }
.rlabel-pol { color: #9B2226; }
.rlabel-leg { color: #3C3489; }
.rlabel-eco { color: #9C6644; }
.rlabel-med { color: #1B6B5E; }
.rlabel-sci { color: #1D3A4C; }
.rlabel-gen { color: #4B5563; }
.rtext { font-size: 14px; line-height: 1.75; color: #1f2937; direction: auto; }

.slang-wrap { border-radius: 12px; overflow: hidden; border: 0.5px solid #9FE1CB; margin-top: 1rem; }
.slang-head { background: #085041; padding: 12px 16px; }
.slang-head-txt { font-size: 11px; font-weight: 600; color: #9FE1CB; letter-spacing: 0.06em; }
.slang-table { width: 100%; border-collapse: collapse; background: #fff; }
.slang-table th { font-size: 10px; font-weight: 600; color: #6b7280; letter-spacing: 0.06em; padding: 8px 14px; border-bottom: 0.5px solid #e5e7eb; text-align: left; }
.slang-table td { font-size: 13px; padding: 10px 14px; border-bottom: 0.5px solid #f3f4f6; vertical-align: top; }
.slang-table tr:last-child td { border-bottom: none; }
.term-cell { font-weight: 600; color: #085041; }
.site-cell { font-weight: 500; color: #3C3489; }

.dym-box { background: #FAEEDA; border-left: 3px solid #BA7517; border-radius: 0 8px 8px 0; padding: 10px 14px; font-size: 13px; color: #412402; margin-bottom: 1rem; }

.swap-btn {
    background: #f3f4f6 !important;
    color: #374151 !important;
    border: 1px solid #d1d5db !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    padding: 0.4rem 0.8rem !important;
    width: auto !important;
}
.swap-btn:hover { background: #e5e7eb !important; }

div.stButton > button[kind="primary"] {
    background: #1a1a2e !important; color: white !important; border: none !important;
    border-radius: 8px !important; font-weight: 500 !important;
    font-size: 15px !important; padding: 0.65rem 2rem !important; width: 100% !important;
}
div.stButton > button[kind="primary"]:hover { background: #0f0f1e !important; }
textarea { border-radius: 8px !important; border: 0.5px solid #d1d5db !important; font-size: 14px !important; }

.api-badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.04em;
}
.api-deepl { background: #0F2B46; color: #8ECAE6; }
.api-google { background: #F4A261; color: #5C3D1E; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-name">HASSAN <span>NASSER</span></div>
    <div class="hero-sub">ENGINEERING · LEGAL · CONTRACTUAL · POLITICAL · ECONOMIC · MEDICAL · SCIENTIFIC TRANSLATIONS</div>
    <div class="hero-pills">
        <span class="pill pill-active">DeepL Precision</span>
        <span class="pill pill-muted">6 Formulations</span>
        <span class="pill pill-muted">Site Slang Detector</span>
        <span class="pill pill-muted">Smart Swap</span>
    </div>
    <div class="lang-bar">
        <span class="ldot"></span><span class="ldot"></span><span class="ldot"></span>
        <span class="ldot"></span><span class="ldot"></span><span class="ldot"></span>
        <span class="ldot"></span><span class="ldot"></span>
        <span class="lang-bar-txt">8 languages</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Languages ────────────────────────────────────────────────────────────────
languages_dict = {
    "العربية": "ar", "English": "en", "Русский": "ru", "中文": "zh",
    "Deutsch": "de", "Español": "es", "Português": "pt", "한국어": "ko"
}

# ── Site Slang DB ───────────────────────────────────────────────────────────
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

# ── Translation Engines ──────────────────────────────────────────────────────
DEEPL_API_KEY = os.environ.get("DEEPL_API_KEY", "")

def fetch_deepl_translation(text, from_lang, to_lang):
    """DeepL API — أفضل دقة للترجمة التخصصية."""
    if not DEEPL_API_KEY:
        return None
    try:
        url = "https://api-free.deepl.com/v2/translate"
        headers = {"Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}", "Content-Type": "application/x-www-form-urlencoded"}
        payload = {"text": text.strip(), "source_lang": from_lang.upper(), "target_lang": to_lang.upper()}
        r = requests.post(url, data=payload, headers=headers, timeout=15)
        if r.status_code == 200:
            return r.json()["translations"][0]["text"]
    except Exception:
        pass
    return None

def fetch_google_translation(text, from_lang, to_lang):
    """Google Translate (gtx) — fallback مجاني."""
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {"client": "gtx", "sl": from_lang, "tl": to_lang, "dt": "t", "q": text.strip()}
        r = requests.get(url, params=params, timeout=10).json()
        return "".join([p[0] for p in r[0] if p[0]])
    except Exception:
        return text

def fetch_ai_translation(text, from_lang, to_lang):
    """يحاول DeepL أولاً، ثم يعود لـ Google."""
    result = fetch_deepl_translation(text, from_lang, to_lang)
    if result:
        return result, "DeepL"
    return fetch_google_translation(text, from_lang, to_lang), "Google"

# ── Helpers ─────────────────────────────────────────────────────────────────
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
    words = text.lower().replace(",", " ").replace(".", " ").split()
    sug = []
    for w in words:
        if len(w) < 3 or w in site_slang_db: continue
        for k in site_slang_db:
            d = calculate_distance(w, k)
            if d == 1 or (len(k) > 6 and d == 2):
                if k not in sug: sug.append(k)
    return sug

def detect_site_slang(text):
    tl = text.lower()
    return [{"term": k.title(), "academic": v["academic"], "slang": v["slang"], "desc": v["desc"]}
            for k, v in site_slang_db.items() if k in tl]

# ── 6 Formulations Engine ────────────────────────────────────────────────────
def build_formulas(base, to_lang):
    if to_lang != "ar":
        return (
            "[Political] In the political context, " + base[0].lower() + base[1:],
            "[Legal] It is strictly stipulated that " + base[0].lower() + base[1:],
            "[Economic] From an economic perspective, " + base[0].lower() + base[1:],
            "[Medical] Clinically, " + base[0].lower() + base[1:],
            "[Scientific] Scientifically, " + base[0].lower() + base[1:],
            base
        )

    # Arabic formulations
    political = {
        "يجب": "تؤكد السياسة الرسمية على",
        "المقاول": "الجهة المنفذة",
        "رب العمل": "الجهة المالكة",
        "من أجل": "في إطار السياسة العامة لـ"
    }
    legal = {
        "يجب": "يلتزم الطرف الثاني بـ",
        "المقاول": "يتعين على المقاول",
        "رب العمل": "صاحب العمل تعاقدياً",
        "من أجل": "بموجب الالتزامات التعاقدية"
    }
    economic = {
        "يجب": "يقتضي التحليل الاقتصادي",
        "المقاول": "الجهة الاقتصادية المنفذة",
        "رب العمل": "الجهة المستثمرة",
        "من أجل": "بهدف تحقيق الجدوى الاقتصادية لـ"
    }
    medical = {
        "يجب": "يُنصح سريرياً بـ",
        "المقاول": "الفريق الطبي المنفذ",
        "رب العمل": "المؤسسة الصحية المالكة",
        "من أجل": "للحفاظ على السلامة الصحية في"
    }
    scientific = {
        "يجب": "تُظهر الدراسة العلمية ضرورة",
        "المقاول": "الجهة البحثية المنفذة",
        "رب العمل": "الجهة الراعية للبحث",
        "من أجل": "من منطلق المنهجية العلمية لـ"
    }

    f_pol, f_leg, f_eco, f_med, f_sci = base, base, base, base, base
    for k, v in political.items(): f_pol = f_pol.replace(k, v)
    for k, v in legal.items(): f_leg = f_leg.replace(k, v)
    for k, v in economic.items(): f_eco = f_eco.replace(k, v)
    for k, v in medical.items(): f_med = f_med.replace(k, v)
    for k, v in scientific.items(): f_sci = f_sci.replace(k, v)

    return f_pol, f_leg, f_eco, f_med, f_sci, base

# ── Session State for Swap ───────────────────────────────────────────────────
if "src_lang" not in st.session_state:
    st.session_state.src_lang = "English"
if "tgt_lang" not in st.session_state:
    st.session_state.tgt_lang = "العربية"
if "trigger_translate" not in st.session_state:
    st.session_state.trigger_translate = False
if "last_text" not in st.session_state:
    st.session_state.last_text = ""

def swap_languages():
    st.session_state.src_lang, st.session_state.tgt_lang = st.session_state.tgt_lang, st.session_state.src_lang

def on_text_change():
    """Callback when user presses Enter in text_area."""
    st.session_state.trigger_translate = True

# ── UI: Language Selectors + Swap ───────────────────────────────────────────
lang_list = list(languages_dict.keys())

col1, col2, col3 = st.columns([4, 1, 4])
with col1:
    src = st.selectbox("FROM", lang_list, index=lang_list.index(st.session_state.src_lang), key="src_lang")
with col2:
    st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)
    st.button("⇄", on_click=swap_languages, help="تبديل اللغات", key="swap_btn")
with col3:
    tgt = st.selectbox("INTO", lang_list, index=lang_list.index(st.session_state.tgt_lang), key="tgt_lang")

fl = languages_dict[src]
tl = languages_dict[tgt]

# ── Text Input ──────────────────────────────────────────────────────────────
text_input = st.text_area(
    "",
    placeholder="اكتب أو الصق النص هنا — تقارير هندسية، بنود تعاقدية، مراسلات رسمية، نصوص سياسية، تقارير طبية...",
    height=160,
    key="text_input",
    on_change=on_text_change
)

btn = st.button("🌐  Translate", use_container_width=True, type="primary", key="translate_btn")

st.divider()

# ── Translation Logic ─────────────────────────────────────────────────────────
should_translate = (btn or st.session_state.trigger_translate) and text_input.strip()

if should_translate:
    st.session_state.trigger_translate = False
    text = text_input.strip()
    st.session_state.last_text = text

    # API status badge
    if DEEPL_API_KEY:
        st.markdown('<span class="api-badge api-deepl">⚡ DeepL API Active</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="api-badge api-google">● Google Translate (Free)</span>', unsafe_allow_html=True)
        st.info("💡 **Tip:** أضف مفتاح DeepL API في `secrets.toml` (DEEPL_API_KEY) لدقة أعلى. احصل على مفتاح مجاني من [deepl.com/pro-api](https://www.deepl.com/pro-api)")

    sug = check_do_you_mean(text)
    if sug:
        fmt = ", ".join([f"<strong>{s.title()}</strong>" for s in sug])
        st.markdown(f'<div class="dym-box">💡 <b>Did you mean:</b> {fmt}?</div>', unsafe_allow_html=True)

    with st.spinner("Translating with best available engine..."):
        is_single = len(text.split()) == 1

        base, engine_used = fetch_ai_translation(text, fl, tl)

        if is_single:
            st.markdown(f"### 🗄️ Contextual Lexicon: `{text}`")
            st.markdown(f"""
| Context | Meaning |
|:---|:---|
| 🏛️ Political | {base} |
| ⚖️ Legal / FIDIC | Binding contractual clause |
| 📈 Economic | Financial / market context |
| 🏥 Medical | Clinical / health context |
| 🔬 Scientific | Research / academic context |
| 💬 General | {base} |
""")
        else:
            f_pol, f_leg, f_eco, f_med, f_sci, f_gen = build_formulas(base, tl)

            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown(f'<div class="rcard rcard-pol"><div class="rlabel rlabel-pol">🏛 POLITICAL</div><div class="rtext">{f_pol}</div></div>', unsafe_allow_html=True)
            with c2:
                st.markdown(f'<div class="rcard rcard-leg"><div class="rlabel rlabel-leg">⚖ LEGAL</div><div class="rtext">{f_leg}</div></div>', unsafe_allow_html=True)
            with c3:
                st.markdown(f'<div class="rcard rcard-eco"><div class="rlabel rlabel-eco">📈 ECONOMIC</div><div class="rtext">{f_eco}</div></div>', unsafe_allow_html=True)

            c4, c5, c6 = st.columns(3)
            with c4:
                st.markdown(f'<div class="rcard rcard-med"><div class="rlabel rlabel-med">🏥 MEDICAL</div><div class="rtext">{f_med}</div></div>', unsafe_allow_html=True)
            with c5:
                st.markdown(f'<div class="rcard rcard-sci"><div class="rlabel rlabel-sci">🔬 SCIENTIFIC</div><div class="rtext">{f_sci}</div></div>', unsafe_allow_html=True)
            with c6:
                st.markdown(f'<div class="rcard rcard-gen"><div class="rlabel rlabel-gen">💬 GENERAL</div><div class="rtext">{f_gen}</div></div>', unsafe_allow_html=True)

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
