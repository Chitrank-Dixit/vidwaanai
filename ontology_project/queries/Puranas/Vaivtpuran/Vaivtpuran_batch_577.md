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

### Verse 1 (Vaivtpuran 45.4401)
- **Original**: भी सर्पका भव नहीं हो सकता।* जिस कृपापूर्वक इनकी सभी अभिलाषाएँ पूर्ण कर दीं,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 45.4402)
- **Original**: शयनागारमें नागोंका भय हो, जिस भबनमें बहुतेरे इनकी पूजाका प्रचार किया और स्वयं भी इनकी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 45.4403)
- **Original**: नाग भरे हों, नागोंसे युक्त होनेके कारण जो महान्‌ पूजा की। स्वर्गमें, ब्रह्मलोकमें, भूमण्डलमें और
- **Translation**: 

---

### Verse 4 (Vaivtpuran 45.4404)
- **Original**: दारुण स्थान बन गया हो तथा जो नागोंसे वेष्टित पातालमें-सर्वत्र इनकी पूजा प्रचलित हुई। हो, वहाँ भी पुरुष इस स्तोत्रका पाठ करके सम्पूर्ण जगत्‌में ये अत्यधिक गौरवर्णा, सुन्दरी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 45.4405)
- **Original**: सर्पभयसे मुक्त हो जाता है-इसमें कोई संशय और मनोहारिणी हैं; अतएवं ये साध्वी देवी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 45.4406)
- **Original**: नहीं है। जो नित्य इसका पाठ करता है, उसे “जगदौरी' के नामसे विख्यात होकर सम्मान प्रास
- **Translation**: 

---

### Verse 7 (Vaivtpuran 45.4407)
- **Original**: देखकर नाग भाग जाते हैं। दस लाख पाठ करनेसे करती हैं। भगवान्‌ शिवसे शिक्षा प्राप्त करनेके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 45.4408)
- **Original**: यह स्तोत्र मनुष्योंके लिये सिद्ध हो जाता है। कारण ये देवी “'शैवी' कहलाती हैं। भगवान्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 45.4409)
- **Original**: जिसे यह स्तोत्र सिद्ध हो गया, वह विष-भक्षण विष्णुकी ये अनन्य उपासिका हैं। अतएवं लोग
- **Translation**: 

---

### Verse 10 (Vaivtpuran 45.4410)
- **Original**: करने तथा नागोंकों भूषण बनाकर नागपर सवारी इन्हें 'वैष्णवी ' कहते हैं। राजा जनमेजयके यज्ञमें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 45.4411)
- **Original**: करनेमें भी समर्थ हो सकता है। वह नागासन, इन्हींके सत्प्रयक्नसे नागोंके प्राणोंको रक्षा हुई थी,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 45.4412)
- **Original**: नागतल्प तथा महान्‌ सिद्ध हो जाता है। अत: इनका नाम “नागेश्वरी' और “नागभगिनी'
- **Translation**: 

---

### Verse 13 (Vaivtpuran 45.4413)
- **Original**: . मुनिवर! अब मैं देवी मनसाकी पूजाका पड़ गया। विषका संहार करनेमें परम समर्थ
- **Translation**: 

---

### Verse 14 (Vaivtpuran 45.4414)
- **Original**: विधान तथा सामवेदोक्त ध्यान बतलाता हूँ, सुनो। होनेसे इनका एक नाम “विषहरी' है। इन्हें भगवती मनसा श्रेतचम्पक-पुष्पके समान वर्णवाली भगवान्‌ शंकरसे योगसिद्धि प्राप्त हुई थी। अतः
- **Translation**: 

---

### Verse 15 (Vaivtpuran 45.4415)
- **Original**: हैं। इनका विग्रह रत्रमय भूषणोंसे विभूषित है। ये 'सिद्धयोगिनी ' कहलाने लगीं। इन्होंने शंकरसे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 45.4416)
- **Original**: अग्रिशुद्ध वस्त्र इनके शरीरकी शोभा बढ़ा रहे हैं। महान्‌ गोपनीय ज्ञान एवं मृतसंजीवनी नामक
- **Translation**: 

---

### Verse 17 (Vaivtpuran 45.4417)
- **Original**: इन्होंने सर्पोंका यज्ञोपवीत धारण कर रखा है। उत्तम विद्या प्राप्त की है, इस कारण विद्वान्‌ पुरुष
- **Translation**: 

---

### Verse 18 (Vaivtpuran 45.4418)
- **Original**: महान्‌ ज्ञानसे सम्पन्न होनेके कारण प्रसिद्ध ज्ञानियोंमें इन्हें “महाज्ञानयुता' कहते हैं। ये परम तपस्विनी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 45.4419)
- **Original**: भी ये प्रमुख मानी जाती हैं। ये सिद्धपुरुषोंकी देवी मुनिवर आस्तीककी माता हैं। अत: ये देवी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 45.4420)
- **Original**: अधिष्ठात्री देवी हैं। सिद्धि प्रदान करनेवाली तथा जगतूमें सुप्रतिष्ठित होकर 'आस्तीकमाता' नामसे
- **Translation**: 

---

