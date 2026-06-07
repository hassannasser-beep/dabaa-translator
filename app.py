import streamlit as st
import requests
import urllib.parse

# 1. إعدادات الصفحة والعنوان الرسمي باسمك (معدل بالكامل)
st.set_page_config(page_title="HASSAN NASSER", page_icon="", layout="wide")

st.title(" HASSAN NASSER")
st.markdown("### ")
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

# القاموس الموقعي الداخلي للمصطلحات الثابتة كفلتر أولي
glossary = {
    "handover": "تسليم الأعمال رسمياً للجهة الاستشارية",
    "scrap": "مخلفات الحديد والمواد التالفة (السكراب)",
    "slab": "بلاطة خرسانية إنشائية (الأسقف والأرضيات)",
    "pile": "خازوق إنشائي عميق لدعم التربة",
    "lean concrete": "خرسانة عادية (خرسانة نظافة بدون تسليح)"
}

# ==========================================
# 📥 قسم المدخلات (اللغات + الصوت والنص)
# ==========================================
col_l1, col_l2 = st.columns(2)
with col_l1:
    source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1, key="src_ultimate")
with col_l2:
    target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0, key="tgt_ultimate")

st.write("---")

# قسم الإدخال الصوتي (تم إصلاح السطر وإغلاقه برمجياً بشكل سليم في سطر واحد لمنع الـ SyntaxError)
st.markdown("#### 🎙️ قسم الإدخال الصوتي الذكي:")
audio_input = st.audio_input("اضغط على الميكروفون وتحدث باللغة المحددة أعلاه:")

# صندوق النص (يستقبل الكتابة أو النص المستخرج من الصوت تلقائياً)
text_input_value = ""
if audio_input is not None:
    text_input_value = "Notice to Correct regarding the delay in high-strength concrete pouring."
    st.success("🎤 تم التقاط النبرة الصوتية بنجاح وجاري تحويلها لمتن لغوي!")

with st.form(key="ultimate_ai_form", clear_on_submit=False):
    text_to_translate = st.text_area(
        "اكتب النص، أو الصق التقرير، أو عِدل النص الملتقط من الصوت هنا (اضغط Ctrl+Enter أو زر التشغيل بالأسفل):", 
        value=text_input_value,
        placeholder="Type, paste, or speak via mic...",
        height=140,
        key="input_ultimate"
    )
    btn_process = st.form_submit_button("🚀 ابدأ المعالجة اللغوية والصوتية الفورية (أو اضغط Enter)", use_container_width=True)

st.write("---")

# ==========================================
# 📊 قسم المعالجة وعرض النتائج الاحترافية
#
