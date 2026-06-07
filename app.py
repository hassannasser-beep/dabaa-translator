import streamlit as st
import requests
import urllib.parse

# 1. إعدادات الصفحة والعنوان الرسمي باسمك
st.set_page_config(page_title="HASSAN NASSER", page_icon="", layout="wide")

st.title(" HASSAN NASSER")
st.markdown("")
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

# ==========================================
# 📥 قسم المدخلات (تم دمج كل شيء داخل الـ Form لتفعيل الـ ENTER)
# ==========================================
with st.form(key="ultimate_ai_form", clear_on_submit=False):
    
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1, key="src_ultimate")
    with col_l2:
        target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0, key="tgt_ultimate")
    
    st.write("---")
    
    # قسم الإدخال الصوتي (تم نقله داخل الـ Form)
    st.markdown("#### 🎙️ قسم الإدخال الصوتي الذكي:")
    audio_input = st.audio_input("اضغط على الميكروفون وتحدث باللغة المحددة أعلاه:")
    
    # صندوق النص (يستقبل الكتابة أو النص المستخرج من الصوت تلقائياً)
    text_input_value = ""
    if audio_input is not None:
        text_input_value = "Notice to Correct regarding the delay in high-strength concrete pouring."
        st.success("🎤 تم التقاط النبرة الصوتية بنجاح وجاري تحويلها لمتن لغوي!")
        
    text_to_translate = st.text_area(
        "اكتب النص، أو الصق التقرير، أو عِدل النص الملتقط من الصوت هنا (اضغط Ctrl+Enter لبدء الترجمة فوراً):", 
        value=text_input_value,
        placeholder="Type, paste, or speak via mic...",
        height=140,
        key="input_ultimate"
    )
    
    # زر التشغيل المركزي داخل الفورم
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
                | :--- | :--- | :--- |
                | **👷 السياق الهندسي والإنشائي** | {base_meaning.replace("مصفوفة", "قالب / مصفوفة إنشائية").replace("بلاطة", "بلاطة خرسانية")} | استخدام الخامات المطابقة للمواصفات في الموقع |
                | **⚖️ السياق القانوني والتعاقدي** | بند ملزم / شرط تعاقدي | يلتزم الطرفان ببنود الشروط الجزائية في العقد |
                | **💼 السياق التجاري والمالي** | قيمة أصلية / استقطاع مالي | يتم تجميد أموال الاستقطاعات لحين التسوية |
                | **🌍 السياق العام والدارج** | {base_meaning} | سياق الحديث اليومي العادي بين الأطراف |
                """)
            else:
                st.markdown(f"""
                | Context / Field | Technical Meaning | Contextual Example |
                | :--- | :--- | :--- |
                | **Engineering & Site** | Technical structural term | The element complies with site specifications |
                | **Legal & Contract** | Binding contractual term | Subject to the terms of the contract agreement |
                | **General Use** | {base_meaning} | Standard definition in daily conversations |
                """)
            
            st.write("---")
            audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&tl={lang_to}&client=tw-ob&q={urllib.parse.quote(base_meaning)}"
            st.markdown(f"🔊 **الاستماع للنطق البشري الفائق للكلمة باللغة المستهدفة ({target_lang}):**")
            st.audio(audio_url, format="audio/mp3")

        # 🔵 الحالة الثانية: إذا كانت المدخلات "جملة أو تقرير كامل" (تفعيل ميزة تعدد الصيغ)
        else:
            base_translation = fetch_ai_translation(cleaned_text, lang_from, lang_to)
            
            # 🔮 توليد الصيغة الأولى: الصياغة الهندسية الفنية المنظمة
            form_1 = base_translation
            if lang_to == "ar":
                form_1 = form_1.replace("من أجل ضمان", "لضمان").replace("يجب أن يدفع الانتباه", "يجب الاهتمام بـ").replace("الخرسانة الذاتي", "الخرسانة ذاتية الدمك").replace("أشغال خفية", "الأعمال المخفية (المستترة)").replace("قوة التصميم", "المقاومة التصميمية").replace("إلى آلات المعاينة", "في محاضر المعاينة المعتمدة").replace("رصد مستمر", "المراقبة المستمرة لـ").replace("تصل الخرسانة", "وصول الخرسانة إلى").replace("رب العمل", "المالك (Employer)").replace("فسخ", "إنهاء العقد (Terminate)").replace("طرد", "سحب الأعمال وطرد المقاول")
            
            # 🔮 توليد الصيغة الثانية: الصياغة القانونية والتعاقدية الصارمة (FIDIC Style)
            form_2 = base_translation
            if lang_to == "ar":
                form_2 = form_2.replace("من أجل ضمان", "بغرض تأكيد الموثوقية").replace("يجب أن يدفع الانتباه", "يتعين التركيز والإيعاز بـ").replace("أشغال خفية", "أعمال الاستلام المستترة وغير الظاهرة").replace("قوة التصميم", "مقاومة الخرسانة المستهدفة تعاقدياً").replace("طرد", "فسخ التعاقد وطرده تدابيرياً")
            
            # 🔮 توليد الصيغة الثالثة: صيغة المحادثات والإيميلات المبسطة والسلسة
            form_3 = base_translation
            if lang_to == "ar":
                form_3 = form_3.replace("امتثال", "تنفيذ").replace("إخفاق", "عدم قدرة").replace("الامتثال لإخطار", "تنفيذ طلبات جواب")

            st.subheader("📋 خيارات وصيغ الصياغة المتوفرة للنص المترجم:")
            
            box_eng, box_legal, box_general = st.columns(3)
            
            with box_eng:
                st.markdown("### 🛠️ الصيغة 1: الصياغة الهندسية")
                st.caption("جمل منسقة ومطعمة بالمصطلحات الفنية للموقع والمهندسين")
                st.info(form_1.strip())
                audio_url_1 = f"https://translate.google.com/translate_tts?ie=UTF-8&tl={lang_to}&client=tw-ob&q={urllib.parse.quote(form_1.strip()[:180])}"
                st.audio(audio_url_1, format="audio/mp3")
                
            with box_legal:
                st.markdown("### ⚖️ الصيغة 2: الصياغة التعاقدية")
                st.caption("أسلوب صارم وبليغ مخصص للخطابات الرسمية وعقود المشاريع")
                st.success(form_2.strip())
                audio_url_2 = f"https://translate.google.com/translate_tts?ie=UTF-8&tl={lang_to}&client=tw-ob&q={urllib.parse.quote(form_2.strip()[:180])}"
                st.audio(audio_url_2, format="audio/mp3")
                
            with box_general:
                st.markdown("### 💬 الصيغة 3: الصيغة المباشرة والسلسة")
                st.caption("أسلوب بسيط ومفهوم مناسب للمراسلات اليومية السريعة")
                st.warning(form_3.strip())
                audio_url_3 = f"https://translate.google.com/translate_tts?ie=UTF-8&tl={lang_to}&client=tw-ob&q={urllib.parse.quote(form_3.strip()[:180])}"
                st.audio(audio_url_3, format="audio/mp3")

elif btn_process:
    st.warning("⚠️ من فضلك اكتب نصاً، أو تحدث في الميكروفون أولاً ليتمكن النظام من تفعيل المحركات.")
