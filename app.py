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
.ldot-off { background: rgba(255,255,255,0.18); }
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
.rcard-detected { box-shadow: 0 0 0 2px rgba(93,202,165,0.4); background: #f6fffd; }

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

.dym-box { background: #FAEEDA; border-left: 3px solid #BA7517; border-radius: 0 8px 8px 0; padding: 10px 14px; font-size: 13px; color: #412402; margin-bottom: 1rem; }
.detected-box { background: #E6F4F1; border-left: 3px solid #5DCAA5; border-radius: 0 8px 8px 0; padding: 10px 14px; font-size: 13px; color: #04342C; margin-bottom: 1rem; }
.abbrev-box { background: #E3F2FD; border-left: 3px solid #1565C0; border-radius: 0 8px 8px 0; padding: 10px 14px; font-size: 13px; color: #0D47A1; margin-bottom: 1rem; }

.swap-btn {
    background: #f3f4f6 !important; color: #374151 !important; border: 1px solid #d1d5db !important;
    border-radius: 8px !important; font-weight: 600 !important; font-size: 16px !important;
    padding: 0.4rem 0.8rem !important; width: auto !important;
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
    display: inline-block; padding: 2px 8px; border-radius: 4px;
    font-size: 10px; font-weight: 600; letter-spacing: 0.04em; margin-right: 4px;
}
.api-deepl { background: #0F2B46; color: #8ECAE6; }
.api-google { background: #F4A261; color: #5C3D1E; }

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
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-name">HASSAN <span>NASSER</span></div>
    <div class="hero-sub">MULTI-DOMAIN SMART TRANSLATOR — 15+ SPECIALIZED FIELDS</div>
    <div class="hero-pills">
        <span class="pill pill-active">Auto-Domain Detect</span>
        <span class="pill pill-muted">DeepL Precision</span>
        <span class="pill pill-muted">Smart Swap</span>
        <span class="pill pill-muted">All Contexts</span>
    </div>
    <div class="lang-bar">
        <span class="ldot"></span><span class="ldot"></span><span class="ldot"></span>
        <span class="ldot"></span><span class="ldot"></span><span class="ldot"></span>
        <span class="ldot"></span><span class="ldot"></span>
        <span class="lang-bar-txt">8 languages supported</span>
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

# ═══════════════════════════════════════════════════════════════════════════════
#  LOAD DOMAIN DICTIONARY FROM JSON (CACHED)
# ═══════════════════════════════════════════════════════════════════════════════
@st.cache_data
def load_domain_dictionary():
    """Load domain dictionary from JSON file once and cache it."""
    dict_path = Path(__file__).parent / "domain_dict.json"
    if dict_path.exists():
        with open(dict_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

DOMAIN_SPECIFIC_TRANSLATIONS = load_domain_dictionary()

# ═══════════════════════════════════════════════════════════════════════════════
#  DOMAIN DETECTION
# ═══════════════════════════════════════════════════════════════════════════════
DOMAIN_KEYWORDS = {
    "political": ["minister", "government", "council", "ministry", "parliament", "political", "diplomatic", "treaty", "election", "vote", "policy", "embassy", "summit", "legislation", "constitution", "foreign affairs", "national security", "coalition", "sanctions", "bilateral", "وزير", "حكومة", "مجلس", "وزارة", "برلمان", "سياسة", "دبلوماسي", "سفير", "معاهدة", "اتفاقية دولية", "حزب", "انتخابات", "تصويت", "أمن قومي", "استراتيجية وطنية", "بيان", "تصريح", "قمة", "مؤتمر", "جلسة", "تشريع", "دستور", "حقوق", "مواطن"],
    "legal": ["contract", "agreement", "clause", "appendix", "legal", "stipulation", "liable", "penalty", "compensation", "arbitration", "court", "judgment", "license", "obligation", "terms and conditions", "binding", "jurisdiction", "warranty", "indemnity", "breach", "عقد", "اتفاقية", "بند", "ملحق", "تعاقد", "قانون", "مرسوم", "لائحة", "نظام", "شرط", "جزاء", "تعويض", "مسؤولية", "ضمان", "FIDIC", "تحكيم", "دعوى", "محكمة", "قاضي", "حكم", "قرار", "تنظيمي", "ترخيص", "التزام", "حق", "ملكية", "إثبات"],
    "economic": ["economic", "financial", "investment", "cost", "budget", "revenue", "profit", "loss", "loan", "bank", "market", "trade", "import", "export", "tax", "fee", "pricing", "tender", "bid", "currency", "inflation", "growth", "GDP", "fiscal", "monetary", "اقتصاد", "مالية", "استثمار", "تكلفة", "سعر", "ميزانية", "عائد", "ربح", "خسارة", "تمويل", "قرض", "بنك", "سوق", "تجارة", "استيراد", "تصدير", "عمولة", "ضريبة", "رسوم", "تسعير", "عطاء", "مناقصة", "صرف", "عملة", "تضخم", "نمو", "تجاري"],
    "medical": ["doctor", "hospital", "treatment", "medication", "dose", "disease", "symptoms", "diagnosis", "laboratory", "clinical", "surgery", "patient", "health", "epidemic", "vaccine", "radiology", "bacteria", "virus", "immunity", "tissue", "cardiac", "renal", "طبيب", "مستشفى", "علاج", "دواء", "جرعة", "مرض", "أعراض", "تشخيص", "فحص", "تحليل", "مختبر", "سريري", "جراحة", "عملية", "مريض", "صحة", "وباء", "تطعيم", "أشعة", "بكتيريا", "فيروس", "مناعة", "أنسجة", "أعضاء", "قلب", "كبد", "كلى"],
    "scientific": ["research", "study", "experiment", "hypothesis", "theory", "scientific", "discovery", "innovation", "technology", "analysis", "data", "statistical", "model", "simulation", "algorithm", "AI", "machine learning", "physics", "chemistry", "biology", "astronomy", "بحث", "دراسة", "مختبر", "تجربة", "فرضية", "نظرية", "علمي", "اكتشاف", "ابتكار", "تقنية", "تكنولوجيا", "تحليل", "بيانات", "إحصائية", "نموذج", "محاكاة", "خوارزمية", "ذكاء اصطناعي", "تعلم آلي", "طاقة", "فيزياء", "كيمياء", "بيولوجيا", "فلك"],
    "engineering": ["engineering", "structural", "civil", "architectural", "electrical", "mechanical", "concrete", "rebar", "foundation", "excavation", "backfill", "pouring", "drawings", "specifications", "construction", "supervision", "quality", "inspection", "survey", "هندسة", "إنشائي", "مدني", "معماري", "كهرباء", "ميكانيك", "صرف", "مياه", "طرق", "جسور", "أنفاق", "خرسانة", "حديد", "تسليح", "صب", "ردم", "حفر", "أساسات", "تصميم", "مخططات", "مواصفات", "بناء", "تشييد", "إشراف", "جودة", "اختبار", "مساحة"],
    "military": ["military", "army", "defense", "war", "battle", "weapon", "air force", "navy", "tank", "missile", "bomb", "base", "recruitment", "officer", "soldier", "rank", "operation", "جيش", "عسكري", "دفاع", "حرب", "معركة", "سلاح", "سلاح الجو", "بحرية", "دبابة", "صاروخ", "قنبلة", "قاعدة عسكرية", "تجنيد", "ضابط", "جندي", "رتبة", "عملية عسكرية"],
    "educational": ["school", "university", "education", "teaching", "teacher", "professor", "student", "curriculum", "exam", "test", "certificate", "thesis", "dissertation", "training", "مدرسة", "جامعة", "تعليم", "تدريس", "معلم", "أستاذ", "طالب", "دراسة", "مناهج", "امتحان", "اختبار", "شهادة", "بحث علمي", "رسالة", "أطروحة", "تدريب", "دورة"],
    "religious": ["mosque", "church", "temple", "prayer", "Quran", "Bible", "hadith", "jurisprudence", "sharia", "pilgrimage", "fasting", "charity", "imam", "sermon", "religion", "faith", "مسجد", "كنيسة", "معبد", "صلاة", "قرآن", "إنجيل", "حديث", "فقه", "شريعة", "حج", "عمرة", "صوم", "زكاة", "إمام", "خطيب", "دين", "عقيدة", "عبادة", "تفسير"],
    "sports": ["sports", "football", "soccer", "basketball", "tennis", "swimming", "running", "stadium", "club", "team", "player", "coach", "referee", "championship", "cup", "match", "fitness", "رياضة", "كرة القدم", "كرة السلة", "تنس", "سباحة", "جري", "ملعب", "نادي", "فريق", "لاعب", "مدرب", "حكم", "بطولة", "كأس", "مباراة", "تدريب", "لياقة", "مسابقة"],
    "literary": ["literature", "story", "novel", "poetry", "poem", "writer", "author", "text", "style", "rhetoric", "metaphor", "simile", "chapter", "paragraph", "narrative", "plot", "character", "أدب", "قصة", "رواية", "شعر", "قصيدة", "كاتب", "مؤلف", "نص", "أسلوب", "بلاغة", "مجاز", "استعارة", "تشبيه", "فصل", "فقرة", "سرد", "حبكة", "شخصية", "حوار"],
    "it": ["programming", "code", "computer", "network", "internet", "software", "application", "website", "server", "database", "cybersecurity", "hacker", "AI", "machine learning", "cloud", "API", "برمجة", "كود", "حاسوب", "كمبيوتر", "شبكة", "إنترنت", "برنامج", "تطبيق", "موقع", "خادم", "قاعدة بيانات", "أمن سيبراني", "هاكر", "ذكاء اصطناعي", "تعلم آلي", "سحابي"],
    "environmental": ["environment", "pollution", "climate", "global warming", "renewable", "solar", "wind", "بيئة", "تلوث", "مناخ", "احتباس حراري", "طاقة متجددة", "شمسية", "رياح", "مياه جوفية", "غابة", "صحراء", "تصحر", "تنوع حيوي", "محمية", "طبيعة", "أوزون", "كربون"],
    "agricultural": ["agriculture", "farm", "crop", "wheat", "rice", "corn", "trees", "irrigation", "soil", "زراعة", "مزرعة", "محصول", "قمح", "أرز", "ذرة", "أشجار", "ماء ري", "تربة", "سماد", "مبيد", "حصاد", "حصادة", "ثروة حيوانية", "مواشي", "أغنام", "دواجن", "سمك"],
    "media": ["media", "journalism", "television", "radio", "newspaper", "news", "report", "anchor", "إعلام", "صحافة", "تلفزيون", "إذاعة", "صحيفة", "خبر", "تقرير", "مذيع", "مراسل", "تحقيق", "صحفي", "إعلان", "دعاية", "بث", "قناة", "برنامج إعلامي"],
    "tourism": ["tourism", "hotel", "travel", "trip", "airport", "aviation", "passport", "visa", "tour", "سياحة", "فندق", "سفر", "رحلة", "مطار", "طيران", "جواز", "تأشيرة", "جولة", "أثر", "تاريخي", "معلم", "منتجع", "شاطئ", "جبل", "صحراء", "متحف", "تراث"],
}

def detect_domains(text):
    text_lower = text.lower()
    scores = {}
    for domain, keywords in DOMAIN_KEYWORDS.items():
        score = sum(text_lower.count(kw.lower()) * (1 + len(kw)/50) for kw in keywords)
        if score > 0: scores[domain] = score
    return sorted(scores, key=scores.get, reverse=True) if scores else []

# ═══════════════════════════════════════════════════════════════════════════════
#  TRANSLATION ENGINES
# ═══════════════════════════════════════════════════════════════════════════════
DEEPL_API_KEY = os.environ.get("DEEPL_API_KEY", "")

def translate_deepl(text, source_lang, target_lang):
    if not DEEPL_API_KEY: return None
    if source_lang == "ar": source_lang = "AR"
    elif source_lang == "zh": source_lang = "ZH"
    else: source_lang = source_lang.upper()
    target_lang = target_lang.upper()
    if target_lang == "AR": target_lang = "AR"
    elif target_lang == "ZH": target_lang = "ZH"
    try:
        resp = requests.post(
            "https://api-free.deepl.com/v2/translate",
            headers={"Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}", "Content-Type": "application/x-www-form-urlencoded"},
            data={"text": text, "source_lang": source_lang, "target_lang": target_lang},
            timeout=15
        )
        if resp.status_code == 200: return resp.json()["translations"][0]["text"]
    except Exception: pass
    return None

def translate_google(text, source_lang, target_lang):
    try:
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_lang}&tl={target_lang}&dt=t&q={requests.utils.quote(text)}"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            return "".join([item[0] for item in data[0] if item[0]])
    except Exception: pass
    return None

def fetch_ai_translation(text, source_lang, target_lang):
    result = translate_deepl(text, source_lang, target_lang)
    if result: return result, "DeepL"
    result = translate_google(text, source_lang, target_lang)
    if result: return result, "Google"
    return None, None

# ═══════════════════════════════════════════════════════════════════════════════
#  SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════
if "source_lang" not in st.session_state:
    st.session_state.source_lang = "English"
if "target_lang" not in st.session_state:
    st.session_state.target_lang = "Arabic"
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# ═══════════════════════════════════════════════════════════════════════════════
#  UI — LANGUAGE PAIR
# ═══════════════════════════════════════════════════════════════════════════════
lang_list = list(languages_dict.keys())

def update_source():
    selected = st.session_state.source_lang_select
    st.session_state.source_lang = selected
    if st.session_state.target_lang == selected:
        for lang in lang_list:
            if lang != selected:
                st.session_state.target_lang = lang
                break

def update_target():
    st.session_state.target_lang = st.session_state.target_lang_select

left, mid, right = st.columns([1, 0.12, 1])

with left:
    source_lang_name = st.selectbox(
        "From Language", 
        lang_list, 
        index=lang_list.index(st.session_state.source_lang),
        key="source_lang_select",
        on_change=update_source
    )

with mid:
    st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
    if st.button("⇄", key="swap_btn", help="Swap languages", use_container_width=True):
        old_source = st.session_state.source_lang
        old_target = st.session_state.target_lang
        st.session_state.source_lang = old_target
        st.session_state.target_lang = old_source
        st.rerun()

with right:
    target_lang_options = [k for k in lang_list if k != source_lang_name]
    target_index = target_lang_options.index(st.session_state.target_lang) if st.session_state.target_lang in target_lang_options else 0

    target_lang_name = st.selectbox(
        "To Language", 
        target_lang_options,
        index=target_index,
        key="target_lang_select",
        on_change=update_target
    )

source_lang = languages_dict[source_lang_name]
target_lang = languages_dict[target_lang_name]

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
    else:
        with st.spinner("Translating..."):
            # Get base translation
            base_translation, api_used = fetch_ai_translation(input_text, source_lang, target_lang)

            if not base_translation:
                st.error("Translation failed. Please check your internet connection or API keys.")
            else:
                # Show base translation
                api_badge = f'<span class="api-badge api-deepl">{api_used}</span>' if api_used == "DeepL" else f'<span class="api-badge api-google">{api_used}</span>'
                st.markdown(f"{api_badge} <b>Base Translation:</b>", unsafe_allow_html=True)
                st.markdown(f'<div class="rtext">{base_translation}</div>', unsafe_allow_html=True)

                # ═══════════════════════════════════════════════════════════════════
                #  COMPREHENSIVE DICTIONARY LOOKUP — ALL DOMAINS
                # ═══════════════════════════════════════════════════════════════════
                all_meanings = {}
                lookup_word = input_text.strip().lower()
                is_single_word = len(lookup_word.split()) == 1

                # 1. Direct lookup of original word
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

                # 2. Translate to English for lookup
                english_word = None
                if source_lang != "en":
                    english_word = translate_google(input_text.strip(), source_lang, "en")
                    if english_word:
                        english_word = english_word.strip().lower()
                else:
                    english_word = lookup_word

                # 2a. Lookup English word
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

                # 3. Fuzzy search for partial matches
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
                #  DISPLAY ALL DOMAIN-SPECIFIC MEANINGS
                # ═══════════════════════════════════════════════════════════════════
                if all_meanings:
                    total_meanings = sum(len(v) for v in all_meanings.values())
                    st.markdown("---")
                    st.markdown(f'<div class="all-meanings-header">🎯 All Domain-Specific Meanings <span class="meaning-count">{total_meanings}</span></div>', unsafe_allow_html=True)

                    sorted_domains = sorted(
                        [d for d in all_meanings.keys() if d != "general"],
                        key=lambda d: len(all_meanings[d]),
                        reverse=True
                    )
                    if "general" in all_meanings:
                        sorted_domains.append("general")

                    cols = st.columns(3)
                    col_idx = 0
                    for domain in sorted_domains:
                        dinfo = DOMAINS.get(domain, DOMAINS["general"])
                        meanings = all_meanings[domain]

                        with cols[col_idx % 3]:
                            for meaning in meanings:
                                st.markdown(
                                    '<div class="rcard rcard-' + domain + ' domain-card">' +
                                    '<div class="rlabel rlabel-' + domain + '">' + dinfo["emoji"] + ' ' + dinfo["name_en"] + '</div>' +
                                    '<div class="rtext" style="font-weight:600;">' + meaning["translation"] + '</div>' +
                                    '<div class="meaning-diff">' + meaning["desc"] + '</div>' +
                                    '</div>',
                                    unsafe_allow_html=True
                                )
                        col_idx += 1

                elif detected:
                    st.markdown("---")
                    st.markdown('<div class="all-meanings-header">🎯 Domain-Specific Context</div>', unsafe_allow_html=True)
                    st.caption("No exact dictionary match. Showing detected domain context.")
                    for domain in detected[:3]:
                        dinfo = DOMAINS[domain]
                        st.markdown(
                            '<div class="rcard rcard-' + domain + ' domain-card">' +
                            '<div class="rlabel rlabel-' + domain + '">' + dinfo["emoji"] + ' ' + dinfo["name_en"] + '</div>' +
                            '<div class="rtext">' + base_translation + '</div>' +
                            '<div class="meaning-diff">General translation in ' + dinfo["name_en"] + ' context</div>' +
                            '</div>',
                            unsafe_allow_html=True
                        )

                # Always show general translation
                st.markdown("---")
                st.markdown('<div class="all-meanings-header">💬 General Translation</div>', unsafe_allow_html=True)
                st.markdown(
                    '<div class="rcard rcard-gen"><div class="rlabel rlabel-gen">💬 General</div><div class="rtext">' + base_translation + '</div></div>',
                    unsafe_allow_html=True
                )
