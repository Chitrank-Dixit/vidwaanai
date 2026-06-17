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

### Verse 1 (Vaivtpuran 9.2316)
- **Original**: ड्लीं जिद्घाग्रवासिन्ये स्वाहाग्रिदिशि रक्षतु
- **Translation**: 

---

### Verse 2 (Vaivtpuran 9.2317)
- **Original**: हीं श्री क्‍लीं सरस्वत्ये बुधजनन्यै स्वाहा । मन्त्ररजोड्यं दक्षणे माँ सदावतु
- **Translation**: 

---

### Verse 3 (Vaivtpuran 9.2318)
- **Original**: श्रों ज्यक्षतो मनन्‍्त्रों नैर्क॒त्यां मे सदावतु। कविजिद्गाग्रवासिन्ये स्वाहा मां वारुणे3वतु
- **Translation**: 

---

### Verse 4 (Vaivtpuran 9.2319)
- **Original**: सर्वाम्बिकाव स्वाहा वायख्ये मां सदावतु। 30 ऐं श्रीं गद्यपध्चवासिन्ये स्वाहा मामुत्तरेडवतु
- **Translation**: 

---

### Verse 5 (Vaivtpuran 9.2320)
- **Original**: सर्वशास्त्रवासिन्ये. स्वाहैशान्यां. सदावतु
- **Translation**: 

---

### Verse 6 (Vaivtpuran 9.2321)
- **Original**: 3» हीं सर्वपूजितायै स्वाहा चोध्य॑सदावतु
- **Translation**: 

---

### Verse 7 (Vaivtpuran 9.2322)
- **Original**: हीं पुस्तकवासिन्ये स्वाहाधो मां सदाबतु । 3» ग्रन्थबीजरूपायैँ स्वाहा मां सर्वतो5बतु
- **Translation**: 

---

### Verse 8 (Vaivtpuran 9.2323)
- **Original**: इति ते कथित विप्र.ब्रह्ममन्त्रौधयिग्रहमू । इद॑ विश्वजयं॑ नाप कवच ब्रह्मरूपकम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 9.2324)
- **Original**: पुर श्रुतं॑ धर्मवक्‍्त्रात्‌ू पर्यते गन्धमादने । तब ख्रेहान्मया55ख्यात॑ प्रवक्तव्य॑ न कस्यचित्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 9.2325)
- **Original**: गुरुमध्यर्च्य विधिवद्स्त्रालंकारचन्दनै: । प्रणम्य दण्डवद्धूमा कवच॑ धारयेत्‌ सुधी:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 9.2326)
- **Original**: पन्नलक्षजपेनेव सिद्ध तु कवच भवेत्‌ । यदि स्यात्‌ सिद्धकवचों बृहस्पतिसमों भवेतू
- **Translation**: 

---

### Verse 12 (Vaivtpuran 9.2327)
- **Original**: महावाग्मी कवोन्द्रः. .. जैलोक्यविजवी भवेत्‌ । शक्रोति सर्व जेतुं च कवचस्य॒प्रसादत;
- **Translation**: 

---

### Verse 13 (Vaivtpuran 9.2328)
- **Original**: (प्रकृतिखण्ड ड
- **Translation**: 

---

### Verse 14 (Vaivtpuran 9.2329)
- **Original**: 63-11) 489 4
- **Translation**: 

---

### Verse 15 (Vaivtpuran 9.2330)
- **Original**: याज्ञवल्क्यद्वारा भगवती सरस्वतीकी स्तुति ऋषिप्रवर भगवान्‌ नारायण कहते हैं--नारद!
- **Translation**: 

---

### Verse 16 (Vaivtpuran 9.2331)
- **Original**: कर देते हैं, वैसे ही तुम भी मेरे लुप्त ज्ञानको सरस्वती देवीका स्तोत्र सुनो, जिससे सम्पूर्ण
- **Translation**: 

---

### Verse 17 (Vaivtpuran 9.2332)
- **Original**: पुनः प्रकाशित कर दो। जो ब्रह्मस्वरूपा, परमा, मनोरथ सिद्ध हो जाते हैं। प्राचीन समयकी बात ज्योतीरूपा, सनातनी तथा सम्पूर्ण विद्याओंकी है--याज्ञवल्क्य नामसे प्रसिद्ध एक महामुनि थे। अधिष्ठात्री हैं, उन वाणीदेवीको बार-बार प्रणाम उन्होंने उसी स्तोत्रसे भगवतों सरस्वतीकी स्तुति
- **Translation**: 

---

### Verse 18 (Vaivtpuran 9.2333)
- **Original**: है। जिनके बिना सारा जगत्‌ सदा जीते-जी मरेके की थी। जब गुरुके शापसे मुनिकी श्रेष्ठ विद्या [समान है तथा जो ज्ञानकी अधिष्ठात्री देवी हैं, नष्ट हो गयी, तब वे अत्यन्त दुःखी होकर उन माता सरस्वतीकों बारंबार नमस्कार है। लोलार्ककुण्डपर, जो उत्तम पुण्य प्रदान करनेवाला
- **Translation**: 

---

### Verse 19 (Vaivtpuran 9.2334)
- **Original**: जिनके बिना सारा जगत्‌ सदा गूँगा और पागलके तीर्थ है, गये। उन्होंने तपस्याके द्वारा सूर्यका प्रत्यक्ष समान हो जायगा तथा जो वाणीकी अधिष्ठात्री दर्शन पाकर शोकविह्नल हो भगवान्‌ सूर्यका स्तवन
- **Translation**: 

---

### Verse 20 (Vaivtpuran 9.2335)
- **Original**: देवी हैं, उन वाग्देवताकों बारंबार नमस्कार है। तथा बारंबार रोदन किया। तब शक्तिशाली सूर्यने
- **Translation**: 

---

