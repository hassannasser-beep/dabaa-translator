import streamlit as st
import google.generativeai as genai

# 1. إعدادات الصفحة والعنوان باسمك
st.set_page_config(page_title="HASSAN NASSER AI Translator", page_icon="🤖", layout="centered")

st.title("🤖 مترجم  HASSAN NASSER بذكاء Gemini")
st.markdown("### أداة سريعة ومباشرة لترجمة المصطلحات الهندسية والمحادثات")
st.write("---")

# 2. قائمة اللغات المتاحة في القوائم الجاهزة
languages_dict = {
    "العربية": "Arabic", "الإنجليزية (English)": "English", 
    "الروسية (Русский)": "Russian", "الكورية (한국어)": "Korean", "الصينية (中文)": "Chinese"
}

# 🔑 ضع مفتاح جيميناي الخاص بك هنا بين علامات الاقتباس
GEMINI_API_KEY = "ضع_هنا_مفتاح_جيميني_السري_API_KEY"

if GEMINI_API_KEY and GEMINI_API_KEY != "ضع_هنا_مفتاح_جيميني_السري_API_KEY":
    genai.configure(api_key=GEMINI_API_KEY)

# 3. تصميم واجهة الاختيار (قوائم جاهزة بجانب بعضها)
col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("ترجم من لغة:", list(languages_dict.keys()), index=1) # الافتراضي إنجليزي
with col2:
    target_lang = st.selectbox("إلى لغة:", list(languages_dict.keys()), index=0) # الافتراضي عربي

st.write("---")

# 4. صندوق إدخال النص وزر الترجمة
text_to_translate = st.text_area("اكتب أو الصق النص هنا:", placeholder="Type your text or engineering terms here...")

if st.button("✨ ترجم الآن عبر الذكاء الاصطناعي", type="primary"):
    if text_to_translate.strip() == "":
        st.warning("⚠️ من فضلك اكتب نصاً أولاً ليتمكن البرنامج من ترجمته.")
    else:
        with st.spinner("جاري الترجمة الذكية عبر Gemini..."):
            try:
                # استدعاء نموذج جيميناي للترجمة الاحترافية بالسياق الهندسي
                model = genai.GenerativeModel("gemini-1.5-flash")
                prompt = f"You are an expert engineer and professional translator. Translate this text from {languages_dict[source_lang]} to {languages_dict[target_lang]}. Provide ONLY the clear translation without any extra comments, introduction or notes:\n\n{text_to_translate}"
                response = model.generate_content(prompt)
                
                # عرض النتيجة فوراً على الشاشة في صندوق مجهز وجميل
                st.success("📝 الترجمة الاحترافية:")
                st.subheader(response.text.strip())
                
            except Exception as e:
                st.error(f"حدث خطأ أثناء الاتصال بـ Gemini: {e}\nتأكد من كتابة الـ API KEY بشكل صحيح في الكود.")
