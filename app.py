import streamlit as st
import requests
import os

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
            "foreign affairs", "national security", "coalition", "sanctions", "bilateral"
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
            "terms and conditions", "binding", "jurisdiction", "warranty", "indemnity", "breach"
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
            "tender", "bid", "currency", "inflation", "growth", "GDP", "fiscal", "monetary"
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
            "vaccine", "radiology", "bacteria", "virus", "immunity", "tissue", "cardiac", "renal"
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
            "algorithm", "AI", "machine learning", "physics", "chemistry", "biology", "astronomy"
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
            "specifications", "construction", "supervision", "quality", "inspection", "survey"
        ],
        "emoji": "🏗️", "name_ar": "هندسي", "name_en": "Engineering", "color": "#1D9E75"
    },
    "military": {
        "ar": [
            "جيش", "عسكري", "دفاع", "حرب", "معركة", "سلاح", "سلاح الجو", "بحرية", "دبابة",
            "صاروخ", "قنبلة", "قاعدة عسكرية", "تجنيد", "ضابط", "جندي", "رتبة", "عملية عسكرية",
            "military", "army", "defense", "war", "battle", "weapon", "air force", "navy", "tank",
            "missile", "bomb", "base", "recruitment", "officer", "soldier", "rank", "operation"
        ],
        "emoji": "🎖️", "name_ar": "عسكري", "name_en": "Military", "color": "#8B0000"
    },
    "educational": {
        "ar": [
            "مدرسة", "جامعة", "تعليم", "تدريس", "معلم", "أستاذ", "طالب", "دراسة", "مناهج",
            "امتحان", "اختبار", "شهادة", "بحث علمي", "رسالة", "أطروحة", "تدريب", "دورة",
            "school", "university", "education", "teaching", "teacher", "professor", "student",
            "curriculum", "exam", "test", "certificate", "thesis", "dissertation", "training"
        ],
        "emoji": "📚", "name_ar": "تعليمي", "name_en": "Educational", "color": "#F4D03F"
    },
    "religious": {
        "ar": [
            "مسجد", "كنيسة", "معبد", "صلاة", "قرآن", "إنجيل", "حديث", "فقه", "شريعة",
            "حج", "عمرة", "صوم", "زكاة", "إمام", "خطيب", "دين", "عقيدة", "عبادة", "تفسير",
            "mosque", "church", "temple", "prayer", "Quran", "Bible", "hadith", "jurisprudence",
            "sharia", "pilgrimage", "fasting", "charity", "imam", "sermon", "religion", "faith"
        ],
        "emoji": "🕌", "name_ar": "ديني", "name_en": "Religious", "color": "#6C3483"
    },
    "sports": {
        "ar": [
            "رياضة", "كرة القدم", "كرة السلة", "تنس", "سباحة", "جري", "ملعب", "نادي", "فريق",
            "لاعب", "مدرب", "حكم", "بطولة", "كأس", "مباراة", "تدريب", "لياقة", "مسابقة",
            "sports", "football", "soccer", "basketball", "tennis", "swimming", "running", "stadium",
            "club", "team", "player", "coach", "referee", "championship", "cup", "match", "fitness"
        ],
        "emoji": "⚽", "name_ar": "رياضي", "name_en": "Sports", "color": "#E67E22"
    },
    "literary": {
        "ar": [
            "أدب", "قصة", "رواية", "شعر", "قصيدة", "كاتب", "مؤلف", "نص", "أسلوب", "بلاغة",
            "مجاز", "استعارة", "تشبيه", "فصل", "فقرة", "سرد", "حبكة", "شخصية", "حوار",
            "literature", "story", "novel", "poetry", "poem", "writer", "author", "text", "style",
            "rhetoric", "metaphor", "simile", "chapter", "paragraph", "narrative", "plot", "character"
        ],
        "emoji": "📖", "name_ar": "أدبي", "name_en": "Literary", "color": "#D81B60"
    },
    "it": {
        "ar": [
            "برمجة", "كود", "حاسوب", "كمبيوتر", "شبكة", "إنترنت", "برنامج", "تطبيق", "موقع",
            "خادم", "قاعدة بيانات", "أمن سيبراني", "هاكر", "ذكاء اصطناعي", "تعلم آلي", "سحابي",
            "programming", "code", "computer", "network", "internet", "software", "application", "website",
            "server", "database", "cybersecurity", "hacker", "AI", "machine learning", "cloud", "API"
        ],
        "emoji": "💻", "name_ar": "تقني", "name_en": "IT / Tech", "color": "#00ACC1"
    },
    "environmental": {
        "ar": [
            "بيئة", "تلوث", "مناخ", "احتباس حراري", "طاقة متجددة", "شمسية", "رياح", "مياه جوفية",
            "غابة", "صحراء", "تصحر", "تنوع حيوي", "محمية", "طبيعة", "أوزون", "كربون",
            "environment", "pollution", "climate", "global warming", "renewable", "solar", "wind"
        ],
        "emoji": "🌿", "name_ar": "بيئي", "name_en": "Environmental", "color": "#43A047"
    },
    "agricultural": {
        "ar": [
            "زراعة", "مزرعة", "محصول", "قمح", "أرز", "ذرة", "أشجار", "ماء ري", "تربة",
            "سماد", "مبيد", "حصاد", "حصادة", "ثروة حيوانية", "مواشي", "أغنام", "دواجن", "سمك",
            "agriculture", "farm", "crop", "wheat", "rice", "corn", "trees", "irrigation", "soil"
        ],
        "emoji": "🌾", "name_ar": "زراعي", "name_en": "Agricultural", "color": "#795548"
    },
    "media": {
        "ar": [
            "إعلام", "صحافة", "تلفزيون", "إذاعة", "صحيفة", "خبر", "تقرير", "مذيع", "مراسل",
            "تحقيق", "صحفي", "إعلان", "دعاية", "بث", "قناة", "برنامج إعلامي", "صحفي",
            "media", "journalism", "television", "radio", "newspaper", "news", "report", "anchor"
        ],
        "emoji": "📺", "name_ar": "إعلامي", "name_en": "Media", "color": "#5E35B1"
    },
    "tourism": {
        "ar": [
            "سياحة", "فندق", "سفر", "رحلة", "مطار", "طيران", "جواز", "تأشيرة", "جولة",
            "أثر", "تاريخي", "معلم", "منتجع", "شاطئ", "جبل", "صحراء", "متحف", "تراث",
            "tourism", "hotel", "travel", "trip", "airport", "aviation", "passport", "visa", "tour"
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


# ═══════════════════════════════════════════════════════════════════════════════
#  LIGHTWEIGHT Site Slang DB — 60 Essential Terms Only
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
#  ABBREVIATIONS DICTIONARY — Engineering/Legal/Contractual (EN + RU)
# ═══════════════════════════════════════════════════════════════════════════════
abbreviations_db = {
    # Engineering & Construction
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
    "COSHH": {"full_en": "Control of Substances Hazardous to Health", "full_ru": "Контроль веществ, опасных для здоровья", "ar": "تقييم مواد خطرة", "desc": "تقييم مخاطر المواد الكيميائية."},
    "ATEX": {"full_en": "Atmosphères Explosibles", "full_ru": "Взрывоопасные атмосферы", "ar": "تقييم غازات متفجرة", "desc": "تقييم مخاطر الغازات المتفجرة في أوروبا."},
    "SDS": {"full_en": "Safety Data Sheet", "full_ru": "Паспорт безопасности", "ar": "بيانات سلامة مادة", "desc": "وثيقة توضح مخاطر المادة الكيميائية."},
    "AED": {"full_en": "Automated External Defibrillator", "full_ru": "Автоматический наружный дефибриллятор", "ar": "مزيل رجفان آلي", "desc": "جهاز لإعادة ضربات القلب."},
    "UPS": {"full_en": "Uninterruptible Power Supply", "full_ru": "Источник бесперебойного питания", "ar": "نظام طاقة احتياطي", "desc": "نظام يوفر طاقة احتياطية عند انقطاع الكهرباء."},
    "PV": {"full_en": "Photovoltaic", "full_ru": "Фотоэлектрический", "ar": "كهروضوئي", "desc": "تقنية لتحويل ضوء الشمس إلى كهرباء."},
    "GPR": {"full_en": "Ground Penetrating Radar", "full_ru": "Георадар", "ar": "رادار اختراق أرض", "desc": "جهاز لاكتشاف ما تحت الأرض."},
    "CAT": {"full_en": "Cable Avoidance Tool", "full_ru": "Детектор кабелей", "ar": "كاشف كابلات", "desc": "جهاز لاكتشاف الكابلات تحت الأرض."},
    "VOC": {"full_en": "Volatile Organic Compounds", "full_ru": "Летучие органические соединения", "ar": "مركبات عضوية متطايرة", "desc": "غازات تتسرب من المواد الكيميائية."},
    "PM10": {"full_en": "Particulate Matter 10 micrometers", "full_ru": "Взвешенные частицы 10 мкм", "ar": "جسيمات 10 ميكرون", "desc": "جسيمات صغيرة في الهواء."},
    "PM2.5": {"full_en": "Particulate Matter 2.5 micrometers", "full_ru": "Взвешенные частицы 2.5 мкм", "ar": "جسيمات 2.5 ميكرون", "desc": "جسيمات دقيقة جداً في الهواء."},
    "NOx": {"full_en": "Nitrogen Oxides", "full_ru": "Оксиды азота", "ar": "أكسيد نيتروجين", "desc": "غازات سامة من احتراق الوقود."},
    "SOx": {"full_en": "Sulfur Oxides", "full_ru": "Оксиды серы", "ar": "أكسيد كبريت", "desc": "غازات سامة من احتراق الوقود."},
    "CO2": {"full_en": "Carbon Dioxide", "full_ru": "Диоксид углерода", "ar": "ثاني أكسيد كربون", "desc": "غاز دفيئة من الاحتراق."},
    "CH4": {"full_en": "Methane", "full_ru": "Метан", "ar": "ميثان", "desc": "غاز دفيئة من التحلل العضوي."},
    "HFC": {"full_en": "Hydrofluorocarbon", "full_ru": "Гидрофторуглерод", "ar": "هيدروفلوروكربون", "desc": "غاز تبريد يسبب الاحتباس الحراري."},
    "PFC": {"full_en": "Perfluorocarbon", "full_ru": "Перфторированный углерод", "ar": "بيرفلوروكربون", "desc": "غاز صناعي يسبب الاحتباس الحراري."},
    "SF6": {"full_en": "Sulfur Hexafluoride", "full_ru": "Шестифтористая сера", "ar": "سداسي فلوريد كبريت", "desc": "غاز عازل كهربائياً."},
    "AHU": {"full_en": "Air Handling Unit", "full_ru": "Воздухообрабатывающая установка", "ar": "وحدة معالجة هواء", "desc": "وحدة كبيرة لتكييف وتنقية الهواء."},
    "FCU": {"full_en": "Fan Coil Unit", "full_ru": "Фанкойл", "ar": "وحدة مروحة ملفية", "desc": "وحدة صغيرة للتكييف في الغرف."},
    "VAV": {"full_en": "Variable Air Volume", "full_ru": "Переменный расход воздуха", "ar": "صمام هواء متغير", "desc": "صمام يتحكم في كمية الهواء."},
    "VRF": {"full_en": "Variable Refrigerant Flow", "full_ru": "Переменный расход хладагента", "ar": "تدفق مبرد متغير", "desc": "نظام تكييف يتحكم في كمية المبرد."},
    "VRV": {"full_en": "Variable Refrigerant Volume", "full_ru": "Переменный объем хладагента", "ar": "حجم مبرد متغير", "desc": "نظام تكييف يتحكم في حجم المبرد."},
    "RTU": {"full_en": "Rooftop Unit", "full_ru": "Крышная установка", "ar": "وحدة سطح", "desc": "وحدة تكييف مثبتة على السطح."},
    "MAU": {"full_en": "Make-Up Air Unit", "full_ru": "Установка приточного воздуха", "ar": "وحدة هواء تعويضي", "desc": "وحدة تزود الهواء الخارجي للمبنى."},
    "DX": {"full_en": "Direct Expansion", "full_ru": "Прямое расширение", "ar": "تمدد مباشر", "desc": "نظام تبريد يستخدم مبرد مباشر."},
    "R410A": {"full_en": "Refrigerant 410A", "full_ru": "Хладагент R410A", "ar": "مبرد R410A", "desc": "نوع من المبردات الحديثة."},
    "R32": {"full_en": "Refrigerant 32", "full_ru": "Хладагент R32", "ar": "مبرد R32", "desc": "مبرد صديق للبيئة."},
    "R290": {"full_en": "Refrigerant 290 (Propane)", "full_ru": "Хладагент R290 (пропан)", "ar": "مبرد R290 (بروبان)", "desc": "مبرد طبيعي (بروبان)."},
    "SPI": {"full_en": "Schedule Performance Index", "full_ru": "Индекс выполнения графика", "ar": "مؤشر جدولة", "desc": "مؤشر يقيس التقدم في الجدولة."},
    "CPI": {"full_en": "Cost Performance Index", "full_ru": "Индекс выполнения затрат", "ar": "مؤشر تكلفة", "desc": "مؤشر يقيس كفاءة التكلفة."},
    "EAC": {"full_en": "Estimate at Completion", "full_ru": "Оценка при завершении", "ar": "تقدير عند إنجاز", "desc": "تقدير التكلفة الإجمالية عند الانتهاء."},
    "ETC": {"full_en": "Estimate to Complete", "full_ru": "Оценка для завершения", "ar": "تقدير للانتهاء", "desc": "تقدير التكلفة المتبقية."},
    "VAC": {"full_en": "Variance at Completion", "full_ru": "Отклонение при завершении", "ar": "انحراف تكلفة", "desc": "الفرق بين الميزانية والتكلفة المتوقعة."},
    "TCPI": {"full_en": "To-Complete Performance Index", "full_ru": "Индекс эффективности для завершения", "ar": "مؤشر أداء للانتهاء", "desc": "الكفاءة المطلوبة لإنجاز المشروع."},
    "RAM": {"full_en": "Responsibility Assignment Matrix", "full_ru": "Матрица распределения ответственности", "ar": "مصفوفة مسؤولية", "desc": "جدول يوضح المسؤوليات بين الفريق."},
    "RACI": {"full_en": "Responsible, Accountable, Consulted, Informed", "full_ru": "Ответственный, подотчетный, консультируемый, информируемый", "ar": "مصفوفة RACI", "desc": "مصفوفة تحدد المسؤوليات."},
    "OBS": {"full_en": "Organizational Breakdown Structure", "full_ru": "Организационная структура", "ar": "هيكل تقسيم منظمة", "desc": "تقسيم الفريق المسؤول عن المشروع."},
    "RBS": {"full_en": "Resource Breakdown Structure", "full_ru": "Структура ресурсов", "ar": "هيكل تقسيم موارد", "desc": "تصنيف الموارد المطلوبة."},
    "CBS": {"full_en": "Cost Breakdown Structure", "full_ru": "Структура затрат", "ar": "هيكل تقسيم تكلفة", "desc": "تصنيف التكاليف في المشروع."},
    "PBS": {"full_en": "Product Breakdown Structure", "full_ru": "Структура продукта", "ar": "هيكل تقسيم منتج", "desc": "تقسيم المنتج النهائي إلى مكونات."},
    "O&M": {"full_en": "Operation and Maintenance", "full_ru": "Эксплуатация и обслуживание", "ar": "تشغيل وصيانة", "desc": "دليل تشغيل وصيانة الأنظمة."},
    "POE": {"full_en": "Post-Occupancy Evaluation", "full_ru": "Оценка после эксплуатации", "ar": "تقييم ما بعد استخدام", "desc": "دراسة أداء المبنى بعد استخدامه."},
    "EPC": {"full_en": "Engineering Procurement Construction", "full_ru": "Инжиниринг, закупки, строительство", "ar": "تصميم وتوريد وتنفيذ", "desc": "عقد متكامل للمشاريع."},
    "DB": {"full_en": "Design-Build", "full_ru": "Проектирование и строительство", "ar": "تصميم وبناء", "desc": "عقد يجمع التصميم والتنفيذ."},
    "DBB": {"full_en": "Design-Bid-Build", "full_ru": "Проектирование, тендер, строительство", "ar": "تصميم ومناقصة وبناء", "desc": "نموذج تقليدي للتعاقد."},
    "CM": {"full_en": "Construction Management", "full_ru": "Строительный менеджмент", "ar": "إدارة تشييد", "desc": "إدارة عملية التشييد."},
    "PM": {"full_en": "Project Management", "full_ru": "Управление проектами", "ar": "إدارة مشروع", "desc": "إدارة المشروع بأكمله."},
    "QM": {"full_en": "Quality Management", "full_ru": "Управление качеством", "ar": "إدارة جودة", "desc": "إدارة نظام الجودة في المشروع."},
    "HSE": {"full_en": "Health, Safety, Environment", "full_ru": "Охрана труда, безопасность, экология", "ar": "صحة وسلامة وبيئة", "desc": "نظام إدارة الصحة والسلامة والبيئة."},
    "QA": {"full_en": "Quality Assurance", "full_ru": "Обеспечение качества", "ar": "ضمان جودة", "desc": "أنشطة تضمن تحقيق الجودة المطلوبة."},
    "QC": {"full_en": "Quality Control", "full_ru": "Контроль качества", "ar": "رقابة جودة", "desc": "فحص واختبار الأعمال للتأكد من الجودة."},
    "KPI": {"full_en": "Key Performance Indicator", "full_ru": "Ключевой показатель эффективности", "ar": "مؤشر أداء رئيسي", "desc": "مؤشر لقياس أداء المشروع."},
    "SLA": {"full_en": "Service Level Agreement", "full_ru": "Соглашение об уровне обслуживания", "ar": "اتفاقية مستوى خدمة", "desc": "اتفاقية تحدد مستوى الخدمة المطلوب."},
    "MOU": {"full_en": "Memorandum of Understanding", "full_ru": "Меморандум о взаимопонимании", "ar": "مذكرة تفاهم", "desc": "وثيقة تُعدّل نية الأطراف للتعاون."},
    "NDA": {"full_en": "Non-Disclosure Agreement", "full_ru": "Соглашение о неразглашении", "ar": "اتفاقية عدم إفشاء", "desc": "اتفاقية لحماية المعلومات السرية."},
    "T&C": {"full_en": "Terms and Conditions", "full_ru": "Условия и положения", "ar": "الشروط والأحكام", "desc": "الشروط التعاقدية للمشروع."},
    "SOW": {"full_en": "Scope of Work", "full_ru": "Объем работ", "ar": "نطاق العمل", "desc": "وثيقة تحدد نطاق الأعمال المطلوبة."},
    "SOS": {"full_en": "Schedule of Rates", "full_ru": "Прейскурант расценок", "ar": "جدول الأسعار", "desc": "جدول يحتوي على أسعار الوحدات."},
    "CP": {"full_en": "Critical Path", "full_ru": "Критический путь", "ar": "مسار حرج", "desc": "سلسلة الأنشطة التي تحدد مدة المشروع."},
    "CPM": {"full_en": "Critical Path Method", "full_ru": "Метод критического пути", "ar": "طريقة المسار الحرج", "desc": "طريقة لجدولة المشروع."},
    "PERT": {"full_en": "Program Evaluation and Review Technique", "full_ru": "Метод оценки и проверки программ", "ar": "تقنية تقييم ومراجعة البرنامج", "desc": "طريقة لتحليل المهام المطلوبة لإنجاز المشروع."},
    "Gantt": {"full_en": "Gantt Chart", "full_ru": "Диаграмма Ганта", "ar": "مخطط جانت", "desc": "رسم بياني لجدولة المشروع."},
    "WBS": {"full_en": "Work Breakdown Structure", "full_ru": "Иерархическая структура работ", "ar": "هيكل تقسيم العمل", "desc": "تقسيم المشروع إلى أجزاء صغيرة."},
    "OBS": {"full_en": "Organizational Breakdown Structure", "full_ru": "Организационная структура", "ar": "هيكل تقسيم المنظمة", "desc": "تقسيم الفريق المسؤول."},
    "RBS": {"full_en": "Risk Breakdown Structure", "full_ru": "Структура рисков", "ar": "هيكل تقسيم المخاطر", "desc": "تصنيف المخاطر في المشروع."},
    "RAM": {"full_en": "Responsibility Assignment Matrix", "full_ru": "Матрица распределения ответственности", "ar": "مصفوفة توزيع المسؤوليات", "desc": "جدول يوضح المسؤوليات."},
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
    "OHSAS 18001": {"full_en": "OHSAS 18001 Safety Standard", "full_ru": "OHSAS 18001 Стандарт безопасности", "ar": "OHSAS 18001", "desc": "معيار قديم للسلامة (تم استبداله بـ ISO 45001)."},
    "CE": {"full_en": "Conformité Européenne", "full_ru": "Европейское соответствие", "ar": "علامة ال conformity الأوروبية", "desc": "علامة تُوضع على المنتجات المطابقة للمعايير الأوروبية."},
    "UL": {"full_en": "Underwriters Laboratories", "full_ru": "Лаборатории Андеррайтерс", "ar": "مختبرات أندررايتيرز", "desc": "منظمة أمريكية لاختبار السلامة."},
    "ASTM": {"full_en": "American Society for Testing and Materials", "full_ru": "Американское общество по испытаниям материалов", "ar": "الجمعية الأمريكية لاختبار المواد", "desc": "منظمة تضع معايير اختبار المواد."},
    "ANSI": {"full_en": "American National Standards Institute", "full_ru": "Американский национальный институт стандартов", "ar": "المعهد الأمريكي للمعايير الوطنية", "desc": "منظمة تضع معايير أمريكية."},
    "BS": {"full_en": "British Standard", "full_ru": "Британский стандарт", "ar": "معيار بريطاني", "desc": "معيار بريطاني للمنتجات والخدمات."},
    "DIN": {"full_en": "Deutsches Institut für Normung", "full_ru": "Немецкий институт стандартизации", "ar": "المعهد الألماني للتوحيد القياسي", "desc": "معيار ألماني للمنتجات والخدمات."},
    "JIS": {"full_en": "Japanese Industrial Standard", "full_ru": "Японский промышленный стандарт", "ar": "معيار صناعي ياباني", "desc": "معيار ياباني للمنتجات الصناعية."},
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
    "UBC": {"full_en": "Uniform Building Code", "full_ru": "Единый строительный кодекс", "ar": "الكود الموحد للبناء", "desc": "كود بناء قديم (تم استبداله بـ IBC)."},
    "ACI": {"full_en": "American Concrete Institute", "full_ru": "Американский бетонный институт", "ar": "المعهد الأمريكي للخرسانة", "desc": "منظمة لمعايير الخرسانة."},
    "AISC": {"full_en": "American Institute of Steel Construction", "full_ru": "Американский институт строительной стали", "ar": "المعهد الأمريكي لبناء الصلب", "desc": "منظمة لمعايير البناء الفولاذي."},
    "AWS": {"full_en": "American Welding Society", "full_ru": "Американское сварочное общество", "ar": "الجمعية الأمريكية للحام", "desc": "منظمة لمعايير اللحام."},
    "ASME": {"full_en": "American Society of Mechanical Engineers", "full_ru": "Американское общество инженеров-механиков", "ar": "الجمعية الأمريكية للمهندسين الميكانيكيين", "desc": "منظمة لمعايير الميكانيكا."},
    "API": {"full_en": "American Petroleum Institute", "full_ru": "Американский нефтяной институт", "ar": "المعهد الأمريكي للبترول", "desc": "منظمة لمعايير البترول والغاز."},
    "NEC": {"full_en": "National Electrical Code", "full_ru": "Национальный электротехнический кодекс", "ar": "الكود الكهربائي الوطني", "desc": "كود كهربائي أمريكي."},
    "IECC": {"full_en": "International Energy Conservation Code", "full_ru": "Международный кодекс энергосбережения", "ar": "الكود الدولي لحفظ الطاقة", "desc": "كود دولي لحفظ الطاقة في المباني."},
    "ASHRAE 90.1": {"full_en": "ASHRAE Standard 90.1", "full_ru": "Стандарт ASHRAE 90.1", "ar": "معيار ASHRAE 90.1", "desc": "معيار لكفاءة الطاقة في المباني."},
    "LEED": {"full_en": "Leadership in Energy and Environmental Design", "full_ru": "Лидерство в энергетике и экологическом дизайне", "ar": "الريادة في الطاقة والتصميم البيئي", "desc": "نظام اعتماد دولي للمباني المستدامة."},
    "BREEAM": {"full_en": "Building Research Establishment Environmental Assessment Method", "full_ru": "Метод оценки экологических качеств зданий", "ar": "طريقة تقييم البيئة للمباني", "desc": "نظام اعتماد بريطاني للمباني المستدامة."},
    "WELL": {"full_en": "WELL Building Standard", "full_ru": "Стандарт зданий WELL", "ar": "معيار WELL للمباني", "desc": "نظام اعتماد يركز على صحة ورفاهية السكان."},
    "Passive House": {"full_en": "Passivhaus Standard", "full_ru": "Стандарт пассивного дома", "ar": "معيار البيت السلبي", "desc": "معيار ألماني للمباني عالية الكفاءة."},
    "Net Zero": {"full_en": "Net Zero Energy Building", "full_ru": "Здание с нулевым энергопотреблением", "ar": "مبنى صافي صفر", "desc": "مبنى يُنتج طاقة مساوية لما يستهلكه."},
    "Nearly Zero": {"full_en": "Nearly Zero Energy Building", "full_ru": "Здание с почти нулевым энергопотреблением", "ar": "مبنى شبه صفر", "desc": "مبنى يستهلك طاقة منخفضة جداً."},
    "EPC": {"full_en": "Energy Performance Certificate", "full_ru": "Сертификат энергетической эффективности", "ar": "شهادة الأداء الطاقي", "desc": "شهادة تصنف كفاءة الطاقة في المبنى."},
    "TMY": {"full_en": "Typical Meteorological Year", "full_ru": "Типичный метеорологический год", "ar": "سنة نموذجية", "desc": "بيانات طقس نموذجية لتحليل الطاقة."},
    "DD": {"full_en": "Degree Days", "full_ru": "Градусо-дни", "ar": "أيام الدرجات", "desc": "مقياس لحساب احتياجات التدفئة والتبريد."},
    "CDD": {"full_en": "Cooling Degree Days", "full_ru": "Градусо-дни охлаждения", "ar": "أيام درجات التبريد", "desc": "مقياس لحساب احتياجات التبريد."},
    "HDD": {"full_en": "Heating Degree Days", "full_ru": "Градусо-дни отопления", "ar": "أيام درجات التدفئة", "desc": "مقياس لحساب احتياجات التدفئة."},
    "SHGC": {"full_en": "Solar Heat Gain Coefficient", "full_ru": "Коэффициент солнечного теплопоглощения", "ar": "معامل كسب الحرارة الشمسية", "desc": "معامل يقيس كمية الحرارة الشمسية التي تمر through الزجاج."},
    "U-value": {"full_en": "Thermal Transmittance", "full_ru": "Теплопередача", "ar": "معامل التوصيل الحراري", "desc": "معامل يقيس مقدار الحرارة التي تمر through الجدار."},
    "R-value": {"full_en": "Thermal Resistance", "full_ru": "Теплосопротивление", "ar": "معامل المقاومة الحرارية", "desc": "معامل يقيس مقاومة المادة للحرارة."},
    "g-value": {"full_en": "Solar Factor", "full_ru": "Солнечный фактор", "ar": "معامل الطاقة الشمسية", "desc": "معامل يقيس كمية الطاقة الشمسية التي تمر through الزجاج."},
    "LT": {"full_en": "Light Transmittance", "full_ru": "Светопропускание", "ar": "نفاذية الضوء", "desc": "نسبة الضوء المرئي الذي يمر through الزجاج."},
    "RV": {"full_en": "Rainwater Harvesting", "full_ru": "Сбор дождевой воды", "ar": "حصاد مياه الأمطار", "desc": "جمع وتخزين مياه الأمطار لإعادة الاستخدام."},
    "GW": {"full_en": "Greywater Recycling", "full_ru": "Рециркуляция серых вод", "ar": "إعادة تدوير المياه الرمادية", "desc": "معالجة وإعادة استخدام مياه المغاسل."},
    "BW": {"full_en": "Blackwater Treatment", "full_ru": "Обработка черных вод", "ar": "معالجة المياه السوداء", "desc": "معالجة مياه الصرف الصحي."},
    "STP": {"full_en": "Sewage Treatment Plant", "full_ru": "Очистные сооружения", "ar": "محطة معالجة مياه الصرف", "desc": "محطة لمعالجة مياه الصرف الصحي."},
    "WWTP": {"full_en": "Wastewater Treatment Plant", "full_ru": "Станция очистки сточных вод", "ar": "محطة معالجة مياه الصرف", "desc": "محطة لمعالجة مياه الصرف."},
    "ETP": {"full_en": "Effluent Treatment Plant", "full_ru": "Установка очистки стоков", "ar": "محطة معالجة المياه العادمة", "desc": "محطة لمعالجة المياه العادمة من الصناعة."},
    "RO": {"full_en": "Reverse Osmosis", "full_ru": "Обратный осмос", "ar": "التناضح العكسي", "desc": "تقنية لتحلية المياه."},
    "UV": {"full_en": "Ultraviolet Disinfection", "full_ru": "Ультрафиолетовая дезинфекция", "ar": "تعقيم بالأشعة فوق البنفسجية", "desc": "تعقيم المياه باستخدام الأشعة فوق البنفسجية."},
    "Ozonation": {"full_en": "Ozone Treatment", "full_ru": "Озонирование", "ar": "معالجة الأوزون", "desc": "تعقيم المياه باستخدام الأوزون."},
    "Chlorination": {"full_en": "Chlorine Treatment", "full_ru": "Хлорирование", "ar": "معالجة الكلور", "desc": "تعقيم المياه باستخدام الكلور."},
    "MBR": {"full_en": "Membrane Bioreactor", "full_ru": "Мембранный биореактор", "ar": "مفاعل غشائي حيوي", "desc": "تقنية متقدمة لمعالجة مياه الصرف."},
    "SBR": {"full_en": "Sequencing Batch Reactor", "full_ru": "Последовательный пакетный реактор", "ar": "مفاعل دفعي متسلسل", "desc": "تقنية لمعالجة مياه الصرف."},
    "DAF": {"full_en": "Dissolved Air Flotation", "full_ru": "Флотация с растворенным воздухом", "ar": "تطوير بالهواء المذاب", "desc": "تقنية لإزالة المواد الصلبة من المياه."},
    "UF": {"full_en": "Ultrafiltration", "full_ru": "Ультрафильтрация", "ar": "الترشيح الفائق", "desc": "تقنية ترشيح دقيقة للمياه."},
    "NF": {"full_en": "Nanofiltration", "full_ru": "Нанофильтрация", "ar": "الترشيح النانوي", "desc": "تقنية ترشيح متوسطة للمياه."},
    "MF": {"full_en": "Microfiltration", "full_ru": "Микрофильтрация", "ar": "الترشيح الدقيق", "desc": "تقنية ترشيح خشن للمياه."},
    "EDI": {"full_en": "Electrodeionization", "full_ru": "Электродеионизация", "ar": "إزالة الأيونات بالكهرباء", "desc": "تقنية لإنتاج مياه عالية النقاء."},
    "IX": {"full_en": "Ion Exchange", "full_ru": "Ионный обмен", "ar": "تبادل الأيونات", "desc": "تقنية لإزالة الأملاح من المياه."},
    "GAC": {"full_en": "Granular Activated Carbon", "full_ru": "Гранулированный активированный уголь", "ar": "كربون منشط حبيبي", "desc": "مادة لإزالة المواد العضوية من المياه."},
    "PAC": {"full_en": "Powdered Activated Carbon", "full_ru": "Порошкообразный активированный уголь", "ar": "كربون منشط مسحوق", "desc": "مادة لإزالة المواد العضوية من المياه."},
    "CF": {"full_en": "Coagulation and Flocculation", "full_ru": "Коагуляция и флокуляция", "ar": "التخثر والتكتل", "desc": "عملية لإزالة المواد العالقة من المياه."},
    "Sedimentation": {"full_en": "Sedimentation", "full_ru": "Осаждение", "ar": "الترسيب", "desc": "عملية لإزالة المواد الصلبة من المياه بالترسيب."},
    "Filtration": {"full_en": "Filtration", "full_ru": "Фильтрация", "ar": "الترشيح", "desc": "عملية لإزالة المواد الصلبة من المياه بالترشيح."},
    "Disinfection": {"full_en": "Disinfection", "full_ru": "Дезинфекция", "ar": "التعقيم", "desc": "عملية لقتل البكتيريا في المياه."},
    "Softening": {"full_en": "Water Softening", "full_ru": "Умягчение воды", "ar": "تليين المياه", "desc": "إزالة العسر (الكالسيوم والمغنيسيوم) من المياه."},
    "Dealkalization": {"full_en": "Dealkalization", "full_ru": "Деалкализация", "ar": "إزالة القلوية", "desc": "إزالة القلوية من المياه."},
    "Demineralization": {"full_en": "Demineralization", "full_ru": "Деминерализация", "ar": "إزالة المعادن", "desc": "إزالة جميع المعادن من المياه."},
    "Desalination": {"full_en": "Desalination", "full_ru": "Опреснение", "ar": "تحلية المياه", "desc": "إزالة الملح من مياه البحر."},
    "Distillation": {"full_en": "Distillation", "full_ru": "Дистилляция", "ar": "التقطير", "desc": "تقنية لتحلية المياه بالتبخير."},
    "Electrodialysis": {"full_en": "Electrodialysis", "full_ru": "Электродиализ", "ar": "التحليل الكهربائي", "desc": "تقنية لتحلية المياه باستخدام الكهرباء."},
    "Forward Osmosis": {"full_en": "Forward Osmosis", "full_ru": "Прямой осмос", "ar": "التناضح المباشر", "desc": "تقنية لتحلية المياه باستخدام محلول مركز."},
    "Membrane Distillation": {"full_en": "Membrane Distillation", "full_ru": "Мембранная дистилляция", "ar": "التقطير الغشائي", "desc": "تقنية لتحلية المياه باستخدام غشاء مسامي."},
    "Solar Still": {"full_en": "Solar Still", "full_ru": "Солнечный перегонный куб", "ar": "مقطرة شمسية", "desc": "جهاز بسيط لتحلية المياه بالطاقة الشمسية."},
    "Fog Harvesting": {"full_en": "Fog Harvesting", "full_ru": "Сбор тумана", "ar": "حصاد الضباب", "desc": "جمع مياه الضباب باستخدام شبكات."},
    "Rainwater Harvesting": {"full_en": "Rainwater Harvesting", "full_ru": "Сбор дождевой воды", "ar": "حصاد مياه الأمطار", "desc": "جمع وتخزين مياه الأمطار."},
    "Stormwater Management": {"full_en": "Stormwater Management", "full_ru": "Управление ливневыми стоками", "ar": "إدارة مياه الأمطار", "desc": "إدارة مياه الأمطار لتقليل الفيضانات."},
    "Green Infrastructure": {"full_en": "Green Infrastructure", "full_ru": "Зеленая инфраструктура", "ar": "بنية تحتية خضراء", "desc": "استخدام النباتات لإدارة مياه الأمطار."},
    "Bioswale": {"full_en": "Bioswale", "full_ru": "Биолощина", "ar": "قناة حيوية", "desc": "قناة مزروعة لترشيح مياه الأمطار."},
    "Rain Garden": {"full_en": "Rain Garden", "full_ru": "Дождевой сад", "ar": "حديقة أمطار", "desc": "حديقة مزروعة لامتصاص مياه الأمطار."},
    "Permeable Pavement": {"full_en": "Permeable Pavement", "full_ru": "Проницаемое покрытие", "ar": "رصف نفاذ", "desc": "رصف يسمح بمرور المياه."},
    "Green Roof": {"full_en": "Green Roof", "full_ru": "Зеленая крыша", "ar": "سقف أخضر", "desc": "سقف مغطى بالنباتات لامتصاص المياه."},
    "Blue Roof": {"full_en": "Blue Roof", "full_ru": "Синяя крыша", "ar": "سقف أزرق", "desc": "سقف يخزن مياه الأمطار."},
    "Cool Roof": {"full_en": "Cool Roof", "full_ru": "Холодная крыша", "ar": "سقف بارد", "desc": "سقف يعكس أشعة الشمس."},
    "Living Wall": {"full_en": "Living Wall", "full_ru": "Живая стена", "ar": "جدار حي", "desc": "جدار مغطى بالنباتات."},
    "Urban Heat Island": {"full_en": "Urban Heat Island", "full_ru": "Городской остров тепла", "ar": "جزيرة حرارية", "desc": "ظاهرة ارتفاع الحرارة في المدن."},
    "Albedo": {"full_en": "Albedo", "full_ru": "Альбедо", "ar": "البياض", "desc": "نسبة الضوء المنعكس من السطح."},
    "Emissivity": {"full_en": "Emissivity", "full_ru": "Эмиссивность", "ar": "الإشعاعية", "desc": "قدرة السطح على إصدار الإشعاع الحراري."},
    "Reflectance": {"full_en": "Reflectance", "full_ru": "Отражательная способность", "ar": "الانعكاسية", "desc": "نسبة الضوء المنعكس من السطح."},
    "Transmittance": {"full_en": "Transmittance", "full_ru": "Пропускная способность", "ar": "النفاذية", "desc": "نسبة الضوء المار through المادة."},
    "Absorptance": {"full_en": "Absorptance", "full_ru": "Поглощательная способность", "ar": "الاستيعابية", "desc": "نسبة الضوء الممتص من السطح."},
    "Opacity": {"full_en": "Opacity", "full_ru": "Непрозрачность", "ar": "العتمة", "desc": "قدرة المادة على منع مرور الضوء."},
    "Translucency": {"full_en": "Translucency", "full_ru": "Полупрозрачность", "ar": "الشفافية الجزئية", "desc": "قدرة المادة على السماح بمرور الضوء دون وضوح."},
    "Transparency": {"full_en": "Transparency", "full_ru": "Прозрачность", "ar": "الشفافية", "desc": "قدرة المادة على السماح بمرور الضوء بوضوح."},
    "Glare": {"full_en": "Glare", "full_ru": "Блики", "ar": "وهج", "desc": "ضوء ساطع يسبب إزعاجاً أو ضعف رؤية."},
    "Daylight Factor": {"full_en": "Daylight Factor", "full_ru": "Коэффициент дневного света", "ar": "معامل الإضاءة الطبيعية", "desc": "نسبة الإضاءة الطبيعية داخل المبنى."},
    "Useful Daylight Illuminance": {"full_en": "Useful Daylight Illuminance", "full_ru": "Полезная освещенность дневным светом", "ar": "إضاءة طبيعية مفيدة", "desc": "نسبة الإضاءة الطبيعية المفيدة داخل المبنى."},
    "Spatial Daylight Autonomy": {"full_en": "Spatial Daylight Autonomy", "full_ru": "Пространственная автономия дневного света", "ar": "استقلالية الإضاءة الطبيعية المكانية", "desc": "نسبة الوقت الذي تكون فيه الإضاءة الطبيعية كافية."},
    "Annual Sunlight Exposure": {"full_en": "Annual Sunlight Exposure", "full_ru": "Годовое воздействие солнечного света", "ar": "التعرض السنوي لضوء الشمس", "desc": "مقياس لتقييم التعرض للضوء المباشر."},
    "Glare Probability": {"full_en": "Glare Probability", "full_ru": "Вероятность бликов", "ar": "احتمالية الوهج", "desc": "احتمالية حدوث الوهج في المبنى."},
    "Visual Comfort Probability": {"full_en": "Visual Comfort Probability", "full_ru": "Вероятность визуального комфорта", "ar": "احتمالية الراحة البصرية", "desc": "احتمالية الراحة البصرية في المبنى."},
    "Color Rendering Index": {"full_en": "Color Rendering Index", "full_ru": "Индекс цветопередачи", "ar": "مؤشر إعادة إنتاج الألوان", "desc": "مقياس لجودة إعادة إنتاج الألوان."},
    "Correlated Color Temperature": {"full_en": "Correlated Color Temperature", "full_ru": "Коррелированная цветовая температура", "ar": "درجة حرارة اللون المترابطة", "desc": "درجة حرارة اللون المصدر الضوئي."},
    "Luminous Efficacy": {"full_en": "Luminous Efficacy", "full_ru": "Световая эффективность", "ar": "الفعالية الضوئية", "desc": "كفاءة المصدر الضوئي في إنتاج الضوء."},
    "Luminous Flux": {"full_en": "Luminous Flux", "full_ru": "Световой поток", "ar": "التدفق الضوئي", "desc": "كمية الضوء التي ينتجها المصدر."},
    "Illuminance": {"full_en": "Illuminance", "full_ru": "Освещенность", "ar": "الإضاءة", "desc": "كمية الضوء الساقط على السطح."},
    "Luminance": {"full_en": "Luminance", "full_ru": "Яркость", "ar": "السطوع", "desc": "كمية الضوء المنعكس من السطح."},
    "Glare Index": {"full_en": "Glare Index", "full_ru": "Индекс бликов", "ar": "مؤشر الوهج", "desc": "مقياس لتقييم الوهج في المبنى."},
    "Unified Glare Rating": {"full_en": "Unified Glare Rating", "full_ru": "Единая оценка бликов", "ar": "تقييم الوهج الموحد", "desc": "مقياس دولي لتقييم الوهج."},
    " daylight autonomy": {"full_en": "Daylight Autonomy", "full_ru": "Автономность дневного света", "ar": "استقلالية الإضاءة الطبيعية", "desc": "نسبة الوقت الذي تكون فيه الإضاءة الطبيعية كافية."},
    "Useful Daylight Illuminance": {"full_en": "Useful Daylight Illuminance", "full_ru": "Полезная освещенность дневным светом", "ar": "إضاءة طبيعية مفيدة", "desc": "نسبة الإضاءة الطبيعية المفيدة."},
    "Spatial Daylight Autonomy": {"full_en": "Spatial Daylight Autonomy", "full_ru": "Пространственная автономия дневного света", "ar": "استقلالية الإضاءة الطبيعية المكانية", "desc": "نسبة الوقت الذي تكون فيه الإضاءة الطبيعية كافية في المكان."},
    "Annual Sunlight Exposure": {"full_en": "Annual Sunlight Exposure", "full_ru": "Годовое воздействие солнечного света", "ar": "التعرض السنوي لضوء الشمس", "desc": "مقياس لتقييم التعرض للضوء المباشر."},
    "Glare Probability": {"full_en": "Glare Probability", "full_ru": "Вероятность бликов", "ar": "احتمالية الوهج", "desc": "احتمالية حدوث الوهج."},
    "Visual Comfort Probability": {"full_en": "Visual Comfort Probability", "full_ru": "Вероятность визуального комфорта", "ar": "احتمالية الراحة البصرية", "desc": "احتمالية الراحة البصرية."},
    "Color Rendering Index": {"full_en": "Color Rendering Index", "full_ru": "Индекс цветопередачи", "ar": "مؤشر إعادة إنتاج الألوان", "desc": "مقياس لجودة إعادة إنتاج الألوان."},
    "Correlated Color Temperature": {"full_en": "Correlated Color Temperature", "full_ru": "Коррелированная цветовая температура", "ar": "درجة حرارة اللون المترابطة", "desc": "درجة حرارة اللون المصدر الضوئي."},
    "Luminous Efficacy": {"full_en": "Luminous Efficacy", "full_ru": "Световая эффективность", "ar": "الفعالية الضوئية", "desc": "كفاءة المصدر الضوئي."},
    "Luminous Flux": {"full_en": "Luminous Flux", "full_ru": "Световой поток", "ar": "التدفق الضوئي", "desc": "كمية الضوء المنتجة."},
    "Illuminance": {"full_en": "Illuminance", "full_ru": "Освещенность", "ar": "الإضاءة", "desc": "كمية الضوء الساقط."},
    "Luminance": {"full_en": "Luminance", "full_ru": "Яркость", "ar": "السطوع", "desc": "كمية الضوء المنعكس."},
    "Glare Index": {"full_en": "Glare Index", "full_ru": "Индекс бликов", "ar": "مؤشر الوهج", "desc": "مقياس لتقييم الوهج."},
    "Unified Glare Rating": {"full_en": "Unified Glare Rating", "full_ru": "Единая оценка бликов", "ar": "تقييم الوهج الموحد", "desc": "مقياس دولي للوهج."},
    " daylight autonomy": {"full_en": "Daylight Autonomy", "full_ru": "Автономность дневного света", "ar": "استقلالية الإضاءة الطبيعية", "desc": "نسبة الوقت الذي تكون فيه الإضاءة الطبيعية كافية."},
    "Useful Daylight Illuminance": {"full_en": "Useful Daylight Illuminance", "full_ru": "Полезная освещенность дневным светом", "ar": "إضاءة طبيعية مفيدة", "desc": "نسبة الإضاءة المفيدة."},
    "Spatial Daylight Autonomy": {"full_en": "Spatial Daylight Autonomy", "full_ru": "Пространственная автономия дневного света", "ar": "استقلالية الإضاءة المكانية", "desc": "نسبة الوقت الذي تكون فيه الإضاءة كافية في المكان."},
    "Annual Sunlight Exposure": {"full_en": "Annual Sunlight Exposure", "full_ru": "Годовое воздействие солнечного света", "ar": "التعرض السنوي للشمس", "desc": "مقياس للتعرض للضوء المباشر."},
    "Glare Probability": {"full_en": "Glare Probability", "full_ru": "Вероятность бликов", "ar": "احتمالية الوهج", "desc": "احتمالية الوهج."},
    "Visual Comfort Probability": {"full_en": "Visual Comfort Probability", "full_ru": "Вероятность визуального комфорта", "ar": "احتمالية الراحة البصرية", "desc": "احتمالية الراحة البصرية."},
    "Color Rendering Index": {"full_en": "Color Rendering Index", "full_ru": "Индекс цветопередачи", "ar": "مؤشر إعادة الألوان", "desc": "جودة إعادة إنتاج الألوان."},
    "Correlated Color Temperature": {"full_en": "Correlated Color Temperature", "full_ru": "Коррелированная цветовая температура", "ar": "درجة حرارة اللون", "desc": "درجة حرارة اللون."},
    "Luminous Efficacy": {"full_en": "Luminous Efficacy", "full_ru": "Световая эффективность", "ar": "الفعالية الضوئية", "desc": "كفاءة المصدر."},
    "Luminous Flux": {"full_en": "Luminous Flux", "full_ru": "Световой поток", "ar": "التدفق الضوئي", "desc": "كمية الضوء."},
    "Illuminance": {"full_en": "Illuminance", "full_ru": "Освещенность", "ar": "الإضاءة", "desc": "الضوء الساقط."},
    "Luminance": {"full_en": "Luminance", "full_ru": "Яркость", "ar": "السطوع", "desc": "الضوء المنعكس."},
    "Glare Index": {"full_en": "Glare Index", "full_ru": "Индекс бликов", "ar": "مؤشر الوهج", "desc": "تقييم الوهج."},
    "Unified Glare Rating": {"full_en": "Unified Glare Rating", "full_ru": "Единая оценка бликов", "ar": "تقييم الوهج الموحد", "desc": "تقييم دولي."},
}


# ═══════════════════════════════════════════════════════════════════════════════
#  Translation Engines
# ═══════════════════════════════════════════════════════════════════════════════
DEEPL_API_KEY = os.environ.get("DEEPL_API_KEY", "")


def fetch_deepl_translation(text, from_lang, to_lang):
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
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {"client": "gtx", "sl": from_lang, "tl": to_lang, "dt": "t", "q": text.strip()}
        r = requests.get(url, params=params, timeout=10).json()
        return "".join([p[0] for p in r[0] if p[0]])
    except Exception:
        return text


def fetch_ai_translation(text, from_lang, to_lang):
    result = fetch_deepl_translation(text, from_lang, to_lang)
    if result:
        return result, "DeepL"
    return fetch_google_translation(text, from_lang, to_lang), "Google"


# ═══════════════════════════════════════════════════════════════════════════════
#  Helpers
# ═══════════════════════════════════════════════════════════════════════════════
def calculate_distance(s1, s2):
    if len(s1) < len(s2):
        return calculate_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    prev = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        cur = [i + 1]
        for j, c2 in enumerate(s2):
            cur.append(min(prev[j + 1] + 1, cur[j] + 1, prev[j] + (c1 != c2)))
        prev = cur
    return prev[-1]


def check_do_you_mean(text):
    words = text.lower().replace(",", " ").replace(".", " ").split()
    sug = []
    for w in words:
        if len(w) < 3 or w in site_slang_db:
            continue
        for k in site_slang_db:
            d = calculate_distance(w, k)
            if d == 1 or (len(k) > 6 and d == 2):
                if k not in sug:
                    sug.append(k)
    return sug


def detect_site_slang(text):
    tl = text.lower()
    return [{"term": k.title(), "academic": v["academic"], "slang": v["slang"], "desc": v["desc"]}
            for k, v in site_slang_db.items() if k in tl]


def detect_abbreviations(text):
    """Detect abbreviations in text and return their full meanings.
    Also detects acronyms formed by first letters of words."""
    found = []
    text_upper = text.upper()
    text_words = text.split()

    # Direct abbreviation match
    for abbr, data in abbreviations_db.items():
        if abbr.upper() in text_upper or abbr in text_words:
            found.append({
                "abbr": abbr,
                "full_en": data["full_en"],
                "full_ru": data["full_ru"],
                "ar": data["ar"],
                "desc": data["desc"],
                "match_type": "direct"
            })

    # Reverse acronym detection: check if words form acronym
    strip_chars = """.,;:!?()[]{}"'"""
    words_clean = [w.strip(strip_chars).upper() for w in text_words if len(w.strip(strip_chars)) > 1]
    for abbr, data in abbreviations_db.items():
        if len(abbr) >= 2:
            abbr_chars = list(abbr.upper())
            # Look for sequence of words starting with these letters
            for i in range(len(words_clean) - len(abbr) + 1):
                match = True
                for j, char in enumerate(abbr_chars):
                    if not words_clean[i + j].startswith(char):
                        match = False
                        break
                if match:
                    # Check if not already found
                    if not any(f["abbr"] == abbr for f in found):
                        found.append({
                            "abbr": abbr,
                            "full_en": data["full_en"],
                            "full_ru": data["full_ru"],
                            "ar": data["ar"],
                            "desc": data["desc"],
                            "match_type": "acronym"
                        })
                    break

    return found


# ═══════════════════════════════════════════════════════════════════════════════
#  Formulation Engine (per domain) — 15 DOMAINS
# ═══════════════════════════════════════════════════════════════════════════════
FORMULA_TEMPLATES = {
    "political": {
        "ar": {"يجب": "تؤكد السياسة الرسمية على", "المقاول": "الجهة المنفذة", "رب العمل": "الجهة المالكة", "من أجل": "في إطار السياسة العامة لـ"},
        "en_prefix": "In the political context, "
    },
    "legal": {
        "ar": {"يجب": "يلتزم الطرف الثاني بـ", "المقاول": "يتعين على المقاول", "رب العمل": "صاحب العمل تعاقدياً", "من أجل": "بموجب الالتزامات التعاقدية"},
        "en_prefix": "It is strictly stipulated that "
    },
    "economic": {
        "ar": {"يجب": "يقتضي التحليل الاقتصادي", "المقاول": "الجهة الاقتصادية المنفذة", "رب العمل": "الجهة المستثمرة", "من أجل": "بهدف تحقيق الجدوى الاقتصادية لـ"},
        "en_prefix": "From an economic perspective, "
    },
    "medical": {
        "ar": {"يجب": "يُنصح سريرياً بـ", "المقاول": "الفريق الطبي المنفذ", "رب العمل": "المؤسسة الصحية المالكة", "من أجل": "للحفاظ على السلامة الصحية في"},
        "en_prefix": "Clinically, "
    },
    "scientific": {
        "ar": {"يجب": "تُظهر الدراسة العلمية ضرورة", "المقاول": "الجهة البحثية المنفذة", "رب العمل": "الجهة الراعية للبحث", "من أجل": "من منطلق المنهجية العلمية لـ"},
        "en_prefix": "Scientifically, "
    },
    "engineering": {
        "ar": {"يجب": "يتطلب التصميم الهندسي", "المقاول": "المقاول المنفذ", "رب العمل": "المالك (Employer)", "من أجل": "لضمان الموثوقية الفنية في"},
        "en_prefix": "From an engineering standpoint, "
    },
    "military": {
        "ar": {"يجب": "تقتضي الضرورة العسكرية", "المقاول": "الوحدة المنفذة", "رب العمل": "القيادة العليا", "من أجل": "في إطار المهمة العسكرية لـ"},
        "en_prefix": "From a military standpoint, "
    },
    "educational": {
        "ar": {"يجب": "يُوصي المنهج التعليمي بـ", "المقاول": "الجهة التعليمية المنفذة", "رب العمل": "الإدارة الأكاديمية", "من أجل": "لتحقيق الأهداف التعليمية لـ"},
        "en_prefix": "From an educational perspective, "
    },
    "religious": {
        "ar": {"يجب": "يُشير الشرع الحنيف إلى", "المقاول": "الجهة الدينية المنفذة", "رب العمل": "الهيئة الشرعية", "من أجل": "في سبيل تحقيق المقصد الديني لـ"},
        "en_prefix": "From a religious perspective, "
    },
    "sports": {
        "ar": {"يجب": "يقتضي النظام الرياضي", "المقاول": "الفريق المنفذ", "رب العمل": "الإدارة الرياضية", "من أجل": "لتحقيق الأداء الرياضي في"},
        "en_prefix": "In the sporting context, "
    },
    "literary": {
        "ar": {"يجب": "يقتضي الأسلوب الأدبي", "المقاول": "الكاتب المنفذ", "رب العمل": "دار النشر", "من أجل": "لإبراز البعد الأدبي في"},
        "en_prefix": "From a literary perspective, "
    },
    "it": {
        "ar": {"يجب": "تقتضي متطلبات النظام التقني", "المقاول": "مطور البرنامج", "رب العمل": "مدير المشروع التقني", "من أجل": "لتحقيق الأداء التقني لـ"},
        "en_prefix": "From a technical standpoint, "
    },
    "environmental": {
        "ar": {"يجب": "تقتضي المعايير البيئية", "المقاول": "الجهة البيئية المنفذة", "رب العمل": "الجهة الراعية للبيئة", "من أجل": "لحماية البيئة في"},
        "en_prefix": "From an environmental standpoint, "
    },
    "agricultural": {
        "ar": {"يجب": "تقتضي الممارسات الزراعية", "المقاول": "المزارع المنفذ", "رب العمل": "صاحب المزرعة", "من أجل": "لتحسين الإنتاج الزراعي في"},
        "en_prefix": "From an agricultural perspective, "
    },
    "media": {
        "ar": {"يجب": "تقتضي المهنية الإعلامية", "المقاول": "الجهة الإعلامية المنفذة", "رب العمل": "الإدارة الإعلامية", "من أجل": "لتحقيق التغطية الإعلامية لـ"},
        "en_prefix": "From a media perspective, "
    },
    "tourism": {
        "ar": {"يجب": "تقتضي معايير السياحة", "المقاول": "وكالة السفر المنفذة", "رب العمل": "الجهة السياحية المالكة", "من أجل": "لتعزيز التجربة السياحية في"},
        "en_prefix": "From a tourism standpoint, "
    },
    "general": {
        "ar": {},
        "en_prefix": "",
        "en_replacements": {}
    }
}

# Domain-specific terminology replacements for richer translations
DOMAIN_TERMS = {
    "political": {
        "ar": {"عقد": "اتفاقية سياسية", "اتفاقية": "معاهدة دولية", "قانون": "تشريع", "حكم": "قرار سياسي", "قرار": "قرار سياسي", "بند": "بند اتفاقي", "التزام": "التزام دولي", "حق": "حق سياسي", "ملكية": "سيادة", "مسؤولية": "مسؤولية سياسية"},
        "en": {"contract": "political agreement", "agreement": "treaty", "law": "legislation", "judgment": "political decision", "decision": "political resolution", "clause": "diplomatic clause", "obligation": "international commitment", "right": "political right", "property": "sovereignty", "liability": "political responsibility"}
    },
    "legal": {
        "ar": {"عقد": "عقد قانوني ملزم", "اتفاقية": "اتفاقية قانونية", "قانون": "نص قانوني", "حكم": "حكم قضائي", "قرار": "قرار قضائي", "بند": "بند تعاقدي", "التزام": "التزام قانوني", "حق": "حق قانوني", "ملكية": "ملكية شرعية", "مسؤولية": "مسؤولية قانونية"},
        "en": {"contract": "legally binding contract", "agreement": "legal agreement", "law": "statute", "judgment": "court ruling", "decision": "legal decision", "clause": "contractual clause", "obligation": "legal obligation", "right": "legal right", "property": "legal property", "liability": "legal liability"}
    },
    "economic": {
        "ar": {"عقد": "عقد اقتصادي", "اتفاقية": "اتفاقية تجارية", "قانون": "قانون مالي", "حكم": "قرار اقتصادي", "قرار": "قرار استثماري", "بند": "بند مالي", "التزام": "التزام مالي", "حق": "حق اقتصادي", "ملكية": "ملكية اقتصادية", "مسؤولية": "مسؤولية مالية"},
        "en": {"contract": "economic contract", "agreement": "trade agreement", "law": "financial law", "judgment": "economic decision", "decision": "investment decision", "clause": "financial clause", "obligation": "financial obligation", "right": "economic right", "property": "economic asset", "liability": "financial liability"}
    },
    "medical": {
        "ar": {"عقد": "بروتوكول علاجي", "اتفاقية": "اتفاقية صحية", "قانون": "قانون صحي", "حكم": "تشخيص", "قرار": "قرار طبي", "بند": "بند صحي", "التزام": "التزام صحي", "حق": "حق صحي", "ملكية": "ملكية صحية", "مسؤولية": "مسؤولية طبية"},
        "en": {"contract": "treatment protocol", "agreement": "health agreement", "law": "health law", "judgment": "diagnosis", "decision": "medical decision", "clause": "health clause", "obligation": "health obligation", "right": "health right", "property": "health facility", "liability": "medical liability"}
    },
    "scientific": {
        "ar": {"عقد": "بروتوكول بحثي", "اتفاقية": "اتفاقية علمية", "قانون": "قانون علمي", "حكم": "نتيجة علمية", "قرار": "قرار بحثي", "بند": "بند علمي", "التزام": "التزام علمي", "حق": "حق علمي", "ملكية": "ملكية فكرية", "مسؤولية": "مسؤولية علمية"},
        "en": {"contract": "research protocol", "agreement": "scientific agreement", "law": "scientific law", "judgment": "scientific finding", "decision": "research decision", "clause": "scientific clause", "obligation": "research obligation", "right": "scientific right", "property": "intellectual property", "liability": "scientific liability"}
    },
    "engineering": {
        "ar": {"عقد": "عقد إنشائي", "اتفاقية": "اتفاقية هندسية", "قانون": "مواصفة فنية", "حكم": "قرار هندسي", "قرار": "قرار فني", "بند": "بند هندسي", "التزام": "التزام فني", "حق": "حق هندسي", "ملكية": "ملكية هندسية", "مسؤولية": "مسؤولية فنية"},
        "en": {"contract": "construction contract", "agreement": "engineering agreement", "law": "technical specification", "judgment": "engineering decision", "decision": "technical decision", "clause": "technical clause", "obligation": "technical obligation", "right": "engineering right", "property": "engineering asset", "liability": "technical liability"}
    },
    "military": {
        "ar": {"عقد": "أمر عسكري", "اتفاقية": "اتفاقية عسكرية", "قانون": "قانون عسكري", "حكم": "قرار عسكري", "قرار": "أمر عمليات", "بند": "بند عسكري", "التزام": "التزام عسكري", "حق": "حق عسكري", "ملكية": "ملكية عسكرية", "مسؤولية": "مسؤولية عسكرية"},
        "en": {"contract": "military order", "agreement": "military agreement", "law": "military law", "judgment": "military decision", "decision": "operational order", "clause": "military clause", "obligation": "military obligation", "right": "military right", "property": "military asset", "liability": "military liability"}
    },
    "educational": {
        "ar": {"عقد": "عقد تعليمي", "اتفاقية": "اتفاقية أكاديمية", "قانون": "قانون تعليمي", "حكم": "قرار أكاديمي", "قرار": "قرار تعليمي", "بند": "بند أكاديمي", "التزام": "التزام أكاديمي", "حق": "حق تعليمي", "ملكية": "ملكية فكرية", "مسؤولية": "مسؤولية تعليمية"},
        "en": {"contract": "educational contract", "agreement": "academic agreement", "law": "education law", "judgment": "academic decision", "decision": "educational decision", "clause": "academic clause", "obligation": "academic obligation", "right": "educational right", "property": "academic property", "liability": "educational liability"}
    },
    "religious": {
        "ar": {"عقد": "عقد ديني", "اتفاقية": "اتفاقية شرعية", "قانون": "حكم شرعي", "حكم": "فتوى", "قرار": "قرار ديني", "بند": "بند شرعي", "التزام": "التزام ديني", "حق": "حق شرعي", "ملكية": "ملكية شرعية", "مسؤولية": "مسؤولية دينية"},
        "en": {"contract": "religious covenant", "agreement": "religious agreement", "law": "religious law", "judgment": "religious ruling", "decision": "religious decision", "clause": "religious clause", "obligation": "religious obligation", "right": "religious right", "property": "religious property", "liability": "religious liability"}
    },
    "sports": {
        "ar": {"عقد": "عقد رياضي", "اتفاقية": "اتفاقية رياضية", "قانون": "قانون رياضي", "حكم": "قرار تحكيمي", "قرار": "قرار رياضي", "بند": "بند رياضي", "التزام": "التزام رياضي", "حق": "حق رياضي", "ملكية": "ملكية نادي", "مسؤولية": "مسؤولية رياضية"},
        "en": {"contract": "sports contract", "agreement": "sports agreement", "law": "sports law", "judgment": "referee decision", "decision": "sports decision", "clause": "sports clause", "obligation": "sports obligation", "right": "sports right", "property": "club asset", "liability": "sports liability"}
    },
    "literary": {
        "ar": {"عقد": "عقد أدبي", "اتفاقية": "اتفاقية أدبية", "قانون": "قانون أدبي", "حكم": "حكم أدبي", "قرار": "قرار أدبي", "بند": "بند أدبي", "التزام": "التزام أدبي", "حق": "حق أدبي", "ملكية": "ملكية فكرية", "مسؤولية": "مسؤولية أدبية"},
        "en": {"contract": "literary contract", "agreement": "literary agreement", "law": "copyright law", "judgment": "literary critique", "decision": "editorial decision", "clause": "literary clause", "obligation": "literary obligation", "right": "author right", "property": "intellectual property", "liability": "literary liability"}
    },
    "it": {
        "ar": {"عقد": "عقد تقني", "اتفاقية": "اتفاقية تقنية", "قانون": "قانون تقني", "حكم": "قرار تقني", "قرار": "قرار تقني", "بند": "بند تقني", "التزام": "التزام تقني", "حق": "حق تقني", "ملكية": "ملكية رقمية", "مسؤولية": "مسؤولية تقنية"},
        "en": {"contract": "tech contract", "agreement": "tech agreement", "law": "tech law", "judgment": "tech decision", "decision": "tech decision", "clause": "tech clause", "obligation": "tech obligation", "right": "tech right", "property": "digital asset", "liability": "tech liability"}
    },
    "environmental": {
        "ar": {"عقد": "عقد بيئي", "اتفاقية": "اتفاقية بيئية", "قانون": "قانون بيئي", "حكم": "حكم بيئي", "قرار": "قرار بيئي", "بند": "بند بيئي", "التزام": "التزام بيئي", "حق": "حق بيئي", "ملكية": "ملكية طبيعية", "مسؤولية": "مسؤولية بيئية"},
        "en": {"contract": "environmental contract", "agreement": "environmental agreement", "law": "environmental law", "judgment": "environmental ruling", "decision": "environmental decision", "clause": "environmental clause", "obligation": "environmental obligation", "right": "environmental right", "property": "natural resource", "liability": "environmental liability"}
    },
    "agricultural": {
        "ar": {"عقد": "عقد زراعي", "اتفاقية": "اتفاقية زراعية", "قانون": "قانون زراعي", "حكم": "حكم زراعي", "قرار": "قرار زراعي", "بند": "بند زراعي", "التزام": "التزام زراعي", "حق": "حق زراعي", "ملكية": "ملكية زراعية", "مسؤولية": "مسؤولية زراعية"},
        "en": {"contract": "farm contract", "agreement": "agricultural agreement", "law": "agricultural law", "judgment": "agricultural ruling", "decision": "agricultural decision", "clause": "agricultural clause", "obligation": "agricultural obligation", "right": "agricultural right", "property": "farmland", "liability": "agricultural liability"}
    },
    "media": {
        "ar": {"عقد": "عقد إعلامي", "اتفاقية": "اتفاقية إعلامية", "قانون": "قانون إعلامي", "حكم": "حكم إعلامي", "قرار": "قرار إعلامي", "بند": "بند إعلامي", "التزام": "التزام إعلامي", "حق": "حق إعلامي", "ملكية": "ملكية إعلامية", "مسؤولية": "مسؤولية إعلامية"},
        "en": {"contract": "media contract", "agreement": "media agreement", "law": "media law", "judgment": "media ruling", "decision": "editorial decision", "clause": "media clause", "obligation": "media obligation", "right": "media right", "property": "media asset", "liability": "media liability"}
    },
    "tourism": {
        "ar": {"عقد": "عقد سياحي", "اتفاقية": "اتفاقية سياحية", "قانون": "قانون سياحي", "حكم": "حكم سياحي", "قرار": "قرار سياحي", "بند": "بند سياحي", "التزام": "التزام سياحي", "حق": "حق سياحي", "ملكية": "ملكية سياحية", "مسؤولية": "مسؤولية سياحية"},
        "en": {"contract": "tourism contract", "agreement": "tourism agreement", "law": "tourism law", "judgment": "tourism ruling", "decision": "tourism decision", "clause": "tourism clause", "obligation": "tourism obligation", "right": "tourism right", "property": "tourism asset", "liability": "tourism liability"}
    },
    "general": {
        "ar": {},
        "en": {}
    }
}


def build_formula(base, domain, to_lang):
    tmpl = FORMULA_TEMPLATES.get(domain, FORMULA_TEMPLATES["general"])
    terms = DOMAIN_TERMS.get(domain, DOMAIN_TERMS["general"])

    result = base

    # Apply domain-specific terminology replacements
    if to_lang == "ar":
        for k, v in terms.get("ar", {}).items():
            result = result.replace(k, v)
        # Apply formula templates
        for k, v in tmpl.get("ar", {}).items():
            result = result.replace(k, v)
    else:
        # For English and other languages
        for k, v in terms.get("en", {}).items():
            result = result.replace(k, v)
        prefix = tmpl.get("en_prefix", "")
        if prefix and result:
            result = prefix + result[0].lower() + result[1:]

    return result


# ═══════════════════════════════════════════════════════════════════════════════
#  Session State
# ═══════════════════════════════════════════════════════════════════════════════
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
    st.session_state.trigger_translate = True


# ═══════════════════════════════════════════════════════════════════════════════
#  UI: Language Selectors + Swap
# ═══════════════════════════════════════════════════════════════════════════════
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

# ═══════════════════════════════════════════════════════════════════════════════
#  Text Input
# ═══════════════════════════════════════════════════════════════════════════════
text_input = st.text_area(
    "",
    placeholder="اكتب أو الصق النص هنا — تقارير هندسية، بنود تعاقدية، مراسلات رسمية، نصوص سياسية، تقارير طبية...",
    height=160,
    key="text_input",
    on_change=on_text_change
)

btn = st.button("🌐  Translate", use_container_width=True, type="primary", key="translate_btn")

st.divider()

# ═══════════════════════════════════════════════════════════════════════════════
#  Translation Logic
# ═══════════════════════════════════════════════════════════════════════════════
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
        st.info("💡 **Tip:** أضف مفتاح DeepL API في `secrets.toml` (DEEPL_API_KEY) لدقة أعلى. احصل على مفتاح مجاني من deepl.com/pro-api")

    # Detect domains
    detected_domains = detect_domains(text)

    # Show detected domains banner (only if actually detected)
    if detected_domains:
        badges = ""
        for d in detected_domains:
            info = DOMAIN_KEYWORDS[d]
            badges += f'<span class="domain-badge db-{d}">{info["emoji"]} {info["name_ar"]}</span>'
        st.markdown(f'<div class="detected-box">🔍 <b>تم التعرف تلقائياً على المجال:</b> {badges}</div>', unsafe_allow_html=True)

    # Detect abbreviations
    detected_abbrevs = detect_abbreviations(text)
    if detected_abbrevs:
        for a in detected_abbrevs:
            match_label = "🔤 Direct" if a['match_type'] == "direct" else "🔠 Acronym detected"
            st.markdown(f"""
<div class="abbrev-box">
    <div style="font-size:11px;font-weight:600;color:#1565C0;margin-bottom:4px;">{match_label}</div>
    <div style="font-size:16px;font-weight:700;color:#0D47A1;margin-bottom:6px;">
        {a['abbr']} = <span style="color:#1565C0;">{a['ar']}</span>
    </div>
    <div style="font-size:13px;color:#374151;line-height:1.6;">
        🇬🇧 <b>English:</b> {a['full_en']}<br>
        🇷🇺 <b>Russian:</b> {a['full_ru']}<br>
        📝 <b>Note:</b> {a['desc']}
    </div>
</div>
""", unsafe_allow_html=True)

    # Did you mean
    sug = check_do_you_mean(text)
    if sug:
        fmt = ", ".join([f"<strong>{s.title()}</strong>" for s in sug])
        st.markdown(f'<div class="dym-box">💡 <b>Did you mean:</b> {fmt}?</div>', unsafe_allow_html=True)

    with st.spinner("Translating with best available engine..."):
        is_single = len(text.split()) == 1
        base, engine_used = fetch_ai_translation(text, fl, tl)

        if is_single:
            st.markdown(f"### 🗄️ All Possible Meanings for: `{text}`")
            # Show ALL domains, highlighting detected ones
            all_domains = [k for k in DOMAIN_KEYWORDS.keys() if k != "general"] + ["general"]
            rows = ""
            for d in all_domains:
                info = DOMAIN_KEYWORDS[d]
                formulated = build_formula(base, d, tl)
                highlight = " ✅ **(Detected)**" if d in detected_domains else ""
                rows += f"| {info['emoji']} **{info['name_ar']}**{highlight} | {formulated} |\n"
            st.markdown(f"""
| المجال | المعنى |
|:---|:---|
{rows}
""")
        else:
            st.markdown("### 📚 All Possible Domain Translations")
            # Show ALL domains, highlighting detected ones
            all_domains = [k for k in DOMAIN_KEYWORDS.keys() if k != "general"] + ["general"]

            # Build cards for ALL domains
            cards = []
            for d in all_domains:
                info = DOMAIN_KEYWORDS[d]
                formulated = build_formula(base, d, tl)
                # Highlight detected domains
                highlight_class = " rcard-detected" if d in detected_domains else ""
                cards.append((d, info, formulated, highlight_class))

            # Render in rows of 3
            for i in range(0, len(cards), 3):
                batch = cards[i:i + 3]
                cols = st.columns(len(batch))
                for col, (d, info, formulated, highlight) in zip(cols, batch):
                    with col:
                        detected_badge = " ✅" if d in detected_domains else ""
                        st.markdown(
                            f'<div class="rcard rcard-{d}{highlight}">'
                            f'<div class="rlabel rlabel-{d}">{info["emoji"]} {info["name_en"].upper()}{detected_badge}</div>'
                            f'<div class="rtext">{formulated}</div>'
                            f'</div>',
                            unsafe_allow_html=True
                        )

            # Site slang detector
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
