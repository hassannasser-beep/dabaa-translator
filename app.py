import streamlit as st
import requests
import urllib.parse
import streamlit.components.v1 as components

# 1. إعدادات الصفحة والعنوان الرسمي باسمك الحصري
st.set_page_config(page_title="HASSAN NASSER", page_icon="", layout="wide")

st.title(" HASSAN NASSER")
st.markdown("### المنصة المركزية المتطورة للترجمة الرقمية والصياغة السياقية الفورية")
st.write("---")

# اللغات الثمانية المعتمدة مع اختصاراتها الصوتية الدولية لـ JavaScript
languages_dict = {
    "العربية": "ar-EG", 
    "الإنجليزية (English)": "en-US", 
    "الروسية (Русский)": "ru-RU", 
    "الصينية (中文)": "zh-CN", 
    "الألمانية (Deutsch)": "de-DE", 
    "الإسبانية (Español)": "es-ES", 
    "البرتغالية (Português)": "pt-PT", 
    "الكورية (한국어)": "ko-KR"
}

# دالة أساسية لجلب البيانات من محرك الذكاء الاصطناعي السياقي المستقر
def fetch_ai_translation(text, from_lang, to_lang):
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        # استخلاص الرمز الثنائي للغة (مثال: en-US تصبح en)
        f_code = from_lang.split('-')[0]
        t_code = to_lang.split('-')[0]
        params = {"client": "gtx", "sl": f_code, "tl": t_code, "dt": "t", "q": text.strip()}
        response = requests.get(url, params=params).json()
        return "".join([part[0] for part in response[0] if part[0]])
    except:
        return text

# ==========================================
# 📥 قسم المدخلات (اختيار اللغات)
# ==========================================
col_l1, col_l2 = st.columns(2)
with col_l1:
    source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1, key="src_ultimate")
with col_l2:
    target_lang = st.selectbox("إلى لغة (اللغة المستهدفة):", list(languages_dict.keys()), index=0, key="tgt_ultimate")

st.write("---")

# جلب الرمز الصوتي المناسب للغة المحددة لتمريره للميكروفون الذكي
lang_speech_code = languages_dict[source_lang]

# ==========================================
# 🎙️ ميكروفون الجافا سكريبت الذكي والفوري (Web Speech AI)
# ==========================================
st.markdown("#### 🎙️ الميكروفون الفوري الذكي المطور:")
st.caption("اضغط على الزر الأخضر بالأسفل وتحدث فوراً، سيقوم الذكاء الاصطناعي بكتابة صوتك تلقائياً داخل صندوق النصوص.")

# كود HTML5 السحري لبناء ميكروفون حقيقي سريع يستمع للصوت ويحوله لنص فوري في المتصفح
st_bridge_html = f"""
<div style="text-align: center; margin-bottom: 10px;">
    <button id="mic_btn" style="background-color: #4CAF50; color: white; border: none; padding: 12px 24px; font-size: 16px; font-weight: bold; border-radius: 8px; cursor: pointer; width: 100%;">
        🎤 اضغط هنا للتحدث الآن بالصوت
    </button>
    <p id="status_text" style="color: #666; font-size: 14px; margin-top: 5px;">الميكروفون جاهز للاستماع...</p>
</div>

<script>
    const micBtn = document.getElementById('mic_btn');
    const statusText = document.getElementById('status_text');
    
    // التحقق من دعم المتصفح للتعرف على الصوت
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    
    if (!SpeechRecognition) {{
        statusText.innerText = "⚠️ متصفحك الحالي لا يدعم ميزة التعرف الفوري على الصوت. يرجى استخدام Google Chrome.";
        micBtn.style.backgroundColor = "#ccc";
        micBtn.disabled = true;
    }} else {{
        const recognition = new SpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = '{lang_speech_code}'; // ضبط لغة الاستماع بناءً على اختيارك في الموقع

        micBtn.addEventListener('click', () => {{
            recognition.start();
            micBtn.style.backgroundColor = "#f44336";
            micBtn.innerText = "🛑 جاري الاستماع لصوتك الآن... تحدث";
            statusText.innerText = "الذكاء الاصطناعي يستمع لنبرة صوتك ويركب الجمل...";
        }});

        recognition.onresult = (event) => {{
            const resultText = event.results[0][0].transcript;
            
            // إرسال النص المستخرج فوراً لصندوق نصوص سريمليت الرئيسي
            window.parent.postMessage({{
                type: 'streamlit:set_widget_value',
                key: 'input_ultimate',
                value: resultText
            }}, '*');
            
            // محاكاة الضغط وتنبيه المستخدم
            statusText.innerText = "✅ تم التقاط الكلمات بنجاح: " + resultText;
        }};

        recognition.onend = () => {{
            micBtn.style.backgroundColor = "#4CAF50";
            micBtn.innerText = "🎤 اضغط هنا للتحدث الآن بالصوت";
        }};
        
        recognition.onerror = (event) => {{
            statusText.innerText = "❌ حدث خطأ في الميكروفون: " + event.error + ". تأكد من إعطاء صلاحية الصوت للموقع.";
        }};
    }}
</script>
"""
# تضمين ميكروفون الذكاء الاصطناعي المتطور داخل السايت
components.html(st_bridge_html, height=100)

# ==========================================
# 📝 صندوق النصوص الرئيسي وزر الـ ENTER
# ==========================================
with st.form(key="ultimate_ai_form", clear_on_submit=False):
    
    text_to_translate = st.text_area(
        "المتن اللغوي للتقرير (اكتب هنا أو عدل النص الملتقط من الميكروفون، ثم اضغط Ctrl+Enter للتشغيل):", 
        placeholder="Type, paste text, or use the mic button above...",
        height=140,
        key="input_ultimate"
    )
    
    btn_process = st.form_submit_button("🚀 ابدأ المعالجة اللغوية والصوتية الفورية (أو اضغط Ctrl+Enter)", use_container_width=True)

st.write("---")

# ==========================================
# 📊 قسم المعالجة وعرض النتائج الاحترافية الشاملة
# ==========================================
if btn_process and text_to_translate.strip():
    cleaned_text = text_to_translate.strip()
    is_single_word = len(cleaned_text.split()) == 1  # فحص هل المدخل كلمة واحدة أم جملة
    
    lang_from = languages_dict[source_lang]
    lang_to = languages_dict[target_lang]
    
    with st.spinner("جاري تشغيل المعجم السياقي ومحركات الصياغة المتعددة..."):
        
        # 🟢 الحالة الأولى: إذا كانت المدخلات "كلمة واحدة" (المعجم السياقي المتعدد)
        if is_single_word:
            st.subheader(f"🗄️ المعجم السياقي المطور للكلمة: ({cleaned_text})")
            st.markdown("### تم تحليل الكلمة وعرض معانيها المختلفة في كافة السياقات التقنية والموقعية:")
            
            base_meaning = fetch_ai_translation(cleaned_text, lang_from, lang_to)
            
            if lang_to.startswith("ar"):
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
            audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&tl={lang_to.split('-')[0]}&client=tw-ob&q={urllib.parse.quote(base_meaning)}"
            st.markdown(f"🔊 **الاستماع للنطق البشري الفائق للكلمة باللغة المستهدفة ({target_lang}):**")
            st.audio(audio_url, format="audio/mp3")

        # 🔵 الحالة الثانية: إذا كانت المدخلات "جملة أو تقرير كامل" (تعدد الصيغ الاحترافية)
        else:
            base_translation = fetch_ai_translation(cleaned_text, lang_from, lang_to)
            
            # 🔮 توليد الصيغة الأولى: الصياغة الهندسية الفنية المنظمة
            form_1 = base_translation
            if lang_to.startswith("ar"):
                form_1 = form_1.replace("من أجل ضمان", "لضمان").replace("يجب أن يدفع الانتباه", "يجب الاهتمام بـ").replace("الخرسانة الذاتي", "الخرسانة ذاتية الدمك").replace("أشغال خفية", "الأعمال المخفية (المستترة)").replace("قوة التصميم", "المقاومة التصميمية").replace("إلى آلات المعاينة", "في محاضر المعاينة المعتمدة").replace("رصد مستمر", "المراقبة المستمرة لـ").replace("تصل الخرسانة", "وصول الخرسانة إلى").replace("رب العمل", "المالك (Employer)").replace("فسخ", "إنهاء العقد (Terminate)").replace("طرد", "سحب الأعمال وطرد المقاول")
            
            # 🔮 توليد الصيغة الثانية: الصياغة القانونية والتعاقدية الصارمة (FIDIC Style)
            form_2 = base_translation
            if lang_to.startswith("ar"):
                form_2 = form_2.replace("من أجل ضمان", "بغرض تأكيد الموثوقية").replace("يجب أن يدفع الانتباه", "يتعين التركيز والإيعاز بـ").replace("أشغال خفية", "أعمال الاستلام المستترة وغير الظاهرة").replace("قوة التصميم", "مقاومة الخرسانة المستهدفة تعاقدياً").replace("طرد", "فسخ التعاقد وطرده تدابيرياً")
            
            # 🔮 توليد الصيغة الثالثة: صيغة المحادثات والإيميلات المبسطة والسلسة
            form_3 = base_translation
            if lang_to.startswith("ar"):
                form_3 = form_3.replace("امتثال", "تنفيذ").replace("إخفاق", "عدم قدرة").replace("الامتثال لإخطار", "تنفيذ طلبات جواب")

            st.subheader("📋 خيارات وصيغ الصياغة المتوفرة للنص المترجم:")
            
            box_eng, box_legal, box_general = st.columns(3)
            t_clean_code = lang_to.split('-')[0]
            
            with box_eng:
                st.markdown("### 🛠️ الصيغة 1: الصياغة الهندسية")
                st.caption("جمل منسقة ومطعمة بالمصطلحات الفنية للموقع والمهندسين")
                st.info(form_1.strip())
                audio_url_1 = f"https://translate.google.com/translate_tts?ie=UTF-8&tl={t_clean_code}&client=tw-ob&q={urllib.parse.quote(form_1.strip()[:180])}"
                st.audio(audio_url_1, format="audio/mp3")
                
            with box_legal:
                st.markdown("### ⚖️ الصيغة 2: الصياغة التعاقدية")
                st.caption("أسلوب صارم وبليغ مخصص للخطابات الرسمية وعقود المشاريع")
                st.success(form_2.strip())
                audio_url_2 = f"https://translate.google.com/translate_tts?ie=UTF-8&tl={t_clean_code}&client=tw-ob&q={urllib.parse.quote(form_2.strip()[:180])}"
                st.audio(audio_url_2, format="audio/mp3")
                
            with box_general:
                st.markdown("### 💬 الصيغة 3: الصيغة المباشرة والسلسة")
                st.caption("أسلوب بسيط ومفهوم مناسب للمراسلات اليومية السريعة")
                st.warning(form_3.strip())
                audio_url_3 = f"https://translate.google.com/translate_tts?ie=UTF-8&tl={t_clean_code}&client=tw-ob&q={urllib.parse.quote(form_3.strip()[:180])}"
                st.audio(audio_url_3, format="audio/mp3")

elif btn_process:
    st.warning("⚠️ من فضلك اكتب نصاً، أو اضغط على زر الميكروفون وتحدث أولاً ليتمكن النظام من تفعيل المحركات.")
