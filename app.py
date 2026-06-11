import streamlit as st
import requests
import os
import difflib

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
.slang-override-box { background: #FFF3E0; border-left: 3px solid #E65100; border-radius: 0 8px 8px 0; padding: 10px 14px; font-size: 13px; color: #3E2723; margin-bottom: 1rem; }

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
        <span class="pill pill-muted">Slang Translator</span>
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
#  Languages
# ═══════════════════════════════════════════════════════════════════════════════
languages_dict = {
    "العربية": "ar", "English": "en", "Русский": "ru", "中文": "zh",
    "Deutsch": "de", "Español": "es", "Português": "pt", "한국어": "ko"
}

# ═══════════════════════════════════════════════════════════════════════════════
#  Domain Detection Engine — 15 DOMAINS
# ═══════════════════════════════════════════════════════════════════════════════
DOMAIN_KEYWORDS = {
    "political": {
        "ar": [
            "وزير", "حكومة", "مجلس", "وزارة", "برلمان", "سياسة", "دبلوماسي", "سفير", "معاهدة",
            "اتفاقية دولية", "حزب", "انتخابات", "تصويت", "أمن قومي", "استراتيجية وطنية",
            "بيان", "تصريح", "قمة", "مؤتمر", "جلسة", "تشريع", "دستور", "حقوق", "مواطن",
            "political", "government", "minister", "parliament", "diplomatic", "treaty",
            "election", "vote", "policy", "embassy", "summit", "legislation", "constitution",
            "foreign affairs", "national security", "coalition", "sanctions", "bilateral",
            "parliamentary", "senate", "congress", "diplomacy", "negotiation", "referendum"
        ],
        "emoji": "🏛️", "name_ar": "سياسي", "name_en": "Political", "color": "#E63946"
    },
    "legal": {
        "ar": [
            "عقد", "اتفاقية", "بند", "ملحق", "تعاقد", "قانون", "مرسوم", "لائحة", "نظام",
            "شرط", "جزاء", "تعويض", "مسؤولية", "ضمان", "FIDIC", "تحكيم", "دعوى", "محكمة",
            "قاضي", "حكم", "قرار", "تنظيمي", "ترخيص", "التزام", "حق", "ملكية", "إثبات",
            "contract", "agreement", "clause", "appendix", "legal", "stipulation", "liable",
            "penalty", "compensation", "arbitration", "court", "judgment", "license", "obligation",
            "terms and conditions", "binding", "jurisdiction", "warranty", "indemnity", "breach",
            "plaintiff", "defendant", "litigation", "statute", "regulation", "compliance"
        ],
        "emoji": "⚖️", "name_ar": "قانوني", "name_en": "Legal", "color": "#534AB7"
    },
    "economic": {
        "ar": [
            "اقتصاد", "مالية", "استثمار", "تكلفة", "سعر", "ميزانية", "عائد", "ربح", "خسارة",
            "تمويل", "قرض", "بنك", "سوق", "تجارة", "استيراد", "تصدير", "عمولة", "ضريبة",
            "رسوم", "تسعير", "عطاء", "مناقصة", "صرف", "عملة", "تضخم", "نمو", "تجاري",
            "economic", "financial", "investment", "cost", "budget", "revenue", "profit", "loss",
            "loan", "bank", "market", "trade", "import", "export", "tax", "fee", "pricing",
            "tender", "bid", "currency", "inflation", "growth", "GDP", "fiscal", "monetary",
            "stock", "exchange", "broker", "dividend", "shareholder", "audit", "accounting"
        ],
        "emoji": "📈", "name_ar": "اقتصادي", "name_en": "Economic", "color": "#F4A261"
    },
    "medical": {
        "ar": [
            "طبيب", "مستشفى", "علاج", "دواء", "جرعة", "مرض", "أعراض", "تشخيص", "فحص",
            "تحليل", "مختبر", "سريري", "جراحة", "عملية", "مريض", "صحة", "وباء", "تطعيم",
            "أشعة", "بكتيريا", "فيروس", "مناعة", "أنسجة", "أعضاء", "قلب", "كبد", "كلى",
            "doctor", "hospital", "treatment", "medication", "dose", "disease", "symptoms",
            "diagnosis", "laboratory", "clinical", "surgery", "patient", "health", "epidemic",
            "vaccine", "radiology", "bacteria", "virus", "immunity", "tissue", "cardiac", "renal",
            "pharmacy", "prescription", "physician", "nurse", "emergency", "ICU", "pharmaceutical"
        ],
        "emoji": "🏥", "name_ar": "طبي", "name_en": "Medical", "color": "#2A9D8F"
    },
    "scientific": {
        "ar": [
            "بحث", "دراسة", "مختبر", "تجربة", "فرضية", "نظرية", "علمي", "اكتشاف", "ابتكار",
            "تقنية", "تكنولوجيا", "تحليل", "بيانات", "إحصائية", "نموذج", "محاكاة", "خوارزمية",
            "ذكاء اصطناعي", "تعلم آلي", "طاقة", "فيزياء", "كيمياء", "بيولوجيا", "فلك",
            "research", "study", "experiment", "hypothesis", "theory", "scientific", "discovery",
            "innovation", "technology", "analysis", "data", "statistical", "model", "simulation",
            "algorithm", "AI", "machine learning", "physics", "chemistry", "biology", "astronomy",
            "quantum", "molecule", "particle", "observation", "peer review", "methodology"
        ],
        "emoji": "🔬", "name_ar": "علمي", "name_en": "Scientific", "color": "#264653"
    },
    "engineering": {
        "ar": [
            "هندسة", "إنشائي", "مدني", "معماري", "كهرباء", "ميكانيك", "صرف", "مياه", "طرق",
            "جسور", "أنفاق", "خرسانة", "حديد", "تسليح", "صب", "ردم", "حفر", "أساسات",
            "تصميم", "مخططات", "مواصفات", "بناء", "تشييد", "إشراف", "جودة", "اختبار", "مساحة",
            "engineering", "structural", "civil", "architectural", "electrical", "mechanical",
            "concrete", "rebar", "foundation", "excavation", "backfill", "pouring", "drawings",
            "specifications", "construction", "supervision", "quality", "inspection", "survey",
            "pipeline", "HVAC", "plumbing", "welding", "blueprint", "geotechnical", "load"
        ],
        "emoji": "🏗️", "name_ar": "هندسي", "name_en": "Engineering", "color": "#1D9E75"
    },
    "military": {
        "ar": [
            "جيش", "عسكري", "دفاع", "حرب", "معركة", "سلاح", "سلاح الجو", "بحرية", "دبابة",
            "صاروخ", "قنبلة", "قاعدة عسكرية", "تجنيد", "ضابط", "جندي", "رتبة", "عملية عسكرية",
            "military", "army", "defense", "war", "battle", "weapon", "air force", "navy", "tank",
            "missile", "bomb", "base", "recruitment", "officer", "soldier", "rank", "operation",
            "tactical", "strategic", "intelligence", "surveillance", "drone", "armored", "combat"
        ],
        "emoji": "🎖️", "name_ar": "عسكري", "name_en": "Military", "color": "#8B0000"
    },
    "educational": {
        "ar": [
            "مدرسة", "جامعة", "تعليم", "تدريس", "معلم", "أستاذ", "طالب", "دراسة", "مناهج",
            "امتحان", "اختبار", "شهادة", "بحث علمي", "رسالة", "أطروحة", "تدريب", "دورة",
            "school", "university", "education", "teaching", "teacher", "professor", "student",
            "curriculum", "exam", "test", "certificate", "thesis", "dissertation", "training",
            "course", "academic", "scholarship", "tuition", "faculty", "campus", "enrollment"
        ],
        "emoji": "📚", "name_ar": "تعليمي", "name_en": "Educational", "color": "#F4D03F"
    },
    "religious": {
        "ar": [
            "مسجد", "كنيسة", "معبد", "صلاة", "قرآن", "إنجيل", "حديث", "فقه", "شريعة",
            "حج", "عمرة", "صوم", "زكاة", "إمام", "خطيب", "دين", "عقيدة", "عبادة", "تفسير",
            "mosque", "church", "temple", "prayer", "Quran", "Bible", "hadith", "jurisprudence",
            "sharia", "pilgrimage", "fasting", "charity", "imam", "sermon", "religion", "faith",
            "worship", "exegesis", "theology", "monastery", "ritual", "sacred", "holy", "doctrine"
        ],
        "emoji": "🕌", "name_ar": "ديني", "name_en": "Religious", "color": "#6C3483"
    },
    "sports": {
        "ar": [
            "رياضة", "كرة القدم", "كرة السلة", "تنس", "سباحة", "جري", "ملعب", "نادي", "فريق",
            "لاعب", "مدرب", "حكم", "بطولة", "كأس", "مباراة", "تدريب", "لياقة", "مسابقة",
            "sports", "football", "soccer", "basketball", "tennis", "swimming", "running", "stadium",
            "club", "team", "player", "coach", "referee", "championship", "cup", "match", "fitness",
            "competition", "athlete", "olympic", "tournament", "league", "score", "goal", "medal"
        ],
        "emoji": "⚽", "name_ar": "رياضي", "name_en": "Sports", "color": "#E67E22"
    },
    "literary": {
        "ar": [
            "أدب", "قصة", "رواية", "شعر", "قصيدة", "كاتب", "مؤلف", "نص", "أسلوب", "بلاغة",
            "مجاز", "استعارة", "تشبيه", "فصل", "فقرة", "سرد", "حبكة", "شخصية", "حوار",
            "literature", "story", "novel", "poetry", "poem", "writer", "author", "text", "style",
            "rhetoric", "metaphor", "simile", "chapter", "paragraph", "narrative", "plot", "character",
            "dialogue", "prose", "fiction", "non-fiction", "anthology", "manuscript", "publisher"
        ],
        "emoji": "📖", "name_ar": "أدبي", "name_en": "Literary", "color": "#D81B60"
    },
    "it": {
        "ar": [
            "برمجة", "كود", "حاسوب", "كمبيوتر", "شبكة", "إنترنت", "برنامج", "تطبيق", "موقع",
            "خادم", "قاعدة بيانات", "أمن سيبراني", "هاكر", "ذكاء اصطناعي", "تعلم آلي", "سحابي",
            "programming", "code", "computer", "network", "internet", "software", "application", "website",
            "server", "database", "cybersecurity", "hacker", "AI", "machine learning", "cloud", "API",
            "frontend", "backend", "devops", "blockchain", "cryptocurrency", "domain", "hosting"
        ],
        "emoji": "💻", "name_ar": "تقني", "name_en": "IT / Tech", "color": "#00ACC1"
    },
    "environmental": {
        "ar": [
            "بيئة", "تلوث", "مناخ", "احتباس حراري", "طاقة متجددة", "شمسية", "رياح", "مياه جوفية",
            "غابة", "صحراء", "تصحر", "تنوع حيوي", "محمية", "طبيعة", "أوزون", "كربون",
            "environment", "pollution", "climate", "global warming", "renewable", "solar", "wind",
            "groundwater", "forest", "desert", "biodiversity", "reserve", "nature", "ozone", "carbon",
            "sustainability", "ecosystem", "greenhouse", "emission", "recycling", "conservation"
        ],
        "emoji": "🌿", "name_ar": "بيئي", "name_en": "Environmental", "color": "#43A047"
    },
    "agricultural": {
        "ar": [
            "زراعة", "مزرعة", "محصول", "قمح", "أرز", "ذرة", "أشجار", "ماء ري", "تربة",
            "سماد", "مبيد", "حصاد", "حصادة", "ثروة حيوانية", "مواشي", "أغنام", "دواجن", "سمك",
            "agriculture", "farm", "crop", "wheat", "rice", "corn", "trees", "irrigation", "soil",
            "fertilizer", "pesticide", "harvest", "combine", "livestock", "cattle", "sheep", "poultry",
            "fishery", "aquaculture", "greenhouse", "plowing", "seeding", "organic", "horticulture"
        ],
        "emoji": "🌾", "name_ar": "زراعي", "name_en": "Agricultural", "color": "#795548"
    },
    "media": {
        "ar": [
            "إعلام", "صحافة", "تلفزيون", "إذاعة", "صحيفة", "خبر", "تقرير", "مذيع", "مراسل",
            "تحقيق", "صحفي", "إعلان", "دعاية", "بث", "قناة", "برنامج إعلامي", "صحفي",
            "media", "journalism", "television", "radio", "newspaper", "news", "report", "anchor",
            "correspondent", "investigation", "journalist", "advertising", "broadcast", "channel",
            "press", "editorial", "column", "headline", "scoop", "documentary", "podcast"
        ],
        "emoji": "📺", "name_ar": "إعلامي", "name_en": "Media", "color": "#5E35B1"
    },
    "tourism": {
        "ar": [
            "سياحة", "فندق", "سفر", "رحلة", "مطار", "طيران", "جواز", "تأشيرة", "جولة",
            "أثر", "تاريخي", "معلم", "منتجع", "شاطئ", "جبل", "صحراء", "متحف", "تراث",
            "tourism", "hotel", "travel", "trip", "airport", "aviation", "passport", "visa", "tour",
            "monument", "historic", "landmark", "resort", "beach", "mountain", "desert", "museum",
            "heritage", "cruise", "destination", "itinerary", "booking", "check-in", "souvenir"
        ],
        "emoji": "✈️", "name_ar": "سياحي", "name_en": "Tourism", "color": "#00838F"
    },
    "general": {
        "ar": [],
        "emoji": "💬", "name_ar": "عام", "name_en": "General", "color": "#6B7280"
    }
}


def detect_domains(text):
    """Returns list of detected domain keys ONLY if found. Empty if nothing detected."""
    text_lower = text.lower()
    scores = {}
    for domain, data in DOMAIN_KEYWORDS.items():
        if domain == "general":
            continue
        score = 0
        for keyword in data["ar"]:
            count = text_lower.count(keyword.lower())
            if count > 0:
                weight = 1 + (len(keyword) / 50)
                score += count * weight
        if score > 0:
            scores[domain] = score
    if not scores:
        return []
    return sorted(scores, key=scores.get, reverse=True)
