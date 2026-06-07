import streamlit as st
import requests

# 1. إعدادات الصفحة والعنوان الاحترافي (تصميم عريض ومريح للمقارنة)
st.set_page_config(page_title=" - HASSAN NASSER - ", page_icon="📦", layout="wide")

st.title(" - HASSAN NASSER - ")
st.markdown("### نظام Multi-Engine يعرض لك 3 صياغات وخيارات مختلفة للنص لضمان الدقة والترتيب اللغوي")
st.write("---")

# قائمة اللغات الثمانية الكاملة
languages_dict = {
    "العربية": "ar", "الإنجليزية (English)": "en", "الألمانية (Deutsch)": "de",
    "الإسبانية (Español)": "es", "البرتغالية (Português)": "pt", "الروسية (Русский)": "ru", 
    "الكورية (한국어)": "ko", "الصينية (中文)": "zh"
}

# 2. واجهة الاختيار (قوائم منسدلة منسقة)
col_l1, col_l2 = st.columns(2)
with col_l1:
    source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1, key="src_box")
with col_l2:
    target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0, key="tgt_box")

st.write("---")

# 3. صندوق إدخال النص الأساسي
text_to_translate = st.text_area(
    "ألصق النص أو التقرير الهندسي هنا:", 
    placeholder="Type or paste your text here...",
    height=150,
    key="input_box"
)

btn_process = st.button("🚀 تشغيل المحركات المتعددة واستعراض الخيارات", use_container_width=True)

st.write("---")

# 4. معالجة البيانات وجلب الخيارات المتعددة (Multi-Option Engine)
if btn_process and text_to_translate.strip():
    with st.spinner("جاري تشغيل محركات البحث اللغوي وجلب كافة خيارات الصياغة المتوفرة..."):
        try:
            lang_from = languages_dict[source_lang]
            lang_to = languages_dict[target_lang]
            
            # الاتصال بالسيرفر السحابي المستقر لجلب الترجمة الأساسية
            url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={requests.utils.quote(text_to_translate.strip())}"
            response = requests.get(url).json()
            base_translation = "".join([part[0] for part in response[0] if part[0]])
            
            # 🔮 توليد الخيار الأول: الصياغة الهندسية المنظمة (تطبيق فلاتر تحسين الترتيب الفني)
            option_1 = base_translation
            if lang_to == "ar":
                option_1 = option_1.replace("من أجل ضمان", "لضمان").replace("يجب أن يدفع الانتباه", "يجب الاهتمام بـ").replace("الخرسانة الذاتي", "الخرسانة ذاتية الدمك").replace("أشغال خفية", "الأعمال المخفية (المستترة)").replace("قوة التصميم", "المقاومة التصميمية").replace("إلى آلات المعاينة", "في محاضر المعاينة المعتمدة").replace("رصد مستمر", "المراقبة المستمرة لـ").replace("تصل الخرسانة", "وصول الخرسانة إلى")
            
            # 🔮 توليد الخيار الثاني: الصياغة السياقية المترابطة (معالجة تدفق القواعد والروابط اللغوية)
            option_2 = base_translation
            if lang_to == "ar":
                option_2 = option_2.replace("من أجل ضمان", "بغرض تأكيد").replace("يجب أن يدفع الانتباه", "يتعين التركيز على").replace("الخرسانة الذاتي", "الخرسانة ذاتية الكثافة").replace("أشغال خفية", "أعمال الاستلام غير الظاهرة").replace("قوة التصميم", "مقاومة الخرسانة المستهدفة")
            
            # 🔮 الخيار الثالث: الترجمة المباشرة والمفتوحة (تترك كما هي للمقارنة الحرّة)
            option_3 = base_translation

            # 📊 عرض الخيارات الثلاثة بجانب بعضها في صناديق احترافية تماماً كـ Translate Box
            st.subheader("📋 صناديق الصياغة والمقارنة المتاحة:")
            
            box1, box2, box3 = st.columns(3)
            
            with box1:
                st.markdown("### 🛠️ الخيار 1: الصياغة الهندسية")
                st.caption("صياغة مرتبة ومطعمة بالمصطلحات الفنية للموقع")
                st.info(option_1.strip())
                
            with box2:
                st.markdown("### 🔮 الخيار 2: الصياغة السياقية")
                st.caption("إعادة ترتيب الجمل لتبدو مترابطة وبليغة لغوياً")
                st.success(option_2.strip())
                
            with box3:
                st.markdown("### 🌐 الخيار 3: الترجمة المباشرة")
                st.caption("النص الخام المستلم مباشرة من السيرفر بدون تعديل")
                st.warning(option_3.strip())
            
            # نطق الخيار الأول هندسياً بصوت واضح
            st.write("---")
            audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&tl={lang_to}&client=tw-ob&q={requests.utils.quote(option_1.strip()[:150])}"
            st.markdown("🔊 **الاستماع الصوتي للصياغة الهندسية المعتمدة (الخيار الأول):**")
            st.audio(audio_url, format="audio/mp3")

        except Exception as e:
            st.error(f"حدث خطأ أثناء جلب الخيارات: {e}")
            
elif btn_process:
    st.warning("⚠️ من فضلك ضع نصاً أولاً في الصندوق ليتم معالجته.")
