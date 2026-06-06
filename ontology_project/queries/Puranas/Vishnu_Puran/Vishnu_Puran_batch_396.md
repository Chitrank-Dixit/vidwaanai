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

### Verse 1 (Vishnu Puran 0.7901)
- **Original**: इनकी ऐसी गुणबान्‌ माता-पितासे उत्पत्ति है तो फिर उनके चले जानेसे यहाँ दुर्भिक्ष और महामारी आदि उपद्रव क्यों न छोंगे ?
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7902)
- **Original**: 127-128
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7903)
- **Original**: अतः उनको यहाँ ले आना चाहिये, अति गुणवानूके अपराधकी अधिक जाँच-परत्ताल करना ठीक नहीं है। ,
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7904)
- **Original**: यादववृद्ध अखकके ऐसे बचन सुनकर कृष्ण, उमग्रसेन '
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7905)
- **Original**: और बलंभद्र आदि यादव श्वफल्कपुत्र अक्रूरके अपराधको भुव्थकर उन्हें अभयदान देकर अपने नगरमें ले आये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7906)
- **Original**: उनके वहाँ आते ही स्थमन्तकमणिके प्रभावसे अनावृष्टि, महामारी, दुर्भिक्ष और सर्पभय आदि स्रभी उपद्रत शान्‍्त हो राये
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7907)
- **Original**: तब श्रीकृष्णचन्द्रने विचार किया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7908)
- **Original**: 'अक्रूरका जन्म गान्दिनीसे भ्रफल्कके द्वारा हुआ है यह तो बहुत सामान्य कारण है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7909)
- **Original**: किन्तु अनावृष्टि, दुर्भिक्ष, महामारी आदि उपद्तबोंकों शान्त्त कर देनेवालां इसका प्रभाव तो अति महान है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7910)
- **Original**: अवदय ही इसके पास वह स्यमत्तक नामक महामणि है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7911)
- **Original**: उसीका ऐसा ग्रभाव सुना जाता है।
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7912)
- **Original**: इसे भी हम देखते हैं कि एक यज्ञके पोछे दूसरा और दूसरेके पीछे तीसरा इस प्रकार
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7913)
- **Original**: मन्यत्कत्वन्तरं तस्थानन्तरमन्यहाज़ान्तरं चाजस््र- मविच्छिन्न॑ यज़तीति
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7914)
- **Original**: अल्पोपादान॑ चास्यासंशयमत्रासो मणिवरस्तिष्ठतीति कृताध्यवसायो5न्यट्ाबोजनमुद्दिश्य सकलयादव- समाजमात्मगृह एवाचीकरत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7915)
- **Original**: तत्र चोपविष्टेष्नखिलेषु यदुषु पूर्व प्रयोजन- पुपन्यस्य पर्यवसिते च तस्पिन्‌ प्रसड्डान्तरपरिहास- कथामक््रेण कृत्वा जाार्दनस्तमक्रूरमाह
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7916)
- **Original**: दानपते जानीम एवं वर्य यथा शातथन्वना तदिदमखिलजगत्सारभूत॑ स्यप्नन्तक रत भवतः समर्पित तदडोषराष्ट्रीपकारक॑ भवत्सकाशे तिष्ठति तिष्ठतु सर्व एवं वर्य॑ त्वेष बलभद्रोउस्मा- 5चिन्तयत्‌ ।। 139
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7917)
- **Original**: किमन्नानुप्लेबमन्यथा चेद्‌ ब्रवीम्यहं॑. तत्केवलाम्बरतिरोश्वानमन्विष्यन्तो रन्नमेते द्रक्ष्यन्ति अतिविरोधो न क्षेम ड़ति सनझिन्त्य तमखिलजगत्कारणभूर्त॑_ नारायणमाहाक़्रः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7918)
- **Original**: भगवतः्ममैतत्स्यपत्तकरलं शतधनुषा समर्पितमपगते च तस्मिन्नद्य श्र: परश्नो वा भगवान्‌ याचयिष्यतीति कृतमतिरतिकृच्छेणैतावन्त काल- मधारयम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7919)
- **Original**: तस्य च्व धारणक्लेशेनाह- मशेषोपभोगेषृसड्भिमानसो न वेहि स्वसुख- कल्लामपि
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7920)
- **Original**: . एतावन्म्ात्रमप्यशेष- राष्ट्रोफारि धारयितुं न शक्तोति भवान्यन्यत डत्यात्मसा न चोदितवान्‌
- **Translation**: 

---

