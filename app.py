```python
import streamlit as st
import requests

# ==========================================
# تحسين الترجمة مع التخزين المؤقت Cache
# ==========================================
@st.cache_data(ttl=3600)
def fetch_ai_translation(text, from_lang, to_lang):
    try:
        url = "https://translate.googleapis.com/translate_a/single"

        params = {
            "client": "gtx",
            "sl": from_lang,
            "tl": to_lang,
            "dt": "t",
            "q": text.strip()
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return "".join(
            part[0]
            for part in data[0]
            if part[0]
        )

    except requests.exceptions.RequestException as e:
        st.error(f"Translation API Error: {e}")
        return text

    except Exception as e:
        st.error(f"Unexpected Error: {e}")
        return text


# ==========================================
# قاعدة المصطلحات بعد تصحيح الأخطاء النصية
# ==========================================
site_slang_db = {

    "slab": {
        "academic": "بلاطة",
        "slang": "سقف / فرش خرساني",
        "desc": "تُطلق في المواقع على الأسقف والمسطحات الخرسانية المسلحة."
    },

    "lean concrete": {
        "academic": "خرسانة عجيفة / ضعيفة",
        "slang": "خرسانة عادية / خرسانة نظافة",
        "desc": "الطبقة الخرسانية غير المسلحة التي تُصب أسفل القواعد لحماية الحديد والأساسات."
    },

    "shop drawings": {
        "academic": "رسومات المتجر",
        "slang": "الرسومات التنفيذية للموقع",
        "desc": "المخططات التفصيلية المعتمدة للبدء في التنفيذ الفعلي بالموقع."
    },

    "as-built drawings": {
        "academic": "رسومات كما بُنيت",
        "slang": "مخططات الواقع الفعلي للمشروع",
        "desc": "الرسومات النهائية التي تعكس ما تم تنفيذه على أرض الواقع بدقة."
    },

    "bill of quantities": {
        "academic": "فاتورة الكميات",
        "slang": "جدول الكميات والمواصفات (BOQ)",
        "desc": "الوثيقة الأساسية لتسعير وحساب كميات المشروع."
    },

    "shuttering": {
        "academic": "إغلاق",
        "slang": "الشدّة الخشبية / الطوبار",
        "desc": "الهيكل المؤقت الذي يُصب بداخله الخرسانة المسلحة لحين تماسكها."
    },

    "scaffolding": {
        "academic": "أشغال السقالة",
        "slang": "السقالات الإنشائية",
        "desc": "الهياكل المعدنية التي يستخدمها العمال لتنفيذ الأعمال المرتفعة."
    },

    "curing": {
        "academic": "معالجة",
        "slang": "رش الخرسانة بالمياه",
        "desc": "الحفاظ على رطوبة الخرسانة لاكتساب المقاومة المطلوبة."
    },

    "honeycombing": {
        "academic": "تعتشيق النحل",
        "slang": "تعشيش الخرسانة",
        "desc": "الفراغات الحصوية التي تظهر في الخرسانة نتيجة ضعف الدمك."
    },

    "kick-off meeting": {
        "academic": "اجتماع البداية",
        "slang": "الاجتماع التحضيري للمشروع",
        "desc": "أول اجتماع رسمي بين المالك والاستشاري والمقاول."
    },

    "variation order": {
        "academic": "أمر تغيير",
        "slang": "VO",
        "desc": "أمر رسمي لتعديل أو إضافة أعمال خارج نطاق العقد الأصلي."
    }
}


# ==========================================
# Levenshtein Distance
# ==========================================
def calculate_distance(s1, s2):

    if len(s1) < len(s2):
        return calculate_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)

    for i, c1 in enumerate(s1):

        current_row = [i + 1]

        for j, c2 in enumerate(s2):

            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)

            current_row.append(
                min(insertions, deletions, substitutions)
            )

        previous_row = current_row

    return previous_row[-1]


# ==========================================
# تحسين اكتشاف الأخطاء للمصطلحات المفردة والمركبة
# ==========================================
def check_do_you_mean(text):

    text = text.lower()

    suggestions = []

    tokens = text.split()

    candidates = []

    candidates.extend(tokens)

    for i in range(len(tokens) - 1):
        candidates.append(
            tokens[i] + " " + tokens[i + 1]
        )

    for phrase in candidates:

        if len(phrase) < 3:
            continue

        for correct_term in site_slang_db.keys():

            dist = calculate_distance(
                phrase,
                correct_term.lower()
            )

            if dist == 1 or (
                len(correct_term) > 6 and dist <= 2
            ):

                if correct_term not in suggestions:
                    suggestions.append(correct_term)

    return suggestions


# ==========================================
# رصد مصطلحات الموقع
# ==========================================
def detect_site_slang(text):

    detected = []

    text_lower = text.lower()

    for key, data in site_slang_db.items():

        if key in text_lower:

            detected.append({
                "term": key.title(),
                "academic": data["academic"],
                "slang": data["slang"],
                "desc": data["desc"]
            })

    return detected
```
