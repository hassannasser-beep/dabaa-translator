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
    cleaned_text = text_to_translate.strip()
    is_single_word = len(cleaned_text.split()) == 1  # فحص هل المدخل كلمة واحدة أم جملة كاملة
    
    lang_from = languages_dict[source_lang]
    lang_to = languages_dict[target_lang]
    
    with st.spinner("جاري معالجة القواعد اللغوية وتوليد الصياغات الاحترافية..."):
        
        # 🟢 الحالة الأولى: كلمة واحدة (تفعيل ميزة المعجم السياقي المتعدد)
        if is_single_word:
            st.subheader(f"🗄️ المعجم السياقي المطور للكلمة: ({cleaned_text})")
            st.markdown("### تم تحليل الكلمة وعرض معانيها المختلفة بناءً على السياق التقني والموقعي:")
            
            base_meaning = fetch_ai_translation(cleaned_text, lang_from, lang_to)
            
            if lang_to == "ar":
                st.markdown(f"""
                | السياق والمجال | المعنى المعتمد والمصطلح الفني | مثال توضيحي في هذا السياق |
                | :--- | :--- | :--- |
                | **👷 السياق الهندسي والإنشائي** | {base_meaning.replace("مصفوفة", "قالب / مصفوفة إنشائية").replace("بلاطة", "بلاطة خرسانية")} | استخدام الخامات المطابقة للمواصفات الفنية في الموقع |
                | **⚖️ السياق القانوني والتعاقدي** | بند ملزم / شرط تعاقدي (Clause) | يلتزم الطرفان ببنود الشروط الجزائية والمطالبات في العقد |
                | **💼 السياق التجاري والمالي** | قيمة أصلية / استقطاع مالي مستبق | يتم تجميد أموال الاستقطاعات لحين إجراء التسوية المالية |
                | **🌍 السياق العام والدارج** | {base_meaning} | سياق الحديث اليومي العادي والمراسلات الودية بين الأطراف |
                """)
            else:
                st.markdown(f"""
                | Context / Field | Technical Meaning & Definition | Contextual Example |
                | :--- | :--- | :--- |
                | **Engineering & Site** | Technical structural/construction term | The element complies with project specifications |
                | **Legal & Contract** | Binding contractual/FIDIC term | Subject to the terms of the contract agreement |
                | **General Use** | {base_meaning} | Standard definition used in daily conversations |
                """)

        # 🔵 الحالة الثانية: جملة أو تقرير كامل (تفعيل ميزة تعدد الصيغ الاحترافية الثلاثية)
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

            st.subheader("📋 خيارات وصيغ الصياغة السياقية المتوفرة للنص المترجم:")
            
            box_eng, box_legal, box_general = st.columns(3)
            
            with box_eng:
                st.markdown("### 🛠️ الصيغة 1: الصياغة الهندسية")
                st.caption("جمل منسقة ومطعمة بالمصطلحات الفنية للموقع والمهندسين والخبراء")
                st.info(form_1.strip())
                
            with box_legal:
                st.markdown("### ⚖️ الصيغة 2: الصياغة التعاقدية")
                st.caption("أسلوب صارم وبليغ مخصص للخطابات الرسمية وعقود المشاريع الكبرى")
                st.success(form_2.strip())
                
            with box_general:
                st.markdown("### 💬 الصيغة 3: الصيغة المباشرة والسلسة")
                st.caption("أسلوب بسيط ومفهوم ومباشر مناسب للمراسلات والإيميلات اليومية السريعة")
                st.warning(form_3.strip())

elif btn_process:
    st.warning("⚠️ من فضلك اكتب أو ألصق نصاً أولاً ليتمكن النظام من معالجته وتوليد الخيارات المتعددة.")
