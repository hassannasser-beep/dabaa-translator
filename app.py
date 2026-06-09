import streamlit as st
import requests
import json
import re

st.set_page_config(page_title="HASSAN NASSER", page_icon="🏗️", layout="wide")

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

.rcard { border-radius: 12px; padding: 1.1rem 1.3rem; border: 0.5px solid #e5e7eb; background: #fff; margin-bottom: 0.5rem; }
.rcard-eng { border-top: 3px solid #1D9E75; }
.rcard-leg { border-top: 3px solid #534AB7; }
.rcard-sci { border-top: 3px solid #0891b2; }
.rcard-med { border-top: 3px solid #dc2626; }
.rcard-pol { border-top: 3px solid #7c3aed; }
.rcard-dir { border-top: 3px solid #D85A30; }
.rcard-slg { border-top: 3px solid #ca8a04; }
.rlabel { font-size: 10px; font-weight: 600; letter-spacing: 0.08em; margin-bottom: 8px; }
.rlabel-e { color: #085041; }
.rlabel-l { color: #3C3489; }
.rlabel-s { color: #0e7490; }
.rlabel-m { color: #991b1b; }
.rlabel-p { color: #5b21b6; }
.rlabel-d { color: #712B13; }
.rlabel-g { color: #92400e; }
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

.tone-box { border-radius: 12px; padding: 1rem 1.3rem; margin-top: 1rem; margin-bottom: 0.5rem; }
.tone-formal { background: #f0f9ff; border: 1px solid #0891b2; }
.tone-political { background: #f5f3ff; border: 1px solid #7c3aed; }
.tone-medical { background: #fff1f2; border: 1px solid #dc2626; }
.tone-scientific { background: #f0fdfa; border: 1px solid #0d9488; }
.tone-legal { background: #f5f3ff; border: 1px solid #4f46e5; }
.tone-casual { background: #fefce8; border: 1px solid #ca8a04; }
.tone-neutral { background: #f9fafb; border: 1px solid #9ca3af; }
.tone-label { font-size: 11px; font-weight: 700; letter-spacing: 0.08em; margin-bottom: 4px; }
.tone-desc { font-size: 13px; color: #374151; }

.proofread-box { border-radius: 12px; padding: 1rem 1.3rem; background: #fef2f2; border: 1px solid #fca5a5; margin-top: 1rem; }
.proofread-title { font-size: 11px; font-weight: 700; color: #991b1b; letter-spacing: 0.08em; margin-bottom: 8px; }
.proofread-item { font-size: 13px; color: #374151; margin-bottom: 4px; padding: 4px 8px; background: #fff; border-radius: 6px; border-left: 3px solid #ef4444; }
.proofread-ok { background: #f0fdf4; border: 1px solid #86efac; }
.proofread-ok-txt { font-size: 13px; color: #166534; }

.mic-box { background: #1a1a2e; border-radius: 10px; padding: 1rem 1.3rem; margin-bottom: 1rem; }
.mic-title { font-size: 11px; font-weight: 600; color: #5DCAA5; letter-spacing: 0.08em; margin-bottom: 8px; }

div.stButton > button {
    background: #1a1a2e !important; color: white !important; border: none !important;
    border-radius: 8px !important; font-weight: 500 !important;
    font-size: 15px !important; padding: 0.65rem 2rem !important; width: 100% !important;
    transition: background 0.2s !important;
}
div.stButton > button:hover { background: #0f0f1e !important; }
div.stButton > button[data-testid="swap-btn"] { background: #5DCAA5 !important; color: #04342C !important; font-size: 22px !important; padding: 0.4rem !important; border-radius: 50% !important; }
textarea { border-radius: 8px !important; border: 0.5px solid #d1d5db !important; font-size: 14px !important; }

.context-badge {
    display: inline-block; padding: 3px 10px; border-radius: 20px;
    font-size: 11px; font-weight: 700; letter-spacing: 0.06em; margin-bottom: 10px;
}
.badge-political { background: #7c3aed; color: white; }
.badge-legal { background: #4f46e5; color: white; }
.badge-medical { background: #dc2626; color: white; }
.badge-scientific { background: #0891b2; color: white; }
.badge-engineering { background: #1D9E75; color: white; }
.badge-casual { background: #ca8a04; color: white; }
.badge-neutral { background: #6b7280; color: white; }
</style>

<script>
// Enable Enter key to trigger translation
document.addEventListener('DOMContentLoaded', function() {
    const observer = new MutationObserver(function() {
        const textareas = document.querySelectorAll('textarea');
        textareas.forEach(function(ta) {
            if (!ta.dataset.enterBound) {
                ta.dataset.enterBound = 'true';
                ta.addEventListener('keydown', function(e) {
                    if (e.key === 'Enter' && !e.shiftKey) {
                        e.preventDefault();
                        const btns = document.querySelectorAll('button');
                        btns.forEach(function(b) {
                            if (b.innerText.includes('Translate') || b.innerText.includes('ترجم')) {
                                b.click();
                            }
                        });
                    }
                });
            }
        });
    });
    observer.observe(document.body, { childList: true, subtree: true });
});
</script>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-name">HASSAN <span>NASSER</span></div>
    <div class="hero-sub">ENGINEERING · LEGAL · SCIENTIFIC · MEDICAL · POLITICAL TRANSLATIONS</div>
    <div class="hero-pills">
        <span class="pill pill-active">Smart Translator</span>
        <span class="pill pill-muted">Tone Analyzer</span>
        <span class="pill pill-muted">Proofreader</span>
        <span class="pill pill-muted">Site Slang</span>
        <span class="pill pill-muted">7 Styles</span>
        <span class="pill pill-muted">Microphone</span>
    </div>
    <div class="lang-bar">
        <span class="ldot"></span><span class="ldot"></span><span class="ldot"></span>
        <span class="ldot"></span><span class="ldot"></span><span class="ldot"></span>
        <span class="ldot"></span><span class="ldot"></span>
        <span class="lang-bar-txt">8 languages</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── DATA ──────────────────────────────────────────────────────────────────────
languages_dict = {
    "العربية": "ar", "English": "en", "Русский": "ru", "中文": "zh",
    "Deutsch": "de", "Español": "es", "Português": "pt", "한국어": "ko"
}

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
    "variation order": {"academic": "ترتيب الاختلاف", "slang": "أمر تغيير / ملحق تعاقدي (VO)", "desc": "أمر رسمي لتعديل بند خارج نطاق التعاقد."},
    "rebar": {"academic": "حديد التسليح", "slang": "الحديد / قضبان الحديد", "desc": "قضبان الفولاذ المستخدمة في تسليح الخرسانة."},
    "subcontractor": {"academic": "مقاول من الباطن", "slang": "سب-مقاول / الطرف الثالث", "desc": "شركة متخصصة تتعاقد مع المقاول الرئيسي."},
    "punch list": {"academic": "قائمة الثقوب", "slang": "قائمة الأعمال الناقصة", "desc": "قائمة الملاحظات قبيل التسليم النهائي."},
    "mobilization": {"academic": "تعبئة", "slang": "تجهيز ودخول الموقع", "desc": "مرحلة تجهيز المقاول وإعداد الموقع قبل البدء الفعلي."},
}

# Context/domain detection keywords
DOMAIN_KEYWORDS = {
    "political": ["parliament", "government", "election", "minister", "president", "treaty", "diplomacy",
                  "سياسي", "حكومة", "برلمان", "وزير", "رئيس", "انتخاب", "دبلوماسية", "معاهدة", "مجلس",
                  "حزب", "دولة", "سيادة", "قرار أممي", "مجلس الأمن"],
    "legal": ["contract", "clause", "liability", "jurisdiction", "plaintiff", "defendant", "whereas",
              "عقد", "بند", "مسؤولية", "قانون", "محكمة", "دعوى", "تعاقدي", "fidic", "تحكيم",
              "ملزم", "اتفاقية", "شرط", "التزام"],
    "medical": ["patient", "diagnosis", "treatment", "symptom", "dosage", "clinical", "surgery",
                "مريض", "تشخيص", "علاج", "جرعة", "عرض", "جراحة", "دواء", "مستشفى", "طبي",
                "إكلينيكي", "بروتوكول علاجي"],
    "scientific": ["hypothesis", "experiment", "data", "analysis", "molecule", "equation", "laboratory",
                   "فرضية", "تجربة", "بيانات", "تحليل", "جزيء", "معادلة", "مختبر", "بحث علمي",
                   "نتائج", "إحصاء"],
    "engineering": ["concrete", "steel", "foundation", "load", "beam", "column", "drawing", "specification",
                    "خرسانة", "حديد", "أساس", "حمل", "كمرة", "عمود", "مواصفات", "إنشاء", "هندسة",
                    "مقاول", "موقع", "بناء"],
    "casual": ["hey", "bro", "gonna", "wanna", "lol", "btw", "يلا", "اخوي", "يعني", "عادي", "زبالة",
               "ما شاء الله", "هههه", "اوكي", "حلو"],
}

# ── FUNCTIONS ─────────────────────────────────────────────────────────────────
def fetch_translation(text, from_lang, to_lang):
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {"client": "gtx", "sl": from_lang, "tl": to_lang, "dt": "t", "q": text.strip()}
        r = requests.get(url, params=params, timeout=10).json()
        return "".join([p[0] for p in r[0] if p[0]])
    except Exception as e:
        return f"[Translation error: {e}]"

def levenshtein(s1, s2):
    if len(s1) < len(s2): return levenshtein(s2, s1)
    if len(s2) == 0: return len(s1)
    prev = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        cur = [i + 1]
        for j, c2 in enumerate(s2):
            cur.append(min(prev[j+1]+1, cur[j]+1, prev[j]+(c1!=c2)))
        prev = cur
    return prev[-1]

def check_did_you_mean(text):
    words = re.sub(r'[,.]', ' ', text.lower()).split()
    suggestions = []
    for w in words:
        if len(w) < 3 or w in site_slang_db: continue
        for k in site_slang_db:
            d = levenshtein(w, k)
            if d == 1 or (len(k) > 6 and d == 2):
                if k not in suggestions: suggestions.append(k)
    return suggestions

def detect_site_slang(text):
    tl = text.lower()
    return [{"term": k.title(), "academic": v["academic"], "slang": v["slang"], "desc": v["desc"]}
            for k, v in site_slang_db.items() if k in tl]

def detect_domain(text):
    """Detect the domain/context of the input text."""
    text_lower = text.lower()
    scores = {domain: 0 for domain in DOMAIN_KEYWORDS}
    for domain, keywords in DOMAIN_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                scores[domain] += 1
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "neutral"

def analyze_tone(text, domain):
    """Analyze the tone of the text."""
    tone_map = {
        "political": {
            "label": "🏛️ POLITICAL",
            "color": "political",
            "desc": "النص ذو طابع سياسي رسمي. يُعالَج بلغة دبلوماسية مباشرة.",
            "desc_en": "The text carries an official political tone. Treated with direct diplomatic language."
        },
        "legal": {
            "label": "⚖️ LEGAL / CONTRACTUAL",
            "color": "legal",
            "desc": "النص تعاقدي قانوني. يُعالَج بدقة قانونية ملزمة.",
            "desc_en": "The text is legal/contractual. Treated with binding legal precision."
        },
        "medical": {
            "label": "🏥 MEDICAL / CLINICAL",
            "color": "medical",
            "desc": "النص طبي سريري. يُعالَج بمصطلحات طبية دقيقة.",
            "desc_en": "The text is medical/clinical. Treated with precise medical terminology."
        },
        "scientific": {
            "label": "🔬 SCIENTIFIC / ACADEMIC",
            "color": "scientific",
            "desc": "النص علمي أكاديمي. يُعالَج بصياغة بحثية محكمة.",
            "desc_en": "The text is scientific/academic. Treated with rigorous academic phrasing."
        },
        "engineering": {
            "label": "🏗️ ENGINEERING / TECHNICAL",
            "color": "engineering",
            "desc": "النص هندسي تقني. يُعالَج بالمصطلحات الهندسية المعيارية.",
            "desc_en": "The text is engineering/technical. Treated with standard engineering terminology."
        },
        "casual": {
            "label": "💬 CASUAL / COLLOQUIAL",
            "color": "casual",
            "desc": "النص عامي غير رسمي. يُعالَج بأسلوب محادثة طبيعي.",
            "desc_en": "The text is casual/colloquial. Treated with natural conversational style."
        },
        "neutral": {
            "label": "📄 GENERAL / NEUTRAL",
            "color": "neutral",
            "desc": "النص عام محايد. يُعالَج بلغة واضحة ومباشرة.",
            "desc_en": "The text is general/neutral. Treated with clear, direct language."
        },
    }
    return tone_map.get(domain, tone_map["neutral"])

def build_formulas(base, to_lang, domain):
    """Build domain-specific translation variants."""
    
    if domain == "political":
        if to_lang == "ar":
            return (
                base,  # Political is only direct — no reformulation
                None, None, None, None, None
            )
        return base, None, None, None, None, None

    if to_lang != "ar":
        eng = f"[Engineering specification] {base}"
        leg = f"Pursuant to the contractual obligations herein, {base[0].lower() + base[1:]}"
        sci = f"[Scientific context] {base}"
        med = f"[Clinical notation] {base}"
        pol = f"[Official statement] {base}"
        slg = base
        return eng, leg, sci, med, pol, slg

    # Arabic reformulations
    eng_replacements = {
        "من أجل ضمان": "لضمان الموثوقية الفنية في",
        "رب العمل": "المالك (Employer)",
        "المهندس": "استشاري المشروع",
        "يجب": "يُشترط هندسياً",
    }
    leg_replacements = {
        "يجب": "يلتزم الطرف الثاني بموجب هذا العقد بـ",
        "المقاول": "المقاول (وفقاً لتعريف المادة الأولى)",
        "رب العمل": "صاحب العمل تعاقدياً",
        "يُسمح": "يحق وفقاً للبنود التعاقدية",
    }
    sci_replacements = {
        "يجب": "يُستوجب علمياً",
        "نتيجة": "المحصلة التجريبية",
        "دراسة": "البحث التحليلي",
    }
    med_replacements = {
        "مريض": "المريض (Patient)",
        "علاج": "البروتوكول العلاجي",
        "دواء": "الدواء (Medication)",
        "جرعة": "الجرعة الدوائية (Dosage)",
    }

    f_eng, f_leg, f_sci, f_med = base, base, base, base
    for k, v in eng_replacements.items(): f_eng = f_eng.replace(k, v)
    for k, v in leg_replacements.items(): f_leg = f_leg.replace(k, v)
    for k, v in sci_replacements.items(): f_sci = f_sci.replace(k, v)
    for k, v in med_replacements.items(): f_med = f_med.replace(k, v)

    return f_eng, f_leg, f_sci, f_med, base, base  # last two: political=base, casual=base

def proofread_translation(original, translated, from_lang, to_lang):
    """Basic proofreading checks."""
    issues = []

    # Check 1: Length sanity
    orig_words = len(original.split())
    trans_words = len(translated.split())
    ratio = trans_words / orig_words if orig_words > 0 else 1
    if ratio < 0.3:
        issues.append("⚠️ الترجمة قصيرة جداً مقارنة بالنص الأصلي — قد تكون هناك أجزاء محذوفة.")
    if ratio > 4:
        issues.append("⚠️ الترجمة طويلة بشكل غير متوقع — تحقق من الاتساق.")

    # Check 2: Untranslated chunks (same lang characters)
    if from_lang == "ar" and to_lang == "en":
        arabic_chars = sum(1 for c in translated if '\u0600' <= c <= '\u06FF')
        if arabic_chars > 5:
            issues.append("⚠️ يوجد نص عربي لم يُترجم في الناتج الإنجليزي.")
    if from_lang == "en" and to_lang == "ar":
        latin_chars = sum(1 for c in translated if c.isalpha() and ord(c) < 128)
        if latin_chars > 20:
            issues.append("⚠️ يوجد نص إنجليزي لم يُترجم في الناتج العربي.")

    # Check 3: Empty output
    if not translated.strip():
        issues.append("❌ الترجمة فارغة — يرجى المحاولة مرة أخرى.")

    # Check 4: Repeated words (basic)
    words = translated.split()
    for i in range(len(words) - 2):
        if words[i] == words[i+1] == words[i+2] and len(words[i]) > 2:
            issues.append(f"⚠️ كلمة مكررة ثلاث مرات: '{words[i]}' — تحقق من الترجمة.")
            break

    return issues

# ── MICROPHONE HTML COMPONENT ─────────────────────────────────────────────────
mic_html = """
<div class="mic-box">
    <div class="mic-title">🎤 VOICE INPUT — انقر واتكلم</div>
    <div style="display:flex; gap:10px; align-items:center; flex-wrap:wrap;">
        <button id="micBtn" onclick="startMic()" style="
            background:#5DCAA5; color:#04342C; border:none; border-radius:8px;
            padding:8px 20px; font-size:13px; font-weight:600; cursor:pointer;">
            🎤 ابدأ التسجيل
        </button>
        <button id="stopBtn" onclick="stopMic()" disabled style="
            background:#ef4444; color:white; border:none; border-radius:8px;
            padding:8px 20px; font-size:13px; font-weight:600; cursor:pointer; opacity:0.4;">
            ⏹ إيقاف
        </button>
        <span id="micStatus" style="font-size:12px; color:#9ca3af;">جاهز للتسجيل</span>
    </div>
    <div id="micResult" style="margin-top:10px; font-size:13px; color:#e5e7eb; min-height:24px; background:rgba(255,255,255,0.05); border-radius:6px; padding:8px; display:none;"></div>
</div>

<script>
let recognition = null;
let finalTranscript = '';

function startMic() {
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        document.getElementById('micStatus').textContent = '❌ المتصفح لا يدعم التعرف على الصوت. استخدم Chrome.';
        return;
    }
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SR();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = 'ar-SA';

    recognition.onstart = function() {
        document.getElementById('micStatus').textContent = '🔴 جارٍ التسجيل...';
        document.getElementById('micBtn').disabled = true;
        document.getElementById('micBtn').style.opacity = '0.5';
        document.getElementById('stopBtn').disabled = false;
        document.getElementById('stopBtn').style.opacity = '1';
        document.getElementById('micResult').style.display = 'block';
    };
    recognition.onresult = function(e) {
        let interim = '';
        for (let i = e.resultIndex; i < e.results.length; i++) {
            if (e.results[i].isFinal) {
                finalTranscript += e.results[i][0].transcript;
            } else {
                interim += e.results[i][0].transcript;
            }
        }
        document.getElementById('micResult').innerHTML =
            '<span style="color:#5DCAA5">' + finalTranscript + '</span>' +
            '<span style="color:#9ca3af">' + interim + '</span>';
    };
    recognition.onerror = function(e) {
        document.getElementById('micStatus').textContent = '❌ خطأ: ' + e.error;
    };
    recognition.onend = function() {
        document.getElementById('micStatus').textContent = '✅ انتهى التسجيل — انسخ النص أدناه';
        document.getElementById('micBtn').disabled = false;
        document.getElementById('micBtn').style.opacity = '1';
        document.getElementById('stopBtn').disabled = true;
        document.getElementById('stopBtn').style.opacity = '0.4';
        // Copy to clipboard
        if (finalTranscript) {
            navigator.clipboard.writeText(finalTranscript).catch(() => {});
        }
    };
    finalTranscript = '';
    recognition.start();
}

function stopMic() {
    if (recognition) recognition.stop();
}
</script>
"""

# ── SESSION STATE ─────────────────────────────────────────────────────────────
if "src_lang" not in st.session_state:
    st.session_state.src_lang = "English"
if "tgt_lang" not in st.session_state:
    st.session_state.tgt_lang = "العربية"

# ── LANGUAGE SELECTOR WITH SWAP ───────────────────────────────────────────────
lang_list = list(languages_dict.keys())

col_src, col_swap, col_tgt = st.columns([5, 1, 5])

with col_src:
    src = st.selectbox(
        "FROM / من",
        lang_list,
        index=lang_list.index(st.session_state.src_lang),
        key="src_select"
    )

with col_swap:
    st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)
    swap = st.button("⇄", key="swap_btn", help="بدّل بين اللغتين")

with col_tgt:
    # Prevent same language selection
    available_tgt = [l for l in lang_list if l != src]
    current_tgt = st.session_state.tgt_lang if st.session_state.tgt_lang != src else available_tgt[0]
    tgt = st.selectbox(
        "INTO / إلى",
        available_tgt,
        index=available_tgt.index(current_tgt) if current_tgt in available_tgt else 0,
        key="tgt_select"
    )

# Handle swap
if swap:
    st.session_state.src_lang = tgt
    st.session_state.tgt_lang = src
    st.rerun()
else:
    st.session_state.src_lang = src
    st.session_state.tgt_lang = tgt

fl = languages_dict[src]
tl = languages_dict[tgt]

# ── MICROPHONE ────────────────────────────────────────────────────────────────
with st.expander("🎤 الإدخال الصوتي — Voice Input", expanded=False):
    st.components.v1.html(mic_html, height=160)
    st.caption("💡 بعد التسجيل، النص يُنسخ تلقائياً. الصقه في خانة النص أدناه ثم اضغط Enter للترجمة.")

# ── TEXT INPUT ────────────────────────────────────────────────────────────────
text_input = st.text_area(
    "",
    placeholder="اكتب أو الصق النص هنا — أو اضغط Enter للترجمة...\nتقارير هندسية، بنود تعاقدية، تقارير طبية، وثائق سياسية...",
    height=140,
    key="text_input"
)

# Enter key JS bridge
st.markdown("""
<script>
setTimeout(function() {
    var textareas = window.parent.document.querySelectorAll('textarea');
    textareas.forEach(function(ta) {
        if (!ta.dataset.enterBound) {
            ta.dataset.enterBound = 'true';
            ta.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    var btns = window.parent.document.querySelectorAll('button');
                    for (var b of btns) {
                        if (b.innerText.includes('Translate') || b.innerText.includes('ترجم')) {
                            b.click(); break;
                        }
                    }
                }
            });
        }
    });
}, 800);
</script>
""", unsafe_allow_html=True)

btn = st.button("🌐  Translate — ترجم", use_container_width=True)

st.divider()

# ── TRANSLATION LOGIC ─────────────────────────────────────────────────────────
if btn and text_input.strip():
    text = text_input.strip()

    # ── 1. Did You Mean ───────────────────────────────────────────────────────
    sug = check_did_you_mean(text)
    if sug:
        fmt = ", ".join([f"<strong>{s.title()}</strong>" for s in sug])
        st.markdown(f'<div class="dym-box">💡 <b>Did you mean / هل تقصد:</b> {fmt}?</div>', unsafe_allow_html=True)

    # ── 2. Domain Detection + Tone Analysis ───────────────────────────────────
    domain = detect_domain(text)
    tone = analyze_tone(text, domain)

    badge_class = f"badge-{tone['color']}"
    st.markdown(f"""
    <div style="margin-bottom:12px;">
        <span class="context-badge {badge_class}">{tone['label']}</span>
        <div class="tone-box tone-{tone['color']}">
            <div class="tone-label" style="color:inherit;">🎯 TONE ANALYSIS — تحليل النبرة</div>
            <div class="tone-desc">
                <b>AR:</b> {tone['desc']}<br>
                <b>EN:</b> {tone['desc_en']}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── 3. Translation ────────────────────────────────────────────────────────
    with st.spinner("جارٍ الترجمة..."):
        base = fetch_translation(text, fl, tl)

    is_single = len(text.split()) <= 2

    if domain == "political":
        # Political: direct only, no multi-formulation
        st.markdown(f"""
        <div class="rcard" style="border-top:3px solid #7c3aed;">
            <div class="rlabel" style="color:#5b21b6;">🏛️ POLITICAL — DIRECT TRANSLATION</div>
            <div class="rtext">{base}</div>
        </div>
        """, unsafe_allow_html=True)

    elif is_single:
        # Single word: lexicon table
        st.markdown(f"### 🗄️ Contextual Lexicon: `{text}`")
        st.markdown(f"""
| Context | Meaning |
|:---|:---|
| 🏗️ Engineering | {base} |
| ⚖️ Legal / FIDIC | {base} |
| 🔬 Scientific | {base} |
| 🏥 Medical | {base} |
| 🏛️ Political | {base} |
| 💬 General | {base} |
""")
    else:
        # Multi-word: domain-aware formulations
        f_eng, f_leg, f_sci, f_med, f_pol, f_slg = build_formulas(base, tl, domain)

        # Show domain-relevant cards first, then others
        domain_order = {
            "engineering": ["eng", "leg", "sci", "med", "dir", "slg"],
            "legal":       ["leg", "eng", "sci", "med", "dir", "slg"],
            "scientific":  ["sci", "eng", "leg", "med", "dir", "slg"],
            "medical":     ["med", "sci", "leg", "eng", "dir", "slg"],
            "casual":      ["slg", "dir", "eng", "leg", "sci", "med"],
            "neutral":     ["eng", "leg", "dir", "sci", "med", "slg"],
        }
        order = domain_order.get(domain, domain_order["neutral"])

        cards = {
            "eng": (f_eng,  "rcard-eng", "rlabel-e", "🏗️ ENGINEERING"),
            "leg": (f_leg,  "rcard-leg", "rlabel-l", "⚖️ LEGAL"),
            "sci": (f_sci,  "rcard-sci", "rlabel-s", "🔬 SCIENTIFIC"),
            "med": (f_med,  "rcard-med", "rlabel-m", "🏥 MEDICAL"),
            "dir": (base,   "rcard-dir", "rlabel-d", "🎯 DIRECT"),
            "slg": (f_slg,  "rcard-slg", "rlabel-g", "💬 CASUAL"),
        }

        # Show primary 3 (most relevant) in a row
        primary = order[:3]
        c1, c2, c3 = st.columns(3)
        cols = [c1, c2, c3]
        for i, key in enumerate(primary):
            txt, card_cls, lbl_cls, label = cards[key]
            with cols[i]:
                st.markdown(f'<div class="rcard {card_cls}"><div class="rlabel {lbl_cls}">{label}</div><div class="rtext">{txt}</div></div>', unsafe_allow_html=True)

        # Show secondary 3 in expander
        with st.expander("📖 المزيد من الصياغات — More Formulations"):
            secondary = order[3:]
            c4, c5, c6 = st.columns(3)
            cols2 = [c4, c5, c6]
            for i, key in enumerate(secondary):
                txt, card_cls, lbl_cls, label = cards[key]
                with cols2[i]:
                    st.markdown(f'<div class="rcard {card_cls}"><div class="rlabel {lbl_cls}">{label}</div><div class="rtext">{txt}</div></div>', unsafe_allow_html=True)

    # ── 4. Proofreading ────────────────────────────────────────────────────────
    issues = proofread_translation(text, base, fl, tl)
    if issues:
        items_html = "".join([f'<div class="proofread-item">{i}</div>' for i in issues])
        st.markdown(f"""
        <div class="proofread-box">
            <div class="proofread-title">🔍 PROOFREADING — مدقق الترجمة</div>
            {items_html}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="border-radius:8px; padding:8px 14px; background:#f0fdf4; border:1px solid #86efac; margin-top:10px;">
            <span style="font-size:13px; color:#166534;">✅ الترجمة اجتازت فحص الجودة — No proofreading issues detected.</span>
        </div>
        """, unsafe_allow_html=True)

    # ── 5. Site Slang Detector ─────────────────────────────────────────────────
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
    st.warning("⚠️ الرجاء إدخال نص للترجمة — Please enter some text first.")
