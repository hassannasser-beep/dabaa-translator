import streamlit as st
import requests
import urllib.parse
import streamlit.components.v1 as components

# 1. إعدادات الصفحة والعنوان الرسمي باسمك
st.set_page_config(page_title="HASSAN NASSER", page_icon="", layout="wide")

st.title " HASSAN NASSER")
st.markdown("### المنصة المركزية المتطورة للترجمة الرقمية والصياغة السياقية الفورية")
st.write("---")

# اللغات الثمانية المعتمدة مع اختصاراتها الصوتية الدولية لـ JavaScript
languages_dict = {
    "العربية": "ar-EG", 
    "الإنجليزية (English)": "en-US", 
    "الروسية (Русский)": "ru-RU", 
    "الصينية (中文)": "zh-CN", 
    "الألمانية (Deutsch)": "de-DE", 
    "الإسبانية (Español)": "es-ES", 
    "البرتغالية (Português)": "pt-PT", 
    "الكورية (한국어)": "ko-KR"
}

# دالة أساسية لجلب البيانات من محرك الذكاء الاصطناعي السياقي المستقر
def fetch_ai_translation(text, from_lang, to_lang):
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        f_code = from_lang.split('-')[0]
        t_code = to_lang.split('-')[0]
        params = {"client": "gtx", "sl": f_code, "tl": t_code, "dt": "t", "q": text.strip()}
        response = requests.get(url, params=params).json()
        return "".join([part[0] for part in response[0] if part[0]])
    except:
        return text

# قراءة النص القادم من الميكروفون عبر الرابط بشكل آمن لتخطي حظر المتصفح
query_params = st.query_params
mic_text = query_params.get("mic_text", "")

# ==========================================
# 📥 قسم المدخلات (اختيار اللغات)
# ==========================================
col_l1, col_l2 = st.columns(2)
with col_l1:
    source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1, key="src_ultimate")
with col_l2:
    target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0, key="tgt_ultimate")

st.write("---")

lang_speech_code = languages_dict[source_lang]

# =================================
