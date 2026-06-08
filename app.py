import streamlit as st
from googletrans import Translator

# 1. إعدادات الواجهة الاحترافية باسمك
st.set_page_config(page_title="HASSAN NASSER", page_icon="🤖", layout="wide")

st.title("🤖 HASSAN NASSER")
st.markdown("### 🧠 LIVE CONTEXTUAL AI TRANSLATOR | محرك الترجمة الديناميكي الحي الشامل")
st.write("---")

# اللغات الثمانية كاملة
languages_dict = {
    "العربية": "ar", " can الإنجليزية (English)": "en", "الروسية (Русский)": "ru",
    "الصينية (中文)": "zh", "الألمانية (Deutsch)": "de", "الإسبانية (Español)": "es",
    "البرتغالية (Português)": "pt", "الكورية (한국어)": "ko"
}

# دالة المعالجة الفنية والذكية للنص المترجم حياً (بدون نصوص ثابتة)
def enrich_engineering_context(translated_text, to_lang):
    if to_lang != "ar":
        return translated_text, f"[Technical Site Interpretation]: {translated_text}", f"[Contractual Form]: {translated_text}"
    
    # تحسين الصياغة الهندسية حياً عبر استبدال المصطلحات الركيكة بمترادفات موقع الضبعة الاحترافية
    eng_replacements = {
        "صب الخرسانة": "أعمال الصب الموقعي للخرسانة الإنشائية",
        "رسومات المتجر": "الرسومات التنفيذية المعتمدة للموقع (Shop Drawings)",
        "أعمدة الجهد العالي": "أبراج الجهد العالي الحاملة لكابلات نقل الطاقة",
        "حديد التسليح": "تسليح العناصر الإنشائية بأسياخ الصلب عالي المقاومة",
        "البلاطة": "البلاطة الخرسانية المسلحة (السقف / الفرش الإنشائي)",
        "خرسانة عجاف": "خرسانة النظافة العادية (الفرشية التأسيسية)",
        "التعشيش": "تعشيش الخرسانة وظهور الفراغات الهوائية (Honeycombing)",
        "النجارة": "أعمال الشدات والنجارة الإنشائية الحاضنة للصب",
        "علاج الخرسانة": "معالجة الخرسانة ورشها بالماء (Curing) لضمان الإنضاج"
    }
    
    # تحسين الصياغة التعاقدية القانونية حياً (FIDIC)
    legal_replacements = {
        "المقاول": "الطرف الثاني (المقاول الرئيسي للمشروع)",
        "رب العمل": "الطرف الأول (صاحب العمل / المالك)",
        "المهندس": "المهندس المشرف / استشاري المشروع (The Engineer)",
        "جدول الكميات": "جدول الكميات والمواصفات المسعرة المعتمد (BOQ)",
        "رسومات كما بنيت": "مخططات الواقع الفعلي المنفذة بالطبيعة (As-Built Drawings)"
    }
    
    # توليد الصيغ حياً بناءً على ترجمة جملتك الفطرية
    eng_context = translated_text
    for key, val in eng_replacements.items():
        eng_context = eng_context.replace(key, f"**[{val}]**")
        
    legal_context = translated_text
    for key, val in legal_replacements.items():
        legal_context = legal_context.replace(key, f"**[{val}]**")
        
    return translated_text, eng_context, legal_context

# ==========================================
# 📥 واجهة المستخدم
# ==========================================
with st.form(key="live_translator_form", clear_on_submit=False):
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1)
    with col_l2:
        target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0)
    
    st.write("---")
    
    text_to_translate = st.text_area(
        "أدخل أي جملة أو مستند فني طويل أو قصير (سيتم ترجمته وتفكيكه حياً 100% تبعاً لسياقك):", 
        placeholder="اكتب هنا بحرية... التطبيق سيتعامل مع كل نص جديد بذكاء وديناميكية...",
        height=140,
        key="input_text"
    )
    
    btn_process = st.form_submit_button("🚀 تشغيل محرك الترجمة الحية والفرز السياقي", use_container_width=True)

st.write("---")

# ==========================================
# 📊 الترجمة الفورية والفرز الديناميكي الحي
# ==========================================
if btn_process and text_to_translate.strip():
    cleaned_text = text_to_translate.strip()
    lang_from = languages_dict[source_lang]
    lang_to = languages_dict[target_lang]
    
    with st.spinner("🔄 يتصل المحرك الآن بالسيرفر الرسمي لترجمة وتفكيك الجملة حياً..."):
        try:
            # استدعاء المترجم الحي لترجمة النص الأصلي أياً كان نوعه
            translator = Translator()
            raw_translation = translator.translate(cleaned_text, src=lang_from, dest=lang_to).text
            
            # تمرير الترجمة الحية عبر مصفاة هندسة السياق لتوليد القوالب الديناميكية
            f_general, f_engineering, f_legal = enrich_engineering_context(raw_translation, lang_to)
            
            st.success("🎯 تم الفرز والترجمة الحية بناءً على نصك الفعلي بنسبة 100%:")
            st.write("---")
            
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.markdown("### 💬 1. صياغة عامة وحرة:")
                st.warning(f_general)
                st.caption("_ترجمة لفظية مرنة ومباشرة للنص الذي أدخلته_")
                
            with col_b:
                st.markdown("### 👷 2. صياغة هندسية موقعية:")
                st.info(f_engineering)
                st.caption("_تدمج المصطلحات الإنشائية والمترادفات الفنية المعتمدة موقعياً_")
                
            with col_c:
                st.markdown("### 📜 3. صياغة تعاقدية وقانونية:")
                st.success(f_legal)
                st.caption("_تطوع الكلمات لتناسب لغة عقود الفيديك والمستندات الرسمية_")
                
        except Exception as e:
            st.error(f"❌ حدث عطل في محرك الترجمة: {e}\nيرجى إعادة الضغط على الزر.")

elif btn_process:
    st.warning("⚠️ يرجى كتابة الجملة المراد ترجمتها أولاً.")
