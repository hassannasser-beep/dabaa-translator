import streamlit as st
from free_google_translate import translate

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(page_title="HASSAN NASSER", page_icon="🤖", layout="wide")

st.title("🤖 HASSAN NASSER")
st.markdown("### 🧠 LIVE AI CONTEXTUAL TRANSLATOR | المحرك الذكي المرن للترجمة الحية")
st.write("---")

# اللغات الثمانية المعتمدة كاملة
languages_dict = {
    "العربية": "ar", 
    "الإنجليزيّة (English)": "en", 
    "الروسية (Русский)": "ru",
    "الصينية (中文)": "zh", 
    "الألمانية (Deutsch)": "de", 
    "الإسبانية (Español)": "es",
    "البرتغالية (Português)": "pt", 
    "الكورية (한국어)": "ko"
}

# دالة هندسة السياق الحي والديناميكي بناءً على نصك الفعلي
def process_live_context(translated_text, to_lang):
    if to_lang != "ar":
        return translated_text, f"[Technical Site Interpretation]: {translated_text}", f"[Contractual Form]: {translated_text}"
    
    # قاموس المترادفات الاحترافية الموقعية لرفع جودة النص الحي
    engineering_terms = {
        "صب الخرسانة": "أعمال الصب الموقعي للخرسانة الإنشائية",
        "رسومات المتجر": "الرسومات التنفيذية المعتمدة للموقع (Shop Drawings)",
        "أعمدة الجهد العالي": "أبراج الجهد العالي وكابلات نقل الطاقة الضغط العالي",
        "حديد التسليح": "تسليح العناصر الإنشائية بأسياخ الصلب عالي المقاومة",
        "البلاطة": "البلاطة الخرسانية المسلحة (السقف / الفرش الإنشائي)",
        "خرسانة عجاف": "خرسانة النظافة العادية (الفرشية التأسيسية للموقع)",
        "التعشيش": "تعشيش الخرسانة وفراغات التعشيش الهوائية (Honeycombing)",
        "النجارة": "أعمال الشدات والنجارة الإنشائية والقوالب الحاضنة للصب",
        "علاج الخرسانة": "معالجة الخرسانة ورشها بالماء (Curing) لضمان الإنضاج الفني"
    }
    
    legal_terms = {
        "المقاول": "الطرف الثاني (المقاول الرئيسي للمشروع)",
        "رب العمل": "الطرف الأول (صاحب العمل / المالك تعاقدياً)",
        "المهندس": "المهندس المشرف / استشاري المشروع (The Engineer)",
        "جدول الكميات": "جدول الكميات والمواصفات المسعرة المعتمد (BOQ)",
        "رسومات كما بنيت": "مخططات الواقع الفعلي المنفذة بالطبيعة (As-Built Drawings)"
    }
    
    # استبدال وتطويع المصطلحات حياً داخل جملتك المترجمة
    eng_context = translated_text
    for key, val in engineering_terms.items():
        if key in eng_context:
            eng_context = eng_context.replace(key, f"**[{val}]**")
            
    legal_context = translated_text
    for key, val in legal_terms.items():
        if key in legal_context:
            legal_context = legal_context.replace(key, f"**[{val}]**")
            
    return translated_text, eng_context, legal_context

# ==========================================
# 📥 واجهة المستخدم
# ==========================================
with st.form(key="safe_live_translator_form", clear_on_submit=False):
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1)
    with col_l2:
        target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0)
    
    st.write("---")
    
    text_to_translate = st.text_area(
        "أدخل أي نص أو عبارة فنية (ترجمة حية ومرنة 100% بدون نصوص محفوظة):", 
        placeholder="اكتب هنا بحرية... سيقوم المحرك بترجمتها حياً وتفكيكها سياقياً على الفور...",
        height=140,
        key="input_text"
    )
    
    btn_process = st.form_submit_button("🚀 تشغيل محرك الترجمة الديناميكية المستقرة", use_container_width=True)

st.write("---")

# ==========================================
# 📊 المعالجة والترجمة الحية
# ==========================================
if btn_process and text_to_translate.strip():
    cleaned_text = text_to_translate.strip()
    lang_from = languages_dict[source_lang]
    lang_to = languages_dict[target_lang]
    
    with st.spinner("🔄 يجري الآن ترجمة النص حياً وتوليد الصياغات السياقية المرنة..."):
        try:
            # الترجمة الحية والديناميكية المتوافقة مع بايثون 3.14
            raw_translation = translate(cleaned_text, src=lang_from, dest=lang_to)
            
            # فلترة وتحسين النص حياً بناءً على ترجمتك
            f_general, f_engineering, f_legal = process_live_context(raw_translation, lang_to)
            
            st.success("🎯 تم توليد الترجمة السياقية الحية لنصك بنجاح:")
            st.write("---")
            
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.markdown("### 💬 1. صياغة لغوية عامة:")
                st.warning(f_general)
                st.caption("_ترجمة ديناميكية مباشرة وحرة للنص المتغير_")
                
            with col_b:
                st.markdown("### 👷 2. صياغة هندسية موقعية:")
                st.info(f_engineering)
                st.caption("_تطوع المصطلحات لتناسب بيئة ومواصفات مواقع الإنشاءات_")
                
            with col_c:
                st.markdown("### 📜 3. صياغة تعاقدية وقانونية:")
                st.success(f_legal)
                st.caption("_تعديل الصياغة لتطابق عقود ومستندات الفيديك الرسمية_")
                
        except Exception as e:
            st.error(f"❌ حدث خطأ غير متوقع في محرك الترجمة: {e}\nيرجى المحاولة مرة أخرى.")

elif btn_process:
    st.warning("⚠️ يرجى كتابة نص أولاً لتشغيل المحرك.")
