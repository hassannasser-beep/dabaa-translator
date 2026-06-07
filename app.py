import streamlit as st
import requests

# 1. إعدادات الصفحة والعنوان باسمك (تصميم متوافق مع الموبايل والكمبيوتر)
st.set_page_config(page_title=" - HASSAN NASSER - ", page_icon="🏗️", layout="centered")

st.title(" - HASSAN NASSER - ")
st.markdown("### نظام متطور يترجم النصوص والملفات، ويعيد صياغتها لغوياً وقواعدياً عبر سيرفرات Google المستقرة")
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

# قائمة اللغات الثمانية الكاملة والمضبوطة
languages_dict = {
    "العربية": "ar", "الإنجليزية (English)": "en", "الألمانية (Deutsch)": "de",
    "الإسبانية (Español)": "es", "البرتغالية (Português)": "pt", "الروسية (Русский)": "ru", 
    "الكورية (한국어)": "ko", "الصينية (中文)": "zh"
}

# 3. واجهة اختيار اللغات بشكل رأسي مريح ومنظم
source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1, key="src_google")
target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0, key="tgt_google")

st.write("---")

# 4. اختيار نمط الصياغة والتدقيق
refine_style = st.radio(
    "🛠️ أسلوب صياغة وترتيب النص المترجم:",
    ["صياغة هندسية وفنية احترافية (منظمة)", "ترجمة مباشرة وبلاغية سليمة"],
    key="style_google"
)

st.write("---")

# 5. صندوق إدخال النص الكبير لسهولة اللصق والكتابة
text_to_translate = st.text_area(
    "اكتب أو الصق النص هنا بأي لغة (كلمات، جمل، أو تقارير):", 
    placeholder="اكتب أو الصق النص هنا ليتم ترجمته وضبط صياغته وقواعده فوراً...",
    height=150,
    key="input_google"
)

# 6. زر الترجمة الصريح بملء عرض الشاشة لسهولة الضغط
btn_process = st.button("✨ ابدأ الترجمة وضبط الصياغة الفورية", use_container_width=True)

st.write("---")

# 7. المعالجة وعرض النتائج المباشرة عبر سيرفر جوجل المستقر
if btn_process and text_to_translate.strip():
    with st.spinner("جاري الاتصال الآمن بسيرفرات Google وترتيب الجمل لغوياً..."):
        try:
            lang_from = languages_dict[source_lang]
            lang_to = languages_dict[target_lang]
            search_word = text_to_translate.strip().lower()
            
            # الفحص أولاً في القاموس المركزي المعتمد للموقع
            if search_word in st.session_state.glossary and lang_to == "ar":
                st.info("💡 تم استخدام الترجمة المعتمدة رسمياً في المشروع من القاموس:")
                st.success(st.session_state.glossary[search_word])
            else:
                # 📡 الاتصال المباشر بسيرفر جوجل القياسي والمستقر عالمياً
                url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={requests.utils.quote(text_to_translate.strip())}"
                
                response = requests.get(url)
                response_json = response.json()
                
                # تجميع أجزاء النص المترجم لضمان قراءة التقارير الطويلة بدون انقطاع
                final_output = "".join([part[0] for part in response_json[0] if part[0]])

                # 🔮 الفلتر الهندسي الذكي الخاص بالمهندس حسن ناصر لضبط الصياغة الفنية العربية
                if "هندسية" in refine_style and lang_to == "ar":
                    final_output = final_output.replace("من أجل ضمان", "لضمان").replace("يجب أن يدفع الانتباه", "يجب الاهتمام بـ").replace("الخرسانة الذاتي", "الخرسانة ذاتية الدمك").replace("أشغال خفية", "الأعمال المخفية (المستترة)").replace("قوة التصميم", "المقاومة التصميمية").replace("إلى آلات المعاينة", "في محاضر المعاينة المعتمدة").replace("رصد مستمر", "المراقبة المستمرة لـ").replace("تصل الخرسانة", "وصول الخرسانة إلى")

                # عرض النتيجة النهائية المصاغة والمنظمة
                st.subheader("📝 النتيجة النهائية المترجمة والمصاغة:")
                st.info(final_output.strip())
                
                # ميزة النطق الصوتي الصحيح من جوجل
                audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&tl={lang_to}&client=tw-ob&q={requests.utils.quote(final_output.strip()[:150])}"
                st.markdown("🔊 **الاستماع للنطق الصحيح والسليم للترجمة:**")
                st.audio(audio_url, format="audio/mp3")
                
        except Exception as e:
            st.error(f"حدث خطأ أثناء المعالجة اللغوية: {e}")
elif btn_process:
    st.warning("⚠️ يرجى إدخال نص أولاً ليتمكن النظام من ترجمته وتصحيحه.")
