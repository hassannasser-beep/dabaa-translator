import streamlit as st
import requests
import re

st.set_page_config(page_title="HASSAN NASSER", page_icon="🏗️", layout="wide")

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; max-width: 1100px; }

/* HERO */
.hero { background:#1a1a2e; border-radius:14px; padding:2rem 2rem 1.5rem; margin-bottom:1.5rem; }
.hero-name { font-size:30px; font-weight:600; color:#fff; letter-spacing:-0.5px; }
.hero-name span { color:#5DCAA5; }
.hero-sub { font-size:13px; color:rgba(255,255,255,.45); margin-top:6px; letter-spacing:.04em; }
.hero-pills { display:flex; gap:8px; flex-wrap:wrap; margin-top:12px; }
.pill { display:inline-block; border-radius:20px; padding:4px 12px; font-size:11px; font-weight:500; letter-spacing:.04em; }
.pill-active { background:#5DCAA5; color:#04342C; }
.pill-muted { background:rgba(255,255,255,.07); border:.5px solid rgba(255,255,255,.12); color:rgba(255,255,255,.5); }

/* CARDS */
.rcard { border-radius:12px; padding:1.1rem 1.3rem; border:.5px solid #e5e7eb; background:#fff; height:100%; }
.rcard-eng { border-top:3px solid #1D9E75; }
.rcard-leg { border-top:3px solid #534AB7; }
.rcard-sci { border-top:3px solid #0891b2; }
.rcard-med { border-top:3px solid #dc2626; }
.rcard-pol { border-top:3px solid #7c3aed; }
.rcard-dir { border-top:3px solid #D85A30; }
.rcard-slg { border-top:3px solid #ca8a04; }
.rlabel { font-size:10px; font-weight:700; letter-spacing:.09em; margin-bottom:10px; }
.rlabel-e { color:#085041; } .rlabel-l { color:#3C3489; } .rlabel-s { color:#0e7490; }
.rlabel-m { color:#991b1b; } .rlabel-p { color:#5b21b6; } .rlabel-d { color:#712B13; } .rlabel-g { color:#92400e; }
.rtext { font-size:14px; line-height:1.8; color:#1f2937; direction:auto; }

/* TONE BOX */
.tone-wrap { border-radius:10px; padding:12px 16px; margin-bottom:14px; display:flex; align-items:flex-start; gap:12px; }
.tone-political { background:#f5f3ff; border:1px solid #7c3aed; }
.tone-legal      { background:#eef2ff; border:1px solid #4f46e5; }
.tone-medical    { background:#fff1f2; border:1px solid #dc2626; }
.tone-scientific { background:#f0fdfa; border:1px solid #0d9488; }
.tone-engineering{ background:#f0fdf4; border:1px solid #1D9E75; }
.tone-casual     { background:#fefce8; border:1px solid #ca8a04; }
.tone-neutral    { background:#f9fafb; border:1px solid #9ca3af; }
.tone-icon { font-size:26px; }
.tone-content {}
.tone-title { font-size:11px; font-weight:700; letter-spacing:.08em; margin-bottom:3px; }
.tone-desc  { font-size:13px; color:#374151; }

/* PROOFREAD */
.proof-ok   { border-radius:8px; padding:9px 14px; background:#f0fdf4; border:1px solid #86efac; font-size:13px; color:#166534; margin-top:10px; }
.proof-warn { border-radius:8px; padding:9px 14px; background:#fef2f2; border:1px solid #fca5a5; font-size:13px; color:#991b1b; margin-top:6px; }

/* SLANG */
.slang-wrap  { border-radius:12px; overflow:hidden; border:.5px solid #9FE1CB; margin-top:1rem; }
.slang-head  { background:#085041; padding:12px 16px; }
.slang-head-txt { font-size:11px; font-weight:600; color:#9FE1CB; letter-spacing:.06em; }
.slang-table { width:100%; border-collapse:collapse; background:#fff; }
.slang-table th { font-size:10px; font-weight:600; color:#6b7280; letter-spacing:.06em; padding:8px 14px; border-bottom:.5px solid #e5e7eb; text-align:left; }
.slang-table td { font-size:13px; padding:10px 14px; border-bottom:.5px solid #f3f4f6; vertical-align:top; }
.slang-table tr:last-child td { border-bottom:none; }
.term-cell { font-weight:600; color:#085041; }
.site-cell { font-weight:500; color:#3C3489; }

/* DYM */
.dym-box { background:#FAEEDA; border-left:3px solid #BA7517; border-radius:0 8px 8px 0; padding:10px 14px; font-size:13px; color:#412402; margin-bottom:1rem; }

/* BUTTONS */
div.stButton > button {
    background:#1a1a2e !important; color:white !important; border:none !important;
    border-radius:8px !important; font-weight:600 !important;
    font-size:15px !important; padding:.65rem 2rem !important; width:100% !important;
}
div.stButton > button:hover { background:#0f0f1e !important; }

/* SWAP BUTTON — target by key */
div[data-testid="column"]:nth-child(2) div.stButton > button {
    background:#5DCAA5 !important; color:#04342C !important;
    font-size:20px !important; padding:.5rem !important;
    border-radius:50% !important; width:48px !important;
    height:48px !important; min-width:0 !important;
}

textarea { border-radius:8px !important; border:.5px solid #d1d5db !important; font-size:14px !important; }
</style>
""", unsafe_allow_html=True)

# ── HERO ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-name">HASSAN <span>NASSER</span></div>
  <div class="hero-sub">ENGINEERING · LEGAL · SCIENTIFIC · MEDICAL · POLITICAL TRANSLATIONS</div>
  <div class="hero-pills">
    <span class="pill pill-active">Smart Translator</span>
    <span class="pill pill-muted">Tone Analyzer</span>
    <span class="pill pill-muted">Proofreader</span>
    <span class="pill pill-muted">7 Styles</span>
    <span class="pill pill-muted">Site Slang</span>
    <span class="pill pill-muted">Microphone</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── DATA ───────────────────────────────────────────────────────────────────────
LANGUAGES = {
    "العربية":"ar","English":"en","Русский":"ru","中文":"zh",
    "Deutsch":"de","Español":"es","Português":"pt","한국어":"ko"
}
LANG_LIST = list(LANGUAGES.keys())

SLANG_DB = {
    "slab":              {"academic":"بلاطة",                  "slang":"سقف / فرش خرساني",         "desc":"الأسقف والمسطحات الخرسانية المسلحة."},
    "lean concrete":     {"academic":"خرسانة عجيفة",           "slang":"خرسانة نظافة",              "desc":"طبقة خرسانية غير مسلحة أسفل القواعد."},
    "shop drawings":     {"academic":"رسومات تنفيذية",         "slang":"الرسومات التنفيذية للموقع", "desc":"المخططات التفصيلية للتنفيذ الفعلي."},
    "as-built drawings": {"academic":"رسومات الواقع الفعلي",   "slang":"مخططات كما نُفِّذ",         "desc":"الرسومات النهائية بعد التنفيذ."},
    "bill of quantities":{"academic":"قائمة الكميات",          "slang":"جدول الكميات BOQ",          "desc":"الوثيقة التعاقدية لتسعير المشروع."},
    "shuttering":        {"academic":"قالب الصب",              "slang":"الشدّة الخشبية / الطوبار",  "desc":"الهيكل المؤقت لصب الخرسانة."},
    "scaffolding":       {"academic":"سقالات",                 "slang":"السقالات الإنشائية",        "desc":"الهياكل المعدنية للعمل على الارتفاعات."},
    "curing":            {"academic":"معالجة الخرسانة",        "slang":"تعتيق الخرسانة بالمياه",   "desc":"رش الخرسانة بعد الصب لاكتساب المقاومة."},
    "honeycombing":      {"academic":"تجاويف خرسانية",         "slang":"تعشيش الخرسانة",           "desc":"فراغات حصوية تظهر بعد فك الشدّة."},
    "kick-off meeting":  {"academic":"اجتماع الانطلاق",        "slang":"الاجتماع التحضيري",         "desc":"أول اجتماع رسمي للمالك والاستشاري والمقاول."},
    "variation order":   {"academic":"أمر تغيير",              "slang":"ملحق تعاقدي (VO)",          "desc":"أمر رسمي لتعديل بند خارج نطاق التعاقد."},
    "rebar":             {"academic":"حديد التسليح",           "slang":"الحديد / قضبان الحديد",     "desc":"قضبان الفولاذ في تسليح الخرسانة."},
    "subcontractor":     {"academic":"مقاول من الباطن",        "slang":"سب-مقاول",                  "desc":"شركة متخصصة تتعاقد مع المقاول الرئيسي."},
    "punch list":        {"academic":"قائمة الأعمال الناقصة",  "slang":"البنش ليست",                "desc":"ملاحظات ما قبل التسليم النهائي."},
    "mobilization":      {"academic":"تجهيز الموقع",           "slang":"المبيليزيشن",               "desc":"مرحلة إعداد الموقع قبل البدء الفعلي."},
}

DOMAIN_KW = {
    "political":   ["parliament","government","election","minister","president","treaty","diplomacy",
                    "سياسي","حكومة","برلمان","وزير","رئيس","انتخاب","دبلوماسية","معاهدة","مجلس الأمن","حزب","سيادة"],
    "legal":       ["contract","clause","liability","jurisdiction","plaintiff","defendant","whereas","fidic",
                    "عقد","بند","مسؤولية","قانون","محكمة","دعوى","تعاقدي","تحكيم","ملزم","اتفاقية","شرط","التزام"],
    "medical":     ["patient","diagnosis","treatment","symptom","dosage","clinical","surgery","prescription",
                    "مريض","تشخيص","علاج","جرعة","جراحة","دواء","مستشفى","طبي","إكلينيكي","بروتوكول"],
    "scientific":  ["hypothesis","experiment","molecule","equation","laboratory","analysis","data","research",
                    "فرضية","تجربة","بيانات","تحليل","جزيء","معادلة","مختبر","بحث علمي","نتائج","إحصاء"],
    "engineering": ["concrete","steel","foundation","beam","column","drawing","specification","load","rebar",
                    "خرسانة","حديد","أساس","كمرة","عمود","مواصفات","إنشاء","مقاول","موقع","بناء","هندسة"],
    "casual":      ["hey","bro","gonna","wanna","lol","btw","يلا","اخوي","يعني","عادي","هههه","اوكي","حلو"],
}

TONE_META = {
    "political":   {"icon":"🏛️","label":"POLITICAL","cls":"tone-political",
                    "ar":"النص ذو طابع سياسي رسمي — يُترجم بلغة دبلوماسية مباشرة فقط، دون إعادة صياغة.",
                    "en":"Official political tone — translated directly with no reformulation."},
    "legal":       {"icon":"⚖️","label":"LEGAL / CONTRACTUAL","cls":"tone-legal",
                    "ar":"النص تعاقدي قانوني — يُعالَج بدقة قانونية ملزمة.",
                    "en":"Legal/contractual text — treated with binding legal precision."},
    "medical":     {"icon":"🏥","label":"MEDICAL / CLINICAL","cls":"tone-medical",
                    "ar":"النص طبي سريري — يُعالَج بمصطلحات طبية دقيقة.",
                    "en":"Medical/clinical text — treated with precise medical terminology."},
    "scientific":  {"icon":"🔬","label":"SCIENTIFIC / ACADEMIC","cls":"tone-scientific",
                    "ar":"النص علمي أكاديمي — يُعالَج بصياغة بحثية محكمة.",
                    "en":"Scientific/academic text — treated with rigorous academic phrasing."},
    "engineering": {"icon":"🏗️","label":"ENGINEERING / TECHNICAL","cls":"tone-engineering",
                    "ar":"النص هندسي تقني — يُعالَج بالمصطلحات الهندسية المعيارية.",
                    "en":"Engineering/technical text — treated with standard engineering terminology."},
    "casual":      {"icon":"💬","label":"CASUAL / COLLOQUIAL","cls":"tone-casual",
                    "ar":"النص عامي غير رسمي — يُعالَج بأسلوب محادثة طبيعي.",
                    "en":"Casual/colloquial text — treated with natural conversational style."},
    "neutral":     {"icon":"📄","label":"GENERAL / NEUTRAL","cls":"tone-neutral",
                    "ar":"النص عام محايد — يُعالَج بلغة واضحة ومباشرة.",
                    "en":"General/neutral text — treated with clear direct language."},
}

# ── HELPERS ────────────────────────────────────────────────────────────────────
def translate(text, src, tgt):
    try:
        r = requests.get(
            "https://translate.googleapis.com/translate_a/single",
            params={"client":"gtx","sl":src,"tl":tgt,"dt":"t","q":text.strip()},
            timeout=10
        ).json()
        return "".join(p[0] for p in r[0] if p[0])
    except Exception as e:
        return f"[خطأ في الترجمة: {e}]"

def levenshtein(a, b):
    if len(a) < len(b): return levenshtein(b, a)
    if not b: return len(a)
    prev = range(len(b)+1)
    for i, ca in enumerate(a):
        cur = [i+1]
        for j, cb in enumerate(b):
            cur.append(min(prev[j+1]+1, cur[j]+1, prev[j]+(ca!=cb)))
        prev = cur
    return prev[-1]

def did_you_mean(text):
    words = re.sub(r'[,.]',' ',text.lower()).split()
    out = []
    for w in words:
        if len(w) < 3 or w in SLANG_DB: continue
        for k in SLANG_DB:
            d = levenshtein(w, k)
            if d == 1 or (len(k) > 6 and d == 2):
                if k not in out: out.append(k)
    return out

def detect_slang(text):
    tl = text.lower()
    return [{"term":k.title(),"academic":v["academic"],"slang":v["slang"],"desc":v["desc"]}
            for k,v in SLANG_DB.items() if k in tl]

def detect_domain(text):
    tl = text.lower()
    scores = {d: sum(1 for kw in kws if kw in tl) for d, kws in DOMAIN_KW.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "neutral"

def proofread(original, translated, src_lang, tgt_lang):
    issues = []
    ow = len(original.split()); tw = len(translated.split())
    if ow > 0:
        ratio = tw / ow
        if ratio < 0.25: issues.append("⚠️ الترجمة قصيرة جداً — قد تكون هناك أجزاء محذوفة.")
        if ratio > 5:    issues.append("⚠️ الترجمة طويلة بشكل غير متوقع — تحقق من التكرار.")
    if src_lang == "ar" and tgt_lang == "en":
        if sum(1 for c in translated if '\u0600'<=c<='\u06FF') > 5:
            issues.append("⚠️ يوجد نص عربي لم يُترجم في الناتج الإنجليزي.")
    if src_lang == "en" and tgt_lang == "ar":
        if sum(1 for c in translated if c.isalpha() and ord(c)<128) > 25:
            issues.append("⚠️ يوجد نص إنجليزي لم يُترجم في الناتج العربي.")
    if not translated.strip():
        issues.append("❌ الترجمة فارغة.")
    words = translated.split()
    for i in range(len(words)-2):
        if words[i]==words[i+1]==words[i+2] and len(words[i])>2:
            issues.append(f"⚠️ تكرار غير طبيعي للكلمة: «{words[i]}»")
            break
    return issues

def build_styles(base, tgt_lang, domain):
    """Return dict of 7 styled translations."""
    styles = {}

    if tgt_lang == "ar":
        # Engineering
        eng = base
        for old, new in [("يجب","يُشترط هندسياً"),("رب العمل","المالك (Employer)"),
                          ("المهندس","استشاري المشروع"),("يُنفَّذ","يُنجَز وفق المواصفات الفنية")]:
            eng = eng.replace(old, new)
        # Legal
        leg = base
        for old, new in [("يجب","يلتزم الطرف الثاني بموجب هذا العقد بـ"),
                          ("المقاول","المقاول (وفق تعريف المادة الأولى)"),
                          ("رب العمل","صاحب العمل تعاقدياً"),
                          ("يُسمح","يُجيز البند التعاقدي")]:
            leg = leg.replace(old, new)
        # Scientific
        sci = base
        for old, new in [("يجب","يُستوجب علمياً"),("نتيجة","المحصلة التجريبية"),
                          ("دراسة","البحث التحليلي"),("بيانات","البيانات الإحصائية")]:
            sci = sci.replace(old, new)
        # Medical
        med = base
        for old, new in [("مريض","المريض (Patient)"),("علاج","البروتوكول العلاجي"),
                          ("دواء","الدواء (Medication)"),("جرعة","الجرعة الدوائية (Dosage)")]:
            med = med.replace(old, new)
        # Political — direct, no change
        pol = base
        # Direct
        direct = base
        # Casual — simplified
        casual = base

    else:
        eng    = f"[Engineering] {base}"
        leg    = f"Pursuant to the contractual obligations herein, {base[:1].lower()+base[1:]}"
        sci    = f"[Scientific context] {base}"
        med    = f"[Clinical notation] {base}"
        pol    = base   # political = direct
        direct = base
        casual = base

    styles["engineering"] = eng
    styles["legal"]       = leg
    styles["scientific"]  = sci
    styles["medical"]     = med
    styles["political"]   = pol
    styles["direct"]      = direct
    styles["casual"]      = casual
    return styles

# ── MICROPHONE COMPONENT (streamlit-audiorecorder) ─────────────────────────────
def mic_section():
    st.markdown("""
    <div style="background:#1a1a2e;border-radius:10px;padding:14px 16px;margin-bottom:6px;">
      <div style="font-size:11px;font-weight:700;color:#5DCAA5;letter-spacing:.08em;margin-bottom:8px;">
        🎤 VOICE INPUT — الإدخال الصوتي
      </div>
      <div style="font-size:12px;color:rgba(255,255,255,.5);">
        اضغط على زر التسجيل أدناه ← ثم تكلّم ← ثم أوقف التسجيل.
        سيُنسخ النص تلقائياً إلى خانة الترجمة.
      </div>
    </div>
    """, unsafe_allow_html=True)
    try:
        from audiorecorder import audiorecorder
        import io, wave, base64
        audio = audiorecorder("🎤 ابدأ التسجيل", "⏹ إيقاف")
        if len(audio) > 0:
            st.audio(audio.export().read(), format="audio/wav")
            st.info("✅ تم تسجيل الصوت. للترجمة الصوتية الكاملة أضف مفتاح OpenAI Whisper في الإعدادات.", icon="ℹ️")
            # Store in session
            st.session_state["mic_audio"] = audio
    except ImportError:
        st.warning("📦 لتفعيل الميكروفون أضف `streamlit-audiorecorder` إلى requirements.txt", icon="🎤")

# ── SESSION STATE ──────────────────────────────────────────────────────────────
if "src_lang" not in st.session_state: st.session_state.src_lang = "English"
if "tgt_lang" not in st.session_state: st.session_state.tgt_lang = "العربية"
if "text_val"  not in st.session_state: st.session_state.text_val = ""

# ── LANGUAGE BAR ───────────────────────────────────────────────────────────────
col_s, col_sw, col_t = st.columns([5,1,5])

with col_s:
    src_idx = LANG_LIST.index(st.session_state.src_lang) if st.session_state.src_lang in LANG_LIST else 1
    src = st.selectbox("FROM / من", LANG_LIST, index=src_idx, key="src_sel")

with col_sw:
    st.markdown("<div style='height:26px'></div>", unsafe_allow_html=True)
    if st.button("⇄", key="swap_btn", help="بدّل اللغتين"):
        st.session_state.src_lang, st.session_state.tgt_lang = \
            st.session_state.tgt_lang, st.session_state.src_lang
        st.rerun()

with col_t:
    available = [l for l in LANG_LIST if l != src]
    cur_tgt = st.session_state.tgt_lang if st.session_state.tgt_lang in available else available[0]
    tgt = st.selectbox("INTO / إلى", available,
                        index=available.index(cur_tgt), key="tgt_sel")

# Update session
st.session_state.src_lang = src
st.session_state.tgt_lang = tgt
fl = LANGUAGES[src]
tl = LANGUAGES[tgt]

# ── MICROPHONE ─────────────────────────────────────────────────────────────────
with st.expander("🎤 الإدخال الصوتي — Voice Input"):
    mic_section()

# ── TEXT INPUT ─────────────────────────────────────────────────────────────────
text_input = st.text_area(
    "",
    value=st.session_state.get("text_val",""),
    placeholder="اكتب النص هنا... (اضغط Ctrl+Enter أو زر الترجمة)\nتقارير هندسية · بنود قانونية · تقارير طبية · وثائق سياسية",
    height=145,
    key="main_text"
)

# ── TRANSLATE BUTTON ───────────────────────────────────────────────────────────
do_translate = st.button("🌐  ترجم — Translate", use_container_width=True, key="translate_btn")

st.divider()

# ── MAIN LOGIC ─────────────────────────────────────────────────────────────────
if do_translate:
    if not text_input.strip():
        st.warning("⚠️ الرجاء إدخال نص للترجمة.")
        st.stop()

    text = text_input.strip()

    # 1 — Did You Mean
    sug = did_you_mean(text)
    if sug:
        fmt = "، ".join([f"<strong>{s.title()}</strong>" for s in sug])
        st.markdown(f'<div class="dym-box">💡 <b>هل تقصد / Did you mean:</b> {fmt}?</div>',
                    unsafe_allow_html=True)

    # 2 — Domain + Tone
    domain = detect_domain(text)
    tone   = TONE_META[domain]
    st.markdown(f"""
    <div class="tone-wrap {tone['cls']}">
      <div class="tone-icon">{tone['icon']}</div>
      <div class="tone-content">
        <div class="tone-title">{tone['label']} — تحليل النبرة والسياق</div>
        <div class="tone-desc">🇸🇦 {tone['ar']}<br>🇬🇧 {tone['en']}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # 3 — Translate
    with st.spinner("🔄 جارٍ الترجمة..."):
        base = translate(text, fl, tl)

    # 4 — Proofreading
    issues = proofread(text, base, fl, tl)
    if issues:
        for iss in issues:
            st.markdown(f'<div class="proof-warn">{iss}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="proof-ok">✅ الترجمة اجتازت فحص الجودة — No proofreading issues detected.</div>',
                    unsafe_allow_html=True)

    # 5 — Styles
    is_word = len(text.split()) <= 2

    if domain == "political":
        # Political only = direct
        st.markdown(f"""
        <div class="rcard rcard-pol" style="margin-top:14px;">
          <div class="rlabel rlabel-p">🏛️ POLITICAL — DIRECT (ترجمة مباشرة فقط)</div>
          <div class="rtext">{base}</div>
        </div>""", unsafe_allow_html=True)

    elif is_word:
        st.markdown(f"#### 🗄️ Contextual Lexicon: `{text}`")
        styles = build_styles(base, tl, domain)
        rows = "".join([
            f"<tr><td>🏗️ Engineering</td><td>{styles['engineering']}</td></tr>",
            f"<tr><td>⚖️ Legal</td><td>{styles['legal']}</td></tr>",
            f"<tr><td>🔬 Scientific</td><td>{styles['scientific']}</td></tr>",
            f"<tr><td>🏥 Medical</td><td>{styles['medical']}</td></tr>",
            f"<tr><td>🎯 Direct</td><td>{styles['direct']}</td></tr>",
            f"<tr><td>💬 Casual</td><td>{styles['casual']}</td></tr>",
        ])
        st.markdown(f"""
        <table style="width:100%;border-collapse:collapse;font-size:13px;margin-top:10px;">
          <thead><tr style="background:#f3f4f6;">
            <th style="padding:8px 12px;text-align:left;font-size:11px;letter-spacing:.06em;color:#6b7280;">CONTEXT</th>
            <th style="padding:8px 12px;text-align:left;font-size:11px;letter-spacing:.06em;color:#6b7280;">TRANSLATION</th>
          </tr></thead>
          <tbody>{rows}</tbody>
        </table>""", unsafe_allow_html=True)

    else:
        styles = build_styles(base, tl, domain)

        # Domain priority order
        ORDER = {
            "engineering": ["engineering","legal","direct","scientific","medical","casual"],
            "legal":       ["legal","engineering","direct","scientific","medical","casual"],
            "scientific":  ["scientific","medical","direct","engineering","legal","casual"],
            "medical":     ["medical","scientific","direct","engineering","legal","casual"],
            "casual":      ["casual","direct","engineering","legal","scientific","medical"],
            "neutral":     ["direct","engineering","legal","scientific","medical","casual"],
        }
        CARD_META = {
            "engineering": ("rcard-eng","rlabel-e","🏗️ ENGINEERING"),
            "legal":       ("rcard-leg","rlabel-l","⚖️ LEGAL"),
            "scientific":  ("rcard-sci","rlabel-s","🔬 SCIENTIFIC"),
            "medical":     ("rcard-med","rlabel-m","🏥 MEDICAL"),
            "political":   ("rcard-pol","rlabel-p","🏛️ POLITICAL"),
            "direct":      ("rcard-dir","rlabel-d","🎯 DIRECT"),
            "casual":      ("rcard-slg","rlabel-g","💬 CASUAL"),
        }
        order = ORDER.get(domain, ORDER["neutral"])

        # Top 3
        st.markdown("<div style='margin-top:14px;'></div>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        for col, key in zip([c1,c2,c3], order[:3]):
            card_cls, lbl_cls, label = CARD_META[key]
            with col:
                st.markdown(f"""
                <div class="rcard {card_cls}">
                  <div class="rlabel {lbl_cls}">{label}</div>
                  <div class="rtext">{styles[key]}</div>
                </div>""", unsafe_allow_html=True)

        # Bottom 3
        with st.expander("📖 المزيد من الصياغات — More Styles"):
            c4, c5, c6 = st.columns(3)
            for col, key in zip([c4,c5,c6], order[3:]):
                card_cls, lbl_cls, label = CARD_META[key]
                with col:
                    st.markdown(f"""
                    <div class="rcard {card_cls}">
                      <div class="rlabel {lbl_cls}">{label}</div>
                      <div class="rtext">{styles[key]}</div>
                    </div>""", unsafe_allow_html=True)

    # 6 — Site Slang
    detected = detect_slang(text)
    if detected:
        rows = "".join([f"""
        <tr>
          <td class="term-cell">{d['term']}</td>
          <td>{d['academic']}</td>
          <td class="site-cell">{d['slang']}</td>
          <td style="font-size:12px;color:#6b7280;">{d['desc']}</td>
        </tr>""" for d in detected])
        st.markdown(f"""
<div class="slang-wrap">
  <div class="slang-head"><span class="slang-head-txt">
    🔍 SITE SLANG DETECTOR — {len(detected)} TERM(S) FOUND
  </span></div>
  <table class="slang-table">
    <thead><tr>
      <th>TERM</th><th>STANDARD</th><th>ON-SITE</th><th>NOTE</th>
    </tr></thead>
    <tbody>{rows}</tbody>
  </table>
</div>""", unsafe_allow_html=True)
