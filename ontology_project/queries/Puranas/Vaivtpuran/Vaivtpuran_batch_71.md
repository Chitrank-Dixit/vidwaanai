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

### Verse 1 (Vaivtpuran 6.9231)
- **Original**: अपने अंशरूपसे भूतलपर अवतार लो। भक्तोंकों नहीं। मेरे भक्त पाप या पुण्य किसी भी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.9232)
- **Original**: ऐसा कहकर जगदीश्वर श्रीकृष्णने गोपों और कर्ममें लिप्त नहीं होते हैं। मैं उनके कर्मभोगोंका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.9233)
- **Original**: गोपियोंको बुलाकर मधुर, सत्य एवं समयोचित निश्चय ही नाश कर देता हूँ। मैं भक्तोंका प्राण
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.9234)
- **Original**: बातें कहीं--'गोपो और गोपियो ! सुनो। तुम सब- हूँ और भक्त भी मेरे लिये प्राणोंके समान हैं।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.9235)
- **Original**: के-सब नन्दरायजीका जो उत्कृष्ट ब्रज है, वहाँ जो नित्य मेरा ध्यान करते हैं, उनका मैं दिन-
- **Translation**: 

---

### Verse 6 (Vaivtpuran 6.9236)
- **Original**: जाओ (उस ब्रजमें अवतार ग्रहण करो) । राधिके ! रात स्मरण करता हूँ*। सोलह अरोंसे युक्त तुम भी शीघ्र ही वृषभानुके घर पधारो। अत्यन्त तीखा सुदर्शन नामक चक्र महान्‌ तेजस्वी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 6.9237)
- **Original**: वृषभानुकी प्यारी स्त्री बड़ी साध्वी हैं। उनका है। सम्पूर्ण जीवधारियोंमें जितना भी तेज है, वह
- **Translation**: 

---

### Verse 8 (Vaivtpuran 6.9238)
- **Original**: नाम कलावती है। वे सुबलकी पुत्री हैं और सब उस चक्रके तेजके सोलहवें अंशके बराबर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 6.9239)
- **Original**: लक्ष्मीके अंशसे प्रकट हुई हैं। वास्तवमें वे भी नहीं है। उस अभीष्ट चक्रको भक्तोंक निकट
- **Translation**: 

---

### Verse 10 (Vaivtpuran 6.9240)
- **Original**: पितरोंकी मानसी कन्या हैं तथा नारियोंमें धन्या उनकी रक्षाके लिये नियुक्त करके भी मुझे प्रतीति
- **Translation**: 

---

### Verse 11 (Vaivtpuran 6.9241)
- **Original**: और मान्या समझी जाती हैं। पूर्वकालमें दुर्वासाके नहीं होती; इसलिये मैं स्वयं भी उनके पास जाता
- **Translation**: 

---

### Verse 12 (Vaivtpuran 6.9242)
- **Original**: शापसे उनका ब्रजमण्डलमें गोपके घरमें जन्म हूँ। तुम सब देवता और प्राणाधिका लक्ष्मी भी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 6.9243)
- **Original**: हुआ है। तुम उन्हीं कलावतीकी पुत्री होकर जन्म मुझे भक्तसे बढ़कर प्यारी नहीं है। देवेश्वरो ! ग्रहण करो। अब शीघ्र नन्दब्रजमें जाओ। भक्तोंका भक्तिपूर्वक दिया हुआ जो द्रव्य है,
- **Translation**: 

---

### Verse 14 (Vaivtpuran 6.9244)
- **Original**: कमलानने! मैं बालकरूपसे वहाँ आकर तुम्हें उसको मैं बड़े प्रेमसे ग्रहण करता हूँ, परंतु
- **Translation**: 

---

### Verse 15 (Vaivtpuran 6.9245)
- **Original**: प्रास करूँगा। राधे! तुम मुझे प्राणोंसे भी अधिक अभक्तोंकी दी हुई कोई भी वस्तु मैं नहीं खाता।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 6.9246)
- **Original**: प्यारी हो और मैं भी तुम्हें प्राणॉंसे भी बढ़कर निश्चय ही उसे राजा बलि ही भोगते हैं। जो अपने
- **Translation**: 

---

### Verse 17 (Vaivtpuran 6.9247)
- **Original**: प्यारा हूँ। हम दोनोंका कुछ भी एक-दूसरेसे भिन्न स्त्री-पुत्र आदि स्वजनोंको त्यागकर दिन-रात मुझे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 6.9248)
- **Original**: नहीं है। हम सदैव एक-रूप हैं।' ही याद करते हैं, उनका स्मरण मैं भी तुमलोगोंको मुने! यह सुनकर श्रीराधा प्रेमसे विह्ल त्यागकर अहर्निश किया करता हूँ। जो लोग
- **Translation**: 

---

### Verse 19 (Vaivtpuran 6.9249)
- **Original**: होकर वहाँ रो पड़ीं और अपने नेत्र-चकोरोंद्वारा भक्तों, ब्राह्मणों तथा गौओंसे द्वेष रखते हैं, यज्ञों
- **Translation**: 

---

### Verse 20 (Vaivtpuran 6.9250)
- **Original**: श्रोहरिके मुखचन्द्रकी सौन्दर्य-सुधाका पान करने और देवताओंकी हिंसा करते हैं, वे शीघ्र ही उसी
- **Translation**: 

---

