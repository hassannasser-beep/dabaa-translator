import streamlit as st
import requests

# 1. إعدادات الصفحة والعنوان باسمك (تم جعل التصميم يتكيف تلقائياً مع الشاشات)
st.set_page_config(page_title="HASSAN NASSER", page_icon="🏗️", layout="centered")

st.title(" - HASSAN NASSER - ")
st.markdown("### نظام متطور يترجم النصوص والملفات، ويعيد صياغتها لغوياً وقواعدياً")
st.write("---")

# 2. القاموس المركزي المعتمد في الذاكرة
if 'glossary' not in st.session_state:
    st.session_state.glossary = {
        "handover": "تسليم الأعمال رسمياً للجهة الاستشارية",
        "scrap": "مخلفات الحديد والمواد التالفة (السكراب)",
        "slab": "بلاطة خرسانية إنشائية (الأسقف والأرضيات)",
        "pile": "خازوق إنشائي عميق لدعم التربة",
        "lean concrete": "خرسانة عادية (خرسانة نظافة بدون تسليح)"
    }

# قائمة اللغات الثمانية الكاملة
languages_dict = {
    "العربية": "ar", "الإنجليزية (English)": "en", "الألمانية (Deutsch)": "de",
    "الإسبانية (Español)": "es", "البرتغالية (Português)": "pt", "الروسية (Русский)": "ru", 
    "الكورية (한국어)": "ko", "الصينية (中文)": "zh"
}

# 3. واجهة اختيار اللغات (تم وضعها بشكل رأسي مريح للعين لمنع الاختفاء)
source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1, key="src_v")
target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0, key="tgt_v")

st.write("---")

# 4. اختيار نمط الصياغة والتدقيق
refine_style = st.radio(
    "🛠️ أسلوب صياغة وترتيب النص المترجم:",
    ["صياغة هندسية وفنية احترافية (منظمة)", "ترجمة مباشرة وبلاغية سليمة"],
    key="style_v"
)

st.write("---")

# 5. صندوق إدخال النص الكبير لسهولة اللصق والكتابة
text_to_translate = st.text_area(
    "اكتب أو الصق النص هنا بأي لغة (كلمات، جمل، أو تقارير):", 
    placeholder="اكتب هنا ليتم ترجمتها وإعادة صياغتها لغوياً فوراً...",
    height=150,
    key="input_v"
)

# 6. زر الترجمة الصريح والكبير (يظهر بملء عرض الشاشة لسهولة الضغط)
btn_process = st.button("✨ ابدأ الترجمة وضبط الصياغة الفورية", use_container_width=True)

st.write("---")

# 7. المعالجة وعرض النتائج بالأسفل بشكل مباشر
if btn_process and text_to_translate.strip():
    with st.spinner("جاري الترجمة العميقة وإعادة صياغة وترتيب الجمل..."):
        try:
            lang_from = languages_dict[source_lang]
            lang_to = languages_dict[target_lang]
            search_word = text_to_translate.strip().lower()
            
            # الفحص في القاموس المركزي
            if search_word in st.session_state.glossary and lang_to == "ar":
                st.info("💡 تم استخدام الترجمة المعتمدة رسمياً في المشروع من القاموس:")
                st.success(st.session_state.glossary[search_word])
            else:
                # محرك الترجمة ونقل المعنى
                url_api = "https://htmltranslator.com/api/translate"
                payload_trans = {"text": text_to_translate.strip(), "from": lang_from, "to": lang_to}
                res_trans = requests.post(url_api, json=payload_trans).json()
                translated_text = res_trans.get('translated_text', '')
                
                if not translated_text:
                    b_url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={requests.utils.quote(text_to_translate.strip())}"
                    translated_text = "".join([p[0] for p in requests.get(b_url).json()[0] if p[0]])
                
                # محرك إعادة الصياغة السليم والترتيب
                payload_refine = {"text": translated_text.strip(), "from": lang_to, "to": "en" if lang_to != "en" else "fr"}
                res_refine_inter = requests.post(url_api, json=payload_refine).json()
                inter_text = res_refine_inter.get('translated_text', '')
                
                if inter_text:
                    payload_final = {"text": inter_text, "from": "en" if lang_to != "en" else "fr", "to": lang_to}
                    res_final = requests.post(url_api, json=payload_final).json()
                    final_output = res_final.get('translated_text', translated_text)
                else:
                    final_output = translated_text

                # الفلتر الهندسي لترتيب العبارات الفنية للمهندس حسن
                if "هندسية" in refine_style and lang_to == "ar":
                    final_output = final_output.replace("من أجل ضمان", "لضمان").replace("يجب أن يدفع الانتباه", "يجب الاهتمام بـ").replace("الخرسانة الذاتي", "الخرسانة ذاتية الدمك").replace("أشغال خفية", "الأعمال المخفية (المستترة)").replace("قوة التصميم", "المقاومة التصميمية").replace("إلى آلات المعاينة", "في محاضر المعاينة").replace("رصد مستمر", "المراقبة المستمرة لـ").replace("تصل الخرسانة", "وصول الخرسانة إلى")

                # عرض النتيجة النهائية تحت بعضها بشكل منسق جداً
                st.subheader("📝 النتيجة النهائية المصاغة:")
                st.info(final_output.strip())
                
                # النطق الصوتي للمصطلحات
                audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&tl={lang_to}&client=tw-ob&q={requests.utils.quote(final_output.strip()[:150])}"
                st.markdown("🔊 **الاستماع للنطق الصحيح والسليم للترجمة:**")
                st.audio(audio_url, format="audio/mp3")
                
        except Exception as e:
            st.error(f"حدث خطأ أثناء المعالجة اللغوية: {e}")
elif btn_process:
    st.warning("⚠️ يرجى إدخال نص أولاً ليتمكن النظام من ترجمته وتصحيحه.")
