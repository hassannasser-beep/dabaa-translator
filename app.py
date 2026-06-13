import streamlit as st
import requests
import os
import json
from pathlib import Path

st.set_page_config(page_title="HASSAN NASSER | Multi-Domain Translator", page_icon="🏗️", layout="wide")

# ═══════════════════════════════════════════════════════════════════════════════
#  CSS
# ═══════════════════════════════════════════════════════════════════════════════
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
.lang-bar-txt { font-size: 11px; color: rgba(255,255,255,0.35); margin-left: 4px; }

.rcard { border-radius: 12px; padding: 1.1rem 1.3rem; border: 0.5px solid #e5e7eb; background: #fff; transition: all 0.2s; }
.rcard-pol { border-top: 3px solid #E63946; }
.rcard-leg { border-top: 3px solid #534AB7; }
.rcard-eco { border-top: 3px solid #F4A261; }
.rcard-med { border-top: 3px solid #2A9D8F; }
.rcard-sci { border-top: 3px solid #264653; }
.rcard-eng { border-top: 3px solid #1D9E75; }
.rcard-mil { border-top: 3px solid #8B0000; }
.rcard-edu { border-top: 3px solid #F4D03F; }
.rcard-rel { border-top: 3px solid #6C3483; }
.rcard-spt { border-top: 3px solid #E67E22; }
.rcard-lit { border-top: 3px solid #D81B60; }
.rcard-it  { border-top: 3px solid #00ACC1; }
.rcard-env { border-top: 3px solid #43A047; }
.rcard-agr { border-top: 3px solid #795548; }
.rcard-med2 { border-top: 3px solid #5E35B1; }
.rcard-tour { border-top: 3px solid #00838F; }
.rcard-gen { border-top: 3px solid #6B7280; }
.rcard-priority { box-shadow: 0 0 0 2px rgba(93,202,165,0.5); background: #f6fffd; }

.rlabel { font-size: 10px; font-weight: 600; letter-spacing: 0.08em; margin-bottom: 8px; }
.rlabel-pol { color: #9B2226; }
.rlabel-leg { color: #3C3489; }
.rlabel-eco { color: #9C6644; }
.rlabel-med { color: #1B6B5E; }
.rlabel-sci { color: #1D3A4C; }
.rlabel-eng { color: #085041; }
.rlabel-mil { color: #8B0000; }
.rlabel-edu { color: #9A7D0A; }
.rlabel-rel { color: #6C3483; }
.rlabel-spt { color: #A04000; }
.rlabel-lit { color: #AD1457; }
.rlabel-it  { color: #006064; }
.rlabel-env { color: #1B5E20; }
.rlabel-agr { color: #4E342E; }
.rlabel-med2 { color: #4527A0; }
.rlabel-tour { color: #006064; }
.rlabel-gen { color: #4B5563; }
.rtext { font-size: 14px; line-height: 1.75; color: #1f2937; direction: auto; }

.detected-box { background: #E6F4F1; border-left: 3px solid #5DCAA5; border-radius: 0 8px 8px 0; padding: 10px 14px; font-size: 13px; color: #04342C; margin-bottom: 1rem; }

.api-badge {
    display: inline-block; padding: 2px 8px; border-radius: 4px;
    font-size: 10px; font-weight: 600; letter-spacing: 0.04em; margin-right: 4px;
}
.api-deepl { background: #0F2B46; color: #8ECAE6; }

.domain-badge {
    display: inline-block; padding: 3px 10px; border-radius: 20px;
    font-size: 11px; font-weight: 600; letter-spacing: 0.04em; margin-right: 6px; margin-bottom: 4px;
}
.db-pol { background: #E63946; color: white; }
.db-leg { background: #534AB7; color: white; }
.db-eco { background: #F4A261; color: #3E2723; }
.db-med { background: #2A9D8F; color: white; }
.db-sci { background: #264653; color: white; }
.db-eng { background: #1D9E75; color: white; }
.db-mil { background: #8B0000; color: white; }
.db-edu { background: #F4D03F; color: #3E2723; }
.db-rel { background: #6C3483; color: white; }
.db-spt { background: #E67E22; color: white; }
.db-lit { background: #D81B60; color: white; }
.db-it  { background: #00ACC1; color: white; }
.db-env { background: #43A047; color: white; }
.db-agr { background: #795548; color: white; }
.db-med2 { background: #5E35B1; color: white; }
.db-tour { background: #00838F; color: white; }
.db-gen { background: #6B7280; color: white; }

.meaning-diff { 
    background: #fff3e0; 
    border-radius: 4px; 
    padding: 2px 6px; 
    font-size: 12px; 
    color: #e65100; 
    font-weight: 600;
    display: inline-block;
    margin-top: 4px;
}
.all-meanings-header { font-size: 18px; font-weight: 600; color: #1a1a2e; margin: 1.5rem 0 1rem; }
.meaning-count { background: #5DCAA5; color: white; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: 600; margin-left: 8px; }
.domain-card { margin-bottom: 12px; }
.dict-stats { font-size: 11px; color: #6b7280; margin-top: 4px; }

.priority-badge {
    display: inline-block;
    background: #5DCAA5;
    color: white;
    padding: 1px 6px;
    border-radius: 4px;
    font-size: 10px;
    font-weight: 700;
    margin-left: 6px;
}

.api-key-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 12px;
    margin-bottom: 1rem;
}
.api-key-label {
    font-size: 12px;
    font-weight: 600;
    color: #1a1a2e;
    margin-bottom: 6px;
}

.error-box {
    background: #fee2e2;
    border-left: 3px solid #ef4444;
    border-radius: 0 8px 8px 0;
    padding: 12px 16px;
    font-size: 14px;
    color: #991b1b;
    margin-bottom: 1rem;
}

textarea { border-radius: 8px !important; border: 0.5px solid #d1d5db !important; font-size: 14px !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-name">HASSAN <span>NASSER</span></div>
    <div class="hero-sub">MULTI-DOMAIN SMART TRANSLATOR — POWERED BY DEEPL API</div>
    <div class="hero-pills">
        <span class="pill pill-active">Auto-Domain Detect</span>
        <span class="pill pill-muted">DeepL Precision</span>
        <span class="pill pill-muted">Smart Swap</span>
        <span class="pill pill-muted">Style Selector</span>
    </div>
    <div class="lang-bar">
        <span class="ldot"></span><span class="ldot"></span><span class="ldot"></span>
        <span class="ldot"></span><span class="ldot"></span><span class="ldot"></span>
        <span class="ldot"></span><span class="ldot"></span>
        <span class="lang-bar-txt">8 languages supported — DeepL API only</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════
languages_dict = {
    "Arabic": "ar", "English": "en", "Russian": "ru", "Chinese": "zh",
    "German": "de", "Spanish": "es", "Portuguese": "pt", "Korean": "ko"
}

DOMAINS = {
    "political":  {"emoji": "🏛️", "name_en": "Political",     "color": "#E63946"},
    "legal":      {"emoji": "⚖️", "name_en": "Legal",         "color": "#534AB7"},
    "economic":   {"emoji": "📈", "name_en": "Economic",      "color": "#F4A261"},
    "medical":    {"emoji": "🏥", "name_en": "Medical",       "color": "#2A9D8F"},
    "scientific": {"emoji": "🔬", "name_en": "Scientific",    "color": "#264653"},
    "engineering":{"emoji": "🏗️", "name_en": "Engineering",   "color": "#1D9E75"},
    "military":   {"emoji": "🎖️", "name_en": "Military",      "color": "#8B0000"},
    "educational":{"emoji": "📚", "name_en": "Educational",   "color": "#F4D03F"},
    "religious":  {"emoji": "🕌", "name_en": "Religious",     "color": "#6C3483"},
    "sports":     {"emoji": "⚽", "name_en": "Sports",        "color": "#E67E22"},
    "literary":   {"emoji": "📖", "name_en": "Literary",      "color": "#D81B60"},
    "it":         {"emoji": "💻", "name_en": "IT / Tech",     "color": "#00ACC1"},
    "environmental":{"emoji": "🌿", "name_en": "Environmental", "color": "#43A047"},
    "agricultural":{"emoji": "🌾", "name_en": "Agricultural",  "color": "#795548"},
    "media":      {"emoji": "📺", "name_en": "Media",         "color": "#5E35B1"},
    "tourism":    {"emoji": "✈️", "name_en": "Tourism",       "color": "#00838F"},
    "general":    {"emoji": "💬", "name_en": "General",       "color": "#6B7280"},
}

STYLE_OPTIONS = {
    "Auto-Detect": None,
    "🏛️ Political": "political",
    "⚖️ Legal": "legal",
    "📈 Economic": "economic",
    "🏥 Medical": "medical",
    "🔬 Scientific": "scientific",
    "🏗️ Engineering": "engineering",
    "🎖️ Military": "military",
    "📚 Educational": "educational",
    "🕌 Religious": "religious",
    "⚽ Sports": "sports",
    "📖 Literary": "literary",
    "💻 IT / Tech": "it",
    "🌿 Environmental": "environmental",
    "🌾 Agricultural": "agricultural",
    "📺 Media": "media",
    "✈️ Tourism": "tourism",
    "💬 General": "general",
}

# ═══════════════════════════════════════════════════════════════════════════════
#  LOAD DOMAIN DICTIONARY FROM JSON (CACHED)
# ═══════════════════════════════════════════════════════════════════════════════
@st.cache_data
def load_domain_dictionary():
    dict_path = Path(__file__).parent / "domain_dict.json"
    if dict_path.exists():
        with open(dict_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

DOMAIN_SPECIFIC_TRANSLATIONS = load_domain_dictionary()

# ═══════════════════════════════════════════════════════════════════════════════
#  DEEPL API KEY — FROM ENV OR SIDEBAR INPUT
# ═══════════════════════════════════════════════════════════════════════════════
st.sidebar.markdown("### 🔑 DeepL API Configuration")
st.sidebar.markdown("<div style='font-size:12px;color:#6b7280;margin-bottom:8px;'>The app requires a DeepL API key to translate. Get one free at deepl.com/pro-api.</div>", unsafe_allow_html=True)

# Try env var first, then session state, then empty
env_key = os.environ.get("DEEPL_API_KEY", "")
if "deepl_api_key" not in st.session_state:
    st.session_state.deepl_api_key = env_key

DEEPL_API_KEY = st.sidebar.text_input(
    "DeepL API Key",
    value=st.session_state.deepl_api_key,
    type="password",
    placeholder="Enter your DeepL API key...",
    help="Free tier: 500,000 characters/month. Key is stored only in this session."
)

# Save to session state
st.session_state.deepl_api_key = DEEPL_API_KEY

if not DEEPL_API_KEY:
    st.sidebar.error("⚠️ No API key provided. Translation will not work.")
else:
    # Masked display
    masked = DEEPL_API_KEY[:8] + "..." + DEEPL_API_KEY[-4:] if len(DEEPL_API_KEY) > 12 else "***"
    st.sidebar.success(f"✅ Key loaded: {masked}")

st.sidebar.markdown("<div style='font-size:11px;color:#9ca3af;margin-top:8px;'>Your key is never stored on disk. It only lives in this browser session.</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  TRANSLATION ENGINE — DEEPL ONLY
# ═══════════════════════════════════════════════════════════════════════════════
def translate_deepl(text, source_lang, target_lang):
    if not DEEPL_API_KEY:
        return None, "No API key configured"

    # DeepL language codes
    sl = source_lang.upper()
    tl = target_lang.upper()
    if sl == "AR": sl = "AR"
    elif sl == "ZH": sl = "ZH"
    if tl == "AR": tl = "AR"
    elif tl == "ZH": tl = "ZH"

    try:
        resp = requests.post(
            "https://api-free.deepl.com/v2/translate",
            headers={
                "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data={"text": text, "source_lang": sl, "target_lang": tl},
            timeout=15
        )
        if resp.status_code == 200:
            return resp.json()["translations"][0]["text"], None
        elif resp.status_code == 403:
            return None, "Invalid API key or authentication failed"
        elif resp.status_code == 429:
            return None, "Rate limit exceeded (too many requests)"
        elif resp.status_code == 456:
            return None, "Quota exceeded — free tier limit reached"
        else:
            return None, f"DeepL error {resp.status_code}: {resp.text[:200]}"
    except requests.exceptions.Timeout:
        return None, "Request timed out — check your internet connection"
    except requests.exceptions.ConnectionError:
        return None, "Connection error — cannot reach DeepL servers"
    except Exception as e:
        return None, f"Unexpected error: {str(e)}"

def fetch_ai_translation(text, source_lang, target_lang):
    result, error = translate_deepl(text, source_lang, target_lang)
    if result:
        return result, "DeepL"
    return None, error

# ═══════════════════════════════════════════════════════════════════════════════
#  SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════
if "source_lang" not in st.session_state:
    st.session_state.source_lang = "English"
if "target_lang" not in st.session_state:
    st.session_state.target_lang = "Arabic"
if "input_text" not in st.session_state:
    st.session_state.input_text = ""
if "selected_style" not in st.session_state:
    st.session_state.selected_style = "Auto-Detect"

# ═══════════════════════════════════════════════════════════════════════════════
#  SWAP CALLBACK
# ═══════════════════════════════════════════════════════════════════════════════
def swap_languages():
    old_source = st.session_state.source_lang
    old_target = st.session_state.target_lang
    st.session_state.source_lang = old_target
    st.session_state.target_lang = old_source

# ═══════════════════════════════════════════════════════════════════════════════
#  UI — LANGUAGE PAIR + STYLE
# ═══════════════════════════════════════════════════════════════════════════════
lang_list = list(languages_dict.keys())
style_list = list(STYLE_OPTIONS.keys())

if st.session_state.target_lang == st.session_state.source_lang:
    for lang in lang_list:
        if lang != st.session_state.source_lang:
            st.session_state.target_lang = lang
            break

src_idx = lang_list.index(st.session_state.source_lang)
tgt_options = [k for k in lang_list if k != st.session_state.source_lang]
tgt_idx = tgt_options.index(st.session_state.target_lang) if st.session_state.target_lang in tgt_options else 0
style_idx = style_list.index(st.session_state.selected_style) if st.session_state.selected_style in style_list else 0

# ── Language Row ──
left, mid, right = st.columns([1, 0.12, 1])

with left:
    source_lang_name = st.selectbox("From Language", lang_list, index=src_idx)

with mid:
    st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
    st.button("⇄", on_click=swap_languages, help="Swap languages", use_container_width=True)

with right:
    target_lang_name = st.selectbox("To Language", tgt_options, index=tgt_idx)

# ── Style Row ──
st.markdown("<div style='margin-top: 0.5rem;'></div>", unsafe_allow_html=True)
style_col1, style_col2 = st.columns([1, 2])
with style_col1:
    selected_style_label = st.selectbox(
        "Translation Style / Domain",
        style_list,
        index=style_idx,
        help="Choose the tone/domain to prioritize. 'Auto-Detect' lets the app decide based on keywords."
    )
with style_col2:
    selected_domain = STYLE_OPTIONS[selected_style_label]
    if selected_domain and selected_domain != "general":
        dinfo = DOMAINS[selected_domain]
        st.markdown(
            f"<div style='margin-top: 28px; font-size: 13px; color: {dinfo['color']}; font-weight: 600;'>"
            f"{dinfo['emoji']} Priority: {dinfo['name_en']} translations will be shown first"
            f"</div>",
            unsafe_allow_html=True
        )
    elif selected_domain == "general":
        st.markdown(
            "<div style='margin-top: 28px; font-size: 13px; color: #6B7280;'>"
            "💬 General / standard translations prioritized"
            "</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div style='margin-top: 28px; font-size: 13px; color: #6B7280;'>"
            "🔍 Auto-detecting domain from your text..."
            "</div>",
            unsafe_allow_html=True
        )

st.session_state.source_lang = source_lang_name
st.session_state.target_lang = target_lang_name
st.session_state.selected_style = selected_style_label

source_lang = languages_dict[source_lang_name]
target_lang = languages_dict[target_lang_name]
selected_domain = STYLE_OPTIONS[selected_style_label]

# Show dictionary stats
if DOMAIN_SPECIFIC_TRANSLATIONS:
    dict_size = len(DOMAIN_SPECIFIC_TRANSLATIONS)
    total_entries = sum(len(v) for v in DOMAIN_SPECIFIC_TRANSLATIONS.values())
    st.markdown(f'<div class="dict-stats">📚 Dictionary loaded: {dict_size} words with {total_entries} total domain entries</div>', unsafe_allow_html=True)

# Input
input_text = st.text_area("Enter text to translate", height=140, placeholder="Type or paste text here...", value=st.session_state.input_text, key="input_text_area")
if input_text != st.session_state.input_text:
    st.session_state.input_text = input_text

# Detected domains
if input_text.strip():
    detected = detect_domains(input_text)
    if detected:
        badges = ""
        for d in detected[:3]:
            dn = DOMAINS[d]["name_en"]
            dc = DOMAINS[d]["color"]
            badges += f'<span class="domain-badge" style="background:{dc};color:white;">{dn}</span>'
        st.markdown(f'<div class="detected-box"><b>Detected domains:</b> {badges}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="detected-box">No specific domain detected — using General context.</div>', unsafe_allow_html=True)

# Translate button
if st.button("Translate", type="primary"):
    if not input_text.strip():
        st.warning("Please enter text to translate.")
    elif not DEEPL_API_KEY:
        st.markdown(
            '<div class="error-box">'
            '<b>🔑 DeepL API Key Required</b><br>'
            'Please enter your DeepL API key in the sidebar to start translating. '
            'Get a free key at <a href="https://www.deepl.com/pro-api" target="_blank">deepl.com/pro-api</a>.'
            '</div>',
            unsafe_allow_html=True
        )
    else:
        with st.spinner("Translating via DeepL..."):
            base_translation, api_used = fetch_ai_translation(input_text, source_lang, target_lang)

            if not base_translation:
                # Show detailed error
                st.markdown(
                    f'<div class="error-box">'
                    f'<b>❌ Translation Failed</b><br>'
                    f'{api_used}<br>'
                    f'<span style="font-size:12px;color:#7f1d1d;">Please check your API key and quota at DeepL dashboard.</span>'
                    f'</div>',
                    unsafe_allow_html=True
                )
            else:
                api_badge = f'<span class="api-badge api-deepl">{api_used}</span>'
                st.markdown(f"{api_badge} <b>Base Translation:</b>", unsafe_allow_html=True)
                st.markdown(f'<div class="rtext">{base_translation}</div>', unsafe_allow_html=True)

                # ═══════════════════════════════════════════════════════════════════
                #  DICTIONARY LOOKUP
                # ═══════════════════════════════════════════════════════════════════
                all_meanings = {}
                lookup_word = input_text.strip().lower()
                is_single_word = len(lookup_word.split()) == 1

                # 1. Direct lookup
                if is_single_word and lookup_word in DOMAIN_SPECIFIC_TRANSLATIONS:
                    word_data = DOMAIN_SPECIFIC_TRANSLATIONS[lookup_word]
                    for domain, trans in word_data.items():
                        if domain not in all_meanings:
                            all_meanings[domain] = []
                        all_meanings[domain].append({
                            "translation": trans.get(target_lang, trans.get("en", "")),
                            "desc": trans.get("desc", ""),
                            "source": f"Direct: '{lookup_word}'"
                        })

                # 2. English lookup (via DeepL, not Google)
                english_word = None
                if source_lang != "en":
                    eng_result, eng_err = translate_deepl(input_text.strip(), source_lang, "en")
                    if eng_result:
                        english_word = eng_result.strip().lower()
                else:
                    english_word = lookup_word

                if english_word and is_single_word and english_word in DOMAIN_SPECIFIC_TRANSLATIONS:
                    word_data = DOMAIN_SPECIFIC_TRANSLATIONS[english_word]
                    for domain, trans in word_data.items():
                        if domain not in all_meanings:
                            all_meanings[domain] = []
                        existing = [m["translation"] for m in all_meanings.get(domain, [])]
                        t = trans.get(target_lang, trans.get("en", ""))
                        if t not in existing:
                            all_meanings[domain].append({
                                "translation": t,
                                "desc": trans.get("desc", ""),
                                "source": f"English: '{english_word}'"
                            })

                # 3. Fuzzy search
                if not all_meanings and is_single_word and english_word:
                    for dict_word, word_data in DOMAIN_SPECIFIC_TRANSLATIONS.items():
                        if english_word in dict_word or dict_word in english_word:
                            for domain, trans in word_data.items():
                                if domain not in all_meanings:
                                    all_meanings[domain] = []
                                existing = [m["translation"] for m in all_meanings.get(domain, [])]
                                t = trans.get(target_lang, trans.get("en", ""))
                                if t not in existing:
                                    all_meanings[domain].append({
                                        "translation": t,
                                        "desc": trans.get("desc", ""),
                                        "source": f"Fuzzy: '{dict_word}'"
                                    })

                # ═══════════════════════════════════════════════════════════════════
                #  DISPLAY MEANINGS — PRIORITIZE SELECTED STYLE
                # ═══════════════════════════════════════════════════════════════════
                if all_meanings:
                    total_meanings = sum(len(v) for v in all_meanings.values())
                    st.markdown("---")
                    st.markdown(f'<div class="all-meanings-header">🎯 All Domain-Specific Meanings <span class="meaning-count">{total_meanings}</span></div>', unsafe_allow_html=True)

                    domain_keys = [d for d in all_meanings.keys() if d != "general"]
                    if selected_domain and selected_domain in domain_keys:
                        domain_keys.remove(selected_domain)
                        domain_keys.insert(0, selected_domain)
                    if "general" in all_meanings:
                        domain_keys.append("general")

                    cols = st.columns(3)
                    col_idx = 0
                    for domain in domain_keys:
                        dinfo = DOMAINS.get(domain, DOMAINS["general"])
                        meanings = all_meanings[domain]
                        is_priority = (selected_domain == domain)

                        with cols[col_idx % 3]:
                            for meaning in meanings:
                                priority_html = '<span class="priority-badge">SELECTED STYLE</span>' if is_priority else ''
                                card_class = 'rcard-priority' if is_priority else ''
                                st.markdown(
                                    '<div class="rcard rcard-' + domain + ' domain-card ' + card_class + '">' +
                                    '<div class="rlabel rlabel-' + domain + '">' + dinfo["emoji"] + ' ' + dinfo["name_en"] + priority_html + '</div>' +
                                    '<div class="rtext" style="font-weight:600;">' + meaning["translation"] + '</div>' +
                                    '<div class="meaning-diff">' + meaning["desc"] + '</div>' +
                                    '</div>',
                                    unsafe_allow_html=True
                                )
                        col_idx += 1

                # Always show general translation
                st.markdown("---")
                st.markdown('<div class="all-meanings-header">💬 General Translation</div>', unsafe_allow_html=True)
                st.markdown(
                    '<div class="rcard rcard-gen"><div class="rlabel rlabel-gen">💬 General</div><div class="rtext">' + base_translation + '</div></div>',
                    unsafe_allow_html=True
                )
