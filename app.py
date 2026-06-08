import streamlit as st
from g4f.client import Client
import json

# 1. إعدادات الصفحة والعنوان الرسمي
st.set_page_config(page_title="HASSAN NASSER", page_icon="🤖", layout="wide")

st.title("🤖 HASSAN NASSER")
st.markdown("### 🧠 REAL AI MULTI-CONTEXT TRANSLATOR | المترجم الذكي المربوط بالذكاء الاصطناعي")
st.write("---")

# اللغات المعتمدة في النظام
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

# دالة الاتصال بمحرك الذكاء الاصطناعي لجلب تحليل سياقي عميق وشرح مفصل
def ask_ai_for_translation(text, from_lang, to_lang):
    # تهيئة عميل الذكاء الاصطناعي المجاني كبديل لكسر الحظر الجغرافي
    client = Client()
    
    # صياغة أمر صارم وذكي جداً ليتصرف المحرك مثل جيميني تماماً ويعيد شرحاً ومترادفات حقيقية
    prompt = f"""
    You are an advanced AI translator like Gemini. Translate the text/word: "{text}" from {from_lang} to {to_lang}.
    Provide a deeply contextual translation and an explanation for each of the following 7 styles/genres. 
    If a certain style does not apply to the word at all, return null for that style, but try your best to find a relevant meaning or technical adaptation.
    
    Styles required:
    1. General (عامة): Basic everyday meaning.
    2. Engineering (هندسة موقعية): Technical site terms, construction slang, structural meaning.
    3. Legal (قانونية تعاقدية): FIDIC contracts style, binding terms.
    4. Scientific (علمية): Academic or research terminology.
    5. Political (سياسية): Diplomatic or official government text.
    6. Economic (اقتصادية): Financial, BOQ, or market context.
    7. Religious (دينية): Spiritual or theological dimension.

    You MUST respond ONLY with a valid JSON object matching this structure. Do not include markdown formatting like ```json or any intro text. Just raw JSON:
    {{
      "general": "Detailed translation + short explanation in Arabic",
      "engineering": "Detailed translation + short explanation in Arabic or null",
      "legal": "Detailed translation + short explanation in Arabic or null",
      "scientific": "Detailed translation + short explanation in Arabic or null",
      "political": "Detailed translation + short explanation in Arabic or null",
      "economic": "Detailed translation + short explanation in Arabic or null",
      "religious": "Detailed translation + short explanation in Arabic or null"
    }}
    """

    try:
        # إرسال الطلب لمحرك الذكاء الاصطناعي التوليدي
        response = client.chat.completions.create(
            model="gpt-4o", # نستخدم gpt-4o المتاح مجاناً والمكافئ لقوة جيميني في فهم السياق الشامل
            messages=[{"role": "user", "content": prompt}]
        )
        
        # تنظيف النص المستلم وتحويله لقاموس برمجى
        raw_text = response.choices[0].message.content.strip()
        # إزالة أي زوائد ماركداون إذا أضافها المحرك خطأً
        if raw_text.startswith("```json"):
            raw_text = raw_text.replace("```json", "").replace("```", "").strip()
        elif raw_text.startswith("```"):
            raw_text = raw_text.replace("```", "").strip()
            
        return json.loads(raw_text)
    except Exception as e:
        st.error(f"❌ حدث خطأ أثناء معالجة العقل الذكي: {e}")
        return None

# ==========================================
# 📥 واجهة المستخدم (Inputs)
# ==========================================
with st.form(key="ai_translator_form", clear_on_submit=False):
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1, key="src_lang")
    with col_l2:
        target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0, key="tgt_lang")
    
    st.write("---")
    
    text_to_translate = st.text_area(
        "أدخل الكلمة أو العبارة (سيقوم العقل الاصطناعي بتشريحها وإعطائك المعاني التفصيلية):", 
        placeholder="اكتب هنا الكلمة الفنية أو الجملة المراد تحليلها بذكاء...",
        height=150,
        key="input_text"
    )
    
    btn_process = st.form_submit_button("🧠 RUN AI PROMPT | تشغيل الفرز والتحليل الذكي الشامل", use_container_width=True)

st.write("---")

# ==========================================
# 📊 عرض النتائج (Outputs)
# ==========================================
if btn_process and text_to_translate.strip():
    cleaned_text = text_to_translate.strip()
    
    lang_from = languages_dict[source_lang]
    lang_to = languages_dict[target_lang]
    
    with st.spinner("🧠 يتصل التطبيق الآن بعقل الذكاء الاصطناعي التوليدي لتحليل النص..."):
        result = ask_ai_for_translation(cleaned_text, lang_from, lang_to)
        
        if result:
            st.success("🎯 تم التحليل السياقي بواسطة الذكاء الاصطناعي بدقة تامة:")
            st.write("---")
            
            st.subheader("🛠️ الصياغات والشروح الأساسية الدائمة:")
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.markdown("### 💬 صياغة عامة وشرحها")
                st.warning(result.get("general", "غير متوفر"))
            with col_b:
                st.markdown("### 👷 صياغة هندسية موقِعية تفصيلية")
                eng_res = result.get("engineering")
                if eng_res: st.info(eng_res)
                else: st.caption("_لا توجد أبعاد إنشائية أو موقعية لهذه الكلمة_")
            with col_c:
                st.markdown("### 📜 صياغة تعاقدية قانونية (FIDIC)")
                leg_res = result.get("legal")
                if leg_res: st.success(leg_res)
                else: st.caption("_لا توجد صيغة شروط تعاقدية مناسبة_")
                
            st.write("---")
            
            st.subheader("🎯 الصياغات التخصصية المشروحة (تظهر إن وجدت):")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🧬 الصياغة العلمية الأكاديمية")
                sci_res = result.get("scientific")
                if sci_res: st.info(sci_res)
                else: st.caption("_لا توجد تفسيرات علمية مختبرية دقيقة لهذا النص_")
                    
                st.markdown("### 📊 الصياغة الاقتصادية والمالية")
                eco_res = result.get("economic")
                if eco_res: st.warning(eco_res)
                else: st.caption("_لا توجد دلالات مالية أو حساب كميات ومقايسات_")

            with col2:
                st.markdown("### 🏛️ الصياغة السياسية والدبلوماسية")
                pol_res = result.get("political")
                if pol_res: st.code(pol_res, language="")
                else: st.caption("_لا توجد تفاسير سياسية أو حكومية رسمية_")
                    
                st.markdown("### 🌙 الصياغة الدينية والروحية")
                rel_res = result.get("religious")
                if rel_res: st.markdown(f"> **{rel_res}**")
                else: st.caption("_لا توجد دلالات لاهوتية أو دينية لهذه الكلمة_")

elif btn_process:
    st.warning("⚠️ من فضلك اكتب النص أولاً لتشغيل محرك الذكاء الاصطناعي.")
