import streamlit as st

# 1. إعدادات الصفحة والعنوان الرسمي
st.set_page_config(page_title="HASSAN NASSER", page_icon="🤖", layout="wide")

st.title("🤖 HASSAN NASSER")
st.markdown("### 🧠 LOCAL CONTEXTUAL DICTIONARY | القاموس السياقي المدمج والمستقر 100%")
st.write("---")

# اللغات الثمانية كاملة ومطابقة لقاعدة البيانات
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

# 🗺️ قاعدة البيانات اليدوية الشاملة (8 لغات × 7 تخصصات لكل مصطلح استراتيجي)
dictionary_db = {
    "concrete casting": {
        "ar": {
            "general": "صب الخرسانة - عملية سكب المخلوط الخرساني في القالب المخصص.",
            "engineering": "أعمال الصب الموقعي - تشمل اختبار الهبوط (Slump Test)، وأخذ المكعبات، واستخدام الهزازات الميكانيكية لتفادي التعشيش.",
            "legal": "بند الصب تعاقدياً - يشترط توقيع محضر استلام حديد التسليح والنجارة (IR) من الاستشاري قبل بدء الصب رسمياً.",
            "scientific": "التفاعل الكيميائي الطارد للحرارة (Hydration) الناتجة عن إماهة جزيئات الإسمنت وتكوين روابط السليكات لرفع المقاومة.",
            "political": "البروتوكول الحكومي المعتمد لتنفيذ البنية التحتية والمشروعات القومية السيادية.",
            "economic": "بند مالي مدرج في مقايسة الأعمال (BOQ) يُحسب بالمتر المكعب ويشمل تكلفة المواد والمعدات والعمالة.",
            "religious": "الأمانة المهنية في نسب خلط المواد ومطابقة المعايير الهندسية دون غش أو تلاعب."
        },
        "en": {
            "general": "Concrete casting - The process of pouring concrete into molds.",
            "engineering": "Site placement of concrete including slump testing, cube sampling, and mechanical vibration to prevent voids.",
            "legal": "Casting item subject to structural inspection request (IR) approval prior to formal execution under FIDIC rules.",
            "scientific": "Exothermic chemical hydration process of cement particles forming calcium silicate hydrate (C-S-H) gel.",
            "political": "State-regulated infrastructure framework for major national development projects.",
            "economic": "Financial item in the Bill of Quantities (BOQ) priced per cubic meter including materials and logistics.",
            "religious": "Ethical compliance with material specification limits and standard engineering integrity."
        },
        "ru": {
            "general": "Заливка бетона - процесс укладки бетонной смеси в опалубку.",
            "engineering": "Укладка бетона на площадке, включая конус усадки, отбор проб и вибрирование для избежания каверн.",
            "legal": "Бетонирование регулируется актом освидетельствования скрытых работ (ИР) до начала заливки.",
            "scientific": "Экзотермический процесс гидратации цемента с образованием гидросиликата кальция для прочности.",
            "political": "Государственный регламент реализации стратегических инфраструктурных объектов.",
            "economic": "Финансовая позиция в ведомости объемов работ (BOQ), оцениваемая в кубических метрах.",
            "religious": "Профессиональная честность при соблюдении пропорций смеси и проектных стандартов."
        },
        "zh": {
            "general": "混凝土浇筑 - 将混凝土拌合物 Markets 浇入模具的过程。",
            "engineering": "现场混凝土施工，包括坍落度測試、試塊留置及機械振搗以防蜂窩麻面。",
            "legal": "根据FIDIC条款，浇筑项目在正式施工前须获得结构检验申请（IR）的批准。",
            "scientific": "水泥颗粒发生放热化学水化反应，形成水化硅酸钙（C-S-H）凝胶以达到设计强度。",
            "political": "国家重大基础设施与战略发展项目规范框架。",
            "economic": "工程量清单（BOQ）中的财务条目，按立方米计价，包含材料与物流成本。",
            "religious": "严格遵守材料配比与工程质量规范的职业道德要求。"
        },
        "de": {
            "general": "Betonieren - Das Gießen von Beton in Schalungen.",
            "engineering": "Einbau von Frischbeton vor Ort inklusive Setzmassprüfung, Würfelproben und Verdichtung mittels Rüttler.",
            "legal": "Betonierabschnitt erfordert die vorherige Abnahme der Bewehrung und Schalung durch den Bauüberwacher.",
            "scientific": "Exothermer Hydratationsprozess der Zementpartikel zur Bildung von Calciumsilicathydrat-Kristallen.",
            "political": "Staatliche Infrastrukturrichtlinien für strategische Großprojekte.",
            "economic": "Leistungsposition im Leistungsverzeichnis (LV), abgerechnet nach Kubikmeter inklusive Logistik.",
            "religious": "Berufliche Integrität bei der Einhaltung von Mischungsverhältnissen und Baunormen."
        },
        "es": {
            "general": "Vaciado de hormigón - El proceso de verter concreto en los moldes.",
            "engineering": "Colocación de concreto en sitio, incluyendo prueba de asentamiento, toma de probetas y vibrado mecánico.",
            "legal": "Ítem de vaciado sujeto a la aprobación de la solicitud de inspección (IR) antes de la ejecución.",
            "scientific": "Proceso químico exotérmico de hidratación del cemento que forma cristales de silicato de calcio.",
            "political": "Marco regulatorio estatal para el desarrollo de proyectos de infraestructura crítica.",
            "economic": "Partida financiera en el Catálogo de Conceptos (BOQ) cotizada por metro cúbico.",
            "religious": "Compromiso ético con el cumplimiento de las especificaciones técnicas sin fraude."
        },
        "pt": {
            "general": "Betonagem - O processo de lançamento do betão/concreto nas cofragens.",
            "engineering": "Colocação de concreto em obra, incluindo ensaio de abatimento, recolha de provetes e vibração mecânica.",
            "legal": "Item de betonagem sujeito à aprovação do pedido de inspeção (IR) antes do início dos trabalhos.",
            "scientific": "Processo químico exotérmico de hidratação do cimento, gerando ligações de silicato de cálcio.",
            "political": "Diretrizes estatais para a execução de obras públicas de infraestrutura estratégica.",
            "economic": "Item financeiro no Caderno de Encargos (BOQ) medido em metros cúbicos com insumos.",
            "religious": "Responsabilidade moral na conformidade dos traços de concreto e segurança estrutural."
        },
        "ko": {
            "general": "콘크리트 타설 - 거푸집에 콘크리트 혼합물을 붓는 과정.",
            "engineering": "슬럼프 테스트, 공시체 채취 및 재료분리 방지를 위한 기계식 진동기 사용을 포함한 현장 타설 작업.",
            "legal": "FIDIC 규정에 따라 실제 타설 전 감리단의 구조물 검사 요청서(IR) 승인이 필수적인 공종.",
            "scientific": "시멘트 입자의 수화 반응에 따른 발열 화학 공정으로, 규산칼슘 수화물(C-S-H) 겔 형성.",
            "political": "국가 주요 기간산업 및 국책 기반시설 검수 지침 법률.",
            "economic": "물량내역서(BOQ) 상의 금융 항목으로, 자재 및 장비 비용을 포함하여 루베(CBM)당 단가 산정.",
            "religious": "부실공사 방지 및 구조적 안전성 확보를 위한 현장 엔지니어의 직업적 양심과 청렴성."
        }
    },
    "honeycombing": {
        "ar": {
            "general": "تعشيش الخرسانة - وجود فراغات هوائية وحصوات ظاهرة في القطاع الإنشائي.",
            "engineering": "عيب تنفيذي ينتج عن ضعف الدمك أو كثافة التسليح، ويتطلب المعالجة بمواد إيبوكسية غير قابلة للانكماش (Grout).",
            "legal": "مخالفة للمواصفات تستوجب إيقاف البند وإلزام المقاول بتقديم تقرير طريقة إصلاح معتمد (Method Statement).",
            "scientific": "انفصال حبيبي (Segregation) يؤدي إلى خفض مساحة القطاع الفعالة المقاومة للإجهادات ويسرع صدأ الحديد.",
            "political": "ملف رقابي حكومي يخص جودة وأمان المنشآت الوطنية الحيوية.",
            "economic": "خسارة مالية للمقاول تشمل تكلفة مواد الترميم التخصصية وأجور العمالة الإضافية دون تعويض.",
            "religious": "ضرورة اتقان العمل لمنع العيوب الخفية التي قد تهدد سلامة وأرواح مستخدمي المبنى."
        },
        "en": {
            "general": "Honeycombing - Voids and empty spaces in concrete face showing coarse aggregate.",
            "engineering": "Defect caused by poor compaction or congested rebar, requiring repair with non-shrink high-strength grout.",
            "legal": "Non-conformance report (NCR) issued under contract terms, forcing the contractor to submit a repair method statement.",
            "scientific": "Particle segregation reducing the effective cross-sectional area and causing early carbonation or rebar corrosion.",
            "political": "Regulatory oversight parameter for public safety and governmental infrastructure quality assurance.",
            "economic": "Financial loss for the contractor due to uncompensated remedial works and specialized repair material costs.",
            "religious": "Professional accountability regarding hidden defects that might compromise human structural safety."
        },
        "ru": {
            "general": "Раковины в бетоне (соты) - пустоты и обнажение крупного заполнителя на поверхности.",
            "engineering": "Дефект из-за плохой вибрации или густой арматуры, требующий ремонта безусадочным составом.",
            "legal": "Акт о несоответствии (NCR), обязывающий подрядчика предоставить утвержденный метод устранения дефекта.",
            "scientific": "Сегрегация смеси, снижающая эффективное сечение элемента и ускоряющая коррозию арматуры.",
            "political": "Критерий государственного строительного надзора за безопасностью ядерных и гражданских объектов.",
            "economic": "Прямые убытки подрядчика на исправление брака и закупку специализированных ремонтных смесей.",
            "religious": "Профессиональный долг по недопущению скрытых дефектов, угрожающих жизни людей."
        },
        "zh": {
            "general": "混凝土蜂窝 - 混凝土表面出现砂浆少、石子多, 石子间有空隙的现象。",
            "engineering": "因振捣不足或钢筋过密引起的缺陷，需使用无收缩高强灌浆料进行修补。",
            "legal": "合同条款下的不合格报告（NCR），强制承包商提交书面修补施工方案（Method Statement）。",
            "scientific": "骨料离析现象，降低了结构构件的有效截面积，加速了主筋碳化与锈蚀进程。",
            "political": "政府对公共安全及国家战略基础设施质量监督的核心控制要点。",
            "economic": "承包商因非补偿性返工及采购特种修补材料而承担的直接经济损失。",
            "religious": "杜绝工程隐患、保障生命安全的职业良心与建筑质量操守。"
        },
        "de": {
            "general": "Kiesnester - Hohlräume im Beton durch fehlenden Zementleim.",
            "engineering": "Ausführungsfehler infolge mangelnder Verdichtung, Reparatur mittels quellfähigem Vergussmörtel erforderlich.",
            "legal": "Mängelrüge (NCR) nach VOB/FIDIC, Verpflichtung des Auftragnehmers zur Sanierung auf eigene Kosten.",
            "scientific": "Entmischung des Korns, verringert den tragenden Querschnitt und begünstigt Korrosion der Bewehrung.",
            "political": "G
