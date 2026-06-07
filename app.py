import streamlit as st
import requests

# 1. إعدادات الصفحة والعنوان الاحترافي باسمك
st.set_page_config(page_title="HASSAN NASSER", page_icon="🏗️", layout="wide")

st.title(" - HASSAN NASSER - ")
st.markdown("### نظام متطور يترجم النصوص والملفات، ويعيد صياغتها لغوياً وقواعدياً لتخرج بلغة سليمة واحترافية 100%")
st.write("---")

# 2. القاموس المركزي المعتمد في الذاكرة للمصطلحات الثابتة
if 'glossary' not in st.session_state:
    st.session_state.glossary = {
        "handover": "تسليم الأعمال رسمياً للجهة الاستشارية",
        "scrap": "مخلفات الحديد والمواد التالفة (السكراب)",
        "slab": "بلاطة خرسانية إنشائية (الأسقف والأرضيات)",
        "pile": "خازوق إنشائي عميق لدعم التربة",
        "lean concrete": "خرسانة عادية (خرسانة نظافة بدون تسليح)"
    }

# اللغات الثمانية المطلوبة بالكامل مع اختصاراتها العالمية
languages_dict = {
    "العربية": "ar", "الإنجليزية (English)": "en", "الألمانية (Deutsch)": "de",
    "الإسبانية (Español)": "es", "البرتغالية (Português)": "pt", "الروسية (Русский)": "ru", 
    "الكورية (한국어)": "ko", "الصينية (中文)": "zh"
}

# تصميم علامات التبويب لتقسيم الخصائص والدمج الشامل
tab_text, tab_files, tab_glossary = st.tabs([
    "🌐 ترجمة النصوص مع الصياغة الاحترافية والصوت", 
    "📄 ترجمة وصياغة الملفات والمستندات الكاملة", 
    "🗄️ القاموس المركزي المعتمد للمشروع"
])

# ==========================================
# 👈 التبويب الأول: ترجمة النصوص مع إعادة الصياغة والترتيب اللغوي
# ==========================================
with tab_text:
    col_inputs, col_outputs = st.columns([1, 1])
    with col_inputs:
        st.subheader("📥 مدخلات النص الأصلية")
        
        c1, c2 = st.columns(2)
        with c1: source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1, key="src_t")
        with c2: target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0, key="tgt_t")
        
        # ميزة دمج أسلوب الصياغة وضبط القواعد للغة المترجم إليها
        refine_style = st.radio(
            "🛠️ أسلوب صياغة وترتيب النص المترجم:",
            ["صياغة هندسية وفنية احترافية (منظمة)", "ترجمة مباشرة وبلاغية سليمة"],
            horizontal=True
        )
        
        text_to_translate = st.text_area(
            "اكتب أو الصق النص هنا بأي لغة (حتى لو كان ركيكاً):", 
            placeholder="اكتب هنا تقارير، كلمات، أو فقرات كاملة ليتم ترجمتها وإعادة صياغتها لغوياً...",
            height=180
        )
        btn_process = st.button("...", type="primary")
