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

### Verse 1 (Vaivtpuran 67.18058)
- **Original**: 3» हीं श्रीं क्लीमिति पृष्ठ चर पातु मे सर्वतः सदा । ह्रीं मे वक्ष:स्थरल पातु हस्त श्रीमिति संततम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 67.18059)
- **Original**: 3* भ्रीं हीं क्लीं पातु सर्वाड्रं स्वप्ने जागरणे तथा । प्राच्यां मां पातु प्रकृति: पातु बद्लौ च चणिडका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 67.18060)
- **Original**: दक्षिणे भद्रकाली उतर नैऋते च महेश्वरी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 67.18061)
- **Original**: वारुण्यां पातु वाराही वायव्यां सर्वमड्भला
- **Translation**: 

---

### Verse 5 (Vaivtpuran 67.18062)
- **Original**: उत्ते बैष्णवी पातु तथैशान्यां शिवप्रिया । जले स्थले चान्तरिक्षे पातु मां जगदम्बिका
- **Translation**: 

---

### Verse 6 (Vaivtpuran 67.18063)
- **Original**: डइति ते कथित वत्स कब च॒ सुद्दुर्लभम्‌ । यस्मै कस्मै न दातव्यं प्रवक्तव्य॑ न कस्यचित्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 67.18064)
- **Original**: गुरुमभ्यर्य्यय विधिवद्‌._ वस्त्रालंकारचन्दनै: । कवच थारयेद्‌ यस्तु सो5पि विष्णुर्न संशयः
- **Translation**: 

---

### Verse 8 (Vaivtpuran 67.18065)
- **Original**: भ्रमणे सर्वतीर्थानां पृथिव्याश्र॒ प्रदक्षिणि । यत्‌ फल लभते लोकस्तदेतद्धारणे मुने
- **Translation**: 

---

### Verse 9 (Vaivtpuran 67.18066)
- **Original**: पड्नलक्षजपेनेव सिद्धमेतद्‌ भवेद्‌ श्रुवम्‌ । लोक॑ च् सिद्धकवच नास्त्र॑ विध्यति सड्डूटे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 67.18067)
- **Original**: न तस्य मृत्युर्भवति जले वह्लौ विशेद्‌ ध्रुवम्‌ । जीवन्मुक्तो भवेत्‌ सो5पि सर्वसिद्धेश्वर: स्वयम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 67.18068)
- **Original**: यदि स्यात्‌ सिद्धकवचों विष्णुतुल्यो भवेद्‌ ध्रुयम्‌। ड्ति श्रीब्रह्मवैवरतें ग्रकृतेग्रह्याण्डम्रोहतकक्चं सम्पूर्णयू। (प्रकृतिखण्ड 67। 1--193) मन्त्रसहितं कालीकवचम्‌ नारद उवाच कवर्च श्रोतुमिच्छामि तांच विद्यां दशाक्षरीम्‌ । नाथ त्वत्तो हि सर्वज्ञ भद्रकाल्याश्न साम्प्रतम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 67.18069)
- **Original**: नारायण उवाच श्रूणु नारद वक्ष्यामि महाविद्यां दशाक्षरीम्‌ । गोपनीयं चर कवर्न त्रिषु लोकेषु दु्लभम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 67.18070)
- **Original**: 30 हीं भ्रीं क्‍्लीं कालिकाय॑ स्वाहेति च दशाक्षरीम्‌ । दुर्वांसा हि ददौ राज्ञे पुष्करे सूर्यपर्वणि
- **Translation**: 

---

### Verse 14 (Vaivtpuran 67.18071)
- **Original**: दशलक्षजपेमैव मनत्रसिद्धि: कृता पुरा । पद्कलक्षजपेनैव पठन्‌ू_ कबचपुत्तमम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 67.18072)
- **Original**: बभूव सिद्धकवचो5प्ययोध्यामाजगाम सः । कृत्मां हि पृथित्रीं जिग्ये कवचस्य प्रसादतः
- **Translation**: 

---

### Verse 16 (Vaivtpuran 67.18073)
- **Original**: नारद उवाच श्रुता दशाक्षरी विद्या त्रिषु लोकेषु दुर्लभा । अधुना ओ्रोतुमिच्छामि कवचं ब्ूहि में प्रभो
- **Translation**: 

---

### Verse 17 (Vaivtpuran 67.18074)
- **Original**: नारायण उवाच श्रूणु वक्ष्यामि विप्रे्न कवच परमाद्भुतम्‌ । नारायणेन यद्‌ दत्त कृपया शूलिने पुरा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 67.18075)
- **Original**: त्रिपुरस्थ खथे प्रोरे शिवस्थ विजयाय च। तदेव शूलिना दत्त पुरा दुर्वाससे मुने
- **Translation**: 

---

### Verse 19 (Vaivtpuran 67.18076)
- **Original**: दुर्वाससा च यद्‌ दत्त सुचन्भाय महात्मने
- **Translation**: 

---

### Verse 20 (Vaivtpuran 67.18077)
- **Original**: अतिगुहातरं तत्त्यं सर्वमनत्रौधविग्रहम्‌
- **Translation**: 

---

