import streamlit as st
from huggingface_hub import InferenceClient

# 1. إعدادات واجهة المترجم الاحترافي
st.set_page_config(page_title="HASSAN NASSER", page_icon="🤖", layout="wide")

st.title("🤖 HASSAN NASSER")
st.markdown("### 🧠 OFFICIAL HYBRID AI TRANSLATOR | المحرك الذكي الرسمي للترجمة السياقية الشاملة")
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

# دالة الاتصال بالسيرفر الرسمي لـ Hugging Face لجلب ترجمة حية وشرح حقيقي
def get_hf_ai_translation(text, from_lang, to_lang, token):
    prompt = f"""
    You are an expert technical translator and linguistic consultant. 
    Translate this text: "{text}" from {from_lang} to {to_lang}.
    
    Provide an extensive, deeply detailed translation and a thorough explanation in Arabic for each of these 7 specific domains. Do not use generic placeholders; analyze the actual input text provided:
    1. General Context (سياق عام وشرح لغوي ومعاني الكلمة)
    2. Engineering & Site Work (هندسة موقعية وإنشائية تفصيلية بمواصفات مواقع البناء والتشييد)
    3. Legal & FIDIC (صياغة تعاقدية قانونية وفقاً لشروط الفيديك)
    4. Scientific & Academic (الأبعاد العلمية، الفيزيائية، أو الأكاديمية الدقيقة للمادة أو المفهوم)
    5. Political (السياق الرسمي والدبلوماسي والخطابات الحكومية)
    6. Economic (الأبعاد المالية، المقايسات، وحساب الكميات BOQ)
    7. Religious & Cultural (الدلالات الثقافية، المجتمعية، أو الروحية للعبارة)
    
    Format the entire output using clear Markdown headings (##) in Arabic for each of the 7 domains. Make it long, rich, and highly beneficial for professional translators.
    """
    
    try:
        # الاتصال بنموذج لاما 3 العملاق والمستقر عبر السيرفر الرسمي
        client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct", token=token)
        response = ""
        for message in client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2500,
            stream=False,
        ).choices:
            response += message.message.content
        return response
    except Exception as e:
        return f"❌ خطأ في الاتصال بالسيرفر الفني: {e}"

# ==========================================
# 📥 واجهة المستخدم
# ==========================================
with st.form(key="hf_ai_form", clear_on_submit=False):
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1)
    with col_l2:
        target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0)
    
    st.write("---")
    
    text_to_translate = st.text_area(
        "أدخل الكلمة أو العبارة الفنية للتحليل الحي المباشر (7 سياقات كاملة):", 
        placeholder="اكتب جملتك أو مصطلحك هنا (مثل: concrete casting أو honeycombing)...",
        height=150,
        key="input_text"
    )
    
    btn_process = st.form_submit_button("🧠 تشغيل المحرك الرسمي | فرز وتحليل حي 100%", use_container_width=True)

st.write("---")

# ==========================================
# 📊 معالجة وعرض التحليل الحقيقي
# ==========================================
if btn_process and text_to_translate.strip():
    # التحقق من وجود المفتاح في الـ Secrets
    try:
        token = st.secrets["HF_TOKEN"]
    except Exception:
        st.error("⚠️ لم يتم العثور على مفتاح HF_TOKEN في إعدادات Secrets لموقع Streamlit. يرجى إضافته أولاً كما موضح في الخطوة الأولى.")
        st.stop()
        
    cleaned_text = text_to_translate.strip()
    lang_from = languages_dict[source_lang]
    lang_to = languages_dict[target_lang]
    
    with st.spinner("🧠 يتصل التطبيق الآن بالسيرفرات الرسمية لمعالجة النص حياً وتوليد الصيغ السبعة..."):
        ai_analysis = get_hf_ai_translation(cleaned_text, lang_from, lang_to, token)
        st.success("🎯 التحليل السياقي والترجمة الفورية التوليدية الحية:")
        st.write("---")
        
        # عرض النتيجة الحية المتكاملة من الذكاء الاصطناعي مباشرة
        st.markdown(ai_analysis)

elif btn_process:
    st.warning("⚠️ يرجى كتابة نص أولاً ليتمكن النظام من تحليله.")
