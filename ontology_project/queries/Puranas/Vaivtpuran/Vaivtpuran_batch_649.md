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

### Verse 1 (Vaivtpuran 67.5775)
- **Original**: दे। बछड़ेसहित सुन्दर गौका भक्तिपूर्वक दान नहीं होती है। वह सम्पूर्ण सिद्धोंका ईश्वर एवं
- **Translation**: 

---

### Verse 2 (Vaivtpuran 67.5776)
- **Original**: करे। मुने! वाचकको वस्त्र, आभूषण तथा रत्र जीवन्मुक्त हो जाता है। जिसको यह कबच सिद्ध
- **Translation**: 

---

### Verse 3 (Vaivtpuran 67.5777)
- **Original**: देकर संतुष्ट करे। पुष्प, आभूषण, वस्त्र तथा नाना हो गया है, वह निश्चय ही भगवान्‌ विष्णुके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 67.5778)
- **Original**: प्रकारके उपहार ले भक्ति और श्रद्धाके साथ समान हो जाता है।* पुस्तककी पूजा करे। जो ऐसा करके कथा सुनता मुने! इस प्रकार प्रकृतिखण्डका वर्णन किया
- **Translation**: 

---

### Verse 5 (Vaivtpuran 67.5779)
- **Original**: है, उसपर भगवान्‌ विष्णु प्रसन्न होते हैं। उसके गया, जो अमृतकी खाँड्से भी अधिक मधुर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 67.5780)
- **Original**: पुत्र-पौत्र आदिकी वृद्धि होती है। वह भगवान्‌की है। जिन्हें मूलप्रकृति कहते हैं तथा जिनके पुत्र
- **Translation**: 

---

### Verse 7 (Vaivtpuran 67.5781)
- **Original**: कृपासे यशस्वी होता है। उसके घरमें लक्ष्मी गणेश हैं, उन देवी पार्वतीने श्रीकृष्णका व्रत
- **Translation**: 

---

### Verse 8 (Vaivtpuran 67.5782)
- **Original**: निवास करती हैं और अन्तमें वह गोलोकको करके ही गणपति-जैसा पुत्र प्राप्त किया था।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 67.5783)
- **Original**: प्राप्त होता है। उसे श्रीकृष्णका दास्यभाव सुलभ साक्षात्‌ भगवान्‌ श्रीकृष्ण अपने अंशसे गणेश
- **Translation**: 

---

### Verse 10 (Vaivtpuran 67.5784)
- **Original**: होता है तथा भगवान्‌ श्रीकृष्णमें उसकी अविचल हुए थे। यह प्रकृतिखण्ड सुननेमें सुखद और
- **Translation**: 

---

### Verse 11 (Vaivtpuran 67.5785)
- **Original**: भक्ति हो जाती है। सुधाके समान मधुर है। इसे सुनकर वक्ताको (अध्याय 66-67) हल“ रियर 2 95-0000000
- **Translation**: 

---

### Verse 12 (Vaivtpuran 67.5786)
- **Original**: प्रकृतिखण्ड सम्पूर्ण
- **Translation**: 

---

### Verse 13 (Vaivtpuran 67.5787)
- **Original**: #3447400#शयकाय8-2>-लज *3& दुर्गेति चतुर्थ्यन्त स्वाहात्तो में शिरोईइवतु । मन्त्र: घडक्षरोई्य च भक्तानां कल्पपादप:। विचारों नास्ति वेदेषु ग्रहणे च॑ मनोर्मुने
- **Translation**: 

---

### Verse 14 (Vaivtpuran 67.5788)
- **Original**: मन्त्रग्रहणमात्रेण विष्णुतुल्यो भवेन्नर: । मम वतन सदा पातु 35 दुर्गाय॑ नमोउन्तत:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 67.5789)
- **Original**: 3& दुर्गे रक्ष इति च कणष्ठ॑ पातु सदा मम । 3» हीं श्रीं इति मन्त्रो5य॑ स्कन्ध॑ पातु निरन्तरम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 67.5790)
- **Original**: 3» हीं श्रीं क्लीं इति पृष्ठ च पातु मे सर्वतः सदा ; हीं मे वक्ष: पातु हस्त॑ श्रीमिति संततम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 67.5791)
- **Original**: 35 श्रों हों क्‍्लों पातु सर्वांड्ठं स्वप्ने जागरणे तथा । प्राच्यां मां पातु प्रकृति: पातु यहाँ च चण्डिका
- **Translation**: 

---

### Verse 18 (Vaivtpuran 67.5792)
- **Original**: दक्षिणे भद्रकाली च नैरऊ़ते च महेश्वरी। वारुणे पातु वाराही वायव्यां सर्वमड्नला
- **Translation**: 

---

### Verse 19 (Vaivtpuran 67.5793)
- **Original**: उत्ते वैष्णवी पातु तथैशान्यां शिवप्रिया । जले स्थले चान्तरिक्षे परातु मां जगदम्बिका
- **Translation**: 

---

### Verse 20 (Vaivtpuran 67.5794)
- **Original**: इति ते कथितं वत्स कवच च सुदुर्लभम्‌ । यस्मै कसम न दातव्यं प्रवक्रव्य॑ न कस्यचित्‌
- **Translation**: 

---

