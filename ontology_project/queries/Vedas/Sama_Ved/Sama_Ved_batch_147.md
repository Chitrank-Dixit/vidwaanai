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

### Verse 1 (Sama Ved 0.2921)
- **Original**: हवियों में सर्वश्रेप् प्रशंसित हवि-सोम, जल में मिश्रित होते हुए मधुर रसधार से पात्र में स्थिर हो रहा है
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2922)
- **Original**: 1130. भ्र युजा वाचो अग्रियो वृषो अचिक्रदद्ने । सद्माभि सत्यो अध्वर:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2923)
- **Original**: आहुतियों में अग्रिम, वाणी के उत्पादक, शक्तिशाली, सत्यतायुबत और अहिंसक यह सोमदेव जल के साथ यज्ञशाला में प्रविष्ट होता है
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2924)
- **Original**: 11391. परि यत्काव्या कविर्तम्णा पुनानो अर्धति । स्वर्वाजी सिघासति
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2925)
- **Original**: प्रज्ञावानु सोम निज शक्ति- सामर्थ्य से, मनुष्यों में पवित्रता का संचार करते हुए, स्तुतियों को जैसे ही स्वीकार करता है, वैसे हो शक्तिशाली इन्द्रदेव स्वर्ग से यज्ञस्थल पर आने के लिए उद्यत होते हैं
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2926)
- **Original**: 1132. पवमानो अभि स्पृधों विशो राजेब सीदति । यदीमृण्वन्ति वेधस:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2927)
- **Original**: संस्कारित सोम याजकों की प्रेरणा से, प्रजा की रक्षा के लिए, राजा की भाँति शत्रुओं का संहार करने के लिए तैयार होता है
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2928)
- **Original**: 1133. अव्या वारे परि प्रियो हरि्वनेषु सीदति। रेभो वनुष्यते मती
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2929)
- **Original**: जल मिश्रित हरिताभ सोम, शोधन यत्त द्वारा पवित्र होते समय, त्रग्रत्वजों द्वारा को गई स्तुतियों को स्वीकार करते हुए, ध्वनि के साथ पात्र में स्थिर हो रहा है
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2930)
- **Original**: उत्तराचक अष्टमो5ध्याय: 03 1234. स वायुमिद्धमश्चिना साक॑ मदेन गच्छति । रणा यो अस्थ थर्मणा
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2931)
- **Original**: जो याजक इस सोम को निकालने एवं शुद्ध करने में संलग्न रहते हैं, वे आनन्दवर्द्धक सोम के साथ वायु, इन्र और अश्विनीकुमारों का सान्िध्य लाभ प्राप्त करते हैं
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2932)
- **Original**: 9135. आ मित्रे वरुणे भगे मधो: पवन्त ऊर्मयः । बिदाना अस्य शक्मभि:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2933)
- **Original**: जिन बऋँत्वजों द्वारा मधुरं सोम की धाराएँ मित्र, वरुण और भग देवों के निमित्त प्रवाहित होती हैं, ऐसे सोम की महिमा से परिचित याजक आनन्द की प्राप्ति करते हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2934)
- **Original**: 1136. अस्मभ्यं रोदसी रविं मध्वो वाजस्य सातये
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2935)
- **Original**: श्रवो वसूनि सज्ञितम्‌
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2936)
- **Original**: हे पृथ्वी और घुलोक के अधिष्ठाता देवता ! सोमरस रूपी श्रेष्ठ पोषक आहार को प्राप्त करने के लिए आप हमें, धन-धान्य के रूप में अपार वैभव प्रदान करें
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2937)
- **Original**: 1137. आ ते दक्ष॑ मयोभुव॑ं वह्निमद्या वृणीमहे
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2938)
- **Original**: पान्तमा पुरुस्पृहम्‌
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2939)
- **Original**: है सोमदेव ! आपकी सुखदायक, अभीष्ट धन देने वाली, संरक्षण करने वाली बहु प्रशंसित शक्ति को आज हम (याजक) प्राप्त करने की इच्छा करते हैं
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2940)
- **Original**: 1138. आ मन्द्रमा वरेण्यमा विप्रमा मनीषिणम्‌ । पान्तमा पुरुस्पृहम्‌
- **Translation**: 

---

