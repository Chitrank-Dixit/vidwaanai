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

### Verse 1 (Vaivtpuran 13.10602)
- **Original**: चारुचम्पकवर्णाभां चन्दतेन विभूषिताम्‌ । कस्तूरीविदुना सा्द्ध सिन्दूरबिन्दुना युताम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10603)
- **Original**: चारुपत्रावलीयुक्तां बहिशुद्धांशुकोण्ज्वलाप्‌ । सद्रबरकुण्डलाभ्यां च सुकपोलस्थलोम्म्बलाम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10604)
- **Original**: रत्लेन्द्रसारहारेण वक्ष:स्थलविराजितामू । रलकड्भडणकेयूरकिड्विणीरत्नरञ्ितान्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10605)
- **Original**: सद्रत्नसाररचिताक्वणन्मजी ररज्िताम्‌ । ब्रह्मादिभिश्ष॒ सेव्येन श्रीकृष्णेनेव सेविताम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10606)
- **Original**: सर्वेशेन स्तूयमानां. सर्वबीजां भजाम्यहम्‌ । इति ध्यात्वा च कृष्णेन सहितां तां च पूजयेत्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10607)
- **Original**: (16। 85-93)
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10608)
- **Original**: डड + संक्षिप्त ब्रह्मवैयर्तपुराण « %44#4%4£#%# 8 ##% # # & # £ # 4 #£ ऋ 44444 4 5 £ % # 4 कद 'श्र कक दअकदअक ड क्र कक कक 5 क 8 58 $ 46 8 8 # 6 दिन जो विधान आवश्यक है, उसे सुनो। विप्रवर !
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10609)
- **Original**: इश्टदेव श्रीहरिके ब्रतोंमें यह श्रेष्ठ ब्रत है। नाथ! नब्बे हजार अक्षत कमलकी आहुति दे और
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10610)
- **Original**: श्रीहरिकी आराधना समस्त मड्जलोंकी कारणरूपा यल्षपूर्वक नौ हजार ब्राह्मणोंको उत्तम, स्वादिष्ट
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10611)
- **Original**: है। यज्ञ, दान, वेदाध्ययन, तीर्थसेबन और एवं मीठे अन्न भोजन करावे। नौ हजार सात सौ
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10612)
- **Original**: पृथ्वीकी परिक्रमा--ये सब श्रीहरिकी आराधनाको बीस फल तथा नाना प्रकारके मनोहर द्रव्यका
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10613)
- **Original**: सोलहवीं कलाके भी बराबर नहीं हैं। जिसके नैवेद्य अर्पएण करें। इसके बाद संस्कारयुक्त
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10614)
- **Original**: बाहर और भीतर प्रतिक्षण श्रीहरिकी स्मृति बनी अग्रिकी स्थापना करके विद्वान्‌ पुरुष होम करे।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10615)
- **Original**: रहती है, उस जीवन्मुक्त पुरुषके दर्शनसे ही मुक्ति घृतयुक्त तिलकी नब्बे हजार आहुतियाँ देकर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10616)
- **Original**: प्राप्त हो जाती है। उसके चरणकमलोंकी धूल ब्राह्मणोंको भक्तिभावसे वस्त्र, भोजन, यज्ञोपवीत
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10617)
- **Original**: पड़नेसे वसुधा उसी क्षण शुद्ध हो जाती है तथा और फलसहित अन्न और तिलके लड्डू दे। उन
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10618)
- **Original**: उसके दर्शनमात्रसे तीनों लोक पवित्र हो जाते लड्डुओंको गन्ध-पुष्पसे अर्चित करके देना
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10619)
- **Original**: हैं। ब्रह्मा, विष्णु, धर्म, शेषनाग, आप महेश्वर चाहिये। साथ ही शीतल जलसे भरे हुए नब्बे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10620)
- **Original**: और गणेश--ये सब लोग जिनके चरणकमलोंका कलशॉका भी दान करना चाहिये। इस प्रकार व्रत
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10621)
- **Original**: चिन्तन करते-करते उन्होंके समान महातेजस्वी करके ब्राह्मणको दक्षिणा देनी चाहिये। दक्षिणाका
- **Translation**: 

---

