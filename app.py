from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import anthropic
import re
import json

# ── 1. Page Config ──────────────────────────────────────────────────────────
st.set_page_config(page_title="HASSAN NASSER", page_icon="🏗️", layout="wide")

# ── 2. CSS ──────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; max-width: 1060px; }

/* Hero */
.hero { background: #1a1a2e; border-radius: 14px; padding: 2rem 2rem 1.5rem; margin-bottom: 1.5rem; }
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

/* Context cards */
.rcard { border-radius: 12px; padding: 1.5rem; border: 0.5px solid rgba(128,128,128,0.2); margin-top: 1rem; }
.rcard-eng  { border-top: 4px solid #1D9E75; }
.rcard-leg  { border-top: 4px solid #534AB7; }
.rcard-dir  { border-top: 4px solid #D85A30; }
.rcard-pol  { border-top: 4px solid #c0392b; }
.rcard-eco  { border-top: 4px solid #e67e22; }
.rcard-med  { border-top: 4px solid #2980b9; }
.rcard-lit  { border-top: 4px solid #8e44ad; }
.rcard-sci  { border-top: 4px solid #27ae60; }
.rlabel { font-size: 11px; font-weight: 600; letter-spacing: 0.08em; margin-bottom: 10px; }
.rlabel-e { color: #1D9E75; }
.rlabel-l { color: #534AB7; }
.rlabel-g { color: #D85A30; }
.rlabel-pol { color: #c0392b; }
.rlabel-eco { color: #e67e22; }
.rlabel-med { color: #2980b9; }
.rlabel-lit { color: #8e44ad; }
.rlabel-sci { color: #27ae60; }
.rtext { font-size: 16px; line-height: 1.9; color: var(--text-color, #1f2937); direction: auto; }

/* Multi-context output */
.ctx-block { margin-bottom: 1rem; }
.ctx-separator { border: none; border-top: 1px dashed rgba(128,128,128,0.25); margin: 1rem 0; }

/* Slang table */
.slang-wrap { border-radius: 12px; overflow: hidden; border: 0.5px solid #9FE1CB; margin-top: 1.5rem; }
.slang-head { background: #085041; padding: 12px 16px; }
.slang-head-txt { font-size: 11px; font-weight: 600; color: #9FE1CB; letter-spacing: 0.06em; }
.slang-table { width: 100%; border-collapse: collapse; background: var(--background-color, #fff); }
.slang-table th { font-size: 10px; font-weight: 600; color: #6b7280; letter-spacing: 0.06em; padding: 8px 14px; border-bottom: 0.5px solid rgba(128,128,128,0.2); text-align: left; }
.slang-table td { font-size: 13px; padding: 10px 14px; border-bottom: 0.5px solid rgba(128,128,128,0.1); vertical-align: top; color: var(--text-color, #1f2937); }
.slang-table tr:last-child td { border-bottom: none; }
.term-cell { font-weight: 600; color: #1D9E75; }
.site-cell { font-weight: 500; color: #534AB7; }

/* Did you mean */
.dym-box { background: #FAEEDA; border-left: 3px solid #BA7517; border-radius: 0 8px 8px 0; padding: 10px 14px; font-size: 13px; color: #412402; margin-bottom: 1rem; }
.dym-btn-wrap { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 8px; }
.dym-btn { display: inline-block; cursor: pointer; background: #fff3dc; border: 1px solid #BA7517; border-radius: 20px; padding: 4px 14px; font-size: 12px; font-weight: 600; color: #7a4800; }

/* Buttons */
div.stButton > button {
    background: #1a1a2e !important; color: white !important; border: none !important;
    border-radius: 8px !important; font-weight: 500 !important;
    font-size: 15px !important; padding: 0.65rem 2rem !important; width: 100% !important;
}
div.stButton > button:hover { background: #0f0f1e !important; }
.swap-btn > button {
    background: rgba(93,202,165,0.12) !important; color: #1D9E75 !important;
    border: 1px solid #5DCAA5 !important; border-radius: 50% !important;
    font-size: 20px !important; padding: 0.4rem 0.7rem !important; width: auto !important;
}
textarea { border-radius: 8px !important; border: 0.5px solid #d1d5db !important; font-size: 14px !important; }
</style>
""", unsafe_allow_html=True)

# ── 3. Hero ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-name">HASSAN <span>NASSER</span></div>
  <div class="hero-sub">ENGINEERING · LEGAL · CONTRACTUAL · SCIENTIFIC · MEDICAL · LITERARY TRANSLATIONS</div>
  <div class="hero-pills">
    <span class="pill pill-active">Claude AI Translator</span>
    <span class="pill pill-muted">Context Classifier</span>
    <span class="pill pill-muted">Site Slang Detector</span>
    <span class="pill pill-muted">8 Domains</span>
  </div>
  <div class="lang-bar">
    <span class="ldot"></span><span class="ldot"></span><span class="ldot"></span>
    <span class="ldot"></span><span class="ldot"></span><span class="ldot"></span>
    <span class="ldot"></span><span class="ldot"></span>
    <span class="lang-bar-txt">8 languages · 8 specialist contexts</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── 4. Data ──────────────────────────────────────────────────────────────────
LANGUAGES = {
    "العربية": "ar", "English": "en", "Русский": "ru", "中文": "zh",
    "Deutsch": "de", "Español": "es", "Português": "pt", "한국어": "ko"
}
LANG_NAMES = list(LANGUAGES.keys())

# Session state defaults
if "src_idx" not in st.session_state: st.session_state.src_idx = 1   # English
if "tgt_idx" not in st.session_state: st.session_state.tgt_idx = 0   # Arabic
if "input_text" not in st.session_state: st.session_state.input_text = ""
if "dym_chosen" not in st.session_state: st.session_state.dym_chosen = None

SITE_SLANG_DB = {
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

CONTEXT_CONFIG = {
    "engineering":  {"icon": "🏗️", "label": "ENGINEERING / TECHNICAL",    "card": "rcard-eng",  "lbl": "rlabel-e"},
    "legal":        {"icon": "⚖️", "label": "LEGAL / CONTRACTUAL (FIDIC)", "card": "rcard-leg",  "lbl": "rlabel-l"},
    "political":    {"icon": "🏛️", "label": "POLITICAL / DIPLOMATIC",      "card": "rcard-pol",  "lbl": "rlabel-pol"},
    "economic":     {"icon": "📊", "label": "ECONOMIC / FINANCIAL",        "card": "rcard-eco",  "lbl": "rlabel-eco"},
    "medical":      {"icon": "🩺", "label": "MEDICAL / CLINICAL",          "card": "rcard-med",  "lbl": "rlabel-med"},
    "literary":     {"icon": "📖", "label": "LITERARY / RHETORICAL",       "card": "rcard-lit",  "lbl": "rlabel-lit"},
    "scientific":   {"icon": "🔬", "label": "SCIENTIFIC / ACADEMIC",       "card": "rcard-sci",  "lbl": "rlabel-sci"},
    "general":      {"icon": "💬", "label": "DIRECT / GENERAL",            "card": "rcard-dir",  "lbl": "rlabel-g"},
}

# ── 5. Utilities ─────────────────────────────────────────────────────────────
def levenshtein(s1, s2):
    if len(s1) < len(s2): return levenshtein(s2, s1)
    if not s2: return len(s1)
    prev = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        cur = [i + 1]
        for j, c2 in enumerate(s2):
            cur.append(min(prev[j+1]+1, cur[j]+1, prev[j]+(c1!=c2)))
        prev = cur
    return prev[-1]

def check_do_you_mean(text):
    words = re.sub(r'[^a-zA-Z\s]', ' ', text).lower().split()
    suggestions = []
    for w in words:
        if len(w) < 3 or w in SITE_SLANG_DB: continue
        for k in SITE_SLANG_DB:
            d = levenshtein(w, k)
            if d == 1 or (len(k) > 6 and d == 2):
                if k not in suggestions: suggestions.append(k)
    return suggestions

def detect_site_slang(text):
    tl = text.lower()
    return [{"term": k.title(), **v} for k, v in SITE_SLANG_DB.items() if k in tl]

def claude_translate(text: str, src_lang: str, tgt_lang: str) -> dict:
    """
    Call Claude API. Returns dict:
    {
      "contexts": [
        {"type": "engineering"|"legal"|..., "translation": "..."},
        ...
      ],
      "is_single_word": bool
    }
    Only contexts actually detected are included; single-word always returns all relevant.
    """
    client = anthropic.Anthropic()   # reads ANTHROPIC_API_KEY from environment

    system_prompt = """You are an expert multi-domain translator specializing in 8 specialist fields:
engineering, legal/contractual, political/diplomatic, economic/financial, medical/clinical, literary/rhetorical, scientific/academic, and general.

When given a text, you must:
1. Detect which specialist contexts apply to this text (can be multiple).
2. Provide a translation for EACH applicable context, using the appropriate terminology and register for that domain.
3. If a single word, cover all 8 contexts.
4. If a sentence/paragraph, only include contexts that genuinely apply.

Respond ONLY with a valid JSON object like this:
{
  "is_single_word": true/false,
  "contexts": [
    {"type": "engineering", "translation": "..."},
    {"type": "legal", "translation": "..."},
    {"type": "medical", "translation": "..."}
  ]
}

Context type values: engineering, legal, political, economic, medical, literary, scientific, general
Do NOT include markdown, backticks, or any text outside the JSON."""

    user_msg = f"Translate from {src_lang} to {tgt_lang}:\n\n{text}"

    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=2000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_msg}]
    )

    raw = response.content[0].text.strip()
    # Strip any accidental markdown fences
    raw = re.sub(r'^```[a-z]*\n?', '', raw)
    raw = re.sub(r'\n?```$', '', raw)
    return json.loads(raw)

# ── 6. Language selector with swap ───────────────────────────────────────────
col_src, col_swap, col_tgt = st.columns([5, 1, 5])

with col_src:
    src_sel = st.selectbox(
        "FROM",
        LANG_NAMES,
        index=st.session_state.src_idx,
        key="src_select"
    )

with col_swap:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="swap-btn">', unsafe_allow_html=True)
    if st.button("⇄", key="swap_btn", help="Swap languages"):
        old_src = st.session_state.src_idx
        old_tgt = st.session_state.tgt_idx
        st.session_state.src_idx = old_tgt
        st.session_state.tgt_idx = old_src
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with col_tgt:
    # Build target options excluding src
    tgt_options = [l for l in LANG_NAMES if l != src_sel]
    tgt_sel = st.selectbox(
        "INTO",
        tgt_options,
        index=min(st.session_state.tgt_idx, len(tgt_options)-1),
        key="tgt_select"
    )

# Keep session indices in sync
st.session_state.src_idx = LANG_NAMES.index(src_sel)
tgt_full = tgt_sel  # already excludes src
src_code = LANGUAGES[src_sel]
tgt_code = LANGUAGES[tgt_full]

# ── 7. Text input — Enter = translate ────────────────────────────────────────
# We use a form so pressing Enter triggers submit
with st.form(key="translate_form", clear_on_submit=False):
    text_input = st.text_area(
        "",
        value=st.session_state.input_text,
        placeholder="اكتب أو الصق النص هنا — تقارير هندسية، بنود تعاقدية، مراسلات رسمية، نصوص طبية، أدبية...",
        height=140,
        key="text_area"
    )
    submitted = st.form_submit_button("🌐  Translate", use_container_width=True)

st.divider()

# ── 8. Did-you-mean suggestion click handler ──────────────────────────────────
# We detect via URL query params workaround — simpler: just show clickable st.buttons
text_to_translate = text_input.strip()

# ── 9. Processing ─────────────────────────────────────────────────────────────
if submitted and text_to_translate:
    st.session_state.input_text = text_to_translate

    # Did-you-mean
    suggestions = check_do_you_mean(text_to_translate)
    if suggestions:
        st.markdown('<div class="dym-box">💡 <b>هل تقصد؟ / Did you mean:</b><div class="dym-btn-wrap">', unsafe_allow_html=True)
        cols = st.columns(len(suggestions))
        for i, sug in enumerate(suggestions):
            with cols[i]:
                if st.button(f"🔍 {sug.title()}", key=f"dym_{sug}"):
                    st.session_state.input_text = sug
                    text_to_translate = sug
                    st.rerun()
        st.markdown('</div></div>', unsafe_allow_html=True)

    with st.spinner("Claude يحلّل السياق ويترجم…"):
        try:
            result = claude_translate(text_to_translate, src_sel, tgt_full)
        except Exception as e:
            st.error(f"خطأ في الاتصال بـ Claude API: {e}")
            st.stop()

    contexts = result.get("contexts", [])
    is_single = result.get("is_single_word", False)

    if is_single:
        st.markdown(f"### 🗄️ Contextual Lexicon: `{text_to_translate}`")
        rows = ""
        for ctx in contexts:
            cfg = CONTEXT_CONFIG.get(ctx["type"], CONTEXT_CONFIG["general"])
            rows += f"<tr><td>{cfg['icon']} {cfg['label']}</td><td style='direction:auto'>{ctx['translation']}</td></tr>"
        st.markdown(f"""
<table style='width:100%;border-collapse:collapse;font-size:14px;'>
  <thead><tr>
    <th style='text-align:left;padding:8px 14px;border-bottom:1px solid #e5e7eb;color:#6b7280;font-size:11px;letter-spacing:.06em'>CONTEXT</th>
    <th style='text-align:left;padding:8px 14px;border-bottom:1px solid #e5e7eb;color:#6b7280;font-size:11px;letter-spacing:.06em'>TRANSLATION</th>
  </tr></thead>
  <tbody>{rows}</tbody>
</table>""", unsafe_allow_html=True)
    else:
        for ctx in contexts:
            cfg = CONTEXT_CONFIG.get(ctx["type"], CONTEXT_CONFIG["general"])
            st.markdown(f"""
<div class="rcard {cfg['card']}">
  <div class="rlabel {cfg['lbl']}">{cfg['icon']} DETECTED CONTEXT: {cfg['label']}</div>
  <div class="rtext">{ctx['translation']}</div>
</div>""", unsafe_allow_html=True)

    # Slang detector (only on English source)
    if src_code == "en":
        detected = detect_site_slang(text_to_translate)
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

elif submitted:
    st.warning("⚠️ الرجاء إدخال نص أولاً.")
