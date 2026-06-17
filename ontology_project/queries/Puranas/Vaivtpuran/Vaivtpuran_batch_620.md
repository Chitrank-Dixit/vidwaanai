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

### Verse 1 (Vaivtpuran 55.19216)
- **Original**: पृताबां दक्षकन्यायामाज़्या परमात्मन: । स्तोत्रेणानेन सप्प्राप्ता सावित्री ब्रह्मणा पुरा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 55.19217)
- **Original**: पुरा दुर्वासस: शापात्नि:श्रीके देवतागणे । स्तोत्रेणानेन देवैस्तैः सम्प्राप्ता श्री: सुदुर्लभा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 55.19218)
- **Original**: श्रेणोति वर्षमेके चर पुत्रार्थी लभते सुतम्‌ । महाव्याधी रोगमुक्तो भवेत्‌ स्तोत्रप्रसादतः
- **Translation**: 

---

### Verse 4 (Vaivtpuran 55.19219)
- **Original**: कार्तिकीपूर्णिमायां तु तां सम्पूज्य पठेत्तु: यः। अचलां श्रियमाप्नरोति राजसूयफलं लभेत्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 55.19220)
- **Original**: नारी श्रृणोति चेत्‌ स्तोत्र स्वामिसौभाग्यसंयुता । भकत्या श्रूणोति यः स्तोत्र बन्धनान्मुच्यते ध्रुवम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 55.19221)
- **Original**: नित्यं पठति यो भक्त्या राधां सम्पूज्य भक्तित: । स॒प्रयाति च गोलोकं निर्मुक्तो भवबन्धनात्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 55.19222)
- **Original**: इति औजबरह्मबैवर्ते श्रीकृष्णकृत श्रीयाधास्तोत्रं सम्पूर्णय्‌। (प्रकृतिखण्ड 55। 73--101) बरहाणा कृतं श्रीराधास्तोत्रम्‌ ब्रह्मोबाच है मातस्त्वत्पदाम्भोजं दृष्ट कृष्णप्रसादत:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 55.19223)
- **Original**: सुदुर्लभ॑च सर्वेषां भारते चर विशेषत: । षष्टिवर्षसहस्लाणि तपस्तप्त॑ पुरा मया
- **Translation**: 

---

### Verse 9 (Vaivtpuran 55.19224)
- **Original**: । भास्करे पुष्करे तीर्थे कृष्णस्थ. परमात्मम: । आजगाम वर दातुं बरदाता हरि: स्वयम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 55.19225)
- **Original**: वर वृणीष्वेत्युक्ते च स्वाभीष्टं चर वृतं मुद्रा । राधिकाचरणाम्भोज॑ सर्वेधामपि दुर्लभम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 55.19226)
- **Original**: है गुणातीत में शीघ्रमधुनैव प्रदर्शय । मयेत्युक्तो हरिर्यमुबाच मां तपस्विनम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 55.19227)
- **Original**: दर्शयिष्याप्ति काले चर बत्सेदानीं क्षमति च ।न हीश्वराज्ञा बिफला तेन दृष्ट पदाम्बुजम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 55.19228)
- **Original**: सर्वेषां बाओ्छितं मातर्गोलोके भारते5धुना । सर्वा देव्य: प्रकृत्यंशा जन्या: प्राकृतिका ध्रुवम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 55.19229)
- **Original**: त्वं कृष्णाड्ार्थसम्भूता तुल्या कृष्णेन सर्वतः । श्रीकृष्णस्त्वमयं राधा त्वं राधा वा हरि: स्वयम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 55.19230)
- **Original**: न हि येदेषु में दृष्ट इति केन निरूपितम्‌ । ब्रह्माण्डाद्‌ बहिरूध्वँ च गोलोको5स्ति यथाम्बिके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 55.19231)
- **Original**: बैकुण्ठश्षाप्पजन्यक्षत्वमजन्या तथाम्बिके । यथा समस्तब्रह्माण्डे श्रीकृष्णांशांशजीविन:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 55.19232)
- **Original**: तथा शक्तिस्वरूपा त्वं तेषु सर्वेषु संस्थिता । पुरुषाश्र॒हरेरंशास्त्वदंशा निखिला: स्थ्रिय:
- **Translation**: 

---

### Verse 18 (Vaivtpuran 55.19233)
- **Original**: आत्मनो देहरूपा त्वमस्याधारस्त्वमेव हि । अस्था नु प्राणैस्त्व॑ मातस्त्वत्प्राणैरयमी श्वर:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 55.19234)
- **Original**: किमहो निर्मित: केन हेतुना शिल्पकारिणा । नित्यो5यं च यथा कृष्णस्त्वं च नित्या तथाम्बिके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 55.19235)
- **Original**: अस्यांशा त्व॑ त्वदंशों वाप्यय॑ केन निरूपित: । अहं विधाता जगतां वेदानां जनक: स्वयम्‌
- **Translation**: 

---

