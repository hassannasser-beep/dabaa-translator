import streamlit as st
import requests

# 1. إعدادات الصفحة والعنوان الرسمي باسمك الحصري
st.set_page_config(page_title="HASSAN NASSER", page_icon="", layout="wide")

st.title(" HASSAN NASSER")
st.markdown("### المنصة المركزية المتطورة للترجمة الرقمية والصياغة السياقية المتعددة")
st.write("---")

# اللغات الثمانية المعتمدة بالكامل في النظام
languages_dict = {
    "العربية": "ar", 
    "الإنجليزية (English)": "en", 
    "الروسية (Русский)": "ru", 
    "الصينية (中文)": "zh", 
    "الألمانية (Deutsch)": "de", 
    "الإسبانية (Español)": "es", 
    "البرتغالية (Português)": "pt", 
    "الكورية (한국어)": "ko"
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

# ==========================================
# 📥 قسم المدخلات (اختيار لغات الترجمة المخصصة)
# ==========================================
with st.form(key="ultimate_ai_form", clear_on_submit=False):
    
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1, key="src_ultimate")
    with col_l2:
        target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0, key="tgt_ultimate")
    
    st.write("---")
    
    # صندوق النصوص الرئيسي المدعوم باختصار الكيبورد الفوري
    text_to_translate = st.text_area(
        "المتن اللغوي للتقرير (اكتب أو ألصق الفقرة هنا، ثم اضغط Ctrl+Enter للتشغيل الفوري):", 
        placeholder="Type or paste your text, contract clauses, or engineering reports here...",
        height=160,
        key="input_ultimate"
    )
    
    # زر المعالجة المركزي داخل الاستمارة لتفعيل زر الـ ENTER
    btn_process = st.form_submit_button("🚀 ابدأ المعالجة اللغوية وضبط الصياغة الفورية (أو اضغط Ctrl+Enter)", use_container_width=True)

st.write("---")

# ==========================================
# 📊 قسم المعالجة وعرض النتائج الاحترافية الشاملة
# ==========================================
if btn_process and text_to_translate.strip():
    cleaned_text = text_to_translate.
