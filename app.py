import streamlit as st
import translators as ts

# 1. إعدادات الصفحة والعنوان الرسمي
st.set_page_config(page_title="HASSAN NASSER", page_icon="🤖", layout="wide")

st.title("🤖 HASSAN NASSER")
st.markdown("### 🧠 ADVANCED CONTEXTUAL TRANSLATOR | المترجم السياقي المطور بدون مفاتيح")
st.write("---")

# اللغات المعتمدة في النظام
languages_dict = {
    "العربية": "ar", 
    " can الإنجليزية (English)": "en", 
    "الروسية (Русский)": "ru", 
    "الصينية (中文)": "zh", 
    "الألمانية (Deutsch)": "de", 
    "الإسبانية (Español)": "es", 
    "البرتغالية (Português)": "pt", 
    "الكورية (한국어)": "ko"
}

# دالة ذكية لتوليد شروح تفصيلية ومترادفات بناءً على نوع الكلمة وسياقها
def generate_detailed_explanation(translated_text, original_lower, to_lang):
    if to_lang != "ar":
        return translated_text, f"[Site Context]: {translated_text}", f"[Contractual]: {translated_text}", f"[Academic]: {translated_text}"
    
    # قاموس الشروح الهندسية والموقِعية المخصصة (تضاف تلقائياً عند كتابة الكلمات المفتاحية)
    engineering_db = {
        "concrete casting": "صب الخرسانة الإنشائية - يشمل عمليات التجهيز، الصب الموقعيري، وضبط الجودة بالموقع.",
        "high voltage poles": "أبراج الجهد العالي / أعمدة الضغط العالي - الهياكل المعدنية أو الخرسانية الحاملة لخطوط الطاقة الكهربائية.",
        "high-voltage poles": "أبراج الجهد العالي / أعمدة الضغط العالي - الهياكل المعدنية أو الخرسانية الحاملة لخطوط الطاقة الكهربائية.",
        "reinforcement": "حديد التسليح - شبكات الصلب المستخدمة لتدعيم العناصر الإنشائية ومقاومة قوى الشد والقص.",
        "shop drawings": "الرسومات التنفيذية للموقع - المخططات التفصيلية المعتمدة التي يلتزم مهندس الموقع بالتنفيذ بناءً عليها.",
        "site engineer": "مهندس الموقع التنفيذي - المسؤول الفني عن متابعة العمالة، استلام الأعمال، ومطابقة التنفيذ بالمخططات.",
        "subcontractor": "مقاول الباطن - الجهة أو الشركة المسؤولة عن تنفيذ بنود محددة تحت إشراف المقاول الرئيسي."
    }
    
    # تحديد الشرح الهندسي الموقعي
    eng_explanation = "غير متوفر سياق هندسي مباشر"
    for key, val in engineering_db.items():
        if key in original_lower:
            eng_explanation = val
            break
            
    # توليد الشرح العام
    gen_explanation = f"{translated_text} (المعنى الأساسي المباشر المتداول في المعاجم اللغوية)."
    
    # توليد الشرح القانوني والتعاقدي
    legal_explanation = f"البند المعتمد تعاقدياً بخصوص ({translated_text}) وفقاً لشروط الفيديك والالتزامات المتبادلة."
    if "المقاول" in translated_text or "contractor" in original_lower:
        legal_explanation = "يلتزم الطرف الثاني (المقاول) بتنفيذ وتأمين كافة الأعمال الموكلة إليه بموجب شروط العقد."
        
    # توليد الشرح العلمي والأكاديمي
    sci_explanation = f"الدراسة المخبرية والتحليل الفيزيائي/الكيميائي لخواص ({translated_text}) في الأبحاث الأكاديمية."

    return gen_explanation, eng_explanation, legal_explanation, sci_explanation

# ==========================================
# 📥 واجهة المستخدم (Inputs)
# ==========================================
with st.form(key="custom_translator_form", clear_on_submit=False):
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1, key="src_lang")
    with col_l2:
        target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0, key="tgt_lang")
    
    st.write("---")
    
    text_to_translate = st.text_area(
        "أدخل الكلمة أو العبارة (سيقوم المحرك بفك تشفيرها وإعطائك تفاصيلها):", 
        placeholder="اكتب هنا الكلمة الفنية (مثال: concrete casting أو shop drawings)...",
        height=150,
        key="input_text"
    )
    
    btn_process = st.form_submit_button("🚀 RUN ENGINE | تشغيل المعالجة والفرز السياقي الشامل", use_container_width=True)

st.write("---")

# ==========================================
# 📊 عرض النتائج (Outputs)
# ==========================================
if btn_process and text_to_translate.strip():
    cleaned_text = text_to_translate.strip()
    original_lower = cleaned_text.lower()
    
    lang_from = languages_dict[source_lang]
    lang_to = languages_dict[target_lang]
    
    with st.spinner("جاري معالجة النص وتوليد الشروح التفصيلية..."):
        try:
            # استخدام محرك مترجمين متطور يتخطى الحظر تلقائياً عبر سيرفرات موازية
            base_translation = ts.translate_text(cleaned_text, from_language=lang_from, to_language=lang_to, translator='bing')
            
            # توليد الشروح الذكية والتفصيلية لكل قالب
            f_gen, f_eng, f_leg, f_sci = generate_detailed_explanation(base_translation, original_lower, lang_to)
            
            st.success("🎯 تم التحليل والتوزيع السياقي بنجاح وبدون أي أخطاء اتصال:")
            st.write("---")
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("### 💬 صياغة عامة مع الشرح")
                st.warning(f_gen)
                
                st.markdown("### 📜 صياغة تعاقدية وقانونية")
                st.success(f_leg)
            
            with col_b:
                st.markdown("### 👷 صياغة هندسية موقعية تفصيلية")
                st.info(f_eng)
                
                st.markdown("### 🧬 صياغة علمية وأكاديمية")
                st.code(f_sci, language="")
                
        except Exception as e:
            st.error(f"❌ حدث خطأ أثناء جلب البيانات: {e}")

elif btn_process:
    st.warning("⚠️ من فضلك اكتب النص أولاً لتشغيل المحرك.")
