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

### Verse 1 (Vishnu Puran 0.6461)
- **Original**: घृष्टके यैहामें धार्शक नामक क्षत्रिय हुए
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6462)
- **Original**: नाभागके नाभाग नामक पुत्र हुआ, नाभागका अम्बरीष और अम्बरीषका पुत्र विरूप हुआ, विरूपसे पृषदश्रका जन्म हुआ तथा उससे रथीतर हुआ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6463)
- **Original**: स्थीतस्के सम्बन्धमें यह इलोक प्रसिद्ध है-- रथीतरके बंशज क्षत्रिय सत्तान होते हुए भी आंगिर्स कहल्वये; अतः बे क्षत्रोपेत ब्राह्मण हुए'
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6464)
- **Original**: छींकनेके समय मनुकी ख्ाणेन्द्रियसे इख्याकु नामक पुत्रका जन्म हुआ
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6465)
- **Original**: उनके सौ पुत्रॉमेंस विकुक्ति, निमि और दण्ड नामक तीन पुत्र प्रधान हुए तथा उनके शकुनि आदि पचास पुत्र उत्तरापधके और डोष
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6466)
- **Original**: आ2)] चत्वारिश्ववष्टो च दक्षिणापथभूपाला:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6467)
- **Original**: स॒ चेक्ष्वाकुरष्टकायाइश्राद्धमुत्पाद. श्राद्धाईं मांसमानयेति विकुक्षिमाज्ञापपामास
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6468)
- **Original**: स तथ्नेति गृहीताज्ञों विधृतशरासनों वनमभ्ये- त्यानेकन्षो मृगान्‌ हत्वा श्रान्तो5तिक्षुत्परीतो विकुक्षिरेके शशम्रभक्षयत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6469)
- **Original**: शेष॑ च मांसमानीय पित्रे निवेदयामास
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6470)
- **Original**: इक्ष्वाकुकुलाचायों.. वसिष्ठस्तत्ोक्षणाय चोदित: प्राह। अलमनेनामेध्येनामिषेण दुरात्मना तब पुत्रेणैतन्मांसमुपहते यतोउनेन. शक्ञो अक्षित:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6471)
- **Original**: ततश्चासरौ विकुक्षिगुरुणैवमुक्त- इच्चश्नादसंज्ञामवाप पित्रा च परित्यक्त:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6472)
- **Original**: पितर्युपते चासावखिलामेतां पृथ्वी धर्मत- इछाशास
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6473)
- **Original**: शज्मादस्य तस्थ पुरक्षयो नाम पुत्रो>भवत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6474)
- **Original**: तस्थेदे चान्यत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6475)
- **Original**: पुरा हि त्रेतायां देवासुरयुद्धमतिभीषणमभवत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6476)
- **Original**: . तत्र चातिबलिभिरसुरैरमरा: पराजितास्ते भगवत्ते बिष्णुमाराधयाज्ञक्कु:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6477)
- **Original**: असन्नश्च देवानामनादिनिधनो5खिलजगत्परायणों नारायण प्राह
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6478)
- **Original**: ज्ञातपेतन्यया युष्याभिर्यदभिलषिते तदर्थमिदं श्रूयताम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6479)
- **Original**: पुरक्षयो नाम राजघेंदशशादस्य तनय: क्षत्रियवरो यस्तस्य शरीरेष्हमंशेन स्वयमेवाबतोीर्य तानझहोषा- नसुराक्षिहनिष्यामि तद्भवद्धि: पुरक्षयो5सुरवधा र्थ- मुद्योग कार्यतामिति
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6480)
- **Original**: एतन्च श्रुत्वा प्रणम्य भगवतन्ते विष्णुममराः पुरक्षयसकाशमाजस्मुरूचुझननम्‌
- **Translation**: 

---

