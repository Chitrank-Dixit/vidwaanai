# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vaivtpuran 265.5157)
- **Original**: रत्केयूरवलयां रत्रमजीररज़िताम्‌ । रत्रकुण्डलयुग्मेव. विचित्रेण.. विराजिताम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 265.5158)
- **Original**: सूर्यप्रभाप्रतिकृतिगण्डस्थलविराजिताम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 265.5159)
- **Original**: अमूल्यरब्रनिर्माणग्रैवेयकविभूषिताम्‌ । सद्रब्नसारनिर्माणकिरीटमुकुटोज्न्बलाम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 265.5160)
- **Original**: रत्ाडुलीयसंयुक्तां रम्रपाशकशोभिताम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 265.5161)
- **Original**: बिभ्रती॑ कबरीभार॑ मालतीमाल्यभूषिताम्‌ । रूपाधिष्ठातदेवी, च गजेन्द्रमन्दगामिनीम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 295.18141)
- **Original**: *+अ्रीलहम्या: स्तोत्राणि + 799 दुर्वाससा कृत॑ कमलाकान्तस्तोत्रम्‌ दुर्वासा उबाच ज्राहि मां कमलाकान्त ज्ाहि मां करुणानिथे । दीनबन्धोडउतिदीनेश._ करुणासागर प्रभो
- **Translation**: 

---

### Verse 7 (Vaivtpuran 295.18142)
- **Original**: वेदवेदाडुसंस्तष्टिधातुअ स्वयं विधे । मृत्योमृ॑त्यों कालकाल त्राहि मां संकटार्णवे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 295.18143)
- **Original**: संहारकर्तु:. संहार सर्वेश सर्वकारण । महाविष्णुतरोबीज रक्ष मां भवजसागरे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 295.18144)
- **Original**: शरणागतशोकार्तभयत्राणपरायण । भगवन्नव मां भीत॑ नारायण नमोउस्तु ते
- **Translation**: 

---

### Verse 10 (Vaivtpuran 295.18145)
- **Original**: वेदेष्चाह्यं च यद्‌ वस्तु वेदाः स्तोतुंन चर क्षमा: । सरस्वती जडीभूता कि स्तुवन्ति विपक्चितः
- **Translation**: 

---

### Verse 11 (Vaivtpuran 295.18146)
- **Original**: शेषः सहस््रवकत्रेण य॑ स्तोतुं जडतां ब्रजेत्‌ । जडीभूतो._ जड़ीभूतशअतुर्मुस्यः
- **Translation**: 

---

### Verse 12 (Vaivtpuran 295.18147)
- **Original**: श्रुत॒य: स्मृतिकर्तारो वाणी चेत्‌ स्तोतुमक्षमा । को5हं विप्रश्न वेदज्ञ: शिष्य: किं स्तौमि मानद
- **Translation**: 

---

### Verse 13 (Vaivtpuran 295.18148)
- **Original**: मनूनां च महेन्द्राणामष्टाविंशतिमे गते । दिवानिशं यस्य विशधेरष्टोत्तशतायुषः
- **Translation**: 

---

### Verse 14 (Vaivtpuran 295.18149)
- **Original**: तस्य यातो भवेद्‌ यस्य चक्षुरुन्मीलनेन च । तमनिर्वचनीयं च किं स्तौमि पाहि मां प्रभो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 295.18150)
- **Original**: इत्येज॑ स्तवनं कृत्वा पपात चरणाम्बुज़े । नयनाम्थुजनरिण. सिषेच भयविड्डल:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 295.18151)
- **Original**: दुर्वाससा कृतं स्तोत्र॑ हरेश्न॒ परमात्मनः । पुण्यदं सामबेदोक्त जगन्मड्जलनामकम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 295.18152)
- **Original**: यः पठेत्‌ संकटग्रस्तो भ्रक्तियुक्तश्ष संयुत:
- **Translation**: 

---

### Verse 18 (Vaivtpuran 295.18153)
- **Original**: नारायणस्त॑ कृपया शीघ्रमागत्य रक्षति
- **Translation**: 

---

### Verse 19 (Vaivtpuran 295.18154)
- **Original**: इति श्रीब्रह्मवैवर्ते दुवाससा कृत कमलाकान्तस्तोत्र॑ सम्पूर्णम्‌। ( श्रीकृष्णजन्मखण्ड 295। 90--101) स्वतेजसा प्रज्वलन्ती सुखदृश्यां मनोहराम्‌ । प्रतप्तकाझ्नननिभां शोभां मूर्तिमर्ती सतीम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 295.18155)
- **Original**: रल्रभूषणभूषालद्मां शोभितां पीतवाससा । ईषद्धास्यप्रसन्नास्यां शघश्वत्सुस्थिरयौवनाम्‌
- **Translation**: 

---

