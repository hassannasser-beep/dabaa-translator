import streamlit as st
import requests

# 1. إعدادات الصفحة والعنوان الاحترافي باسمك
st.set_page_config(page_title=" - HASSAN NASSER - ", page_icon="", layout="centered")

st.title(" - HASSAN NASSER - ")
st.markdown("")
st.write("---")

# اللغات الثمانية المدعومة بالكامل
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

# دالة الذكاء الاصطناعي لمعالجة النصوص سياقياً ولغوياً
def ai_core_translator(text, from_lang, to_lang):
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {
            "client": "gtx",
            "sl": from_lang,
            "tl": to_lang,
            "dt": "t",
            "q": text.strip()
        }
        response = requests.get(url, params=params).json()
        return "".join([part[0] for part in response[0] if part[0]])
    except Exception as e:
        return f"⚠️ خطأ مؤقت في السيرفر: {e}"

# 2. بناء الاستمارة (Form) لتفعيل زر ENTER عند الكتابة والضغط مباشرة
with st.form(key="custom_ai_form", clear_on_submit=False):
    
    source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1, key="src_custom")
    target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0, key="tgt_custom")
    
    st.write("---")
    
    text_to_translate = st.text_area(
        "اكتب أو الصق النص هنا (اضغط Ctrl + Enter أو زر التشغيل بالأسفل لبدء الترجمة):", 
        placeholder="Type or paste your text here...",
        height=180,
        key="input_custom"
    )
    
    btn_process = st.form_submit_button("TRANSLATING", use_container_width=True)

st.write("---")

# 3. المعالجة وعرض النتيجة في صندوق مخصص واحد بناءً على اختيارك
if btn_process and text_to_translate.strip():
    with st.spinner("جاري الترجمة وإعادة ترتيب الجمل لغوياً..."):
        try:
            lang_from = languages_dict[source_lang]
            lang_to = languages_dict[target_lang]
            
            # استدعاء المحرك الذكي
            final_output = ai_core_translator(text_to_translate, lang_from, lang_to)
            
            # 🔮 فلتر الصياغة الهندسية التلقائي إذا كانت اللغة المستهدفة هي العربية
            if lang_to == "ar":
                final_output = final_output.replace("من أجل ضمان", "لضمان").replace("يجب أن يدفع الانتباه", "يجب الاهتمام بـ").replace("الخرسانة الذاتي", "الخرسانة ذاتية الدمك").replace("أشغال خفية", "الأعمال المخفية (المستترة)").replace("قوة التصميم", "المقاومة التصميمية").replace("إلى آلات المعاينة", "في محاضر المعاينة المعتمدة").replace("رصد مستمر", "المراقبة المستمرة لـ").replace("تصل الخرسانة", "وصول الخرسانة إلى").replace("رب العمل", "المالك (Employer)").replace("فسخ", "إنهاء العقد (Terminate)").replace("طرد", "سحب الأعمال وطرد المقاول")

            # عرض النتيجة المخصصة في صندوق واحد مريح
            st.subheader("📝 النتيجة النهائية المصاغة:")
            st.success(final_output.strip())
            
            # 
            audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&tl={lang_to}&client=tw-ob&q={requests.utils.quote(final_output.strip()[:150])}"
            st.markdown("🔊 **الاستماع للنطق الصحيح والسليم للترجمة:**")
            st.audio(audio_url, format="audio/mp3")
            
        except Exception as e:
            st.error(f"حدث خطأ أثناء المعالجة اللغوية: {e}")
            
elif btn_process:
    st.warning("⚠️ من فضلك اكتب أو الصق نصاً أولاً ليتمكن النظام من معالجته.")
