import streamlit as st
from duckduckgo_search import DDGS

# 1. إعدادات الصفحة والعنوان الرسمي باسمك
st.set_page_config(page_title="HASSAN NASSER", page_icon="🤖", layout="wide")

st.title("🤖 HASSAN NASSER")
st.markdown("### 🧠 GEMINI-STYLE AI TRANSLATOR | المترجم الذكي المطور الشامل")
st.write("---")

# إعادة اللغات الثمانية كاملة بدون أي نقص
languages_dict = {
    "العربية": "Arabic", 
    " can الإنجليزية (English)": "English", 
    "الروسية (Русский)": "Russian", 
    "الصينية (中文)": "Chinese", 
    "الألمانية (Deutsch)": "German", 
    "الإسبانية (Español)": "Spanish", 
    "البرتغالية (Português)": "Portuguese", 
    "الكورية (한국어)": "Korean"
}

# دالة ذكية لمخاطبة الذكاء الاصطناعي مباشرة بعد تعديل التحديث الجديد
def get_ai_translation(text, from_lang, to_lang):
    # أمر توجيه عقل الذكاء الاصطناعي ليتصرف كخبير ومترجم تفصيلي
    prompt = f"""
    You are an expert technical translator like Gemini. Translate this text: "{text}" from {from_lang} to {to_lang}.
    Provide a deeply detailed translation and an extensive explanation in Arabic for each of these 7 specific domains:
    1. General Context (سياق عام وشرحه اللغوي متضمناً معاني الكلمة)
    2. Engineering & Site Work (هندسة موقعية وإنشائية تفصيلية بمواصفات المواقع الإنشائية)
    3. Legal & FIDIC (صياغة تعاقدية قانونية وفقاً لدفاتر الشروط)
    4. Scientific & Academic (أبعاد علمية وأكاديمية دقيقة)
    5. Political (سياق رسمي ودبلوماسي)
    6. Economic (أبعاد مالية وحساب كميات ومقايسات)
    7. Religious & Cultural (دلالات ثقافية أو روحية إن وجدت)
    
    Make the explanation long, comprehensive, and helpful for a professional translator. Format your entire output clearly with professional markdown headings for each of the 7 domains.
    """
    
    try:
        # استخدام الأمر الرسمي الجديد .aichat بدلاً من .chat الملغي
        with DDGS() as ddgs:
            response = ddgs.aichat(keywords=prompt, model="gpt-4o-mini")
            return response
    except Exception as e:
        return f"❌ حدث خطأ أثناء الاتصال بعقل الذكاء الاصطناعي: {e}"

# ==========================================
# 📥 واجهة المستخدم
# ==========================================
with st.form(key="ai_global_form", clear_on_submit=False):
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1)
    with col_l2:
        target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0)
    
    st.write("---")
    
    text_to_translate = st.text_area(
        "أدخل الكلمة أو العبارة (سيقوم الذكاء الاصطناعي بتشريحها وإعطائك شرحاً تفصيلياً عميقاً بـ 7 سياقات مختلفة):", 
        placeholder="اكتب هنا أي كلمة أو جملة هندسية مثل: concrete casting أو honeycombing أو أي عبارة أخرى...",
        height=150,
        key="input_text"
    )
    
    btn_process = st.form_submit_button("🧠 RUN AI ENGINE | تشغيل الفرز والتحليل الشامل وفك التشفير", use_container_width=True)

st.write("---")

# ==========================================
# 📊 عرض النتائج الشاملة والمطولة
# ==========================================
if btn_process and text_to_translate.strip():
    cleaned_text = text_to_translate.strip()
    lang_from = languages_dict[source_lang]
    lang_to = languages_dict[target_lang]
    
    with st.spinner("🧠 يتصل التطبيق الآن بعقل الذكاء الاصطناعي التوليدي لتشريح النص وشرحه..."):
        ai_analysis = get_ai_translation(cleaned_text, lang_from, lang_to)
        
        st.success("🎯 تحليل الذكاء الاصطناعي السياقي المطور:")
        st.write("---")
        
        # عرض الناتج التفصيلي بالكامل داخل صندوق منظم وقابل للقراءة المريحة
        st.markdown(ai_analysis)

elif btn_process:
    st.warning("⚠️ من فضلك اكتب النص أو المصطلح أولاً لتشغيل محرك الذكاء الاصطناعي.")
