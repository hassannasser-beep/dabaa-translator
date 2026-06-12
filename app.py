import streamlit as st
import requests
import os
import sqlite3
import re
from pathlib import Path

st.set_page_config(page_title="HASSAN NASSER", page_icon="🏗️", layout="wide")

# ═══════════════════════════════════════════════════════════════════════════════
#  CSS
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; max-width: 1100px; }
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
.rcard { border-radius: 12px; padding: 1.1rem 1.3rem; border: 0.5px solid #e5e7eb; background: #fff; transition: all 0.2s; }
.rcard-pol { border-top: 3px solid #E63946; } .rcard-leg { border-top: 3px solid #534AB7; }
.rcard-eco { border-top: 3px solid #F4A261; } .rcard-med { border-top: 3px solid #2A9D8F; }
.rcard-sci { border-top: 3px solid #264653; } .rcard-eng { border-top: 3px solid #1D9E75; }
.rcard-mil { border-top: 3px solid #8B0000; } .rcard-edu { border-top: 3px solid #F4D03F; }
.rcard-rel { border-top: 3px solid #6C3483; } .rcard-spt { border-top: 3px solid #E67E22; }
.rcard-lit { border-top: 3px solid #D81B60; } .rcard-it  { border-top: 3px solid #00ACC1; }
.rcard-env { border-top: 3px solid #43A047; } .rcard-agr { border-top: 3px solid #795548; }
.rcard-med2 { border-top: 3px solid #5E35B1; } .rcard-tour { border-top: 3px solid #00838F; }
.rcard-gen { border-top: 3px solid #6B7280; }
.rcard-detected { box-shadow: 0 0 0 2px rgba(93,202,165,0.4); background: #f6fffd; }
.rlabel { font-size: 10px; font-weight: 600; letter-spacing: 0.08em; margin-bottom: 8px; }
.rlabel-pol { color: #9B2226; } .rlabel-leg { color: #3C3489; } .rlabel-eco { color: #9C6644; }
.rlabel-med { color: #1B6B5E; } .rlabel-sci { color: #1D3A4C; } .rlabel-eng { color: #085041; }
.rlabel-mil { color: #8B0000; } .rlabel-edu { color: #9A7D0A; } .rlabel-rel { color: #6C3483; }
.rlabel-spt { color: #A04000; } .rlabel-lit { color: #AD1457; } .rlabel-it  { color: #006064; }
.rlabel-env { color: #1B5E20; } .rlabel-agr { color: #4E342E; } .rlabel-med2 { color: #4527A0; }
.rlabel-tour { color: #006064; } .rlabel-gen { color: #4B5563; }
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
.detected-box { background: #E6F4F1; border-left: 3px solid #5DCAA5; border-radius: 0 8px 8px 0; padding: 10px 14px; font-size: 13px; color: #04342C; margin-bottom: 1rem; }
.abbrev-box { background: #E3F2FD; border-left: 3px solid #1565C0; border-radius: 0 8px 8px 0; padding: 10px 14px; font-size: 13px; color: #0D47A1; margin-bottom: 1rem; }
.swap-btn { background: #f3f4f6 !important; color: #374151 !important; border: 1px solid #d1d5db !important; border-radius: 8px !important; font-weight: 600 !important; font-size: 16px !important; padding: 0.4rem 0.8rem !important; width: auto !important; }
.swap-btn:hover { background: #e5e7eb !important; }
div.stButton > button[kind="primary"] { background: #1a1a2e !important; color: white !important; border: none !important; border-radius: 8px !important; font-weight: 500 !important; font-size: 15px !important; padding: 0.65rem 2rem !important; width: 100% !important; }
div.stButton > button[kind="primary"]:hover { background: #0f0f1e !important; }
textarea { border-radius: 8px !important; border: 0.5px solid #d1d5db !important; font-size: 14px !important; }
.api-badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: 600; letter-spacing: 0.04em; margin-right: 4px; }
.api-deepl { background: #0F2B46; color: #8ECAE6; }
.api-google { background: #F4A261; color: #5C3D1E; }
.domain-badge { display: inline-block; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600; letter-spacing: 0.04em; margin-right: 6px; margin-bottom: 4px; }
.db-pol { background: #E63946; color: white; } .db-leg { background: #534AB7; color: white; }
.db-eco { background: #F4A261; color: #3E2723; } .db-med { background: #2A9D8F; color: white; }
.db-sci { background: #264653; color: white; } .db-eng { background: #1D9E75; color: white; }
.db-mil { background: #8B0000; color: white; } .db-edu { background: #F4D03F; color: #3E2723; }
.db-rel { background: #6C3483; color: white; } .db-spt { background: #E67E22; color: white; }
.db-lit { background: #D81B60; color: white; } .db-it  { background: #00ACC1; color: white; }
.db-env { background: #43A047; color: white; } .db-agr { background: #795548; color: white; }
.db-med2 { background: #5E35B1; color: white; } .db-tour { background: #00838F; color: white; }
.db-gen { background: #6B7280; color: white; }
.meaning-diff { background: #fff3e0; border-radius: 4px; padding: 2px 6px; font-size: 12px; color: #e65100; font-weight: 600; display: inline-block; margin-top: 4px; }
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
        <span class="pill pill-muted">Slang + Abbreviations</span>
    </div>
    <div class="lang-bar">
        <span class="ldot"></span><span class="ldot"></span><span class="ldot"></span>
        <span class="ldot"></span><span class="ldot"></span><span class="ldot"></span>
        <span class="ldot"></span><span class="ldot"></span>
        <span class="lang-bar-txt">8 languages</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════
languages_dict = {"العربية": "ar", "English": "en", "Русский": "ru", "中文": "zh",
                  "Deutsch": "de", "Español": "es", "Português": "pt", "한국어": "ko"}

lang_names = {"ar": "العربية", "en": "English", "ru": "Русский", "zh": "中文",
              "de": "Deutsch", "es": "Español", "pt": "Português", "ko": "한국어"}

lang_flags = {"ar": "🇸🇦", "en": "🇬🇧", "ru": "🇷🇺", "zh": "🇨🇳",
              "de": "🇩🇪", "es": "🇪🇸", "pt": "🇵🇹", "ko": "🇰🇷"}

DOMAINS = {
    "political":  {"emoji": "🏛️", "name_ar": "سياسي",  "name_en": "Political",     "color": "#E63946"},
    "legal":      {"emoji": "⚖️", "name_ar": "قانوني", "name_en": "Legal",         "color": "#534AB7"},
    "economic":   {"emoji": "📈", "name_ar": "اقتصادي","name_en": "Economic",      "color": "#F4A261"},
    "medical":    {"emoji": "🏥", "name_ar": "طبي",    "name_en": "Medical",       "color": "#2A9D8F"},
    "scientific": {"emoji": "🔬", "name_ar": "علمي",   "name_en": "Scientific",    "color": "#264653"},
    "engineering":{"emoji": "🏗️", "name_ar": "هندسي",  "name_en": "Engineering",   "color": "#1D9E75"},
    "military":   {"emoji": "🎖️", "name_ar": "عسكري",  "name_en": "Military",      "color": "#8B0000"},
    "educational":{"emoji": "📚", "name_ar": "تعليمي", "name_en": "Educational",   "color": "#F4D03F"},
    "religious":  {"emoji": "🕌", "name_ar": "ديني",   "name_en": "Religious",     "color": "#6C3483"},
    "sports":     {"emoji": "⚽", "name_ar": "رياضي",  "name_en": "Sports",        "color": "#E67E22"},
    "literary":   {"emoji": "📖", "name_ar": "أدبي",   "name_en": "Literary",      "color": "#D81B60"},
    "it":         {"emoji": "💻", "name_ar": "تقني",   "name_en": "IT / Tech",     "color": "#00ACC1"},
    "environmental":{"emoji": "🌿", "name_ar": "بيئي",  "name_en": "Environmental", "color": "#43A047"},
    "agricultural":{"emoji": "🌾", "name_ar": "زراعي", "name_en": "Agricultural",  "color": "#795548"},
    "media":      {"emoji": "📺", "name_ar": "إعلامي", "name_en": "Media",         "color": "#5E35B1"},
    "tourism":    {"emoji": "✈️", "name_ar": "سياحي",  "name_en": "Tourism",       "color": "#00838F"},
    "general":    {"emoji": "💬", "name_ar": "عام",    "name_en": "General",       "color": "#6B7280"},
}

# ═══════════════════════════════════════════════════════════════════════════════
#  DATABASE CONNECTION
# ═══════════════════════════════════════════════════════════════════════════════
DB_PATH = Path(__file__).parent / "dictionary.db"

def get_db_connection():
    """Get SQLite database connection."""
    return sqlite3.connect(str(DB_PATH))

# ═══════════════════════════════════════════════════════════════════════════════
#  DOMAIN DETECTION KEYWORDS (in-memory for speed)
# ═══════════════════════════════════════════════════════════════════════════════
DOMAIN_KEYWORDS = {
    "political": ["وزير", "حكومة", "مجلس", "وزارة", "برلمان", "سياسة", "دبلوماسي", "سفير", "معاهدة",
        "اتفاقية دولية", "حزب", "انتخابات", "تصويت", "أمن قومي", "استراتيجية وطنية", "بيان", "تصريح", "قمة",
        "مؤتمر", "جلسة", "تشريع", "دستور", "حقوق", "مواطن", "political", "government", "minister",
        "parliament", "diplomatic", "treaty", "election", "vote", "policy", "embassy", "summit", "legislation",
        "constitution", "foreign affairs", "national security", "coalition", "sanctions", "bilateral"],
    "legal": ["عقد", "اتفاقية", "بند", "ملحق", "تعاقد", "قانون", "مرسوم", "لائحة", "نظام", "شرط", "جزاء",
        "تعويض", "مسؤولية", "ضمان", "FIDIC", "تحكيم", "دعوى", "محكمة", "قاضي", "حكم", "قرار", "تنظيمي",
        "ترخيص", "التزام", "حق", "ملكية", "إثبات", "contract", "agreement", "clause", "appendix", "legal",
        "stipulation", "liable", "penalty", "compensation", "arbitration", "court", "judgment", "license",
        "obligation", "terms and conditions", "binding", "jurisdiction", "warranty", "indemnity", "breach"],
    "economic": ["اقتصاد", "مالية", "استثمار", "تكلفة", "سعر", "ميزانية", "عائد", "ربح", "خسارة", "تمويل",
        "قرض", "بنك", "سوق", "تجارة", "استيراد", "تصدير", "عمولة", "ضريبة", "رسوم", "تسعير", "عطاء",
        "مناقصة", "صرف", "عملة", "تضخم", "نمو", "تجاري", "economic", "financial", "investment", "cost",
        "budget", "revenue", "profit", "loss", "loan", "bank", "market", "trade", "import", "export", "tax",
        "fee", "pricing", "tender", "bid", "currency", "inflation", "growth", "GDP", "fiscal", "monetary"],
    "medical": ["طبيب", "مستشفى", "علاج", "دواء", "جرعة", "مرض", "أعراض", "تشخيص", "فحص", "تحليل",
        "مختبر", "سريري", "جراحة", "عملية", "مريض", "صحة", "وباء", "تطعيم", "أشعة", "بكتيريا", "فيروس",
        "مناعة", "أنسجة", "أعضاء", "قلب", "كبد", "كلى", "doctor", "hospital", "treatment", "medication",
        "dose", "disease", "symptoms", "diagnosis", "laboratory", "clinical", "surgery", "patient", "health",
        "epidemic", "vaccine", "radiology", "bacteria", "virus", "immunity", "tissue", "cardiac", "renal"],
    "scientific": ["بحث", "دراسة", "مختبر", "تجربة", "فرضية", "نظرية", "علمي", "اكتشاف", "ابتكار", "تقنية",
        "تكنولوجيا", "تحليل", "بيانات", "إحصائية", "نموذج", "محاكاة", "خوارزمية", "ذكاء اصطناعي", "تعلم آلي",
        "طاقة", "فيزياء", "كيمياء", "بيولوجيا", "فلك", "research", "study", "experiment", "hypothesis",
        "theory", "scientific", "discovery", "innovation", "technology", "analysis", "data", "statistical",
        "model", "simulation", "algorithm", "AI", "machine learning", "physics", "chemistry", "biology", "astronomy"],
    "engineering": ["هندسة", "إنشائي", "مدني", "معماري", "كهرباء", "ميكانيك", "صرف", "مياه", "طرق", "جسور",
        "أنفاق", "خرسانة", "حديد", "تسليح", "صب", "ردم", "حفر", "أساسات", "تصميم", "مخططات", "مواصفات",
        "بناء", "تشييد", "إشراف", "جودة", "اختبار", "مساحة", "engineering", "structural", "civil",
        "architectural", "electrical", "mechanical", "concrete", "rebar", "foundation", "excavation", "backfill",
        "pouring", "drawings", "specifications", "construction", "supervision", "quality", "inspection", "survey"],
    "military": ["جيش", "عسكري", "دفاع", "حرب", "معركة", "سلاح", "سلاح الجو", "بحرية", "دبابة", "صاروخ",
        "قنبلة", "قاعدة عسكرية", "تجنيد", "ضابط", "جندي", "رتبة", "عملية عسكرية", "military", "army",
        "defense", "war", "battle", "weapon", "air force", "navy", "tank", "missile", "bomb", "base",
        "recruitment", "officer", "soldier", "rank", "operation"],
    "educational": ["مدرسة", "جامعة", "تعليم", "تدريس", "معلم", "أستاذ", "طالب", "دراسة", "مناهج", "امتحان",
        "اختبار", "شهادة", "بحث علمي", "رسالة", "أطروحة", "تدريب", "دورة", "school", "university",
        "education", "teaching", "teacher", "professor", "student", "curriculum", "exam", "test", "certificate",
        "thesis", "dissertation", "training"],
    "religious": ["مسجد", "كنيسة", "معبد", "صلاة", "قرآن", "إنجيل", "حديث", "فقه", "شريعة", "حج", "عمرة",
        "صوم", "زكاة", "إمام", "خطيب", "دين", "عقيدة", "عبادة", "تفسير", "mosque", "church", "temple",
        "prayer", "Quran", "Bible", "hadith", "jurisprudence", "sharia", "pilgrimage", "fasting", "charity",
        "imam", "sermon", "religion", "faith"],
    "sports": ["رياضة", "كرة القدم", "كرة السلة", "تنس", "سباحة", "جري", "ملعب", "نادي", "فريق", "لاعب",
        "مدرب", "حكم", "بطولة", "كأس", "مباراة", "تدريب", "لياقة", "مسابقة", "sports", "football", "soccer",
        "basketball", "tennis", "swimming", "running", "stadium", "club", "team", "player", "coach", "referee",
        "championship", "cup", "match", "fitness"],
    "literary": ["أدب", "قصة", "رواية", "شعر", "قصيدة", "كاتب", "مؤلف", "نص", "أسلوب", "بلاغة", "مجاز",
        "استعارة", "تشبيه", "فصل", "فقرة", "سرد", "حبكة", "شخصية", "حوار", "literature", "story", "novel",
        "poetry", "poem", "writer", "author", "text", "style", "rhetoric", "metaphor", "simile", "chapter",
        "paragraph", "narrative", "plot", "character"],
    "it": ["برمجة", "كود", "حاسوب", "كمبيوتر", "شبكة", "إنترنت", "برنامج", "تطبيق", "موقع", "خادم",
        "قاعدة بيانات", "أمن سيبراني", "هاكر", "ذكاء اصطناعي", "تعلم آلي", "سحابي", "programming", "code",
        "computer", "network", "internet", "software", "application", "website", "server", "database",
        "cybersecurity", "hacker", "AI", "machine learning", "cloud", "API"],
    "environmental": ["بيئة", "تلوث", "مناخ", "احتباس حراري", "طاقة متجددة", "شمسية", "رياح", "مياه جوفية",
        "غابة", "صحراء", "تصحر", "تنوع حيوي", "محمية", "طبيعة", "أوزون", "كربون", "environment", "pollution",
        "climate", "global warming", "renewable", "solar", "wind"],
    "agricultural": ["زراعة", "مزرعة", "محصول", "قمح", "أرز", "ذرة", "أشجار", "ماء ري", "تربة", "سماد",
        "مبيد", "حصاد", "حصادة", "ثروة حيوانية", "مواشي", "أغنام", "دواجن", "سمك", "agriculture", "farm",
        "crop", "wheat", "rice", "corn", "trees", "irrigation", "soil"],
    "media": ["إعلام", "صحافة", "تلفزيون", "إذاعة", "صحيفة", "خبر", "تقرير", "مذيع", "مراسل", "تحقيق",
        "صحفي", "إعلان", "دعاية", "بث", "قناة", "برنامج إعلامي", "صحفي", "media", "journalism", "television",
        "radio", "newspaper", "news", "report", "anchor"],
    "tourism": ["سياحة", "فندق", "سفر", "رحلة", "مطار", "طيران", "جواز", "تأشيرة", "جولة", "أثر", "تاريخي",
        "معلم", "منتجع", "شاطئ", "جبل", "صحراء", "متحف", "تراث", "tourism", "hotel", "travel", "trip",
        "airport", "aviation", "passport", "visa", "tour"],
}

def detect_domains(text):
    text_lower = text.lower()
    scores = {}
    for domain, keywords in DOMAIN_KEYWORDS.items():
        score = sum(text_lower.count(kw.lower()) * (1 + len(kw)/50) for kw in keywords)
        if score > 0: scores[domain] = score
    return sorted(scores, key=scores.get, reverse=True) if scores else []

# ═══════════════════════════════════════════════════════════════════════════════
#  DATABASE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════
def get_db_connection():
    """Get SQLite database connection."""
    return sqlite3.connect(str(DB_PATH))

def get_domain_translation_from_db(word, domain, target_lang):
    """Get domain-specific translation from SQLite database."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT translation, description FROM domain_translations WHERE word = ? AND domain = ? AND target_lang = ?",
            (word.lower(), domain, target_lang)
        )
        result = cursor.fetchone()
        conn.close()
        if result:
            return {"translation": result[0], "desc": result[1]}
        return None
    except Exception:
        return None

def get_all_domain_translations_from_db(word, target_lang):
    """Get all domain translations for a word from database."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT domain, translation, description FROM domain_translations WHERE word = ? AND target_lang = ?",
            (word.lower(), target_lang)
        )
        results = cursor.fetchall()
        conn.close()
        return {row[0]: {"translation": row[1], "desc": row[2]} for row in results}
    except Exception:
        return {}

def get_slang_term(term):
    """Get slang term from database."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT academic, slang, description FROM slang_terms WHERE term = ?",
            (term.lower(),)
        )
        result = cursor.fetchone()
        conn.close()
        if result:
            return {"academic": result[0], "slang": result[1], "desc": result[2]}
        return None
    except Exception:
        return None

def search_slang_terms(text):
    """Search for slang terms in text."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT term, academic, slang, description FROM slang_terms")
        all_terms = cursor.fetchall()
        conn.close()

        found = []
        text_lower = text.lower()
        for term, academic, slang, desc in all_terms:
            if term.lower() in text_lower:
                found.append((term, {"academic": academic, "slang": slang, "desc": desc}))
        return found
    except Exception:
        return []

def get_abbreviation(abbrev):
    """Get abbreviation from database."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT full_en, full_ru, ar, description FROM abbreviations WHERE abbrev = ?",
            (abbrev.upper(),)
        )
        result = cursor.fetchone()
        conn.close()
        if result:
            return {"full_en": result[0], "full_ru": result[1], "ar": result[2], "desc": result[3]}
        return None
    except Exception:
        return None

def search_abbreviations(text):
    """Search for abbreviations in text."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT abbrev, full_en, full_ru, ar, description FROM abbreviations")
        all_abbrevs = cursor.fetchall()
        conn.close()

        found = []
        text_upper = text.upper()
        for abbrev, full_en, full_ru, ar, desc in all_abbrevs:
            if abbrev.upper() in text_upper:
                found.append((abbrev, {"full_en": full_en, "full_ru": full_ru, "ar": ar, "desc": desc}))
        return found
    except Exception:
        return []

def detect_abbreviations_from_words(text):
    """Detect abbreviations from first letters of word sequences."""
    words = text.split()
    found = []
    for i in range(len(words)):
        for j in range(i+1, min(i+6, len(words)+1)):
            phrase = " ".join(words[i:j])
            first_letters = "".join([w[0].upper() for w in words[i:j] if w])
            abbrev_data = get_abbreviation(first_letters)
            if abbrev_data:
                found.append((first_letters, abbrev_data, phrase))
    return found


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
#  HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════
def calculate_distance(a, b):
    n, m = len(a), len(b)
    if n == 0: return m
    if m == 0: return n
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): dp[i][0] = i
    for j in range(m+1): dp[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = 0 if a[i-1] == b[j-1] else 1
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+cost)
    return dp[n][m]

def find_closest_slang(word, max_distance=3):
    word_lower = word.lower().strip()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT term FROM slang_terms")
        all_terms = [row[0] for row in cursor.fetchall()]
        conn.close()
    except Exception:
        return None

    best_match, best_dist = None, max_distance + 1
    for term in all_terms:
        dist = calculate_distance(word_lower, term.lower())
        if dist < best_dist:
            best_dist = dist
            best_match = term
    if best_match and best_dist <= max_distance:
        return best_match
    return None


def build_formula(text, domain, target_lang):
    """Build domain-specific translation by replacing keywords using database."""
    if not domain or domain == "general":
        return text

    result = text
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT word, translation FROM domain_translations WHERE domain = ? AND target_lang = ?",
            (domain, target_lang)
        )
        translations = cursor.fetchall()
        conn.close()

        for word, translation in translations:
            if word.lower() in result.lower():
                result = re.sub(r'\b' + re.escape(word) + r'\b', translation, result, flags=re.IGNORECASE)
    except Exception:
        pass

    return result

# ═══════════════════════════════════════════════════════════════════════════════
#  UI — LANGUAGE PAIR
# ═══════════════════════════════════════════════════════════════════════════════
left, right = st.columns([1, 1])
with left:
    source_lang_name = st.selectbox("From", list(languages_dict.keys()), key="source_lang")
with right:
    target_lang_options = [k for k in languages_dict.keys() if k != source_lang_name]
    if "target_lang" not in st.session_state or st.session_state.target_lang not in target_lang_options:
        st.session_state.target_lang = target_lang_options[0]
    target_lang_name = st.selectbox("To", target_lang_options, key="target_lang")

source_lang = languages_dict[source_lang_name]
target_lang = languages_dict[target_lang_name]

# Swap button
c1, c2, c3 = st.columns([1, 0.15, 1])
with c2:
    if st.button("⇄", key="swap_btn", help="Swap languages"):
        st.session_state.source_lang, st.session_state.target_lang = st.session_state.target_lang, st.session_state.source_lang
        st.rerun()

# Input
input_text = st.text_area("Enter text to translate", height=140, placeholder="Type or paste text here...")

# Detected domains
if input_text.strip():
    detected = detect_domains(input_text)
    if detected:
        badges = ""
        for d in detected[:3]:
            dn = DOMAINS[d]["name_en"]
            dc = DOMAINS[d]["color"]
            badges += f'<span class="domain-badge" style="background:{dc};color:white;">{dn}</span>'
        st.markdown(f'<div class="detected-box">Detected domains: {badges}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="detected-box">No specific domain detected — using General context.</div>', unsafe_allow_html=True)

# Abbreviations detection
if input_text.strip():
    abbrevs = search_abbreviations(input_text)
    abbrevs_words = detect_abbreviations_from_words(input_text)
    if abbrevs or abbrevs_words:
        abbrev_html = "<b>Abbreviations detected:</b><br>"
        for abbrev, data in abbrevs:
            abbrev_html += f"<b>{abbrev}</b>: {data['full_en']} | {data['ar']} — {data['desc']}<br>"
        for abbrev, data, phrase in abbrevs_words:
            abbrev_html += f"<b>{abbrev}</b> (from '{phrase}'): {data['full_en']} | {data['ar']} — {data['desc']}<br>"
        st.markdown(f'<div class="abbrev-box">{abbrev_html}</div>', unsafe_allow_html=True)

# Slang detection
if input_text.strip():
    slang_found = search_slang_terms(input_text)
    if slang_found:
        st.markdown('<div class="slang-wrap"><div class="slang-head"><span class="slang-head-txt">🏗️ SITE SLANG DETECTED</span></div><table class="slang-table"><tr><th>Term</th><th>Academic</th><th>Site Slang</th><th>Description</th></tr>', unsafe_allow_html=True)
        for term, data in slang_found:
            st.markdown(f'<tr><td class="term-cell">{term}</td><td>{data["academic"]}</td><td class="site-cell">{data["slang"]}</td><td>{data["desc"]}</td></tr>', unsafe_allow_html=True)
        st.markdown('</table></div>', unsafe_allow_html=True)

    # Did-you-mean for slang
    words = input_text.split()
    for word in words:
        closest = find_closest_slang(word)
        if closest:
            closest_data = get_slang_term(closest)
            if closest_data and closest.lower() != word.lower():
                st.markdown(f'<div class="dym-box">Did you mean: <b>{closest}</b> (site slang for: {closest_data["academic"]})?</div>', unsafe_allow_html=True)
                break

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
                st.markdown(f"{api_badge} **Base Translation:**", unsafe_allow_html=True)
                st.markdown(f'<div class="rtext">{base_translation}</div>', unsafe_allow_html=True)

                # Check if input is a single word that has domain-specific translations
                input_word = input_text.strip().lower()
                is_single_word = len(input_word.split()) == 1

                if is_single_word:
                    # Check database for domain translations
                    all_trans = get_all_domain_translations_from_db(input_word, target_lang)
                    if all_trans:
                        st.markdown("---")
                        st.markdown("### 🎯 Domain-Specific Meanings")
                        st.markdown(f"*Showing different meanings for '{input_text.strip()}' across all domains:*")

                        cols = st.columns(3)
                        col_idx = 0
                        for domain in all_trans:
                            if domain == "general":
                                continue
                            with cols[col_idx % 3]:
                                dinfo = DOMAINS[domain]
                                trans = all_trans[domain]["translation"]
                                desc = all_trans[domain]["desc"]
                                st.markdown(
                                    '<div class="rcard rcard-' + domain + '">' +
                                    '<div class="rlabel rlabel-' + domain + '">' + dinfo["emoji"] + ' ' + dinfo["name_en"] + ' | ' + dinfo["name_ar"] + '</div>' +
                                    '<div class="rtext" style="font-weight:600;">' + trans + '</div>' +
                                    '<div class="meaning-diff">' + desc + '</div>' +
                                    '</div>',
                                    unsafe_allow_html=True
                                )
                            col_idx += 1

                elif detected:
                    # Show domain-specific translations for phrases
                    st.markdown("---")
                    st.markdown("### 🎯 Domain-Specific Translations")

                    for domain in detected[:3]:
                        dinfo = DOMAINS[domain]
                        domain_translation = build_formula(base_translation, domain, target_lang)

                        if domain_translation != base_translation:
                            st.markdown(
                                '<div class="rcard rcard-' + domain + ' rcard-detected">' +
                                '<div class="rlabel rlabel-' + domain + '">' + dinfo["emoji"] + ' ' + dinfo["name_en"] + ' | ' + dinfo["name_ar"] + '</div>' +
                                '<div class="rtext">' + domain_translation + '</div>' +
                                '<div class="meaning-diff">Domain-specific formulation</div>' +
                                '</div>',
                                unsafe_allow_html=True
                            )
                        else:
                            st.markdown(
                                '<div class="rcard rcard-' + domain + '">' +
                                '<div class="rlabel rlabel-' + domain + '">' + dinfo["emoji"] + ' ' + dinfo["name_en"] + ' | ' + dinfo["name_ar"] + '</div>' +
                                '<div class="rtext">' + base_translation + '</div>' +
                                '<div class="meaning-diff">General translation (no domain-specific terms found)</div>' +
                                '</div>',
                                unsafe_allow_html=True
                            )

                # Show general translation as fallback
                st.markdown("---")
                st.markdown("### 💬 General Translation")
                st.markdown(
                    '<div class="rcard rcard-gen"><div class="rlabel rlabel-gen">💬 General | عام</div><div class="rtext">' + base_translation + '</div></div>',
                    unsafe_allow_html=True
                )
