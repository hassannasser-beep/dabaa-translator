import streamlit as st
import requests, os, json, sqlite3, re
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
#  DOMAIN DETECTION KEYWORDS
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
#  DOMAIN-SPECIFIC TRANSLATIONS — TEMPLATE-BASED (Compact)
# ═══════════════════════════════════════════════════════════════════════════════

LANG_CODES = ["ar", "en", "ru", "zh", "de", "es", "pt", "ko"]

DOMAIN_MODIFIERS = {
    "political":  {"ar": "سياسي", "en": "political", "ru": "политический", "zh": "政治", "de": "politisch", "es": "político", "pt": "político", "ko": "정치적"},
    "legal":      {"ar": "قانوني", "en": "legal", "ru": "юридический", "zh": "法律", "de": "rechtlich", "es": "legal", "pt": "legal", "ko": "법적"},
    "economic":   {"ar": "اقتصادي", "en": "economic", "ru": "экономический", "zh": "经济", "de": "wirtschaftlich", "es": "económico", "pt": "econômico", "ko": "경제적"},
    "medical":    {"ar": "طبي", "en": "medical", "ru": "медицинский", "zh": "医疗", "de": "medizinisch", "es": "médico", "pt": "médico", "ko": "의료"},
    "scientific": {"ar": "علمي", "en": "scientific", "ru": "научный", "zh": "科学", "de": "wissenschaftlich", "es": "científico", "pt": "científico", "ko": "과학적"},
    "engineering":{"ar": "هندسي", "en": "engineering", "ru": "инженерный", "zh": "工程", "de": "technisch", "es": "de ingeniería", "pt": "de engenharia", "ko": "공학적"},
    "military":   {"ar": "عسكري", "en": "military", "ru": "военный", "zh": "军事", "de": "militärisch", "es": "militar", "pt": "militar", "ko": "군사적"},
    "educational":{"ar": "تعليمي", "en": "educational", "ru": "образовательный", "zh": "教育", "de": "bildungs", "es": "educativo", "pt": "educacional", "ko": "교육적"},
    "religious":  {"ar": "ديني", "en": "religious", "ru": "религиозный", "zh": "宗教", "de": "religiös", "es": "religioso", "pt": "religioso", "ko": "종교적"},
    "sports":     {"ar": "رياضي", "en": "sports", "ru": "спортивный", "zh": "体育", "de": "sportlich", "es": "deportivo", "pt": "esportivo", "ko": "스포츠"},
    "literary":   {"ar": "أدبي", "en": "literary", "ru": "литературный", "zh": "文学", "de": "literarisch", "es": "literario", "pt": "literário", "ko": "문학적"},
    "it":         {"ar": "تقني", "en": "tech", "ru": "технический", "zh": "技术", "de": "technisch", "es": "tecnológico", "pt": "tecnológico", "ko": "기술적"},
    "environmental":{"ar": "بيئي", "en": "environmental", "ru": "экологический", "zh": "环境", "de": "Umwelt", "es": "ambiental", "pt": "ambiental", "ko": "환경"},
    "agricultural":{"ar": "زراعي", "en": "agricultural", "ru": "сельскохозяйственный", "zh": "农业", "de": "landwirtschaftlich", "es": "agrícola", "pt": "agrícola", "ko": "농업"},
    "media":      {"ar": "إعلامي", "en": "media", "ru": "медийный", "zh": "媒体", "de": "Medien", "es": "de medios", "pt": "de mídia", "ko": "미디어"},
    "tourism":    {"ar": "سياحي", "en": "tourism", "ru": "туристический", "zh": "旅游", "de": "Tourismus", "es": "turístico", "pt": "turístico", "ko": "관광"},
    "general":    {"ar": "عام", "en": "general", "ru": "общий", "zh": "一般", "de": "allgemein", "es": "general", "pt": "geral", "ko": "일반"},
}

# Word templates: base word + domain modifier patterns per language
WORD_TEMPLATES = {
    "contract": {
        "ar": {"base": "عقد", "special": {"political": "معاهدة دولية", "medical": "بروتوكول علاجي", "scientific": "بروتوكول بحثي", "military": "أمر عسكري", "religious": "عقد ديني", "sports": "عقد رياضي", "literary": "عقد أدبي"}},
        "en": {"base": "contract", "special": {"political": "international treaty", "medical": "treatment protocol", "scientific": "research protocol", "military": "military order", "religious": "religious covenant", "sports": "sports contract", "literary": "literary contract"}},
        "ru": {"base": "контракт", "special": {"political": "международный договор", "medical": "протокол лечения", "scientific": "исследовательский протокол", "military": "военный приказ", "religious": "религиозный договор", "sports": "спортивный контракт", "literary": "литературный договор"}},
        "zh": {"base": "合同", "special": {"political": "国际条约", "medical": "治疗方案", "scientific": "研究方案", "military": "军事命令", "religious": "宗教契约", "sports": "体育合同", "literary": "文学合同"}},
        "de": {"base": "Vertrag", "special": {"political": "internationaler Vertrag", "medical": "Behandlungsprotokoll", "scientific": "Forschungsprotokoll", "military": "militärischer Befehl", "religious": "religiöser Bund", "sports": "Sportvertrag", "literary": "Literaturvertrag"}},
        "es": {"base": "contrato", "special": {"political": "tratado internacional", "medical": "protocolo de tratamiento", "scientific": "protocolo de investigación", "military": "orden militar", "religious": "pacto religioso", "sports": "contrato deportivo", "literary": "contrato literario"}},
        "pt": {"base": "contrato", "special": {"political": "tratado internacional", "medical": "protocolo de tratamento", "scientific": "protocolo de pesquisa", "military": "ordem militar", "religious": "pacto religioso", "sports": "contrato esportivo", "literary": "contrato literário"}},
        "ko": {"base": "계약", "special": {"political": "국제 조약", "medical": "치료 프로토콜", "scientific": "연구 프로토콜", "military": "군사 명령", "religious": "종교 계약", "sports": "스포츠 계약", "literary": "문학 계약"}},
        "desc": "اتفاق ملزم بين طرفين"
    },
    "agreement": {
        "ar": {"base": "اتفاقية", "special": {"political": "اتفاقية دولية", "medical": "اتفاقية صحية", "scientific": "اتفاقية علمية", "military": "اتفاقية عسكرية", "religious": "اتفاقية شرعية", "sports": "اتفاقية رياضية", "literary": "اتفاقية أدبية"}},
        "en": {"base": "agreement", "special": {"political": "diplomatic treaty", "medical": "health agreement", "scientific": "scientific agreement", "military": "military agreement", "religious": "religious agreement", "sports": "sports agreement", "literary": "literary agreement"}},
        "ru": {"base": "соглашение", "special": {"political": "дипломатический договор", "medical": "медицинское соглашение", "scientific": "научное соглашение", "military": "военное соглашение", "religious": "религиозное соглашение", "sports": "спортивное соглашение", "literary": "литературное соглашение"}},
        "zh": {"base": "协议", "special": {"political": "外交条约", "medical": "健康协议", "scientific": "科学协议", "military": "军事协议", "religious": "宗教协议", "sports": "体育协议", "literary": "文学协议"}},
        "de": {"base": "Vereinbarung", "special": {"political": "diplomatischer Vertrag", "medical": "Gesundheitsvereinbarung", "scientific": "wissenschaftliche Vereinbarung", "military": "Militärabkommen", "religious": "religiöse Vereinbarung", "sports": "Sportvereinbarung", "literary": "Literaturvereinbarung"}},
        "es": {"base": "acuerdo", "special": {"political": "tratado diplomático", "medical": "acuerdo de salud", "scientific": "acuerdo científico", "military": "acuerdo militar", "religious": "acuerdo religioso", "sports": "acuerdo deportivo", "literary": "acuerdo literario"}},
        "pt": {"base": "acordo", "special": {"political": "tratado diplomático", "medical": "acordo de saúde", "scientific": "acordo científico", "military": "acordo militar", "religious": "acordo religioso", "sports": "acordo esportivo", "literary": "acordo literário"}},
        "ko": {"base": "협정", "special": {"political": "외교 조약", "medical": "건강 협정", "scientific": "과학 협정", "military": "군사 협정", "religious": "종교 협정", "sports": "스포츠 협정", "literary": "문학 협정"}},
        "desc": "تفاهم بين طرفين"
    },
    "law": {
        "ar": {"base": "قانون", "special": {"political": "تشريع", "legal": "نص قانوني", "engineering": "مواصفة فنية", "religious": "حكم شرعي", "literary": "قانون أدبي"}},
        "en": {"base": "law", "special": {"political": "legislation", "legal": "statute", "engineering": "technical specification", "religious": "religious law", "literary": "copyright law"}},
        "ru": {"base": "закон", "special": {"political": "законодательство", "legal": "указ", "engineering": "техническая спецификация", "religious": "религиозный закон", "literary": "авторское право"}},
        "zh": {"base": "法律", "special": {"political": "立法", "legal": "法规", "engineering": "技术规范", "religious": "宗教法", "literary": "版权法"}},
        "de": {"base": "Gesetz", "special": {"political": "Gesetzgebung", "legal": "Satzung", "engineering": "Technische Spezifikation", "religious": "Religionsrecht", "literary": "Urheberrecht"}},
        "es": {"base": "ley", "special": {"political": "legislación", "legal": "estatuto", "engineering": "especificación técnica", "religious": "ley religiosa", "literary": "derecho de autor"}},
        "pt": {"base": "lei", "special": {"political": "legislação", "legal": "estatuto", "engineering": "especificação técnica", "religious": "lei religiosa", "literary": "direito autoral"}},
        "ko": {"base": "법", "special": {"political": "입법", "legal": "법규", "engineering": "기술 사양", "religious": "종교법", "literary": "저작권법"}},
        "desc": "قاعدة ملزمة"
    },
    "judgment": {
        "ar": {"base": "حكم", "special": {"political": "قرار سياسي", "legal": "حكم قضائي", "medical": "تشخيص", "scientific": "نتيجة علمية", "religious": "فتوى", "sports": "قرار تحكيمي", "literary": "حكم أدبي"}},
        "en": {"base": "judgment", "special": {"political": "political decision", "legal": "court ruling", "medical": "diagnosis", "scientific": "scientific finding", "religious": "religious ruling", "sports": "referee decision", "literary": "literary critique"}},
        "ru": {"base": "суждение", "special": {"political": "политическое решение", "legal": "судебное решение", "medical": "диагноз", "scientific": "научный вывод", "religious": "религиозное постановление", "sports": "решение судьи", "literary": "литературная критика"}},
        "zh": {"base": "判断", "special": {"political": "政治决定", "legal": "法院判决", "medical": "诊断", "scientific": "科学发现", "religious": "宗教裁决", "sports": "裁判决定", "literary": "文学批评"}},
        "de": {"base": "Urteil", "special": {"political": "politische Entscheidung", "legal": "Gerichtsentscheidung", "medical": "Diagnose", "scientific": "wissenschaftlicher Befund", "religious": "religiöses Urteil", "sports": "Schiedsrichterentscheidung", "literary": "literarische Kritik"}},
        "es": {"base": "juicio", "special": {"political": "decisión política", "legal": "fallo judicial", "medical": "diagnóstico", "scientific": "hallazgo científico", "religious": "dictamen religioso", "sports": "decisión arbitral", "literary": "crítica literaria"}},
        "pt": {"base": "julgamento", "special": {"political": "decisão política", "legal": "decisão judicial", "medical": "diagnóstico", "scientific": "descoberta científica", "religious": "decisão religiosa", "sports": "decisão arbitral", "literary": "crítica literária"}},
        "ko": {"base": "판단", "special": {"political": "정치적 결정", "legal": "법원 판결", "medical": "진단", "scientific": "과학적 발견", "religious": "종교적 판결", "sports": "심판 결정", "literary": "문학 비평"}},
        "desc": "قرار أو رأي"
    },
    "decision": {
        "ar": {"base": "قرار", "special": {"political": "قرار سياسي", "legal": "قرار قضائي", "military": "أمر عمليات", "religious": "قرار ديني", "sports": "قرار رياضي", "literary": "قرار أدبي"}},
        "en": {"base": "decision", "special": {"political": "political resolution", "legal": "legal decision", "military": "operational order", "religious": "religious decision", "sports": "sports decision", "literary": "editorial decision"}},
        "ru": {"base": "решение", "special": {"political": "политическая резолюция", "legal": "юридическое решение", "military": "оперативный приказ", "religious": "религиозное решение", "sports": "спортивное решение", "literary": "редакционное решение"}},
        "zh": {"base": "决定", "special": {"political": "政治决议", "legal": "法律决定", "military": "作战命令", "religious": "宗教决定", "sports": "体育决定", "literary": "编辑决定"}},
        "de": {"base": "Entscheidung", "special": {"political": "politische Resolution", "legal": "rechtliche Entscheidung", "military": "Einsatzbefehl", "religious": "religiöse Entscheidung", "sports": "Sportentscheidung", "literary": "redaktionelle Entscheidung"}},
        "es": {"base": "decisión", "special": {"political": "resolución política", "legal": "decisión legal", "military": "orden operativa", "religious": "decisión religiosa", "sports": "decisión deportiva", "literary": "decisión editorial"}},
        "pt": {"base": "decisão", "special": {"political": "resolução política", "legal": "decisão legal", "military": "ordem operacional", "religious": "decisão religiosa", "sports": "decisão esportiva", "literary": "decisão editorial"}},
        "ko": {"base": "결정", "special": {"political": "정치적 결의", "legal": "법적 결정", "military": "작전 명령", "religious": "종교적 결정", "sports": "스포츠 결정", "literary": "편집 결정"}},
        "desc": "اختيار بين بدائل"
    },
    "treatment": {
        "ar": {"base": "علاج", "special": {"political": "معاملة دبلوماسية", "legal": "معاملة قانونية", "medical": "علاج طبي", "military": "معاملة عسكرية", "religious": "معاملة دينية"}},
        "en": {"base": "treatment", "special": {"political": "diplomatic treatment", "legal": "legal treatment", "medical": "medical treatment", "military": "military treatment", "religious": "religious treatment"}},
        "ru": {"base": "обращение", "special": {"political": "дипломатическое обращение", "legal": "юридическое обращение", "medical": "медицинское лечение", "military": "военное обращение", "religious": "религиозное обращение"}},
        "zh": {"base": "待遇", "special": {"political": "外交待遇", "legal": "法律待遇", "medical": "医疗治疗", "military": "军事待遇", "religious": "宗教待遇"}},
        "de": {"base": "Behandlung", "special": {"political": "diplomatische Behandlung", "legal": "rechtliche Behandlung", "medical": "medizinische Behandlung", "military": "militärische Behandlung", "religious": "religiöse Behandlung"}},
        "es": {"base": "trato", "special": {"political": "trato diplomático", "legal": "trato legal", "medical": "tratamiento médico", "military": "trato militar", "religious": "trato religioso"}},
        "pt": {"base": "tratamento", "special": {"political": "tratamento diplomático", "legal": "tratamento legal", "medical": "tratamento médico", "military": "tratamento militar", "religious": "tratamento religioso"}},
        "ko": {"base": "대우", "special": {"political": "외교적 대우", "legal": "법적 대우", "medical": "의료 치료", "military": "군사적 대우", "religious": "종교적 대우"}},
        "desc": "طريقة التعامل"
    },
    "analysis": {
        "ar": {"base": "تحليل", "special": {}},
        "en": {"base": "analysis", "special": {}},
        "ru": {"base": "анализ", "special": {}},
        "zh": {"base": "分析", "special": {}},
        "de": {"base": "Analyse", "special": {}},
        "es": {"base": "análisis", "special": {}},
        "pt": {"base": "análise", "special": {}},
        "ko": {"base": "분석", "special": {}},
        "desc": "فحص مفصل"
    },
    "report": {
        "ar": {"base": "تقرير", "special": {}},
        "en": {"base": "report", "special": {}},
        "ru": {"base": "отчет", "special": {}},
        "zh": {"base": "报告", "special": {}},
        "de": {"base": "Bericht", "special": {}},
        "es": {"base": "informe", "special": {}},
        "pt": {"base": "relatório", "special": {}},
        "ko": {"base": "보고서", "special": {}},
        "desc": "وثيقة رسمية"
    },
    "system": {
        "ar": {"base": "نظام", "special": {}},
        "en": {"base": "system", "special": {}},
        "ru": {"base": "система", "special": {}},
        "zh": {"base": "系统", "special": {}},
        "de": {"base": "System", "special": {}},
        "es": {"base": "sistema", "special": {}},
        "pt": {"base": "sistema", "special": {}},
        "ko": {"base": "시스템", "special": {}},
        "desc": "منظومة منظمة"
    },
    "plan": {
        "ar": {"base": "خطة", "special": {"medical": "خطة علاجية"}},
        "en": {"base": "plan", "special": {"medical": "treatment plan"}},
        "ru": {"base": "план", "special": {"medical": "план лечения"}},
        "zh": {"base": "计划", "special": {"medical": "治疗计划"}},
        "de": {"base": "Plan", "special": {"medical": "Behandlungsplan"}},
        "es": {"base": "plan", "special": {"medical": "plan de tratamiento"}},
        "pt": {"base": "plano", "special": {"medical": "plano de tratamento"}},
        "ko": {"base": "계획", "special": {"medical": "치료 계획"}},
        "desc": "تصور مستقبلي"
    },
    "project": {
        "ar": {"base": "مشروع", "special": {}},
        "en": {"base": "project", "special": {}},
        "ru": {"base": "проект", "special": {}},
        "zh": {"base": "项目", "special": {}},
        "de": {"base": "Projekt", "special": {}},
        "es": {"base": "proyecto", "special": {}},
        "pt": {"base": "projeto", "special": {}},
        "ko": {"base": "프로젝트", "special": {}},
        "desc": "عمل مخطط له"
    },
    "study": {
        "ar": {"base": "دراسة", "special": {}},
        "en": {"base": "study", "special": {}},
        "ru": {"base": "исследование", "special": {}},
        "zh": {"base": "研究", "special": {}},
        "de": {"base": "Studie", "special": {}},
        "es": {"base": "estudio", "special": {}},
        "pt": {"base": "estudo", "special": {}},
        "ko": {"base": "연구", "special": {}},
        "desc": "بحث مفصل"
    },
    "test": {
        "ar": {"base": "اختبار", "special": {"medical": "فحص طبي", "engineering": "اختبار هندسي"}},
        "en": {"base": "test", "special": {"medical": "medical test", "engineering": "engineering test"}},
        "ru": {"base": "тест", "special": {"medical": "медицинский тест", "engineering": "инженерный тест"}},
        "zh": {"base": "测试", "special": {"medical": "医学测试", "engineering": "工程测试"}},
        "de": {"base": "Test", "special": {"medical": "medizinischer Test", "engineering": "technischer Test"}},
        "es": {"base": "prueba", "special": {"medical": "prueba médica", "engineering": "prueba de ingeniería"}},
        "pt": {"base": "teste", "special": {"medical": "teste médico", "engineering": "teste de engenharia"}},
        "ko": {"base": "시험", "special": {"medical": "의학 시험", "engineering": "공학 시험"}},
        "desc": "تقييم الأداء"
    },
    "control": {
        "ar": {"base": "رقابة", "special": {"engineering": "ضبط", "it": "تحكم"}},
        "en": {"base": "control", "special": {"engineering": "engineering control", "it": "system control"}},
        "ru": {"base": "контроль", "special": {"engineering": "инженерный контроль", "it": "системный контроль"}},
        "zh": {"base": "控制", "special": {"engineering": "工程控制", "it": "系统控制"}},
        "de": {"base": "Kontrolle", "special": {"engineering": "technische Kontrolle", "it": "Systemkontrolle"}},
        "es": {"base": "control", "special": {"engineering": "control de ingeniería", "it": "control de sistema"}},
        "pt": {"base": "controle", "special": {"engineering": "controle de engenharia", "it": "controle de sistema"}},
        "ko": {"base": "통제", "special": {"engineering": "공학 통제", "it": "시스템 제어"}},
        "desc": "إدارة ومراقبة"
    },
    "management": {
        "ar": {"base": "إدارة", "special": {}},
        "en": {"base": "management", "special": {}},
        "ru": {"base": "управление", "special": {}},
        "zh": {"base": "管理", "special": {}},
        "de": {"base": "Management", "special": {}},
        "es": {"base": "gestión", "special": {}},
        "pt": {"base": "gerenciamento", "special": {}},
        "ko": {"base": "관리", "special": {}},
        "desc": "تنظيم الموارد"
    },
    "design": {
        "ar": {"base": "تصميم", "special": {}},
        "en": {"base": "design", "special": {}},
        "ru": {"base": "проектирование", "special": {}},
        "zh": {"base": "设计", "special": {}},
        "de": {"base": "Design", "special": {}},
        "es": {"base": "diseño", "special": {}},
        "pt": {"base": "design", "special": {}},
        "ko": {"base": "설계", "special": {}},
        "desc": "تخطيط الشكل"
    },
    "review": {
        "ar": {"base": "مراجعة", "special": {"legal": "تدقيق قانوني", "scientific": "مراجعة علمية"}},
        "en": {"base": "review", "special": {"legal": "legal review", "scientific": "peer review"}},
        "ru": {"base": "обзор", "special": {"legal": "юридическая проверка", "scientific": "научная рецензия"}},
        "zh": {"base": "审查", "special": {"legal": "法律审查", "scientific": "同行评审"}},
        "de": {"base": "Überprüfung", "special": {"legal": "rechtliche Überprüfung", "scientific": "wissenschaftliche Begutachtung"}},
        "es": {"base": "revisión", "special": {"legal": "revisión legal", "scientific": "revisión por pares"}},
        "pt": {"base": "revisão", "special": {"legal": "revisão legal", "scientific": "revisão por pares"}},
        "ko": {"base": "검토", "special": {"legal": "법적 검토", "scientific": "동료 검토"}},
        "desc": "تقييم نقدي"
    },
    "assessment": {
        "ar": {"base": "تقييم", "special": {"medical": "تقييم سريري", "environmental": "تقييم بيئي"}},
        "en": {"base": "assessment", "special": {"medical": "clinical assessment", "environmental": "environmental assessment"}},
        "ru": {"base": "оценка", "special": {"medical": "клиническая оценка", "environmental": "экологическая оценка"}},
        "zh": {"base": "评估", "special": {"medical": "临床评估", "environmental": "环境评估"}},
        "de": {"base": "Bewertung", "special": {"medical": "klinische Bewertung", "environmental": "Umweltbewertung"}},
        "es": {"base": "evaluación", "special": {"medical": "evaluación clínica", "environmental": "evaluación ambiental"}},
        "pt": {"base": "avaliação", "special": {"medical": "avaliação clínica", "environmental": "avaliação ambiental"}},
        "ko": {"base": "평가", "special": {"medical": "임상 평가", "environmental": "환경 평가"}},
        "desc": "تحليل الوضع"
    },
    "procedure": {
        "ar": {"base": "إجراء", "special": {"medical": "عملية جراحية", "legal": "إجراء قانوني"}},
        "en": {"base": "procedure", "special": {"medical": "surgical procedure", "legal": "legal procedure"}},
        "ru": {"base": "процедура", "special": {"medical": "хирургическая процедура", "legal": "юридическая процедура"}},
        "zh": {"base": "程序", "special": {"medical": "手术程序", "legal": "法律程序"}},
        "de": {"base": "Verfahren", "special": {"medical": "chirurgisches Verfahren", "legal": "rechtliches Verfahren"}},
        "es": {"base": "procedimiento", "special": {"medical": "procedimiento quirúrgico", "legal": "procedimiento legal"}},
        "pt": {"base": "procedimento", "special": {"medical": "procedimento cirúrgico", "legal": "procedimento legal"}},
        "ko": {"base": "절차", "special": {"medical": "수술 절차", "legal": "법적 절차"}},
        "desc": "خطوات منظمة"
    },
    "policy": {
        "ar": {"base": "سياسة", "special": {"political": "سياسة دولية", "economic": "سياسة مالية"}},
        "en": {"base": "policy", "special": {"political": "foreign policy", "economic": "fiscal policy"}},
        "ru": {"base": "политика", "special": {"political": "внешняя политика", "economic": "финансовая политика"}},
        "zh": {"base": "政策", "special": {"political": "外交政策", "economic": "财政政策"}},
        "de": {"base": "Politik", "special": {"political": "Außenpolitik", "economic": "Finanzpolitik"}},
        "es": {"base": "política", "special": {"political": "política exterior", "economic": "política fiscal"}},
        "pt": {"base": "política", "special": {"political": "política externa", "economic": "política fiscal"}},
        "ko": {"base": "정책", "special": {"political": "외교 정책", "economic": "재정 정책"}},
        "desc": "توجه رسمي"
    },
    "operation": {
        "ar": {"base": "عملية", "special": {"medical": "عملية جراحية", "military": "عملية عسكرية", "economic": "عملية تجارية"}},
        "en": {"base": "operation", "special": {"medical": "surgical operation", "military": "military operation", "economic": "business operation"}},
        "ru": {"base": "операция", "special": {"medical": "хирургическая операция", "military": "военная операция", "economic": "коммерческая операция"}},
        "zh": {"base": "操作", "special": {"medical": "手术", "military": "军事行动", "economic": "商业运营"}},
        "de": {"base": "Operation", "special": {"medical": "chirurgische Operation", "military": "militärische Operation", "economic": "Geschäftsoperation"}},
        "es": {"base": "operación", "special": {"medical": "operación quirúrgica", "military": "operación militar", "economic": "operación comercial"}},
        "pt": {"base": "operação", "special": {"medical": "operação cirúrgica", "military": "operação militar", "economic": "operação comercial"}},
        "ko": {"base": "작전", "special": {"medical": "수술", "military": "군사 작전", "economic": "사업 운영"}},
        "desc": "نشاط منظم"
    },
    "evaluation": {
        "ar": {"base": "تقييم", "special": {}},
        "en": {"base": "evaluation", "special": {}},
        "ru": {"base": "оценка", "special": {}},
        "zh": {"base": "评价", "special": {}},
        "de": {"base": "Evaluierung", "special": {}},
        "es": {"base": "evaluación", "special": {}},
        "pt": {"base": "avaliação", "special": {}},
        "ko": {"base": "평가", "special": {}},
        "desc": "تحديد القيمة"
    },
    "inspection": {
        "ar": {"base": "تفتيش", "special": {"engineering": "فحص هندسي", "medical": "فحص طبي"}},
        "en": {"base": "inspection", "special": {"engineering": "engineering inspection", "medical": "medical examination"}},
        "ru": {"base": "инспекция", "special": {"engineering": "инженерная инспекция", "medical": "медицинский осмотр"}},
        "zh": {"base": "检查", "special": {"engineering": "工程检查", "medical": "医学检查"}},
        "de": {"base": "Inspektion", "special": {"engineering": "technische Inspektion", "medical": "medizinische Untersuchung"}},
        "es": {"base": "inspección", "special": {"engineering": "inspección de ingeniería", "medical": "examen médico"}},
        "pt": {"base": "inspeção", "special": {"engineering": "inspeção de engenharia", "medical": "exame médico"}},
        "ko": {"base": "검사", "special": {"engineering": "공학 검사", "medical": "의학 검사"}},
        "desc": "فحص ميداني"
    },
    "survey": {
        "ar": {"base": "مسح", "special": {"engineering": "مساحة هندسية", "economic": "دراسة سوق"}},
        "en": {"base": "survey", "special": {"engineering": "engineering survey", "economic": "market survey"}},
        "ru": {"base": "обследование", "special": {"engineering": "инженерное обследование", "economic": "рыночное исследование"}},
        "zh": {"base": "调查", "special": {"engineering": "工程测量", "economic": "市场调查"}},
        "de": {"base": "Erhebung", "special": {"engineering": "technische Erhebung", "economic": "Markterhebung"}},
        "es": {"base": "encuesta", "special": {"engineering": "encuesta de ingeniería", "economic": "encuesta de mercado"}},
        "pt": {"base": "pesquisa", "special": {"engineering": "pesquisa de engenharia", "economic": "pesquisa de mercado"}},
        "ko": {"base": "조사", "special": {"engineering": "공학 조사", "economic": "시장 조사"}},
        "desc": "جمع بيانات"
    },
    "standard": {
        "ar": {"base": "معيار", "special": {"engineering": "مواصفة فنية", "legal": "معيار قانوني"}},
        "en": {"base": "standard", "special": {"engineering": "technical standard", "legal": "legal standard"}},
        "ru": {"base": "стандарт", "special": {"engineering": "технический стандарт", "legal": "правовой стандарт"}},
        "zh": {"base": "标准", "special": {"engineering": "技术标准", "legal": "法律标准"}},
        "de": {"base": "Standard", "special": {"engineering": "technischer Standard", "legal": "rechtlicher Standard"}},
        "es": {"base": "estándar", "special": {"engineering": "estándar técnico", "legal": "estándar legal"}},
        "pt": {"base": "padrão", "special": {"engineering": "padrão técnico", "legal": "padrão legal"}},
        "ko": {"base": "표준", "special": {"engineering": "기술 표준", "legal": "법적 표준"}},
        "desc": "مستوى مرجعي"
    },
    "protocol": {
        "ar": {"base": "بروتوكول", "special": {"political": "بروتوكول دبلوماسي", "medical": "بروتوكول علاجي", "scientific": "بروتوكول بحثي", "it": "بروتوكول شبكة"}},
        "en": {"base": "protocol", "special": {"political": "diplomatic protocol", "medical": "treatment protocol", "scientific": "research protocol", "it": "network protocol"}},
        "ru": {"base": "протокол", "special": {"political": "дипломатический протокол", "medical": "протокол лечения", "scientific": "исследовательский протокол", "it": "сетевой протокол"}},
        "zh": {"base": "协议", "special": {"political": "外交礼仪", "medical": "治疗方案", "scientific": "研究方案", "it": "网络协议"}},
        "de": {"base": "Protokoll", "special": {"political": "diplomatisches Protokoll", "medical": "Behandlungsprotokoll", "scientific": "Forschungsprotokoll", "it": "Netzwerkprotokoll"}},
        "es": {"base": "protocolo", "special": {"political": "protocolo diplomático", "medical": "protocolo de tratamiento", "scientific": "protocolo de investigación", "it": "protocolo de red"}},
        "pt": {"base": "protocolo", "special": {"political": "protocolo diplomático", "medical": "protocolo de tratamento", "scientific": "protocolo de pesquisa", "it": "protocolo de rede"}},
        "ko": {"base": "프로토콜", "special": {"political": "외교 프로토콜", "medical": "치료 프로토콜", "scientific": "연구 프로토콜", "it": "네트워크 프로토콜"}},
        "desc": "قواعد رسمية"
    },
}


def get_domain_translation(word, domain, target_lang):
    """Get domain-specific translation for a word."""
    word_lower = word.lower().strip()
    if word_lower not in WORD_TEMPLATES:
        return None

    template = WORD_TEMPLATES[word_lower]
    if target_lang not in template:
        return None

    lang_template = template[target_lang]
    base = lang_template["base"]
    special = lang_template.get("special", {})

    # Check if there's a special translation for this domain
    if domain in special:
        return special[domain]

    # Generate translation using domain modifier + base word
    modifier = DOMAIN_MODIFIERS.get(domain, DOMAIN_MODIFIERS["general"]).get(target_lang, "")

    # Language-specific combination patterns
    if target_lang == "ar":
        return f"{modifier} {base}"
    elif target_lang == "zh":
        return f"{modifier}{base}"
    elif target_lang == "de":
        return f"{modifier} {base}"
    elif target_lang in ["es", "pt"]:
        return f"{base} {modifier}"
    else:
        return f"{modifier} {base}"


def get_all_domain_translations(word, target_lang):
    """Get translations for all domains for a given word."""
    word_lower = word.lower().strip()
    if word_lower not in WORD_TEMPLATES:
        return None

    results = {}
    for domain in list(DOMAINS.keys()):
        trans = get_domain_translation(word, domain, target_lang)
        if trans:
            results[domain] = {
                "translation": trans,
                "desc": WORD_TEMPLATES[word_lower].get("desc", "")
            }
    return results

# ═══════════════════════════════════════════════════════════════════════════════
#  SITE SLANG DB — 60 Essential Terms
# ═══════════════════════════════════════════════════════════════════════════════
site_slang_db = {
    "slab": {"academic": "بلاطة خرسانية", "slang": "سقف / فرشة خرسانية", "desc": "الأسقف والمسطحات الخرسانية المسلحة."},
    "lean concrete": {"academic": "خرسانة عجيفة", "slang": "خرسانة نظافة", "desc": "طبقة خرسانية غير مسلحة أسفل القواعد."},
    "shop drawings": {"academic": "رسومات تنفيذية", "slang": "رسومات الورشة", "desc": "المخططات التفصيلية للتنفيذ الفعلي."},
    "as-built drawings": {"academic": "رسومات الواقع", "slang": "مخططات As-Built", "desc": "الرسومات النهائية التي تعكس ما نُفِّذ فعلياً."},
    "bill of quantities": {"academic": "جدول الكميات", "slang": "BOQ / جدول الكميات", "desc": "الوثيقة التعاقدية لتسعير خامات المشروع."},
    "shuttering": {"academic": "قوالب الصب", "slang": "الشدة / الطوبار", "desc": "الهيكل المؤقت لصب الخرسانة."},
    "formwork": {"academic": "قوالب الخرسانة", "slang": "الشدة الخشبية", "desc": "القوالب المؤقتة لصب الخرسانة."},
    "scaffolding": {"academic": "سقالات إنشائية", "slang": "السقالات / الأبراج", "desc": "الهياكل المعدنية للعمل على الارتفاعات."},
    "curing": {"academic": "معالجة الخرسانة", "slang": "سقي الخرسانة", "desc": "رش الخرسانة بالمياه بعد الصب."},
    "honeycombing": {"academic": "تعشيش الخرسانة", "slang": "خلايا النحل", "desc": "فراغات حصوية في سطح الخرسانة."},
    "kick-off meeting": {"academic": "اجتماع بدء المشروع", "slang": "اجتماع الإنطلاق", "desc": "أول اجتماع رسمي للمالك والاستشاري والمقاول."},
    "variation order": {"academic": "أمر تغيير", "slang": "VO / أمر التغيير", "desc": "أمر رسمي لتعديل بند خارج نطاق التعاقد."},
    "rebar": {"academic": "حديد التسليح", "slang": "السيخ / الحديد", "desc": "قضبان الفولاذ لتقوية الخرسانة."},
    "pouring": {"academic": "صب الخرسانة", "slang": "الصب / الجبس", "desc": "عملية إفراغ الخرسانة في القوالب."},
    "backfilling": {"academic": "أعمال الردم", "slang": "الردم / التراب", "desc": "إعادة ملء الحفر بالتربة."},
    "excavation": {"academic": "أعمال الحفر", "slang": "الحفر / التنقيب", "desc": "إزالة التربة للأساسات أو الأنفاق."},
    "subcontractor": {"academic": "مقاول من الباطن", "slang": "المقاول الصغير / الباطن", "desc": "مقاول يتعاقد مع المقاول الرئيسي."},
    "retention": {"academic": "استبقاء مالي", "slang": "الضمان المالي / المبلغ المحجوز", "desc": "نسبة من المستخلصات يحتجزها المالك كضمان."},
    "mobilization": {"academic": "تعبئة وإحضار", "slang": "النقل والإحضار", "desc": "نقل المعدات والعمالة إلى الموقع."},
    "demobilization": {"academic": "إخلاء الموقع", "slang": "الجمع والمغادرة", "desc": "إزالة المعدات والعمالة بعد الانتهاء."},
    "snag list": {"academic": "قائمة العيوب", "slang": "قائمة الملاحظات", "desc": "العيوب التي يجب إصلاحها قبل التسليم."},
    "practical completion": {"academic": "الانتهاء العملي", "slang": "التسليم المؤقت", "desc": "المشروع جاهز للاستخدام مع عيوب طفيفة."},
    "final completion": {"academic": "الانتهاء النهائي", "slang": "التسليم النهائي", "desc": "المرحلة النهائية بعد إصلاح جميع العيوب."},
    "dewatering": {"academic": "تخفيف المياه", "slang": "شفط المياه / تجفيف", "desc": "إزالة المياه من الموقع للحفر والبناء."},
    "pile": {"academic": "خوازيق", "slang": "الركائز العميقة", "desc": "عناصر إنشائية تنقل الأحمال للطبقات العميقة."},
    "pile cap": {"academic": "قبعة الخازوق", "slang": "القبعة / الغطاء", "desc": "الجزء الخرساني يربط الخوازيق بالعنصر العلوي."},
    "grade beam": {"academic": "كمرة ربط", "slang": "العصاية / كمرة التسوية", "desc": "كمرة تربط القواعد المنفصلة."},
    "raft foundation": {"academic": "قاعدة مسطحة", "slang": "الفرشة الخرسانية", "desc": "قاعدة خرسانية ضخمة تغطي كامل المبنى."},
    "strip footing": {"academic": "أساس شريطي", "slang": "الأساس المستمر", "desc": "أساس خرساني مستمر تحت الجدران."},
    "spread footing": {"academic": "أساس منفرد", "slang": "القاعدة المنفردة", "desc": "أساس خرساني منفرد لكل عمود."},
    "masonry": {"academic": "أعمال بناء", "slang": "البناء / البلوك", "desc": "بناء بالطوب أو البلوك أو الحجر."},
    "plastering": {"academic": "لياسة", "slang": "المحارة / البياض", "desc": "طبقة مونة على الجدران للتشطيب."},
    "tiling": {"academic": "تبليط", "slang": "السيراميك / البلاط", "desc": "تركيب بلاط السيراميك على الأرضيات."},
    "waterproofing": {"academic": "عزل مائي", "slang": "العزل / العازل", "desc": "حماية الأسطح والخزانات من تسرب المياه."},
    "false ceiling": {"academic": "سقف معلق", "slang": "الجبس بورد", "desc": "سقف ثانوي معلق تحت السقف الرئيسي."},
    "partitions": {"academic": "جدران فاصلة", "slang": "الفواصل / الجدران الخفيفة", "desc": "جدران غير حاملة لتقسيم الفراغات."},
    "cladding": {"academic": "واجهات خارجية", "slang": "الكادينج / الوجهات", "desc": "الطبقة الخارجية تغلف المبنى."},
    "curtain wall": {"academic": "واجهة زجاجية", "slang": "الكرتن وول", "desc": "واجهة زجاجية خفيفة معلقة على الهيكل."},
    "lintel": {"academic": "عتابة", "slang": "العتبة", "desc": "عنصر إنشائي يعلو الفتحات."},
    "MEP": {"academic": "ميكانيكا وكهرباء وسباكة", "slang": "الكهرباء والميكانيكا", "desc": "أعمال الميكانيكا والكهرباء والسباكة."},
    "HVAC": {"academic": "تكييف وتبريد", "slang": "التكييف / المكيفات", "desc": "أنظمة التدفئة والتهوية وتكييف الهواء."},
    "BMS": {"academic": "نظام إدارة مباني", "slang": "التحكم الذكي", "desc": "نظام إلكتروني لمراقبة أنظمة المبنى."},
    "BIM": {"academic": "نمذجة معلومات البناء", "slang": "النمذجة ثلاثية الأبعاد", "desc": "نماذج ثلاثية الأبعاد للمباني."},
    "site engineer": {"academic": "مهندس موقع", "slang": "مهندس الموقع", "desc": "المهندس المسؤول عن الإشراف في الموقع."},
    "resident engineer": {"academic": "مهندس مقيم", "slang": "المشرف المقيم", "desc": "مهندس الاستشاري المقيم في الموقع."},
    "foreman": {"academic": "مشرف عمال", "slang": "المعلم / الباش مهندس", "desc": "العامل المسؤول عن مجموعة عمال."},
    "steel fixer": {"academic": "حداد تسليح", "slang": "حداد الحديد / رابز", "desc": "العامل المتخصص في حديد التسليح."},
    "carpenter": {"academic": "نجار", "slang": "نجار الشدة", "desc": "العامل المتخصص في النجارة والقوالب."},
    "mason": {"academic": "بناء", "slang": "الحطاب", "desc": "العامل المتخصص في البناء بالطوب."},
    "plasterer": {"academic": "محارة", "slang": "المحارة", "desc": "العامل المتخصص في اللياسة."},
    "tiler": {"academic": "بلاط", "slang": "البلاط / السراميك", "desc": "العامل المتخصص في تركيب البلاط."},
    "electrician": {"academic": "كهربائي", "slang": "فني الكهرباء", "desc": "العامل المتخصص في التركيبات الكهربائية."},
    "plumber": {"academic": "سباك", "slang": "فني السباكة", "desc": "العامل المتخصص في التركيبات الصحية."},
    "welder": {"academic": "لحام", "slang": "اللحام", "desc": "العامل المتخصص في أعمال اللحام."},
    "crane operator": {"academic": "مشغل رافعة", "slang": "سائق الرافعة", "desc": "العامل المتخصص في تشغيل الرافعات."},
    "batching plant": {"academic": "محطة خلط خرسانة", "slang": "محطة الباطون", "desc": "المحطة التي تُنتج الخرسانة الجاهزة."},
    "concrete pump": {"academic": "مضخة خرسانة", "slang": "مضخة الباطون", "desc": "مضخة لنقل الخرسانة للأماكن المرتفعة."},
    "tower crane": {"academic": "رافعة برجية", "slang": "التوركرين", "desc": "رافعة عالية لرفع المواد في المشاريع."},
    "excavator": {"academic": "حفارة", "slang": "البوكلين", "desc": "آلية ثقيلة للحفر ونقل التربة."},
    "bulldozer": {"academic": "جرافة زحافة", "slang": "البلدوزر", "desc": "آلية ثقيلة لدفع التربة وتسوية الأرض."},
    "loader": {"academic": "محمل أمامي", "slang": "الشيول", "desc": "آلية لتحميل ونقل المواد."},
    "dump truck": {"academic": "شاحنة قلاب", "slang": "القلاب", "desc": "شاحنة لنقل التربة والمواد."},
    "vibrator": {"academic": "هزاز خرسانة", "slang": "الهزاز", "desc": "جهاز لاهتزاز الخرسانة لإخراج الهواء."},
    "compactor": {"academic": "مدحلة", "slang": "الرصاصة", "desc": "آلية لردم ودمك التربة."},
    "total station": {"academic": "محطة شاملة", "slang": "التوتال", "desc": "جهاز إلكتروني لقياس الزوايا والمسافات."},
    "GPS": {"academic": "نظام تحديد مواقع", "slang": "الجي بي اس", "desc": "نظام أقمار صناعية لتحديد المواقع."},
    "asphalt": {"academic": "إسفلت", "slang": "الزفت", "desc": "مادة لرصف الطرق."},
    "aggregate": {"academic": "ركام", "slang": "الحصى / الزلط", "desc": "مواد حبيبية للخرسانة والأسفلت."},
    "cement": {"academic": "أسمنت", "slang": "الإسمنت", "desc": "مادة رابطة لصناعة الخرسانة."},
    "ready-mix concrete": {"academic": "خرسانة جاهزة", "slang": "الباطون الجاهز", "desc": "خرسانة تُنتج في محطة وتوصل جاهزة."},
    "precast": {"academic": "خرسانة مسبقة الصنع", "slang": "البركاست", "desc": "عناصر خرسانية تُصنع في المصنع."},
    "shear wall": {"academic": "جدار قص", "slang": "جدار مقاوم للزلازل", "desc": "جدار خرساني سميك لمقاومة القوى الأفقية."},
    "core wall": {"academic": "جدار نواة", "slang": "اللب / النواة", "desc": "جدران خرسانية سميكة في مركز المبنى."},
    "transfer slab": {"academic": "بلاطة تحويل", "slang": "بلاطة النقل", "desc": "بلاطة ضخمة تنقل الأحمال للأعمدة السفلية."},
    "column": {"academic": "عمود", "slang": "العامود", "desc": "عنصر إنشائي رأسي ينقل الأحمال."},
    "beam": {"academic": "كمرة", "slang": "العارضة", "desc": "عنصر إنشائي أفقي يحمل الأحمال."},
    "footing": {"academic": "أساس", "slang": "القاعدة", "desc": "الجزء السفلي ينقل الأحمال للتربة."},
    "retaining wall": {"academic": "جدار استنادي", "slang": "جدار الصد", "desc": "جدار لمنع انهيار التربة."},
    "basement": {"academic": "سرداب", "slang": "البدروم", "desc": "الطوابق تحت سطح الأرض."},
    "green roof": {"academic": "سقف أخضر", "slang": "الحديقة على السطح", "desc": "سقف مغطى بالنباتات."},
    "solar panel": {"academic": "لوحة شمسية", "slang": "الألواح الشمسية", "desc": "لوحة تحول ضوء الشمس إلى كهرباء."},
    "thermal insulation": {"academic": "عزل حراري", "slang": "العازل الحراري", "desc": "مواد لتقليل انتقال الحرارة."},
    "fireproofing": {"academic": "حماية من حريق", "slang": "العازل الحراري المقاوم", "desc": "حماية العناصر المعدنية من الحريق."},
}

# ═══════════════════════════════════════════════════════════════════════════════
#  ABBREVIATIONS DICTIONARY
# ═══════════════════════════════════════════════════════════════════════════════
abbreviations_db = {
    "BOQ": {"full_en": "Bill of Quantities", "full_ru": "Ведомость объемов работ", "ar": "جدول الكميات", "desc": "وثيقة تعاقدية تحتوي على كميات وأسعار أعمال المشروع."},
    "RFI": {"full_en": "Request for Information", "full_ru": "Запрос информации", "ar": "طلب معلومات", "desc": "وثيقة يُرسلها المقاول للاستشاري لطلب توضيح."},
    "RFP": {"full_en": "Request for Proposal", "full_ru": "Запрос предложений", "ar": "طلب عرض أسعار", "desc": "وثيقة يُرسلها المالك للمقاولين لطلب عروض."},
    "RFQ": {"full_en": "Request for Quotation", "full_ru": "Запрос котировки", "ar": "طلب عرض سعر", "desc": "وثيقة لطلب أسعار محددة لبنود معينة."},
    "NCR": {"full_en": "Non-Conformance Report", "full_ru": "Отчет о несоответствии", "ar": "تقرير عدم مطابقة", "desc": "تقرير يسجل عدم مطابقة في الأعمال."},
    "CAR": {"full_en": "Corrective Action Report", "full_ru": "Отчет о корректирующих действиях", "ar": "تقرير إجراء تصحيحي", "desc": "تقرير يصف الإجراءات لتصحيح العيب."},
    "PAR": {"full_en": "Preventive Action Report", "full_ru": "Отчет о превентивных действиях", "ar": "تقرير إجراء وقائي", "desc": "تقرير يصف الإجراءات لمنع تكرار العيب."},
    "MS": {"full_en": "Method Statement", "full_ru": "Методическое заявление", "ar": "بيان منهجية", "desc": "وثيقة تصف طريقة تنفيذ عمل معين."},
    "RA": {"full_en": "Risk Assessment", "full_ru": "Оценка рисков", "ar": "تقييم مخاطر", "desc": "تحليل المخاطر في الموقع."},
    "ITP": {"full_en": "Inspection and Test Plan", "full_ru": "План инспекции и испытаний", "ar": "خطة فحص واختبار", "desc": "خطة تحدد مراحل الفحص والاختبار."},
    "WBS": {"full_en": "Work Breakdown Structure", "full_ru": "Структура разбиения работ", "ar": "هيكل تقسيم عمل", "desc": "تقسيم المشروع إلى أجزاء صغيرة."},
    "EPC": {"full_en": "Engineering, Procurement, Construction", "full_ru": "Инжиниринг, закупки, строительство", "ar": "تصميم وتوريد وتنفيذ", "desc": "عقد متكامل يشمل التصميم والتوريد والتنفيذ."},
    "FIDIC": {"full_en": "Fédération Internationale Des Ingénieurs-Conseils", "full_ru": "Международная федерация инженеров-консультантов", "ar": "الفيديك", "desc": "اتحاد دولي للمهندسين الاستشاريين — نموذج عقود دولية."},
    "DLP": {"full_en": "Defects Liability Period", "full_ru": "Период ответственности за дефекты", "ar": "فترة مسؤولية عن عيوب", "desc": "فترة يكون فيها المقاول مسؤولاً عن إصلاح العيوب."},
    "PPE": {"full_en": "Personal Protective Equipment", "full_ru": "Средства индивидуальной защиты", "ar": "معدات حماية شخصية", "desc": "معدات لحماية العمال من المخاطر."},
    "LOTO": {"full_en": "Lockout Tagout", "full_ru": "Блокировка и маркировка", "ar": "عزل ووسم", "desc": "إجراء لعزل مصادر الطاقة قبل الصيانة."},
    "HVAC": {"full_en": "Heating, Ventilation, and Air Conditioning", "full_ru": "Отопление, вентиляция и кондиционирование", "ar": "تدفئة وتهوية وتكييف", "desc": "أنظمة التدفئة والتهوية وتكييف الهواء."},
    "MEP": {"full_en": "Mechanical, Electrical, Plumbing", "full_ru": "Механические, электрические, сантехнические системы", "ar": "ميكانيكا وكهرباء وسباكة", "desc": "أنظمة الميكانيكا والكهرباء والسباكة."},
    "BMS": {"full_en": "Building Management System", "full_ru": "Система управления зданием", "ar": "نظام إدارة مباني", "desc": "نظام إلكتروني لمراقبة أنظمة المبنى."},
    "BIM": {"full_en": "Building Information Modeling", "full_ru": "Информационное моделирование зданий", "ar": "نمذجة معلومات البناء", "desc": "نماذج ثلاثية الأبعاد للمباني."},
    "GIS": {"full_en": "Geographic Information System", "full_ru": "Географическая информационная система", "ar": "نظام معلومات جغرافية", "desc": "نظام لتحليل البيانات الجغرافية."},
    "CAD": {"full_en": "Computer-Aided Design", "full_ru": "Автоматизированное проектирование", "ar": "تصميم بمساعدة حاسوب", "desc": "برامج لرسم المخططات الهندسية."},
    "CAM": {"full_en": "Computer-Aided Manufacturing", "full_ru": "Автоматизированное производство", "ar": "تصنيع بمساعدة حاسوب", "desc": "برامج للتحكم في الآلات الصناعية."},
    "CAE": {"full_en": "Computer-Aided Engineering", "full_ru": "Инженерный анализ с помощью ЭВМ", "ar": "هندسة بمساعدة حاسوب", "desc": "برامج لتحليل الأداء الهندسي."},
    "FEA": {"full_en": "Finite Element Analysis", "full_ru": "Метод конечных элементов", "ar": "تحليل عناصر منتهية", "desc": "طريقة رقمية لتحليل الإجهادات."},
    "CFD": {"full_en": "Computational Fluid Dynamics", "full_ru": "Вычислительная гидродинамика", "ar": "ديناميكا حسابية للموائع", "desc": "محاكاة رقمية لتدفق السوائل."},
    "LEED": {"full_en": "Leadership in Energy and Environmental Design", "full_ru": "Лидерство в энергетике и экологическом дизайне", "ar": "قيادة في الطاقة والتصميم البيئي", "desc": "نظام اعتماد دولي للمباني المستدامة."},
    "LCA": {"full_en": "Life Cycle Assessment", "full_ru": "Оценка жизненного цикла", "ar": "تقييم دورة حياة", "desc": "تحليل الأثر البيئي طوال عمر المبنى."},
    "EPD": {"full_en": "Environmental Product Declaration", "full_ru": "Экологическая декларация продукта", "ar": "إعلان بيئي منتج", "desc": "وثيقة توضح الأثر البيئي للمنتج."},
    "ISO": {"full_en": "International Organization for Standardization", "full_ru": "Международная организация по стандартизации", "ar": "منظمة المواصفات الدولية", "desc": "منظمة دولية لوضع المعايير."},
    "OSHA": {"full_en": "Occupational Safety and Health Administration", "full_ru": "Управление по охране труда", "ar": "إدارة السلامة والصحة المهنية", "desc": "إدارة أمريكية لمعايير السلامة."},
    "KPI": {"full_en": "Key Performance Indicator", "full_ru": "Ключевой показатель эффективности", "ar": "مؤشر أداء رئيسي", "desc": "مؤشر لقياس أداء المشروع."},
    "SLA": {"full_en": "Service Level Agreement", "full_ru": "Соглашение об уровне обслуживания", "ar": "اتفاقية مستوى خدمة", "desc": "اتفاقية تحدد مستوى الخدمة المطلوب."},
    "MOU": {"full_en": "Memorandum of Understanding", "full_ru": "Меморандум о взаимопонимании", "ar": "مذكرة تفاهم", "desc": "وثيقة تُعدّل نية الأطراف للتعاون."},
    "NDA": {"full_en": "Non-Disclosure Agreement", "full_ru": "Соглашение о неразглашении", "ar": "اتفاقية عدم إفشاء", "desc": "اتفاقية لحماية المعلومات السرية."},
    "SOW": {"full_en": "Scope of Work", "full_ru": "Объем работ", "ar": "نطاق العمل", "desc": "وثيقة تحدد نطاق الأعمال المطلوبة."},
    "PM": {"full_en": "Project Management", "full_ru": "Управление проектами", "ar": "إدارة مشروع", "desc": "إدارة المشروع بأكمله."},
    "QM": {"full_en": "Quality Management", "full_ru": "Управление качеством", "ar": "إدارة جودة", "desc": "إدارة نظام الجودة في المشروع."},
    "HSE": {"full_en": "Health, Safety, Environment", "full_ru": "Охрана труда, безопасность, экология", "ar": "صحة وسلامة وبيئة", "desc": "نظام إدارة الصحة والسلامة والبيئة."},
    "QA": {"full_en": "Quality Assurance", "full_ru": "Обеспечение качества", "ar": "ضمان جودة", "desc": "أنشطة تضمن تحقيق الجودة المطلوبة."},
    "QC": {"full_en": "Quality Control", "full_ru": "Контроль качества", "ar": "رقابة جودة", "desc": "فحص واختبار الأعمال للتأكد من الجودة."},
    "CP": {"full_en": "Critical Path", "full_ru": "Критический путь", "ar": "مسار حرج", "desc": "سلسلة الأنشطة التي تحدد مدة المشروع."},
    "CPM": {"full_en": "Critical Path Method", "full_ru": "Метод критического пути", "ar": "طريقة المسار الحرج", "desc": "طريقة لجدولة المشروع."},
    "Gantt": {"full_en": "Gantt Chart", "full_ru": "Диаграмма Ганта", "ar": "مخطط جانت", "desc": "رسم بياني لجدولة المشروع."},
    "SPI": {"full_en": "Schedule Performance Index", "full_ru": "Индекс выполнения графика", "ar": "مؤشر جدولة", "desc": "مؤشر يقيس التقدم في الجدولة."},
    "CPI": {"full_en": "Cost Performance Index", "full_ru": "Индекс выполнения затрат", "ar": "مؤشر تكلفة", "desc": "مؤشر يقيس كفاءة التكلفة."},
    "EAC": {"full_en": "Estimate at Completion", "full_ru": "Оценка при завершении", "ar": "تقدير عند إنجاز", "desc": "تقدير التكلفة الإجمالية عند الانتهاء."},
    "ETC": {"full_en": "Estimate to Complete", "full_ru": "Оценка для завершения", "ar": "تقدير للانتهاء", "desc": "تقدير التكلفة المتبقية."},
    "RAM": {"full_en": "Responsibility Assignment Matrix", "full_ru": "Матрица распределения ответственности", "ar": "مصفوفة مسؤولية", "desc": "جدول يوضح المسؤوليات بين الفريق."},
    "RACI": {"full_en": "Responsible, Accountable, Consulted, Informed", "full_ru": "Ответственный, подотчетный, консультируемый, информируемый", "ar": "مصفوفة RACI", "desc": "مصفوفة تحدد المسؤوليات."},
    "PMBOK": {"full_en": "Project Management Body of Knowledge", "full_ru": "Свод знаний по управлению проектами", "ar": "دليل إدارة المشاريع", "desc": "دليل معايير إدارة المشاريع."},
    "PRINCE2": {"full_en": "Projects IN Controlled Environments", "full_ru": "Проекты в контролируемых средах", "ar": "مشاريع في بيئات مراقبة", "desc": "منهجية إدارة مشاريع شائعة في المملكة المتحدة."},
    "Agile": {"full_en": "Agile Project Management", "full_ru": "Гибкое управление проектами", "ar": "إدارة مشاريع رشيقة", "desc": "منهجية إدارة مشاريع مرنة."},
    "Scrum": {"full_en": "Scrum Framework", "full_ru": "Фреймворк Скрам", "ar": "إطار سكروم", "desc": "إطار عمل لإدارة المشاريع بشكل رشيق."},
    "Kanban": {"full_en": "Kanban Method", "full_ru": "Метод Канбан", "ar": "طريقة كانبان", "desc": "طريقة لإدارة سير العمل."},
    "Lean": {"full_en": "Lean Construction", "full_ru": "Бережливое строительство", "ar": "بناء هزيل", "desc": "منهجية لتقليل الهدر في البناء."},
    "Six Sigma": {"full_en": "Six Sigma Quality", "full_ru": "Шесть сигм", "ar": "ستة سيجما", "desc": "منهجية لتحسين الجودة وتقليل العيوب."},
    "TQM": {"full_en": "Total Quality Management", "full_ru": "Всеобщее управление качеством", "ar": "إدارة الجودة الشاملة", "desc": "نظام إداري شامل للجودة."},
    "ISO 9001": {"full_en": "ISO 9001 Quality Management", "full_ru": "ISO 9001 Управление качеством", "ar": "ايزو 9001", "desc": "معيار دولي لإدارة الجودة."},
    "ISO 14001": {"full_en": "ISO 14001 Environmental Management", "full_ru": "ISO 14001 Экологический менеджмент", "ar": "ايزو 14001", "desc": "معيار دولي لإدارة البيئة."},
    "ISO 45001": {"full_en": "ISO 45001 Safety Management", "full_ru": "ISO 45001 Управление безопасностью", "ar": "ايزو 45001", "desc": "معيار دولي للسلامة والصحة المهنية."},
    "CE": {"full_en": "Conformité Européenne", "full_ru": "Европейское соответствие", "ar": "علامة ال conformity الأوروبية", "desc": "علامة تُوضع على المنتجات المطابقة للمعايير الأوروبية."},
    "ASTM": {"full_en": "American Society for Testing and Materials", "full_ru": "Американское общество по испытаниям материалов", "ar": "الجمعية الأمريكية لاختبار المواد", "desc": "منظمة تضع معايير اختبار المواد."},
    "ANSI": {"full_en": "American National Standards Institute", "full_ru": "Американский национальный институт стандартов", "ar": "المعهد الأمريكي للمعايير الوطنية", "desc": "منظمة تضع معايير أمريكية."},
    "BS": {"full_en": "British Standard", "full_ru": "Британский стандарт", "ar": "معيار بريطاني", "desc": "معيار بريطاني للمنتجات والخدمات."},
    "DIN": {"full_en": "Deutsches Institut für Normung", "full_ru": "Немецкий институт стандартизации", "ar": "المعهد الألماني للتوحيد القياسي", "desc": "معيار ألماني للمنتجات والخدمات."},
    "GOST": {"full_en": "Gosudarstvennyy Standart (Russian Standard)", "full_ru": "Государственный стандарт", "ar": "معيار روسي حكومي", "desc": "معيار روسي للمنتجات والخدمات."},
    "SNiP": {"full_en": "Stroitelnye Normy i Pravila (Russian Building Code)", "full_ru": "Строительные нормы и правила", "ar": "القواعد والمعايير الإنشائية الروسية", "desc": "معايير البناء الروسية."},
    "SP": {"full_en": "Svod Pravil (Russian Code of Practice)", "full_ru": "Свод правил", "ar": "مجموعة القواعد الروسية", "desc": "قواعد ممارسة البناء الروسية."},
    "EN": {"full_en": "European Standard", "full_ru": "Европейский стандарт", "ar": "معيار أوروبي", "desc": "معيار أوروبي للمنتجات والخدمات."},
    "IEC": {"full_en": "International Electrotechnical Commission", "full_ru": "Международная электротехническая комиссия", "ar": "اللجنة الكهروتقنية الدولية", "desc": "منظمة دولية للمعايير الكهربائية."},
    "IEEE": {"full_en": "Institute of Electrical and Electronics Engineers", "full_ru": "Институт инженеров по электротехнике и электронике", "ar": "معهد مهندسي الكهرباء والإلكترونيات", "desc": "منظمة مهنية للمهندسين الكهربائيين."},
    "ASHRAE": {"full_en": "American Society of Heating, Refrigerating and Air-Conditioning Engineers", "full_ru": "Американское общество инженеров по отоплению, охлаждению и кондиционированию", "ar": "الجمعية الأمريكية لمهندسي التدفئة والتبريد", "desc": "منظمة لمعايير HVAC."},
    "NFPA": {"full_en": "National Fire Protection Association", "full_ru": "Национальная ассоциация пожарной защиты", "ar": "الجمعية الوطنية للحماية من الحريق", "desc": "منظمة لمعايير الحماية من الحريق."},
    "ADA": {"full_en": "Americans with Disabilities Act", "full_ru": "Закон об американцах с ограниченными возможностями", "ar": "قانون الأمريكيين ذوي الإعاقة", "desc": "قانون أمريكي لإمكانية الوصول للمعاقين."},
    "IBC": {"full_en": "International Building Code", "full_ru": "Международный строительный кодекс", "ar": "الكود الدولي للبناء", "desc": "كود بناء دولي شائع في الولايات المتحدة."},
    "ACI": {"full_en": "American Concrete Institute", "full_ru": "Американский бетонный институт", "ar": "المعهد الأمريكي للخرسانة", "desc": "منظمة لمعايير الخرسانة."},
    "AISC": {"full_en": "American Institute of Steel Construction", "full_ru": "Американский институт строительной стали", "ar": "المعهد الأمريكي لبناء الصلب", "desc": "منظمة لمعايير البناء الفولاذي."},
    "AWS": {"full_en": "American Welding Society", "full_ru": "Американское сварочное общество", "ar": "الجمعية الأمريكية للحام", "desc": "منظمة لمعايير اللحام."},
    "ASME": {"full_en": "American Society of Mechanical Engineers", "full_ru": "Американское общество инженеров-механиков", "ar": "الجمعية الأمريكية للمهندسين الميكانيكيين", "desc": "منظمة لمعايير الميكانيكا."},
    "API": {"full_en": "American Petroleum Institute", "full_ru": "Американский нефтяной институт", "ar": "المعهد الأمريكي للبترول", "desc": "منظمة لمعايير البترول والغاز."},
    "NEC": {"full_en": "National Electrical Code", "full_ru": "Национальный электротехнический кодекс", "ar": "الكود الكهربائي الوطني", "desc": "كود كهربائي أمريكي."},
    "LEED": {"full_en": "Leadership in Energy and Environmental Design", "full_ru": "Лидерство в энергетике и экологическом дизайне", "ar": "الريادة في الطاقة والتصميم البيئي", "desc": "نظام اعتماد دولي للمباني المستدامة."},
    "BREEAM": {"full_en": "Building Research Establishment Environmental Assessment Method", "full_ru": "Метод оценки экологических качеств зданий", "ar": "طريقة تقييم البيئة للمباني", "desc": "نظام اعتماد بريطاني للمباني المستدامة."},
    "WELL": {"full_en": "WELL Building Standard", "full_ru": "Стандарт зданий WELL", "ar": "معيار WELL للمباني", "desc": "نظام اعتماد يركز على صحة ورفاهية السكان."},
    "AHU": {"full_en": "Air Handling Unit", "full_ru": "Воздухообрабатывающая установка", "ar": "وحدة معالجة هواء", "desc": "وحدة كبيرة لتكييف وتنقية الهواء."},
    "FCU": {"full_en": "Fan Coil Unit", "full_ru": "Фанкойл", "ar": "وحدة مروحة ملفية", "desc": "وحدة صغيرة للتكييف في الغرف."},
    "UPS": {"full_en": "Uninterruptible Power Supply", "full_ru": "Источник бесперебойного питания", "ar": "نظام طاقة احتياطي", "desc": "نظام يوفر طاقة احتياطية عند انقطاع الكهرباء."},
    "PV": {"full_en": "Photovoltaic", "full_ru": "Фотоэлектрический", "ar": "كهروضوئي", "desc": "تقنية لتحويل ضوء الشمس إلى كهرباء."},
    "RO": {"full_en": "Reverse Osmosis", "full_ru": "Обратный осмос", "ar": "التناضح العكسي", "desc": "تقنية لتحلية المياه."},
    "UV": {"full_en": "Ultraviolet Disinfection", "full_ru": "Ультрафиолетовая дезинфекция", "ar": "تعقيم بالأشعة فوق البنفسجية", "desc": "تعقيم المياه باستخدام الأشعة فوق البنفسجية."},
    "MBR": {"full_en": "Membrane Bioreactor", "full_ru": "Мембранный биореактор", "ar": "مفاعل غشائي حيوي", "desc": "تقنية متقدمة لمعالجة مياه الصرف."},
    "EDI": {"full_en": "Electrodeionization", "full_ru": "Электродеионизация", "ar": "إزالة الأيونات بالكهرباء", "desc": "تقنية لإنتاج مياه عالية النقاء."},
    "GAC": {"full_en": "Granular Activated Carbon", "full_ru": "Гранулированный активированный уголь", "ar": "كربون منشط حبيبي", "desc": "مادة لإزالة المواد العضوية من المياه."},
    "CF": {"full_en": "Coagulation and Flocculation", "full_ru": "Коагуляция и флокуляция", "ar": "التخثر والتكتل", "desc": "عملية لإزالة المواد العالقة من المياه."},
    "Sedimentation": {"full_en": "Sedimentation", "full_ru": "Осаждение", "ar": "الترسيب", "desc": "عملية لإزالة المواد الصلبة من المياه بالترسيب."},
    "Filtration": {"full_en": "Filtration", "full_ru": "Фильтрация", "ar": "الترشيح", "desc": "عملية لإزالة المواد الصلبة من المياه بالترشيح."},
    "Disinfection": {"full_en": "Disinfection", "full_ru": "Дезинфекция", "ar": "التعقيم", "desc": "عملية لقتل البكتيريا في المياه."},
    "Softening": {"full_en": "Water Softening", "full_ru": "Умягчение воды", "ar": "تليين المياه", "desc": "إزالة العسر (الكالسيوم والمغنيسيوم) من المياه."},
    "Desalination": {"full_en": "Desalination", "full_ru": "Опреснение", "ar": "تحلية المياه", "desc": "إزالة الملح من مياه البحر."},
    "Green Roof": {"full_en": "Green Roof", "full_ru": "Зеленая крыша", "ar": "سقف أخضر", "desc": "سقف مغطى بالنباتات لامتصاص المياه."},
    "Cool Roof": {"full_en": "Cool Roof", "full_ru": "Холодная крыша", "ar": "سقف بارد", "desc": "سقف يعكس أشعة الشمس."},
    "Urban Heat Island": {"full_en": "Urban Heat Island", "full_ru": "Городской остров тепла", "ar": "جزيرة حرارية", "desc": "ظاهرة ارتفاع الحرارة في المدن."},
    "Albedo": {"full_en": "Albedo", "full_ru": "Альбедо", "ar": "البياض", "desc": "نسبة الضوء المنعكس من السطح."},
    "Daylight Factor": {"full_en": "Daylight Factor", "full_ru": "Коэффициент дневного света", "ar": "معامل الإضاءة الطبيعية", "desc": "نسبة الإضاءة الطبيعية داخل المبنى."},
    "Color Rendering Index": {"full_en": "Color Rendering Index", "full_ru": "Индекс цветопередачи", "ar": "مؤشر إعادة إنتاج الألوان", "desc": "مقياس لجودة إعادة إنتاج الألوان."},
    "Luminous Efficacy": {"full_en": "Luminous Efficacy", "full_ru": "Световая эффективность", "ar": "الفعالية الضوئية", "desc": "كفاءة المصدر الضوئي في إنتاج الضوء."},
    "Illuminance": {"full_en": "Illuminance", "full_ru": "Освещенность", "ar": "الإضاءة", "desc": "كمية الضوء الساقط على السطح."},
    "Luminance": {"full_en": "Luminance", "full_ru": "Яркость", "ar": "السطوع", "desc": "كمية الضوء المنعكس من السطح."},
    "Glare Index": {"full_en": "Glare Index", "full_ru": "Индекс бликов", "ar": "مؤشر الوهج", "desc": "مقياس لتقييم الوهج في المبنى."},
    "Unified Glare Rating": {"full_en": "Unified Glare Rating", "full_ru": "Единая оценка бликов", "ar": "تقييم الوهج الموحد", "desc": "مقياس دولي لتقييم الوهج."},
}

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
    best_match, best_dist = None, max_distance + 1
    for term in site_slang_db:
        dist = calculate_distance(word_lower, term.lower())
        if dist < best_dist:
            best_dist = dist
            best_match = term
    if best_match and best_dist <= max_distance:
        return best_match
    return None

def detect_abbreviations(text):
    found = []
    text_upper = text.upper()
    for abbrev, data in abbreviations_db.items():
        if abbrev.upper() in text_upper:
            found.append((abbrev, data))
    return found

def detect_abbreviations_from_words(text):
    words = text.split()
    found = []
    for i in range(len(words)):
        for j in range(i+1, min(i+6, len(words)+1)):
            phrase = " ".join(words[i:j])
            first_letters = "".join([w[0].upper() for w in words[i:j] if w])
            if first_letters in abbreviations_db:
                found.append((first_letters, abbreviations_db[first_letters], phrase))
    return found


def build_formula(text, domain, target_lang):
    """Build domain-specific translation by replacing keywords."""
    if not domain or domain == "general":
        return text

    result = text
    # Replace words that have domain-specific translations
    for word in WORD_TEMPLATES:
        word_lower = word.lower()
        if word_lower in result.lower():
            domain_trans = get_domain_translation(word, domain, target_lang)
            if domain_trans:
                # Replace the word (case-insensitive)
                result = re.sub(r'\b' + re.escape(word) + r'\b', domain_trans, result, flags=re.IGNORECASE)

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
    abbrevs = detect_abbreviations(input_text)
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
    slang_found = []
    for term, data in site_slang_db.items():
        if term.lower() in input_text.lower():
            slang_found.append((term, data))
    if slang_found:
        st.markdown('<div class="slang-wrap"><div class="slang-head"><span class="slang-head-txt">🏗️ SITE SLANG DETECTED</span></div><table class="slang-table"><tr><th>Term</th><th>Academic</th><th>Site Slang</th><th>Description</th></tr>', unsafe_allow_html=True)
        for term, data in slang_found:
            st.markdown(f'<tr><td class="term-cell">{term}</td><td>{data["academic"]}</td><td class="site-cell">{data["slang"]}</td><td>{data["desc"]}</td></tr>', unsafe_allow_html=True)
        st.markdown('</table></div>', unsafe_allow_html=True)

    # Did-you-mean for slang
    words = input_text.split()
    for word in words:
        closest = find_closest_slang(word)
        if closest and closest.lower() != word.lower():
            st.markdown(f'<div class="dym-box">Did you mean: <b>{closest}</b> (site slang for: {site_slang_db[closest]["academic"]})?</div>', unsafe_allow_html=True)
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

                if is_single_word and input_word in WORD_TEMPLATES:
                    # Show all domain translations for this word
                    st.markdown("---")
                    st.markdown("### 🎯 Domain-Specific Meanings")
                    st.markdown(f"*Showing different meanings for '{input_text.strip()}' across all domains:*")

                    all_trans = get_all_domain_translations(input_word, target_lang)
                    if all_trans:
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
