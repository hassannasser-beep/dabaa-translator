import streamlit as st
from deep_translator import GoogleTranslator
from github import Github
import json

# 1. إعدادات الصفحة والعنوان
st.set_page_config(page_title="HASSAN NASSER Translator", page_icon="🏗️", layout="wide")

st.title("🏗️ مترجم المهندس HASSAN NASSER المركزي الدائم")
st.markdown("### نظام الترجمة الفورية المركزي المحمي والمربوط بقاعدة بيانات GitHub للأبد")
st.write("---")

# لغات النظام
languages_dict = {
    "العربية": "ar", "الإنجليزية (English)": "en", "الروسية (Русский)": "ru",
    "الكورية (한국어)": "ko", "الصينية (中文)": "zh"
}

# 🔒 كلمة المرور الخاصة بك للتعديل من الشاشة
ADMIN_PASSWORD = "1992002" 

# 🔑 وضع الرموز السرية داخل الكود مباشرة (الحل البديل والمضمون)
GITHUB_TOKEN = "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"
REPO_NAME = "hassannasser-beep/dabaa-translator"

DB_FILE = "glossary_db.json"

# دالة لجلب البيانات من ملف JSON في جيت هاب
@st.cache_data(ttl=2) # تحديث فوري كل ثانيتين لضمان رؤية الجميع للتعديلات فوراً
def load_permanent_glossary():
    default_data = [
        {"from_lang": "en", "to_lang": "ar", "word": "handover", "translation": "تسليم المواد لشركة دايسون"},
        {"from_lang": "en", "to_lang": "ar", "word": "scrap", "translation": "المخلفات والسكراب التالف"}
    ]
    if GITHUB_TOKEN == "ضع_الرمز_الذي_يبدأ_بـ_ghp_هنا_داخل_الاقتباس":
        return default_data
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(REPO_NAME)
        file_content = repo.get_contents(DB_FILE)
        return json.loads(file_content.decoded_content.decode("utf-8"))
    except:
        return default_data

# دالة لحفظ وتحديث الملف مباشرة في جيت هاب أونلاين
def save_permanent_glossary(data_list):
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(REPO_NAME)
        try:
            file_content = repo.get_contents(DB_FILE)
            repo.update_file(DB_FILE, "تحديث القاموس بواسطة المهندس حسن", json.dumps(data_list, ensure_ascii=False, indent=4), file_content.sha)
        except:
            repo.create_file(DB_FILE, "إنشاء قاعدة بيانات القاموس لأول مرة", json.dumps(data_list, ensure_ascii=False, indent=4))
        st.cache_data.clear()
    except Exception as e:
        st.error(f"خطأ في الاتصال بقاعدة بيانات جيت هاب: {e}")

# تحميل الكلمات الحالية
global_dict = load_permanent_glossary()

# تصميم الواجهة (تقسيم الشاشة)
col_left, col_right = st.columns([2, 1])

# 👈 الجزء الأيسر: المترجم للجميع (يظهر الصحيح للباقيين دائمًا)
with col_left:
    st.subheader("🌐 قسم الترجمة الفورية الذكي")
    c1, c2 = st.columns(2)
    with c1: source_lang = st.selectbox("من لغة:", list(languages_dict.keys()), index=1)
    with c2: target_lang = st.selectbox("إلى لغة:", list(languages_dict.keys()), index=0)
        
    text_to_translate = st.text_area("اكتب النص أو الكلمة هنا للفحص والترجمة:", height=100)
    
    if st.button("✨ ترجم الآن", type="primary"):
        if text_to_translate.strip() != "":
            src_code = languages_dict[source_lang]
            tgt_code = languages_dict[target_lang]
            search_word = text_to_translate.strip().lower()
            
            # فحص قاعدة البيانات الدائمة
            found_translation = None
            for item in global_dict:
                if item["from_lang"] == src_code and item["to_lang"] == tgt_code and item["word"] == search_word:
                    found_translation = item["translation"]
                    break
            
            if found_translation:
                st.info("💡 تم استخدام الترجمة الدائمة المعتمدة من المهندس حسن:")
                st.subheader(found_translation)
            else:
                with st.spinner("جاري الترجمة العالمية..."):
                    try:
                        translated = GoogleTranslator(source=src_code, target=tgt_code).translate(text_to_translate)
                        st.success("📝 النتيجة:")
                        st.subheader(translated)
                    except Exception as e: st.error(f"حدث خطأ: {e}")

# 👉 الجزء الأيمن: لوحة تحكم حسن ناصر (أنت فقط تعدل وتمسح وتُحفظ للأبد)
with col_right:
    st.subheader("🔒 لوحة الإدارة والتعديل الدائم")
    password_input = st.text_input("أدخل كلمة مرور المسؤول للتعديل أو المسح المستمر:", type="password")
    
    if password_input == ADMIN_PASSWORD:
        st.success("🔓 صلاحيات المسؤول نشطة. أي تعديل سيُحفظ في قاعدة البيانات فوراً!")
        st.write("---")
        st.markdown("#### 📥 إضافة مصطلح جديد")
        
        add_src = st.selectbox("لغة الكلمة الأصلية:", list(languages_dict.keys()), key="add_src")
        add_tgt = st.selectbox("لغة الترجمة المعتمدة:", list(languages_dict.keys()), key="add_tgt")
        word_in = st.text_input("الكلمة الأصلية:")
        trans_in = st.text_input("الترجمة الصحيحة:")
        
        if st.button("📥 حفظ وتعميم للأبد"):
            if word_in.strip() != "" and trans_in.strip() != "":
                global_dict.append({
                    "from_lang": languages_dict[add_src], "to_lang": languages_dict[add_tgt],
                    "word": word_in.strip().lower(), "translation": trans_in.strip()
                })
                save_permanent_glossary(global_dict) # الحفظ الفوري المباشر في جيت هاب
                st.success("✅ تم حفظ الكلمة في جيت هاب وتعميمها بشكل دائم!")
                st.rerun()
            else: st.error("⚠️ يرجى ملء البيانات.")
                
        st.write("---")
        st.markdown("#### 🗑️ إدارة ومسح الكلمات الحالية")
        for index, item in enumerate(global_dict):
            f_name = [k for k, v in languages_dict.items() if v == item["from_lang"]][0]
            t_name = [k for k, v in languages_dict.items() if v == item["to_lang"]][0]
            
            c_word, c_btn = st.columns([3, 1])
            c_word.write(f"🔹 **{item['word']}** ({f_name}) ➔ {item['translation']} ({t_name})")
            
            if c_btn.button("🗑️ مسح", key=f"del_{index}"):
                global_dict.pop(index)
                save_permanent_glossary(global_dict) # تحديث الحذف في جيت هاب فورًا
                st.success("تم المسح نهائياً!")
                st.rerun()
    elif password_input != "":
        st.error("❌ كلمة المرور خاطئة!")
    else:
        st.info("💡 هذه اللوحة مغلقة. التعديلات والمسح متاحة للمسؤول فقط عبر كلمة السر.")
        
    if password_input != ADMIN_PASSWORD:
        st.write("---")
        with st.expander("📖 استعراض القاموس الفني المعتمد حالياً"):
            for item in global_dict:
                f_name = [k for k, v in languages_dict.items() if v == item["from_lang"]][0]
                t_name = [k for k, v in languages_dict.items() if v == item["to_lang"]][0]
                st.write(f"🔹 **{item['word']}** ({f_name}) ➔ {item['translation']} ({t_name})")
