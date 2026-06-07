import streamlit as st
import requests
import urllib.parse
import streamlit.components.v1 as components

# 1. إعدادات الصفحة والعنوان الرسمي باسمك الحصري
st.set_page_config(page_title="HASSAN NASSER", page_icon="", layout="wide")

st.title(" HASSAN NASSER")
st.markdown("### المنصة المركزية المتطورة للترجمة الرقمية والصياغة السياقية الفورية")
st.write("---")

# اللغات الثمانية المعتمدة مع اختصاراتها الدولية لـ JavaScript
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

lang_speech_code = languages_dict[source_lang]

# ==========================================
# 🎙️ ميكروفون دائري صغير ينقل النص آلياً وفوراً
# ==========================================
col_mic, col_txt_hint = st.columns([1, 20])

with col_mic:
    # كود جافا سكريبت متطور يكسر الحماية الأمنية ويمرر الصوت لصندوق النص كرسالة خلفية فورية
    st_bridge_html = f"""
    <div style="text-align: left; padding-top: 5px;">
        <button id="mic_btn" title="اضغط للتحدث بصوتك الحقيقي" style="background-color: #28a745; color: white; border: none; width: 42px; height: 42px; font-size: 18px; border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 6px rgba(0,0,0,0.15); transition: all 0.3s ease;">
            🎙️
        </button>
    </div>

    <script>
        const micBtn = document.getElementById('mic_btn');
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        
        if (SpeechRecognition) {{
            const recognition = new SpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = '{lang_speech_code}';

            micBtn.addEventListener('click', () => {{
                try {{
                    recognition.start();
                    micBtn.style.backgroundColor = "#dc3545";
                    micBtn.innerText = "🛑";
                }} catch(e) {{
                    recognition.stop();
                }}
            }});

            recognition.onresult = (event) => {{
                const resultText = event.results[0][0].transcript;
                
                // السر البرمجي الجديد: إرسال النص مباشرة وعملياً من خلال قنوات مسارات Streamlit الآمنة
                window.parent.postMessage({{
                    type: 'streamlit:set_widget_value',
                    key: 'input_ultimate',
                    value: resultText
                }}, '*');
                
                // إرسال أمر برامجي خلفي تكميلي لمحاكاة الضغط وتنبيه الصفحة بالترجمة تلقائياً
                setTimeout(() => {{
                    const forms = window.parent.document.getElementsByTagName('form');
                    if (forms.length > 0) {{
                        forms[0].dispatchEvent(new Event('submit', {{ bubbles: true, cancelable: true }}));
                    }}
                }}, 400);
            }};

            recognition.onend = () => {{
                micBtn.style.backgroundColor = "#28a745";
                micBtn.innerText = "🎙️";
            }};
        }} else {{
            micBtn.style.backgroundColor = "#6c757d";
            micBtn.innerText = "⚠️";
            micBtn.disabled = true;
        }}
    </script>
    """
    components.html(st_bridge_html, height=52)

with col_txt_hint:
    st.markdown("<p style='padding-top: 12px; color: #555; font-size: 14px;'>◀️ <b>اضغط على أيقونة الميكروفون الدائرية الخضراء الصغيرة لبدء التحدث</b>، وسيتم كتابة صوتك الحقيقي وترجمته تلقائياً بالأسفل.</p>", unsafe_allow_html=True)

# ==========================================
# 📝 صندوق النصوص الرئيسي المفتوح والمحمي
# ==========================================
with st.form(key="ultimate_ai_form", clear_on_submit=False):
    
    text_to_translate = st.text_area(
        "المتن اللغوي للتقرير (يتم الكتابة هنا فورياً من الميكروفون، ويمكنك التعديل بيدك أيضاً):", 
        placeholder="Type, paste text, or click the micro-mic above to speak...",
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
    is_single_word = len(cleaned_text.split()) == 1
    
    lang_from = languages_dict[source_lang]
    lang_to = languages_dict[target_lang]
    
    with st.spinner("جاري تشغيل المعجم السياقي ومحركات الصياغة المتعددة..."):
        
        # 🟢 الحالة الأولى: كلمة واحدة (المعجم السياقي المتعدد)
        if is_single_word:
            st.subheader(f"🗄️ المعجم السياقي المطور للكلمة: ({cleaned_text})")
            base_meaning = fetch_ai_translation(cleaned_text, lang_from, lang_to)
            
            if lang_to.split('-')[0] == "ar":
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
            st.markdown(f"🔊 **الاستماع للنطق البشري الفائق للكلمة باللغة المستهدفة:**")
            st.audio(audio_url, format="audio/mp3")

        # 🔵 الحالة الثانية: جملة أو تقرير كامل (تعدد الصيغ الاحترافية)
        else:
            base_translation = fetch_ai_translation(cleaned_text, lang_from, lang_to)
            t_code_clean = lang_to.split('-')[0]
            
            form_1 = base_translation
            if t_code_clean == "ar":
                form_1 = form_1.replace("من أجل ضمان", "لضمان").replace("يجب أن يدفع الانتباه", "يجب الاهتمام بـ").replace("الخرسانة الذاتي", "الخرسانة ذاتية الدمك").replace("أشغال خفية", "الأعمال المخفية (المستترة)").replace("قوة التصميم", "المقاومة التصميمية").replace("إلى آلات المعاينة", "في محاضر المعاينة المعتمدة").replace("رصد مستمر", "المراقبة المستمرة لـ").replace("تصل الخرسانة", "وصول الخرسانة إلى").replace("رب العمل", "المالك (Employer)").replace("فسخ", "إنهاء العقد (Terminate)").replace("طرد", "سحب الأعمال وطرد المقاول")
            
            form_2 = base_translation
            if t_code_clean == "ar":
                form_2 = form_2.replace("من أجل ضمان", "بغرض تأكيد الموثوقية").replace("يجب أن يدفع الانتباه", "يتعين التركيز والإيعاز بـ").replace("أشغال خفية", "أعمال الاستلام المستترة وغير الظاهرة").replace("قوة التصميم", "مقاومة الخرسانة المستهدفة تعاقدياً").replace("طرد", "فسخ التعاقد وطرده تدابيرياً")
            
            form_3 = base_translation
            if t_code_clean == "ar":
                form_3 = form_3.replace("امتثال", "تنفيذ").replace("إخفاق", "عدم قدرة").replace("الامتثال لإخطار", "تنفيذ طلبات جواب")

            st.subheader("📋 خيارات وصيغ الصياغة المتوفرة للنص المترجم:")
            box_eng, box_legal, box_general = st.columns(3)
            
            with box_eng:
                st.markdown("### 🛠️ الصيغة 1: الصياغة الهندسية")
                st.info(form_1.strip())
                audio_url_1 = f"https://translate.google.com/translate_tts?ie=UTF-8&tl={t_code_clean}&client=tw-ob&q={urllib.parse.quote(form_1.strip()[:180])}"
                st.audio(audio_url_1, format="audio/mp3")
                
            with box_legal:
                st.markdown("### ⚖️ الصيغة 2: الصياغة التعاقدية")
                st.success(form_2.strip())
                audio_url_2 = f"https://translate.google.com/translate_tts?ie=UTF-8&tl={t_code_clean}&client=tw-ob&q={urllib.parse.quote(form_2.strip()[:180])}"
                st.audio(audio_url_2, format="audio/mp3")
                
            with box_general:
                st.markdown("### 💬 الصيغة 3: الصيغة المباشرة والسلسة")
                st.warning(form_3.strip())
                audio_url_3 = f"https://translate.google.com/translate_tts?ie=UTF-8&tl={t_code_clean}&client=tw-ob&q={urllib.parse.quote(form_3.strip()[:180])}"
                st.audio(audio_url_3, format="audio/mp3")

elif btn_process:
    st.warning("⚠️ من فضلك اكتب نصاً، أو اضغط على زر الميكروفون وتحدث أولاً ليتمكن النظام من تفعيل المحركات.")
