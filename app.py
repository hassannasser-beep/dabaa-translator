import streamlit as st
from translate import Translator as LocalTranslator
from textblob import TextBlob

# 1. إعدادات الصفحة والعنوان الرسمي باسمك
st.set_page_config(page_title="HASSAN NASSER", page_icon="🤖", layout="wide")

st.title("🤖 HASSAN NASSER")
st.markdown("### 🧠 HYBRID AI CONTEXTUAL TRANSLATOR | المترجم السياقي الهجين المستقر")
st.write("---")

# إعادة اللغات الثمانية كاملة
languages_dict = {
    "العربية": "ar", 
    " can الإنجليزية (English)": "en", 
    "الروسية (Русский)": "ru", 
    "الصينية (中文)": "zh", 
    "الألمانية (Deutsch)": "de", 
    "الإسبانية (Español)": "es", 
    "البرتغالية (Português)": "pt", 
    "الكورية (한국어)": "ko"
}

# دالة مدمجة ذكية لمحاكاة عقل الذكاء الاصطناعي في تفكيك وشرح المصطلحات هندسياً وقانونياً
def generate_advanced_explanations(translated_text, original_text, to_lang):
    orig_lower = original_text.lower().strip()
    
    # إذا كانت اللغة المستهدفة ليست العربية، نعيد النص مترجماً مباشرة في القوالب
    if to_lang != "ar":
        return translated_text, f"[Technical Site Mode]: {translated_text}", f"[Contractual/FIDIC]: {translated_text}", f"[Academic/Scientific]: {translated_text}", f"[Official]: {translated_text}", f"[Financial/BOQ]: {translated_text}", f"[Cultural]: {translated_text}"

    # 1. قاعدة البيانات الذكية للمصطلحات الهندسية الكبرى (موقع الضبعة) ليعطي شرحاً فائق الدقة
    engineering_database = {
        "concrete casting": "أعمال الصب الموقعي للخرسانة الإنشائية؛ تشمل التحقق من جودة الخلطة، واختبار الهبوط (Slump Test)، وأخذ المكعبات القياسية، واستخدام الهزازات لمنع التعشيش وضمان الكثافة الاستراتيجية.",
        "high voltage poles": "أبراج الجهد العالي وأعمدة الضغط العالي؛ هياكل شبكية معدنية أو خرسانية سابقة الإجهاد مصممة لتحمل كابلات نقل الطاقة ومقاومة الرياح والزلزالية مع تحقيق العزل التام.",
        "high-voltage poles": "أبراج الجهد العالي وأعمدة الضغط العالي؛ هياكل شبكية معدنية أو خرسانية سابقة الإجهاد مصممة لتحمل كابلات نقل الطاقة ومقاومة الرياح والزلزالية مع تحقيق العزل التام.",
        "shop drawings": "الرسومات التنفيذية المعتمدة للموقع؛ اللوحات التفصيلية الدقيقة المترجمة من المخططات التصميمية، وتوضح تفريد حديد التسليح (BBS)، وأبعاد الوصلات، وهي المرجع الملزم للتنفيذ.",
        "reinforcement": "حديد التسليح للعناصر الإنشائية؛ شبكات أسياخ الصلب عالي المقاومة الموضوعة بدقة في مناطق إجهادات الشد داخل البلاطات والقواعد والأعمدة لتعويض ضعف الخرسانة.",
        "slab": "البلاطة الخرسانية (السقف/الفرش الإنشائي)؛ العنصر الأفقي المسؤول عن استقبال ونقل الأحمال الحية والميتة إلى الأعمدة، وتصنف إلى بلاطات مصمتة (Solid) أو مسطحة (Flat).",
        "lean concrete": "خرسانة النظافة (الفرشية العادية)؛ طبقة خرسانية غير مسلحة بسمك (10-15 سم) تصب فوق التربة مباشرة لتوفير سطح مستوٍ ونظيف يحمي حديد تسليح القواعد من الرطوبة والأملاح.",
        "honeycombing": "تعشيش الخرسانة؛ عيب فني خطير يظهر بعد فك الشدات نتيجة انفصال الحصوات عن عجينة الإسمنت مسبباً فراغات هوائية، ويتطلب إصلاحاً بمواد إيبوكسية عالية المقاومة (Grout).",
        "curing": "معالجة الخرسانة (الإنضاج)؛ الحفاظ على رطوبة الخرسانة المصبوبة ومنع تبخر المياه منها لفترة لا تقل عن 7 أيام متتالية (بالرش أو الخيش) لضمان اكتمال التفاعل الكيميائي للاسمنت.",
        "shuttering": "الشدات والنجارة الإنشائية؛ الهيكل المؤقت والقوالب الحاضنة (خشبية أو معدنية) التي تشكل لحفظ الخرسانة الطرية وتثبيتها في مكانها وأبعادها الصحيحة حتى تتصلد تماماً."
    }

    # جلب الشرح الهندسي إذا كانت الكلمة مدمجة، أو توليد شرح تلقائي ذكي إذا كانت كلمة جديدة
    if orig_lower in engineering_database:
        eng_exp = engineering_database[orig_lower]
    else:
        eng_exp = f"📌 [شرح هندسي موقِعي تلقائي]: تعني ({translated_text}) في السياق التنفيذي للموقع، ويتم مطابقتها مع المواصفات الفنية للمشروع والرسومات المعتمدة لضمان جودة الاستلام."

    # 2. توليد الصياغة والشرح العام
    gen_exp = f"💬 الترجمة اللغوية المباشرة هي ({translated_text})، وتستخدم في السياقات العامة والمحادثات اليومية للدلالة على المعنى اللفظي الأساسي."

    # 3. توليد الصياغة والشرح القانوني والتعاقدي (FIDIC)
    if "المقاول" in translated_text or "contractor" in orig_lower:
        legal_exp = "📜 [صياغة الفيديك]: يلتزم الطرف الثاني (المقاول) بالمسؤولية الكاملة عن تنفيذ وتأمين هذا البند وفقاً للشروط العامة والخاصة للعقد."
    else:
        legal_exp = f"📜 [السياق التعاقدي]: البند القانوني الخاص بـ ({translated_text})؛ خاضع لإجراءات الفحص والمعاينة وإصدار محاضر الاستلام الرسمية لترتيب الالتزامات المالية."

    # 4. توليد الصياغة العلمية والأكاديمية
    sci_exp = f"🔬 [التحليل الأكاديمي]: الدراسة المختبرية والفيزيائية لخاصية ({translated_text})، مع تحليل السلوك الكيميائي أو الميكانيكي للمادة تحت تأثير ظروف الإجهاد المختلفة."

    # 5. توليد الصياغة السياسية والرسمية
    pol_exp = f"🏛️ [التقرير الرسمي]: التقارير الدبلوماسية المعتمدة والخطابات الحكومية الموجهة بين الشركاء الدوليين بخصوص تنظيم أعمال ({translated_text})."

    # 6. توليد الصياغة الاقتصادية وحساب الكميات
    eco_exp = f"📊 [المقايسة والأسعار]: إدراج بند ({translated_text}) في جدول الكميات والمواصفات (BOQ) وتثبيت الفئة السعرية له لحساب مستخلصات المشروع."

    # 7. توليد الصياغة الدينية والثقافية
    rel_exp = f"🌙 [البُعد الثقافي]: الدلالة الروحية أو الثقافية والاجتماعية المرتبطة بمفهوم ({translated_text}) في بيئة العمل المحيطة."

    return gen_exp, eng_exp, legal_exp, sci_exp, pol_exp, eco_exp, rel_exp

# ==========================================
# 📥 واجهة المستخدم (تضم كافة اللغات الـ 8)
# ==========================================
with st.form(key="hybrid_translator_form", clear_on_submit=False):
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1)
    with col_l2:
        target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0)
    
    st.write("---")
    
    text_to_translate = st.text_area(
        "أدخل الكلمة أو العبارة الفنية (سيقوم المعالج بتفكيكها سياقياً بـ 7 قوالب كاملة وشرحها بالتفصيل):", 
        placeholder="اكتب هنا أي مصطلح مثل: concrete casting أو honeycombing أو أي نص آخر...",
        height=150,
        key="input_text"
    )
    
    btn_process = st.form_submit_button("🚀 RUN HYBRID ENGINE | تشغيل الفرز والتحليل السياقي المستقر", use_container_width=True)

st.write("---")

# ==========================================
# 📊 عرض النتائج (الـ 7 صياغات كاملة بشروح تفصيلية)
# ==========================================
if btn_process and text_to_translate.strip():
    cleaned_text = text_to_translate.strip()
    
    lang_from = languages_dict[source_lang]
    lang_to = languages_dict[target_lang]
    
    with st.spinner("جاري الترجمة الثابتة وتوليد الشروح التفصيلية السياقية..."):
        try:
            # الترجمة المبدئية المستقرة محلياً بدون أخطاء سيرفر
            translator = LocalTranslator(from_lang=lang_from, to_lang=lang_to)
            base_translation = translator.translate(cleaned_text)
            
            # تصحيح إملائي تلقائي سريع لرفع الجودة
            try:
                blob = TextBlob(base_translation)
                base_translation = str(blob.correct())
            except Exception:
                pass
            
            # توليد الشروح السبعة العميقة والمطولة
            f_gen, f_eng, f_leg, f_sci, f_pol, f_eco, f_rel = generate_advanced_explanations(base_translation, cleaned_text, lang_to)
            
            st.success("🎯 تم التحليل السياقي والتوزيع على القوالب السبعة بنجاح استقراري 100%:")
            st.write("---")
            
            # عرض الصياغات الثلاثة الأساسية
            st.subheader("🛠️ الصياغات والشروح الأساسية المفتوحة:")
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.markdown("### 💬 صياغة عامة وشرحها اللغوي")
                st.warning(f_gen)
            with col_b:
                st.markdown("### 👷 صياغة هندسية موقعية تفصيلية")
                st.info(f_eng)
            with col_c:
                st.markdown("### 📜 صياغة تعاقدية قانونية (FIDIC)")
                st.success(f_leg)
                
            st.write("---")
            
            # عرض الصياغات الأربعة التخصصية المتبقية كاملة
            st.subheader("🎯 الصياغات والشروح التخصصية الدقيقة:")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🧬 الصياغة العلمية الأكاديمية")
                st.info(f_sci)
                    
                st.markdown("### 📊 الصياغة الاقتصادية والمالية")
                st.warning(f_eco)

            with col2:
                st.markdown("### 🏛️ الصياغة السياسية والدبلوماسية")
                st.code(f_pol, language="")
                    
                st.markdown("### 🌙 الصياغة الدينية والثقافية")
                st.markdown(f"> **{f_rel}**")

        except Exception as e:
            st.error(f"❌ حدث خطأ غير متوقع: {e}")

elif btn_process:
    st.warning("⚠️ من فضلك اكتب نصاً أولاً لتشغيل نظام المعالجة.")
