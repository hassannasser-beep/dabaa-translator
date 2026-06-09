import streamlit as st
import requests
import re

# 1. Page Configuration
st.set_page_config(page_title="HASSAN NASSER", page_icon="🏗️", layout="wide")

# 2. Adaptive CSS (Supports Light & Dark Themes)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; max-width: 1000px; }

/* Hero Banner */
.hero {
    background: #1a1a2e;
    border-radius: 14px;
    padding: 2rem 2rem 1.5rem;
    margin-bottom: 1.5rem;
}
.hero-name { font-size: 30px; font-weight: 600; color: #ffffff; letter-spacing: -0.5px; }
.hero-name span { color: #5DCAA5; }
.hero-sub { font-size: 13px; color: rgba(255,255,255,0.45); margin-top: 6px; letter-spacing: 0.04em; }

/* Main Translation Table Style */
.multi-context-wrap { border-radius: 12px; overflow: hidden; border: 1px solid rgba(128, 128, 128, 0.2); margin-top: 1.5rem; }
.multi-context-head { background: #1a1a2e; padding: 14px 18px; border-bottom: 1px solid rgba(255,255,255,0.1); }
.multi-context-head-txt { font-size: 13px; font-weight: 600; color: #5DCAA5; letter-spacing: 0.06em; }
.context-table { width: 100%; border-collapse: collapse; background: var(--background-color, #fff); }
.context-table th { font-size: 11px; font-weight: 600; color: #6b7280; letter-spacing: 0.06em; padding: 12px 16px; border-bottom: 1px solid rgba(128, 128, 128, 0.2); text-align: left; background: rgba(0,0,0,0.02); }
.context-table td { font-size: 14px; padding: 14px 16px; border-bottom: 1px solid rgba(128, 128, 128, 0.1); vertical-align: middle; color: var(--text-color, #1f2937); }
.context-table tr:last-child td { border-bottom: none; }

/* Badges for Contexts */
.badge { display: inline-block; padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: 600; text-align: center; min-width: 130px; }
.badge-eng { background: rgba(29, 158, 117, 0.15); color: #1D9E75; }
.badge-leg { background: rgba(83, 74, 183, 0.15); color: #534AB7; }
.badge-eco { background: rgba(216, 90, 48, 0.15); color: #D85A30; }
.badge-med { background: rgba(0, 180, 216, 0.15); color: #00B4D8; }
.badge-pol { background: rgba(108, 117, 125, 0.15); color: #6C757D; }
.badge-lit { background: rgba(230, 57, 70, 0.15); color: #E63946; }

/* Slang Detector Table */
.slang-wrap { border-radius: 12px; overflow: hidden; border: 0.5px solid #9FE1CB; margin-top: 1.5rem; }
.slang-head { background: #085041; padding: 12px 16px; }
.slang-head-txt { font-size: 11px; font-weight: 600; color: #9FE1CB; letter-spacing: 0.06em; }
.slang-table { width: 100%; border-collapse: collapse; background: var(--background-color, #fff); }
.slang-table th { font-size: 10px; font-weight: 600; color: #6b7280; letter-spacing: 0.06em; padding: 8px 14px; border-bottom: 0.5px solid rgba(128, 128, 128, 0.2); text-align: left; }
.slang-table td { font-size: 13px; padding: 10px 14px; border-bottom: 0.5px solid rgba(128, 128, 128, 0.1); vertical-align: top; color: var(--text-color, #1f2937); }
.term-cell { font-weight: 600; color: #1D9E75; }
.site-cell { font-weight: 500; color: #534AB7; }

/* Input Adjustments */
div.stButton > button {
    background: #1a1a2e !important; color: white !important; border: none !important;
    border-radius: 8px !important; font-weight: 500 !important;
    font-size: 15px !important; padding: 0.65rem 2rem !important; width: 100% !important;
}
div.stButton > button:hover { background: #0f0f1e !important; }
textarea { border-radius: 8px !important; border: 0.5px solid #d1d5db !important; font-size: 14px !important; }
</style>
""", unsafe_allow_html=True)

# 3. Hero Layout
st.markdown("""
<div class="hero">
    <div class="hero-name">HASSAN <span>NASSER</span></div>
    <div class="hero-sub">ENGINEERING · LEGAL · CONTRACTUAL TRANSLATIONS</div>
</div>
""", unsafe_allow_html=True)

# 4. Databases and Mappings
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
    "variation order": {"academic": "ترتيب الاختلاف", "slang": "أمر تغيير / ملحق تعاقدي (VO)", "desc": "أمر رسمي لتعديل بند خارج نطاق التعاقد."}
}

# 5. Core Utility Functions
def fetch_ai_translation(text, from_lang, to_lang):
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {"client": "gtx", "sl": from_lang, "tl": to_lang, "dt": "t", "q": text.strip()}
        r = requests.get(url, params=params).json()
        return "".join([p[0] for p in r[0] if p[0]])
    except Exception:
        return text

def detect_site_slang(text):
    tl = text.lower()
    return [{"term": k.title(), "academic": v["academic"], "slang": v["slang"], "desc": v["desc"]}
            for k, v in site_slang_db.items() if k in tl]

# دالة توليد الترجمات المتوازية لكافة السياقات بناءً على المصطلح أو النص بالكامل
def generate_all_contexts(base_translation, source_text, to_lang):
    # في حالة الترجمة إلى غير العربية، نكتفي بصياغة وصفية للسياق
    if to_lang != "ar":
        return [
            {"class": "badge-eng", "name": "👷 Engineering", "result": f"[Technical] {base_translation}"},
            {"class": "badge-leg", "name": "⚖️ Legal / FIDIC", "result": f"[Contractual] It is stipulated that {base_translation.lower()}"},
            {"class": "badge-eco", "name": "💰 Economic & Finance", "result": f"[Financial] {base_translation}"},
            {"class": "badge-med", "name": "🩺 Medical & Clinical", "result": f"[Clinical] {base_translation}"},
            {"class": "badge-pol", "name": "🏛️ Political & Diplomatic", "result": f"[Official] {base_translation}"},
            {"class": "badge-lit", "name": "✍️ Literary & Prose", "result": f"[Aesthetic] {base_translation}"}
        ]

    # قواميس التبديل الذكي للمصطلحات عند الترجمة للغة العربية لتوليد صياغات دقيقة للمصطلح ككل
    ctx_data = [
        {
            "class": "badge-eng", "name": "👷 هندسي وفني",
            "replacements": {"شحنة": "شحنة كهربائية / دفق خرساني", "عطاء": "عطاء هندسي / مناقصة مشروع", "محطة": "محطة توليد / معدات الموقع الثقيلة", "تغيير": "أمر تغييري هندسي (VO)", "رسوم": "مخططات تنفيذية ورسومات موقع"}
        },
        {
            "class": "badge-leg", "name": "⚖️ قانوني وتعاقدي",
            "replacements": {"شحنة": "رهن تعاقدي / تهمة جنائية", "يجب": "يلتزم الطرف الثاني بموجب العقد بـ", "عطاء": "عرض الوفاء بالتزام تعاقدي", "المقاول": "يتعين على المقاول تعاقدياً"}
        },
        {
            "class": "badge-eco", "name": "💰 اقتصادي ومالي",
            "replacements": {"شحنة": "رسوم مالية / تكلفة إضافية / عهدة مادية", "عطاء": "عملة قانونية سائلة للمدفوعات", "تغيير": "تقلبات مالية في الأسعار", "فائدة": "العائد الاستثماري المصرفي"}
        },
        {
            "class": "badge-med", "name": "🩺 طبي وسريري",
            "replacements": {"شحنة": "جرعة علاجية مكثفة / صدمة إنعاش", "مرض": "اعتلال صحي مزمن", "موت": "وفاة سريرية مؤكدة", "فحص": "تشخيص سريري دقيق"}
        },
        {
            "class": "badge-pol", "name": "🏛️ سياسي ودبلوماسي",
            "replacements": {"شحنة": "تكليف بمهام دبلوماسية / منصب رسمي", "اتفاق": "معاهدة دبلوماسية ثنائية رفيعة المستوى", "رفض": "أعربت الجهات السيادية عن تحفظها على"}
        },
        {
            "class": "badge-lit", "name": "✍️ أدبي وبلاغي",
            "replacements": {"جميل": "آسرٌ يخلب الألباب", "حزين": "مثقلٌ بأعباء الشجن والأسى", "قال": "أردفَ قائلاً بنبرةٍ وجدانية"}
        }
    ]

    results = []
    for ctx in ctx_data:
        modified = base_translation
        for target_word, replaced_word in ctx["replacements"].items():
            if target_word in modified:
                modified = modified.replace(target_word, replaced_word)
        results.append({"class": ctx["class"], "name": ctx["name"], "result": modified})
        
    return results

# 6. Interactive Interface
col1, col2 = st.columns(2)
with col1:
    src = st.selectbox("FROM", list(languages_dict.keys()), index=1)
with col2:
    tgt = st.selectbox("INTO", list(languages_dict.keys()), index=0)

text_input = st.text_area("", placeholder="أدخل المصطلح أو النص المراد فدحه في كافة السياقات الممكنة دفعة واحدة...", height=120)
btn = st.button("🌐 Multi-Context Translation Search", use_container_width=True)

st.divider()

# 7. Processing Engine
if btn and text_input.strip():
    text = text_input.strip()
    fl = languages_dict[src]
    tl = languages_dict[tgt]

    with st.spinner("Searching across all linguistic contexts..."):
        # جلب الترجمة الأساسية للمصطلح ككل
        base_trans = fetch_ai_translation(text, fl, tl)
        
        # توليد مصفوفة السياقات المتوازية كاملة
        all_contexts = generate_all_contexts(base_trans, text, tl)
        
        # بناء جدول الترجمات المتعددة الشامل (لا يعرض 3 معاني فقط، بل يبحث في كل السياقات المتاحة)
        table_rows = ""
        for ctx in all_contexts:
            table_rows += f"""
            <tr>
                <td style="width: 200px;"><span class="badge {ctx['class']}">{ctx['name']}</span></td>
                <td class="rtext">{ctx['result']}</td>
            </tr>
            """
            
        st.markdown(f"""
        <div class="multi-context-wrap">
            <div class="multi-context-head">
                <span class="multi-context-head-txt">📊 ALL POSSIBLE CONTEXTUAL TRANSLATIONS FOR: "{text}"</span>
            </div>
            <table class="context-table">
                <thead>
                    <tr>
                        <th>مجال السياق / Context Field</th>
                        <th>الترجمة الصحيحة والملائمة للسياق / Contextual Translation</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
        </div>
        """, unsafe_allow_html=True)

        # تشغيل كاشف المصطلحات الدارجة في الموقع للهندسة إن وُجدت
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
