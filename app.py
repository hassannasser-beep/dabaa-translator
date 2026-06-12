import streamlit as st
import requests
import os
import re

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
#  DOMAIN-SPECIFIC DICTIONARIES — REAL DIFFERENT MEANINGS
# ═══════════════════════════════════════════════════════════════════════════════
# هذه القواميس تعطي معاني فعلية مختلفة حسب المجال لنفس الكلمة

DOMAIN_SPECIFIC_TRANSLATIONS = {
    # === الكلمة: "contract" / "عقد" ===
    "contract": {
        "political": {"ar": "معاهدة دولية", "en": "international treaty", "ru": "международный договор", "desc": "في السياق السياسي: اتفاق بين دول"},
        "legal": {"ar": "عقد قانوني ملزم", "en": "legally binding contract", "ru": "юридически обязательный договор", "desc": "في السياق القانوني: وثيقة قانونية"},
        "economic": {"ar": "عقد اقتصادي", "en": "economic agreement", "ru": "экономическое соглашение", "desc": "في السياق الاقتصادي: صفقة تجارية"},
        "medical": {"ar": "بروتوكول علاجي", "en": "treatment protocol", "ru": "протокол лечения", "desc": "في السياق الطبي: خطة علاج"},
        "scientific": {"ar": "بروتوكول بحثي", "en": "research protocol", "ru": "исследовательский протокол", "desc": "في السياق العلمي: اتفاقية بحث"},
        "engineering": {"ar": "عقد إنشائي", "en": "construction contract", "ru": "строительный контракт", "desc": "في السياق الهندسي: عقد تنفيذ"},
        "military": {"ar": "أمر عسكري", "en": "military order", "ru": "военный приказ", "desc": "في السياق العسكري: أمر عمليات"},
        "educational": {"ar": "عقد تعليمي", "en": "educational agreement", "ru": "образовательный договор", "desc": "في السياق التعليمي: اتفاقية تعليم"},
        "religious": {"ar": "عقد ديني", "en": "religious covenant", "ru": "религиозный договор", "desc": "في السياق الديني: عهد ديني"},
        "sports": {"ar": "عقد رياضي", "en": "sports contract", "ru": "спортивный контракт", "desc": "في السياق الرياضي: عقد لاعب"},
        "literary": {"ar": "عقد أدبي", "en": "literary contract", "ru": "литературный договор", "desc": "في السياق الأدبي: عقد نشر"},
        "it": {"ar": "عقد تقني", "en": "tech contract", "ru": "технический контракт", "desc": "في السياق التقني: اتفاقية تطوير"},
        "environmental": {"ar": "عقد بيئي", "en": "environmental agreement", "ru": "экологическое соглашение", "desc": "في السياق البيئي: اتفاقية حماية"},
        "agricultural": {"ar": "عقد زراعي", "en": "farm contract", "ru": "сельскохозяйственный договор", "desc": "في السياق الزراعي: عقد مزرعة"},
        "media": {"ar": "عقد إعلامي", "en": "media contract", "ru": "медийный контракт", "desc": "في السياق الإعلامي: عقد إعلان"},
        "tourism": {"ar": "عقد سياحي", "en": "tourism contract", "ru": "туристический договор", "desc": "في السياق السياحي: حجز وإقامة"},
        "general": {"ar": "عقد", "en": "contract", "ru": "контракт", "desc": "المعنى العام"}
    },
    # === الكلمة: "agreement" / "اتفاقية" ===
    "agreement": {
        "political": {"ar": "اتفاقية دولية", "en": "diplomatic treaty", "ru": "дипломатический договор", "desc": "معاهدة بين دول"},
        "legal": {"ar": "اتفاقية قانونية", "en": "legal agreement", "ru": "юридическое соглашение", "desc": "وثيقة قانونية"},
        "economic": {"ar": "اتفاقية تجارية", "en": "trade agreement", "ru": "торговое соглашение", "desc": "صفقة اقتصادية"},
        "medical": {"ar": "اتفاقية صحية", "en": "health agreement", "ru": "медицинское соглашение", "desc": "بروتوكول صحي"},
        "scientific": {"ar": "اتفاقية علمية", "en": "scientific agreement", "ru": "научное соглашение", "desc": "تعاون بحثي"},
        "engineering": {"ar": "اتفاقية هندسية", "en": "engineering agreement", "ru": "инженерное соглашение", "desc": "عقد هندسي"},
        "military": {"ar": "اتفاقية عسكرية", "en": "military agreement", "ru": "военное соглашение", "desc": "تعاون عسكري"},
        "educational": {"ar": "اتفاقية أكاديمية", "en": "academic agreement", "ru": "академическое соглашение", "desc": "تعاون جامعي"},
        "religious": {"ar": "اتفاقية شرعية", "en": "religious agreement", "ru": "религиозное соглашение", "desc": "عهدة دينية"},
        "sports": {"ar": "اتفاقية رياضية", "en": "sports agreement", "ru": "спортивное соглашение", "desc": "عقد رعاية"},
        "literary": {"ar": "اتفاقية أدبية", "en": "literary agreement", "ru": "литературное соглашение", "desc": "عقد نشر"},
        "it": {"ar": "اتفاقية تقنية", "en": "tech agreement", "ru": "техническое соглашение", "desc": "اتفاقية برمجيات"},
        "environmental": {"ar": "اتفاقية بيئية", "en": "environmental agreement", "ru": "экологическое соглашение", "desc": "اتفاقية مناخ"},
        "agricultural": {"ar": "اتفاقية زراعية", "en": "agricultural agreement", "ru": "сельскохозяйственное соглашение", "desc": "عقد محصول"},
        "media": {"ar": "اتفاقية إعلامية", "en": "media agreement", "ru": "медийное соглашение", "desc": "عقد بث"},
        "tourism": {"ar": "اتفاقية سياحية", "en": "tourism agreement", "ru": "туристическое соглашение", "desc": "حجز فنادق"},
        "general": {"ar": "اتفاقية", "en": "agreement", "ru": "соглашение", "desc": "المعنى العام"}
    },
    # === الكلمة: "law" / "قانون" ===
    "law": {
        "political": {"ar": "تشريع", "en": "legislation", "ru": "законодательство", "desc": "قانون دولي"},
        "legal": {"ar": "نص قانوني", "en": "statute", "ru": "указ", "desc": "نص تشريعي"},
        "economic": {"ar": "قانون مالي", "en": "financial law", "ru": "финансовый закон", "desc": "قانون اقتصادي"},
        "medical": {"ar": "قانون صحي", "en": "health law", "ru": "медицинский закон", "desc": "قانون طبي"},
        "scientific": {"ar": "قانون علمي", "en": "scientific law", "ru": "научный закон", "desc": "قانون طبيعة"},
        "engineering": {"ar": "مواصفة فنية", "en": "technical specification", "ru": "техническая спецификация", "desc": "معيار هندسي"},
        "military": {"ar": "قانون عسكري", "en": "military law", "ru": "военный закон", "desc": "نظام عسكري"},
        "educational": {"ar": "قانون تعليمي", "en": "education law", "ru": "образовательный закон", "desc": "نظام تعليمي"},
        "religious": {"ar": "حكم شرعي", "en": "religious law", "ru": "религиозный закон", "desc": "شريعة إسلامية"},
        "sports": {"ar": "قانون رياضي", "en": "sports law", "ru": "спортивный закон", "desc": "قانون اللعبة"},
        "literary": {"ar": "قانون أدبي", "en": "copyright law", "ru": "авторское право", "desc": "حقوق المؤلف"},
        "it": {"ar": "قانون تقني", "en": "tech law", "ru": "технический закон", "desc": "قانون سيبراني"},
        "environmental": {"ar": "قانون بيئي", "en": "environmental law", "ru": "экологический закон", "desc": "قانون حماية"},
        "agricultural": {"ar": "قانون زراعي", "en": "agricultural law", "ru": "сельскохозяйственный закон", "desc": "قانون أراضي"},
        "media": {"ar": "قانون إعلامي", "en": "media law", "ru": "медийный закон", "desc": "قانون نشر"},
        "tourism": {"ar": "قانون سياحي", "en": "tourism law", "ru": "туристический закон", "desc": "قانون سفر"},
        "general": {"ar": "قانون", "en": "law", "ru": "закон", "desc": "المعنى العام"}
    },
    # === الكلمة: "judgment" / "حكم" ===
    "judgment": {
        "political": {"ar": "قرار سياسي", "en": "political decision", "ru": "политическое решение", "desc": "قرار دبلوماسي"},
        "legal": {"ar": "حكم قضائي", "en": "court ruling", "ru": "судебное решение", "desc": "قرار المحكمة"},
        "economic": {"ar": "قرار اقتصادي", "en": "economic decision", "ru": "экономическое решение", "desc": "قرار استثماري"},
        "medical": {"ar": "تشخيص", "en": "diagnosis", "ru": "диагноз", "desc": "حالة مرضية"},
        "scientific": {"ar": "نتيجة علمية", "en": "scientific finding", "ru": "научный вывод", "desc": "نتيجة بحث"},
        "engineering": {"ar": "قرار هندسي", "en": "engineering decision", "ru": "инженерное решение", "desc": "قرار فني"},
        "military": {"ar": "قرار عسكري", "en": "military decision", "ru": "военное решение", "desc": "أمر قتال"},
        "educational": {"ar": "قرار أكاديمي", "en": "academic decision", "ru": "академическое решение", "desc": "قرار تعليمي"},
        "religious": {"ar": "فتوى", "en": "religious ruling", "ru": "религиозное постановление", "desc": "حكم شرعي"},
        "sports": {"ar": "قرار تحكيمي", "en": "referee decision", "ru": "решение судьи", "desc": "حكم المباراة"},
        "literary": {"ar": "حكم أدبي", "en": "literary critique", "ru": "литературная критика", "desc": "نقد أدبي"},
        "it": {"ar": "قرار تقني", "en": "tech decision", "ru": "техническое решение", "desc": "قرار برمجي"},
        "environmental": {"ar": "حكم بيئي", "en": "environmental ruling", "ru": "экологическое постановление", "desc": "قرار حماية"},
        "agricultural": {"ar": "حكم زراعي", "en": "agricultural ruling", "ru": "сельскохозяйственное решение", "desc": "قرار محصول"},
        "media": {"ar": "حكم إعلامي", "en": "media ruling", "ru": "медийное решение", "desc": "قرار رقابة"},
        "tourism": {"ar": "حكم سياحي", "en": "tourism ruling", "ru": "туристическое решение", "desc": "قرار سفر"},
        "general": {"ar": "حكم", "en": "judgment", "ru": "суждение", "desc": "المعنى العام"}
    },
    # === الكلمة: "decision" / "قرار" ===
    "decision": {
        "political": {"ar": "قرار سياسي", "en": "political resolution", "ru": "политическая резолюция", "desc": "قرار دبلوماسي"},
        "legal": {"ar": "قرار قضائي", "en": "legal decision", "ru": "юридическое решение", "desc": "قرار محكمة"},
        "economic": {"ar": "قرار استثماري", "en": "investment decision", "ru": "инвестиционное решение", "desc": "قرار مالي"},
        "medical": {"ar": "قرار طبي", "en": "medical decision", "ru": "медицинское решение", "desc": "قرار علاج"},
        "scientific": {"ar": "قرار بحثي", "en": "research decision", "ru": "исследовательское решение", "desc": "قرار علمي"},
        "engineering": {"ar": "قرار فني", "en": "technical decision", "ru": "техническое решение", "desc": "قرار تصميم"},
        "military": {"ar": "أمر عمليات", "en": "operational order", "ru": "оперативный приказ", "desc": "أمر عسكري"},
        "educational": {"ar": "قرار تعليمي", "en": "educational decision", "ru": "образовательное решение", "desc": "قرار أكاديمي"},
        "religious": {"ar": "قرار ديني", "en": "religious decision", "ru": "религиозное решение", "desc": "قرار شرعي"},
        "sports": {"ar": "قرار رياضي", "en": "sports decision", "ru": "спортивное решение", "desc": "قرار اتحاد"},
        "literary": {"ar": "قرار أدبي", "en": "editorial decision", "ru": "редакционное решение", "desc": "قرار نشر"},
        "it": {"ar": "قرار تقني", "en": "tech decision", "ru": "техническое решение", "desc": "قرار تقني"},
        "environmental": {"ar": "قرار بيئي", "en": "environmental decision", "ru": "экологическое решение", "desc": "قرار حماية"},
        "agricultural": {"ar": "قرار زراعي", "en": "agricultural decision", "ru": "сельскохозяйственное решение", "desc": "قرار محصول"},
        "media": {"ar": "قرار إعلامي", "en": "editorial decision", "ru": "редакционное решение", "desc": "قرار تحرير"},
        "tourism": {"ar": "قرار سياحي", "en": "tourism decision", "ru": "туристическое решение", "desc": "قرار سفر"},
        "general": {"ar": "قرار", "en": "decision", "ru": "решение", "desc": "المعنى العام"}
    },
    # === الكلمة: "clause" / "بند" ===
    "clause": {
        "political": {"ar": "بند اتفاقي", "en": "diplomatic clause", "ru": "дипломатическая оговорка", "desc": "بند معاهدة"},
        "legal": {"ar": "بند تعاقدي", "en": "contractual clause", "ru": "договорная оговорка", "desc": "شرط قانوني"},
        "economic": {"ar": "بند مالي", "en": "financial clause", "ru": "финансовая оговорка", "desc": "بند سعري"},
        "medical": {"ar": "بند صحي", "en": "health clause", "ru": "медицинская оговорка", "desc": "بند تأمين صحي"},
        "scientific": {"ar": "بند علمي", "en": "scientific clause", "ru": "научная оговорка", "desc": "بند بحث"},
        "engineering": {"ar": "بند هندسي", "en": "technical clause", "ru": "техническая оговорка", "desc": "بند مواصفات"},
        "military": {"ar": "بند عسكري", "en": "military clause", "ru": "военная оговорка", "desc": "بند تعاون عسكري"},
        "educational": {"ar": "بند أكاديمي", "en": "academic clause", "ru": "академическая оговорка", "desc": "بند منهج"},
        "religious": {"ar": "بند شرعي", "en": "religious clause", "ru": "религиозная оговорка", "desc": "بند فقهي"},
        "sports": {"ar": "بند رياضي", "en": "sports clause", "ru": "спортивная оговорка", "desc": "بند عقد لاعب"},
        "literary": {"ar": "بند أدبي", "en": "literary clause", "ru": "литературная оговорка", "desc": "بند نشر"},
        "it": {"ar": "بند تقني", "en": "tech clause", "ru": "техническая оговорка", "desc": "بند برمجيات"},
        "environmental": {"ar": "بند بيئي", "en": "environmental clause", "ru": "экологическая оговорка", "desc": "بند حماية"},
        "agricultural": {"ar": "بند زراعي", "en": "agricultural clause", "ru": "сельскохозяйственная оговорка", "desc": "بند محصول"},
        "media": {"ar": "بند إعلامي", "en": "media clause", "ru": "медийная оговорка", "desc": "بند إعلان"},
        "tourism": {"ar": "بند سياحي", "en": "tourism clause", "ru": "туристическая оговорка", "desc": "بند حجز"},
        "general": {"ar": "بند", "en": "clause", "ru": "пункт", "desc": "المعنى العام"}
    },
    # === الكلمة: "obligation" / "التزام" ===
    "obligation": {
        "political": {"ar": "التزام دولي", "en": "international commitment", "ru": "международное обязательство", "desc": "التزام دبلوماسي"},
        "legal": {"ar": "التزام قانوني", "en": "legal obligation", "ru": "юридическое обязательство", "desc": "التزام تعاقدي"},
        "economic": {"ar": "التزام مالي", "en": "financial obligation", "ru": "финансовое обязательство", "desc": "التزام مالي"},
        "medical": {"ar": "التزام صحي", "en": "health obligation", "ru": "медицинское обязательство", "desc": "التزام طبي"},
        "scientific": {"ar": "التزام علمي", "en": "research obligation", "ru": "научное обязательство", "desc": "التزام بحثي"},
        "engineering": {"ar": "التزام فني", "en": "technical obligation", "ru": "техническое обязательство", "desc": "التزام هندسي"},
        "military": {"ar": "التزام عسكري", "en": "military obligation", "ru": "военное обязательство", "desc": "التزام قتالي"},
        "educational": {"ar": "التزام أكاديمي", "en": "academic obligation", "ru": "академическое обязательство", "desc": "التزام تعليمي"},
        "religious": {"ar": "التزام ديني", "en": "religious obligation", "ru": "религиозное обязательство", "desc": "فريضة دينية"},
        "sports": {"ar": "التزام رياضي", "en": "sports obligation", "ru": "спортивное обязательство", "desc": "التزام لاعب"},
        "literary": {"ar": "التزام أدبي", "en": "literary obligation", "ru": "литературное обязательство", "desc": "التزام نشر"},
        "it": {"ar": "التزام تقني", "en": "tech obligation", "ru": "техническое обязательство", "desc": "التزام تقني"},
        "environmental": {"ar": "التزام بيئي", "en": "environmental obligation", "ru": "экологическое обязательство", "desc": "التزام حماية"},
        "agricultural": {"ar": "التزام زراعي", "en": "agricultural obligation", "ru": "сельскохозяйственное обязательство", "desc": "التزام مزرعة"},
        "media": {"ar": "التزام إعلامي", "en": "media obligation", "ru": "медийное обязательство", "desc": "التزام صحفي"},
        "tourism": {"ar": "التزام سياحي", "en": "tourism obligation", "ru": "туристическое обязательство", "desc": "التزام سفر"},
        "general": {"ar": "التزام", "en": "obligation", "ru": "обязательство", "desc": "المعنى العام"}
    },
    # === الكلمة: "right" / "حق" ===
    "right": {
        "political": {"ar": "حق سياسي", "en": "political right", "ru": "политическое право", "desc": "حق مواطنة"},
        "legal": {"ar": "حق قانوني", "en": "legal right", "ru": "юридическое право", "desc": "حق شرعي"},
        "economic": {"ar": "حق اقتصادي", "en": "economic right", "ru": "экономическое право", "desc": "حق مالي"},
        "medical": {"ar": "حق صحي", "en": "health right", "ru": "медицинское право", "desc": "حق علاج"},
        "scientific": {"ar": "حق علمي", "en": "scientific right", "ru": "научное право", "desc": "حق بحث"},
        "engineering": {"ar": "حق هندسي", "en": "engineering right", "ru": "инженерное право", "desc": "حق فني"},
        "military": {"ar": "حق عسكري", "en": "military right", "ru": "военное право", "desc": "حق قتال"},
        "educational": {"ar": "حق تعليمي", "en": "educational right", "ru": "образовательное право", "desc": "حق تعلم"},
        "religious": {"ar": "حق شرعي", "en": "religious right", "ru": "религиозное право", "desc": "حق ديني"},
        "sports": {"ar": "حق رياضي", "en": "sports right", "ru": "спортивное право", "desc": "حق لعب"},
        "literary": {"ar": "حق أدبي", "en": "author right", "ru": "авторское право", "desc": "حق نشر"},
        "it": {"ar": "حق تقني", "en": "tech right", "ru": "техническое право", "desc": "حق رقمي"},
        "environmental": {"ar": "حق بيئي", "en": "environmental right", "ru": "экологическое право", "desc": "حق نظيف"},
        "agricultural": {"ar": "حق زراعي", "en": "agricultural right", "ru": "сельскохозяйственное право", "desc": "حق أرض"},
        "media": {"ar": "حق إعلامي", "en": "media right", "ru": "медийное право", "desc": "حق صحافة"},
        "tourism": {"ar": "حق سياحي", "en": "tourism right", "ru": "туристическое право", "desc": "حق سفر"},
        "general": {"ar": "حق", "en": "right", "ru": "право", "desc": "المعنى العام"}
    },
    # === الكلمة: "property" / "ملكية" ===
    "property": {
        "political": {"ar": "سيادة", "en": "sovereignty", "ru": "суверенитет", "desc": "سيادة دولة"},
        "legal": {"ar": "ملكية شرعية", "en": "legal property", "ru": "законная собственность", "desc": "ملكية قانونية"},
        "economic": {"ar": "ملكية اقتصادية", "en": "economic asset", "ru": "экономический актив", "desc": "أصل مالي"},
        "medical": {"ar": "ملكية صحية", "en": "health facility", "ru": "медицинское учреждение", "desc": "مستشفى أو عيادة"},
        "scientific": {"ar": "ملكية فكرية", "en": "intellectual property", "ru": "интеллектуальная собственность", "desc": "براءة اختراع"},
        "engineering": {"ar": "ملكية هندسية", "en": "engineering asset", "ru": "инженерный актив", "desc": "معدات هندسية"},
        "military": {"ar": "ملكية عسكرية", "en": "military asset", "ru": "военный актив", "desc": "سلاح أو معدات"},
        "educational": {"ar": "ملكية فكرية", "en": "academic property", "ru": "академическая собственность", "desc": "بحث أو براءة"},
        "religious": {"ar": "ملكية شرعية", "en": "religious property", "ru": "религиозная собственность", "desc": "وقف أو دير"},
        "sports": {"ar": "ملكية نادي", "en": "club asset", "ru": "актив клуба", "desc": "ملعب أو لاعب"},
        "literary": {"ar": "ملكية فكرية", "en": "intellectual property", "ru": "интеллектуальная собственность", "desc": "حقوق مؤلف"},
        "it": {"ar": "ملكية رقمية", "en": "digital asset", "ru": "цифровой актив", "desc": "برمجيات أو بيانات"},
        "environmental": {"ar": "ملكية طبيعية", "en": "natural resource", "ru": "природный ресурс", "desc": "غابة أو نهر"},
        "agricultural": {"ar": "ملكية زراعية", "en": "farmland", "ru": "сельскохозяйственные угодья", "desc": "أرض زراعية"},
        "media": {"ar": "ملكية إعلامية", "en": "media asset", "ru": "медийный актив", "desc": "قناة أو صحيفة"},
        "tourism": {"ar": "ملكية سياحية", "en": "tourism asset", "ru": "туристический актив", "desc": "فندق أو أثر"},
        "general": {"ar": "ملكية", "en": "property", "ru": "собственность", "desc": "المعنى العام"}
    },
    # === الكلمة: "liability" / "مسؤولية" ===
    "liability": {
        "political": {"ar": "مسؤولية سياسية", "en": "political responsibility", "ru": "политическая ответственность", "desc": "مسؤولية دبلوماسية"},
        "legal": {"ar": "مسؤولية قانونية", "en": "legal liability", "ru": "юридическая ответственность", "desc": "مسؤولية تعاقدية"},
        "economic": {"ar": "مسؤولية مالية", "en": "financial liability", "ru": "финансовая ответственность", "desc": "دين أو التزام مالي"},
        "medical": {"ar": "مسؤولية طبية", "en": "medical liability", "ru": "медицинская ответственность", "desc": "خطأ طبي"},
        "scientific": {"ar": "مسؤولية علمية", "en": "scientific liability", "ru": "научная ответственность", "desc": "خطأ بحثي"},
        "engineering": {"ar": "مسؤولية فنية", "en": "technical liability", "ru": "техническая ответственность", "desc": "خطأ هندسي"},
        "military": {"ar": "مسؤولية عسكرية", "en": "military liability", "ru": "военная ответственность", "desc": "مسؤولية قتال"},
        "educational": {"ar": "مسؤولية تعليمية", "en": "educational liability", "ru": "образовательная ответственность", "desc": "مسؤولية تدريس"},
        "religious": {"ar": "مسؤولية دينية", "en": "religious liability", "ru": "религиозная ответственность", "desc": "مسؤولية شرعية"},
        "sports": {"ar": "مسؤولية رياضية", "en": "sports liability", "ru": "спортивная ответственность", "desc": "إصابة لاعب"},
        "literary": {"ar": "مسؤولية أدبية", "en": "literary liability", "ru": "литературная ответственность", "desc": "سرقة أدبية"},
        "it": {"ar": "مسؤولية تقنية", "en": "tech liability", "ru": "техническая ответственность", "desc": "اختراق بيانات"},
        "environmental": {"ar": "مسؤولية بيئية", "en": "environmental liability", "ru": "экологическая ответственность", "desc": "تلويث"},
        "agricultural": {"ar": "مسؤولية زراعية", "en": "agricultural liability", "ru": "сельскохозяйственная ответственность", "desc": "فشل محصول"},
        "media": {"ar": "مسؤولية إعلامية", "en": "media liability", "ru": "медийная ответственность", "desc": "تشهير أو ذم"},
        "tourism": {"ar": "مسؤولية سياحية", "en": "tourism liability", "ru": "туристическая ответственность", "desc": "حادث سائح"},
        "general": {"ar": "مسؤولية", "en": "liability", "ru": "ответственность", "desc": "المعنى العام"}
    },
    # === الكلمة: "treatment" / "علاج" ===
    "treatment": {
        "political": {"ar": "معاملة دبلوماسية", "en": "diplomatic treatment", "ru": "дипломатическое обращение", "desc": "معاملة دول"},
        "legal": {"ar": "معاملة قانونية", "en": "legal treatment", "ru": "юридическое обращение", "desc": "معاملة متهم"},
        "economic": {"ar": "معاملة مالية", "en": "financial treatment", "ru": "финансовое обращение", "desc": "معاملة ضريبية"},
        "medical": {"ar": "علاج طبي", "en": "medical treatment", "ru": "медицинское лечение", "desc": "علاج مرض"},
        "scientific": {"ar": "معالجة بحثية", "en": "scientific treatment", "ru": "научная обработка", "desc": "تحليل بيانات"},
        "engineering": {"ar": "معالجة هندسية", "en": "engineering treatment", "ru": "инженерная обработка", "desc": "معالجة سطح"},
        "military": {"ar": "معاملة عسكرية", "en": "military treatment", "ru": "военное обращение", "desc": "معاملة أسرى"},
        "educational": {"ar": "معاملة تعليمية", "en": "educational treatment", "ru": "образовательное обращение", "desc": "معاملة طلاب"},
        "religious": {"ar": "معاملة دينية", "en": "religious treatment", "ru": "религиозное обращение", "desc": "معاملة شرعية"},
        "sports": {"ar": "معاملة رياضية", "en": "sports treatment", "ru": "спортивное обращение", "desc": "إصابة لاعب"},
        "literary": {"ar": "معاملة أدبية", "en": "literary treatment", "ru": "литературная обработка", "desc": "أسلوب سرد"},
        "it": {"ar": "معالجة تقنية", "en": "tech treatment", "ru": "техническая обработка", "desc": "معالجة بيانات"},
        "environmental": {"ar": "معالجة بيئية", "en": "environmental treatment", "ru": "экологическая обработка", "desc": "معالجة مياه"},
        "agricultural": {"ar": "معالجة زراعية", "en": "agricultural treatment", "ru": "сельскохозяйственная обработка", "desc": "مبيدات"},
        "media": {"ar": "معاملة إعلامية", "en": "media treatment", "ru": "медийное обращение", "desc": "تغطية إعلامية"},
        "tourism": {"ar": "معاملة سياحية", "en": "tourism treatment", "ru": "туристическое обращение", "desc": "خدمة ضيافة"},
        "general": {"ar": "معاملة", "en": "treatment", "ru": "обращение", "desc": "المعنى العام"}
    },
    # === الكلمة: "analysis" / "تحليل" ===
    "analysis": {
        "political": {"ar": "تحليل سياسي", "en": "political analysis", "ru": "политический анализ", "desc": "تحليل موقف دولي"},
        "legal": {"ar": "تحليل قانوني", "en": "legal analysis", "ru": "юридический анализ", "desc": "تحليل نص قانوني"},
        "economic": {"ar": "تحليل اقتصادي", "en": "economic analysis", "ru": "экономический анализ", "desc": "تحليل سوق"},
        "medical": {"ar": "تحليل طبي", "en": "medical analysis", "ru": "медицинский анализ", "desc": "تحليل مخبري"},
        "scientific": {"ar": "تحليل علمي", "en": "scientific analysis", "ru": "научный анализ", "desc": "تحليل تجربة"},
        "engineering": {"ar": "تحليل هندسي", "en": "engineering analysis", "ru": "инженерный анализ", "desc": "تحليل إنشائي"},
        "military": {"ar": "تحليل عسكري", "en": "military analysis", "ru": "военный анализ", "desc": "تحليل استخباراتي"},
        "educational": {"ar": "تحليل تعليمي", "en": "educational analysis", "ru": "образовательный анализ", "desc": "تحليل منهج"},
        "religious": {"ar": "تحليل ديني", "en": "religious analysis", "ru": "религиозный анализ", "desc": "تفسير نص ديني"},
        "sports": {"ar": "تحليل رياضي", "en": "sports analysis", "ru": "спортивный анализ", "desc": "تحليل أداء"},
        "literary": {"ar": "تحليل أدبي", "en": "literary analysis", "ru": "литературный анализ", "desc": "نقد نص أدبي"},
        "it": {"ar": "تحليل تقني", "en": "tech analysis", "ru": "технический анализ", "desc": "تحليل بيانات"},
        "environmental": {"ar": "تحليل بيئي", "en": "environmental analysis", "ru": "экологический анализ", "desc": "تحليل تلوث"},
        "agricultural": {"ar": "تحليل زراعي", "en": "agricultural analysis", "ru": "сельскохозяйственный анализ", "desc": "تحليل تربة"},
        "media": {"ar": "تحليل إعلامي", "en": "media analysis", "ru": "медийный анализ", "desc": "تحليل محتوى"},
        "tourism": {"ar": "تحليل سياحي", "en": "tourism analysis", "ru": "туристический анализ", "desc": "تحليل سوق سفر"},
        "general": {"ar": "تحليل", "en": "analysis", "ru": "анализ", "desc": "المعنى العام"}
    },
    # === الكلمة: "report" / "تقرير" ===
    "report": {
        "political": {"ar": "تقرير سياسي", "en": "political report", "ru": "политический отчет", "desc": "تقرير دبلوماسي"},
        "legal": {"ar": "تقرير قانوني", "en": "legal report", "ru": "юридический отчет", "desc": "تقرير تحقيق"},
        "economic": {"ar": "تقرير اقتصادي", "en": "economic report", "ru": "экономический отчет", "desc": "تقرير مالي"},
        "medical": {"ar": "تقرير طبي", "en": "medical report", "ru": "медицинский отчет", "desc": "تقرير حالة"},
        "scientific": {"ar": "تقرير علمي", "en": "scientific report", "ru": "научный отчет", "desc": "تقرير بحث"},
        "engineering": {"ar": "تقرير هندسي", "en": "engineering report", "ru": "инженерный отчет", "desc": "تقرير إشراف"},
        "military": {"ar": "تقرير عسكري", "en": "military report", "ru": "военный отчет", "desc": "تقرير استخبارات"},
        "educational": {"ar": "تقرير تعليمي", "en": "educational report", "ru": "образовательный отчет", "desc": "تقرير أكاديمي"},
        "religious": {"ar": "تقرير ديني", "en": "religious report", "ru": "религиозный отчет", "desc": "تقرير شرعي"},
        "sports": {"ar": "تقرير رياضي", "en": "sports report", "ru": "спортивный отчет", "desc": "تقرير مباراة"},
        "literary": {"ar": "تقرير أدبي", "en": "literary report", "ru": "литературный отчет", "desc": "تقرير نقد"},
        "it": {"ar": "تقرير تقني", "en": "tech report", "ru": "технический отчет", "desc": "تقرير برمجي"},
        "environmental": {"ar": "تقرير بيئي", "en": "environmental report", "ru": "экологический отчет", "desc": "تقرير تأثير"},
        "agricultural": {"ar": "تقرير زراعي", "en": "agricultural report", "ru": "сельскохозяйственный отчет", "desc": "تقرير محصول"},
        "media": {"ar": "تقرير إعلامي", "en": "media report", "ru": "медийный отчет", "desc": "تقرير صحفي"},
        "tourism": {"ar": "تقرير سياحي", "en": "tourism report", "ru": "туристический отчет", "desc": "تقرير رحلة"},
        "general": {"ar": "تقرير", "en": "report", "ru": "отчет", "desc": "المعنى العام"}
    },
    # === الكلمة: "system" / "نظام" ===
    "system": {
        "political": {"ar": "نظام سياسي", "en": "political system", "ru": "политическая система", "desc": "نظام حكم"},
        "legal": {"ar": "نظام قانوني", "en": "legal system", "ru": "правовая система", "desc": "منظومة تشريعية"},
        "economic": {"ar": "نظام اقتصادي", "en": "economic system", "ru": "экономическая система", "desc": "نظام مالي"},
        "medical": {"ar": "نظام صحي", "en": "health system", "ru": "медицинская система", "desc": "منظومة طبية"},
        "scientific": {"ar": "نظام علمي", "en": "scientific system", "ru": "научная система", "desc": "نظام بحث"},
        "engineering": {"ar": "نظام هندسي", "en": "engineering system", "ru": "инженерная система", "desc": "منظومة ميكانيكية"},
        "military": {"ar": "نظام عسكري", "en": "military system", "ru": "военная система", "desc": "نظام دفاع"},
        "educational": {"ar": "نظام تعليمي", "en": "educational system", "ru": "образовательная система", "desc": "منظومة تعليم"},
        "religious": {"ar": "نظام ديني", "en": "religious system", "ru": "религиозная система", "desc": "منظومة شرعية"},
        "sports": {"ar": "نظام رياضي", "en": "sports system", "ru": "спортивная система", "desc": "نظام بطولة"},
        "literary": {"ar": "نظام أدبي", "en": "literary system", "ru": "литературная система", "desc": "منظومة نقد"},
        "it": {"ar": "نظام تقني", "en": "tech system", "ru": "техническая система", "desc": "نظام برمجي"},
        "environmental": {"ar": "نظام بيئي", "en": "environmental system", "ru": "экологическая система", "desc": "منظومة طبيعية"},
        "agricultural": {"ar": "نظام زراعي", "en": "agricultural system", "ru": "сельскохозяйственная система", "desc": "نظام ري"},
        "media": {"ar": "نظام إعلامي", "en": "media system", "ru": "медийная система", "desc": "منظومة بث"},
        "tourism": {"ar": "نظام سياحي", "en": "tourism system", "ru": "туристическая система", "desc": "نظام حجز"},
        "general": {"ar": "نظام", "en": "system", "ru": "система", "desc": "المعنى العام"}
    },
    # === الكلمة: "plan" / "خطة" ===
    "plan": {
        "political": {"ar": "خطة سياسية", "en": "political plan", "ru": "политический план", "desc": "استراتيجية دولية"},
        "legal": {"ar": "خطة قانونية", "en": "legal plan", "ru": "юридический план", "desc": "خطة دفاع"},
        "economic": {"ar": "خطة اقتصادية", "en": "economic plan", "ru": "экономический план", "desc": "خطة مالية"},
        "medical": {"ar": "خطة علاجية", "en": "treatment plan", "ru": "план лечения", "desc": "بروتوكول طبي"},
        "scientific": {"ar": "خطة بحثية", "en": "research plan", "ru": "исследовательский план", "desc": "خطة تجربة"},
        "engineering": {"ar": "خطة هندسية", "en": "engineering plan", "ru": "инженерный план", "desc": "مخطط تنفيذ"},
        "military": {"ar": "خطة عسكرية", "en": "military plan", "ru": "военный план", "desc": "خطة عمليات"},
        "educational": {"ar": "خطة تعليمية", "en": "educational plan", "ru": "образовательный план", "desc": "خطة منهج"},
        "religious": {"ar": "خطة دينية", "en": "religious plan", "ru": "религиозный план", "desc": "خطة شرعية"},
        "sports": {"ar": "خطة رياضية", "en": "sports plan", "ru": "спортивный план", "desc": "خطة تدريب"},
        "literary": {"ar": "خطة أدبية", "en": "literary plan", "ru": "литературный план", "desc": "خطة رواية"},
        "it": {"ar": "خطة تقنية", "en": "tech plan", "ru": "технический план", "desc": "خطة تطوير"},
        "environmental": {"ar": "خطة بيئية", "en": "environmental plan", "ru": "экологический план", "desc": "خطة حماية"},
        "agricultural": {"ar": "خطة زراعية", "en": "agricultural plan", "ru": "сельскохозяйственный план", "desc": "خطة موسم"},
        "media": {"ar": "خطة إعلامية", "en": "media plan", "ru": "медийный план", "desc": "خطة حملة"},
        "tourism": {"ar": "خطة سياحية", "en": "tourism plan", "ru": "туристический план", "desc": "خطة رحلة"},
        "general": {"ar": "خطة", "en": "plan", "ru": "план", "desc": "المعنى العام"}
    },
    # === الكلمة: "project" / "مشروع" ===
    "project": {
        "political": {"ar": "مشروع سياسي", "en": "political project", "ru": "политический проект", "desc": "مبادرة دولية"},
        "legal": {"ar": "مشروع قانوني", "en": "legal project", "ru": "юридический проект", "desc": "مشروع قانون"},
        "economic": {"ar": "مشروع اقتصادي", "en": "economic project", "ru": "экономический проект", "desc": "استثمار تجاري"},
        "medical": {"ar": "مشروع صحي", "en": "medical project", "ru": "медицинский проект", "desc": "مشروع مستشفى"},
        "scientific": {"ar": "مشروع بحثي", "en": "research project", "ru": "исследовательский проект", "desc": "مشروع علمي"},
        "engineering": {"ar": "مشروع إنشائي", "en": "construction project", "ru": "строительный проект", "desc": "مشروع بناء"},
        "military": {"ar": "مشروع عسكري", "en": "military project", "ru": "военный проект", "desc": "مشروع سلاح"},
        "educational": {"ar": "مشروع تعليمي", "en": "educational project", "ru": "образовательный проект", "desc": "مشروع أكاديمي"},
        "religious": {"ar": "مشروع ديني", "en": "religious project", "ru": "религиозный проект", "desc": "مشروع خيري"},
        "sports": {"ar": "مشروع رياضي", "en": "sports project", "ru": "спортивный проект", "desc": "مشروع ملعب"},
        "literary": {"ar": "مشروع أدبي", "en": "literary project", "ru": "литературный проект", "desc": "مشروع نشر"},
        "it": {"ar": "مشروع تقني", "en": "tech project", "ru": "технический проект", "desc": "مشروع برمجي"},
        "environmental": {"ar": "مشروع بيئي", "en": "environmental project", "ru": "экологический проект", "desc": "مشورة حماية"},
        "agricultural": {"ar": "مشروع زر
