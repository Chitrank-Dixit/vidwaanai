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

### Verse 1 (Bhagwat_Geeta 1.141)
- **Original**: वर्णसंकर कुलघातियोंको और कुलको नरकमें ले जानेके लिये ही होता है। लुप्त हुई पिण्ड और जलकी क्रियावाले अर्थात्‌ श्राद्ध और तर्पणसे वच्चित इनके पितरलोग भी अधोगतिको प्राप्त होते हैं
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 1.142)
- **Original**: दोषेरेते: कुलघ्लानां वर्णसड्डूरकारकै:
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 1.143)
- **Original**: उत्साह्यन्ते जातिधर्मा: कुलधर्माश्व शाश्वताः
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 1.144)
- **Original**: इन वर्णसंकरकारक दोषोंसे कुलघातियोंके सनातन कुल-धर्म और जाति-धर्म नष्ट हो जाते हैं
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 1.145)
- **Original**: उत्सन्नकुलधर्माणां मनुष्याणां जनार्दन। नरकेउनियतं वासो भवतीत्यनुशुश्रुम
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 1.146)
- **Original**: । हे जनार्दन! जिनका कुल-धर्म नष्ट हो गया है, ऐसे मनुष्योंका अनिश्चित कालतक नरकमें वास होता है, ऐसा हम सुनते आये हैं
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 1.147)
- **Original**: 24 * श्रीमद्धगवद्रीता * अहो बत महत्पापं कर्तु व्यवसिता वयम्‌। यद्राज्यसुखलोभेन हन्तुं स्वजनमुद्यता:
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 1.148)
- **Original**: हा! शोक ! हमलोग बुद्धिमान्‌ होकर भी महान्‌ पाप करनेको तैयार हो गये हैं, जो राज्य और सुखके लोभसे स्वजनोंको मारनेके लिये उद्यत हो गये हैं
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 1.149)
- **Original**: यदि मामप्रतीकारमशस्त्र शस्त्रपाणय: । धार्तराष्ट्रा रणे हन्युस्तन्मे क्षेमतरं भवेत्‌
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 1.150)
- **Original**: यदि मुझ शस्त्ररहित एवं सामना न करनेवालेको शस्त्र हाथमें लिये हुए धृतराष्ट्रके पुत्र रणमें मार डालें तो वह मारना भी मेरे लिये अधिक कल्याणकारक होगा
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 1.151)
- **Original**: सञ्ञय उवाच एवमुकक्‍्त्वार्जुन: सड़ख्ये रथोपस्थ उपाविशत्‌। विसृज्य सशरं चापं शोकसंविग्रमानसः
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 1.152)
- **Original**: संजय बोले--रणभूमिमें शोकसे उद्ठिग्न मनवाले अर्जुन इस प्रकार कहकर, बाणसहित धनुषको त्यागकर रथके पिछले भागमें बैठ गये
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 1.153)
- **Original**: 3& तत्सदिति श्रीमद्धगवर्गीतासूपनिषत्सु ब्रह्मविद्यायां योगशास्त्रे श्रीकृष्णार्जुनसंवादे$र्जुनविषादयोगो नाम प्रथमो ध्याय:
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 1.154)
- **Original**: #्शलजट () 23242
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 1.155)
- **Original**: अथ द्विवीयो5 ध्याय: सञ्ञय उवाच त॑ तथा कृपयादविष्टरमश्रुपूर्णाकुलेक्षणम्‌ । विषीदन्तमिदं वाक्यमुवाच मथधुसूदन:
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 1.156)
- **Original**: संजय बोले--उस प्रकार करुणासे व्याप्त और आँसुओंसे पूर्ण तथा व्याकुल नेत्रोंवाले शोकयुक्त उस अर्जुनके प्रति भगवान्‌ मधुसूदनने यह वचन कहा
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 1.157)
- **Original**: श्रीभयवानुवाच कुतस्त्वा कश्मलमिद्‌ं विषमे समुपस्थितम्‌ । अनार्यजुष्टमस्वर्ग्यमकीर्तिकरमर्जुन
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 1.158)
- **Original**: श्रीभगवान्‌ बोले-हे अर्जुन ! तुझे इस असमयमें यह मोह किस हेतुसे प्राप्त हुआ? क्योंकि न तो यह श्रेष्ठ पुरुषोंद्दारा आचरित है, न स्वर्गको देनेवाला है और न कीर्तिको करनेवाला ही है
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 1.159)
- **Original**: क्लैब्यं मा सम गमः पार्थ नैतत्त्वय्युपपद्मयते। क्षुद्रं हृदयदौर्बल्यं त्यक्त्वोत्तिष्ठ परन्तप
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 1.160)
- **Original**: इसलिये हे अर्जुन
- **Translation**: 

---

