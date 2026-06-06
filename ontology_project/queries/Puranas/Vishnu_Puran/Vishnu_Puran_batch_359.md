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

### Verse 1 (Vishnu Puran 0.7161)
- **Original**: उर्वशी च् तदुपभोगा- ऋतिदिनप्रवर्द्मानानुरागा अपरलोकवासेठपि न स्पृहाँ चकार
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7162)
- **Original**: विना चोर्वश्या सुरत्मेकोउप्ससां सिद्ध- गन्धर्वाणां च नातिर्मणीयो5भवत्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7163)
- **Original**: किया था उसका वर्णन पहले हो कर चुके हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7164)
- **Original**: पुरूरवा अति दानशील, अति याज्ञिक और अति तेजस्वों था। 'मित्रावरुणके शापसे मुझे मर्त्यल्तरेकमें रहना पड़ेगा' ऐसा विचार करते हुए उर्वशी अप्सराकी दुष्टि उस अति सत्यवादी, रूपके घनो और मतिमान्‌ राजा पुरूरवापर पड़ी
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7165)
- **Original**: देखते ही बह सम्पूर्ण मान तथा स्वर्ग-सुर्तकती इच्छाको छोड़कर तनन्‍्मयभावसे उसीके पास आयी
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7166)
- **Original**: राजा पुरूरवाका चित्त भी उसे संसारकों समस्त स्त्रियोमें विशिष्ट तथा ब्ग्रन्ति-सुकुमारता, सुन्दरता, गतिबिलास और मुसकान आदि गुणोंसे युक्त देखकर उसके वच्नोभूत हो गया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7167)
- **Original**: इस प्रकार ले दोनों ही परस्पर तम्मय और अनन्यचित्त होकर और सब कामोंको भूल गये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7168)
- **Original**: निदान राजाने निःसंकोच होकर कहा---
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7169)
- **Original**: “है सुभ्रु ! मैं तुम्हारी 37छा करता हूँ, तुम प्रसन्न होकर मुझे प्रेम-दान दो।” राजाके ऐसा कहनेपर उर्वशीने भी लूज्जावश स्वल्लित स्वरमें कहा---
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7170)
- **Original**: “यदि आप मेरी प्रतिज्ञाको निभा सकें तो अवइय ऐसा ही हो सकता है।'' यह सुनकर सजाने कहा--
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7171)
- **Original**: अच्छा, तुम अपनी प्रतिज्ञा मझसे कहो
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7172)
- **Original**: इस प्रकार पूछनेपर वह फिर बोली--
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7173)
- **Original**: “मेरे पुत्रकप इन दो मेषों (भेड़ों) को आप कभी मेरी द्ाव्यासे दूर न कर सकेंगे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7174)
- **Original**: मैं कभी आपको नग्न न देखने पाऊँ
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7175)
- **Original**: और केवल घृत हो मेरा आहार होगा-- [यही मेरी तीस प्रतिज्ञाएँ है]
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7176)
- **Original**: तब राजाने कहा--“ऐसा ही होगा ।/'
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7177)
- **Original**: तदनन्तर राजा पुरूरबाने दिन-दिन बढ़ते हुए आनन्दके साथ कभी अल्काप्रोके अन्तर्गत चैत्ररथ आदि यनॉमें और कधी सुन्दर पद्मखण्डॉंसे युक्त अति रमणीय मानस आदि सरोवरोंमें विहार करते हुए स्राठ हजार वर्ष ब्रित्त दिये
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7178)
- **Original**: उसके उपभोगसुखसे प्रतिदिन अनुरागके बढ़ते रहनेसे उर्वशीकों भी देवलोकमें रहनेकी इच्छा नहों रहो
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7179)
- **Original**: इधर, उर्वज्ञीके ब्रिना अप्सगओं, सिद्धों और गन्धवॉको स्वर्गलोक अत्यन्त रमणीय नहीं मालूम होता था
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7180)
- **Original**: अतः उर्वशी और पुरूरवाकी प्रतिज्ञके जाननेवाले विश्वावसुने एक दिन रात्रिके समय गन्धर्वोंके साथ जाकर उसके दायनागारके पाससे एक मेषका हरण कर लिया
- **Translation**: 

---

