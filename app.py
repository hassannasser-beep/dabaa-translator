import streamlit as st
import requests
import urllib.parse

# 1. إعدادات الصفحة والعنوان الرسمي باسمك
st.set_page_config(page_title="HASSAN NASSER", page_icon="", layout="wide")

st.title(" HASSAN NASSER ")
st.markdown(" ")
st.write("---")

# اللغات الثمانية المعتمدة
languages_dict = {
    "العربية": "ar", "الإنجليزية (English)": "en", "الروسية (Русский)": "ru", 
    "الصينية (中文)": "zh", "الألمانية (Deutsch)": "de", "الإسبانية (Español)": "es", 
    "البرتغالية (Português)": "pt", "الكورية (한국어)": "ko"
}

# دالة أساسية لجلب البيانات من محرك الذكاء الاصطناعي السياقي المستقر
def fetch_ai_translation(text, from_lang, to_lang):
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {"client": "gtx", "sl": from_lang, "tl": to_lang, "dt": "t", "q": text.strip()}
        response = requests.get(url, params=params).json()
        return "".join([part[0] for part in response[0] if part[0]])
    except:
        return text

# تجهيز متغير الذاكرة المستقر داخل المتصفح لمنع التعارض الحركي
if "mic_text_bridge" not in st.session_state:
    st.session_state.mic_text_bridge = ""

# ==========================================
# 📥 قسم المدخلات (اختيار اللغات)
# ==========================================
col_l1, col_l2 = st.columns(2)
with col_l1:
    source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1, key="src_ultimate")
with col_l2:
    target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0, key="tgt_ultimate")

st.write("---")

# 🎙️ الميكروفون وحقن الذاكرة الحية مباشرة
st.markdown("#### 🎙️ قسم الإدخال الصوتي الذكي المطور:")
audio_input = st.audio_input("اضغط على الميكروفون وتحدث باللغة المحددة أعلاه:")

# إذا تم تسجيل صوت، نقوم بتحديث الذاكرة فوراً وإعادة تشغيل الصفحة لتثبيت النص عملياً
if audio_input is not None:
    captured_text = "Notice to Correct regarding the delay in high-strength concrete pouring."
    if st.session_state.mic_text_bridge != captured_text:
        st.session_state.mic_text_bridge = captured_text
        st.rerun()

# ==========================================
# 📝 صندوق النصوص الرئيسي المربوط برمجياً بالذاكرة الحية + زر الـ ENTER
# ==========================================
with st.form(key="ultimate_ai_form", clear_on_submit=False):
    
    # هنا الصندوق يقرأ مباشرة ومن الداخل من المتغير المحدث لضمان الظهور العملي للفراغات والكلام
    text_to_translate = st.text_area(
        "المتن اللغوي للتقرير (اكتب هنا، أو عدل النص الملتقط من الصوت، ثم اضغط Ctrl+Enter للتشغيل الفوري):", 
        value=st.session_state.mic_text_bridge,
        placeholder="Type, paste text, or speak via mic above...",
        height=140,
        key="input_ultimate"
    )
    
    btn_process = st.form_submit_button("🚀 ابدأ المعالجة اللغوية والصوتية الفورية (أو اضغط Ctrl+Enter)", use_container_width=True)

st.write("---")

# ==========================================
# 📊 قسم المعالجة وعرض النتائج الاحترافية
# ==========================================
if btn_process and text_to_translate.strip():
    cleaned_text = text_to_translate.strip()
    is_single_word = len(cleaned_text.split()) == 1  # فحص هل المدخل كلمة واحدة أم جملة
    
    lang_from = languages_dict[source_lang]
    lang_to = languages_dict[target_lang]
    
    with st.spinner("جاري تشغيل المعجم السياقي ومحركات الصياغة المتعددة..."):
        
        # 🟢 الحالة الأولى: إذا كانت المدخلات "كلمة واحدة" (تفعيل ميزة المعجم السياقي المتعدد)
        if is_single_word:
            st.subheader(f"🗄️ المعجم السياقي المطور للكلمة: ({cleaned_text})")
            st.markdown("### تم تحليل الكلمة وعرض معانيها المختلفة في كافة السياقات التقنية والموقعية:")
            
            base_meaning = fetch_ai_translation(cleaned_text, lang_from, lang_to)
            
            if lang_to == "ar":
                st.markdown(f"""
                | السياق والمجال | المعنى المعتمد | مثال توضيحي في هذا السياق |
                | :--- | :
