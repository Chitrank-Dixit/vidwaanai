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

### Verse 1 (Vaivtpuran 67.5995)
- **Original**: हैं, वे भगवान्‌ आपके बिना करोड़ों जन्मोंमें भी उसे संतोष नहीं है। प्राचीन कालमें इस मानिनीने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 67.5996)
- **Original**: साध्य नहीं हो सकते। अपने पिताके यज्ञमें मेरी निन्दा होनेके कारण
- **Translation**: 

---

### Verse 3 (Vaivtpuran 67.5997)
- **Original**: सूर्य, शिव, नारायणी माया, कला आदिकी अपने शरीरका त्याग कर दिया था और अब
- **Translation**: 

---

### Verse 4 (Vaivtpuran 67.5998)
- **Original**: दीर्घकालतक उपासना करनेके बाद मनुष्य भक्त- पुनः हिमालयके घरमें जन्म धारण किया है।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 67.5999)
- **Original**: संसर्गकी हेतुस्वरूपा कृष्णभक्तिको पाता है। यह सारा वृत्तान्त तो आप जानते ही हैं, आप
- **Translation**: 

---

### Verse 6 (Vaivtpuran 67.6000)
- **Original**: शिवजी! उस निष्पक्व भक्तिको पाकर भारतवर्षमें सर्वज्ञकों मैं क्या बतलाऊँ। तत्त्वज्ञ! इस विषयमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 67.6001)
- **Original**: बारंबार भ्रमण करते हुए जब भक्तोंकी सेवा आपकी क्‍या आज्ञा है? आप परिणाममें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 67.6002)
- **Original**: करनेसे उसकी भक्ति परिपक्व हो जाती है, तब शुभप्रदायिनी अपनी वह आज्ञा बतलाइये। नाथ!
- **Translation**: 

---

### Verse 9 (Vaivtpuran 67.6003)
- **Original**: भक्तोंकी कृपासे तथा देवताओंके आशीर्वादसे उसे मैंने सब कुछ निवेदन कर दिया है, अब जो
- **Translation**: 

---

### Verse 10 (Vaivtpuran 67.6004)
- **Original**: श्रीकृष्णमन्त्र प्राप्त होता है, जो परमोत्कृष्ट कर्तव्य हो, उसे बतानेकी कृपा कोजिये; क्‍योंकि
- **Translation**: 

---

### Verse 11 (Vaivtpuran 67.6005)
- **Original**: निर्वाणरूप फल प्रदान करनेवाला है। कृष्णब्रत परामर्शपूर्वक किया हुआ सारा कार्य परिणाममें
- **Translation**: 

---

### Verse 12 (Vaivtpuran 67.6006)
- **Original**: और कृष्णमन्त्र सम्पूर्ण कामनाओंके फलके प्रदाता सुखदायक होता है। हैं। चिर्कालतक श्रीकृष्णकी सेवा करनेसे भक्त श्रीनारायणजी कहते हैं--नारद! उस
- **Translation**: 

---

### Verse 13 (Vaivtpuran 67.6007)
- **Original**: श्रीकृष्ण-तुल्य हो जाता है। महाप्रलयके अवसरपर सभामें यों कहकर भगवान्‌ शंकरने कमलापति
- **Translation**: 

---

### Verse 14 (Vaivtpuran 67.6008)
- **Original**: समस्त प्राणियोंका विनाश हो जाता है-यह विष्णुकी स्तुति की और फिर त्रह्माके मुखकी [सर्वथा निश्चित है; परंतु जो कृष्णभक्त हैं, वे ओर देखकर वे चुप हो गये। शंकरजीका वचन
- **Translation**: 

---

### Verse 15 (Vaivtpuran 67.6009)
- **Original**: अविनाशी हैं। उन साधुओंका नाश नहीं होता। सुनकर जगदीश्वर विष्णु ठठाकर हँस पड़े और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 67.6010)
- **Original**: शिवजी! श्रीकृष्णभक्त अत्यन्त निश्चित होकर हितकारक तथा नीतिपूर्ण वचन कहने लगे।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 67.6011)
- **Original**: अविनाशी गोलोकमें आनन्द मनाते हैं। महेश्वर! श्रीविष्णुने कहा--पार्वती श्वर! आपकी पत्नी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 67.6012)
- **Original**: आप सबका संहार करनेवाले हैं, परंतु कृष्णभक्तोंपर सती संतान-प्राप्तिक लिये जिस उत्तम पुण्यक-
- **Translation**: 

---

### Verse 19 (Vaivtpuran 67.6013)
- **Original**: आपका वश नहीं चलता। उसी प्रकार माया ब्रतको करना चाहती है, बह ब्रतोंका सारतत्त्व, [सबको मोहग्रस्त कर लेती है, परंतु मेरी कृपासे स्वामि-सौभाग्यका बीज, सबके द्वारा असाध्य,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 67.6014)
- **Original**: वह भक्तोंकों नहीं मोह याती। नारायणी माया दुराराध्य, सम्पूर्ण अभीष्ट फलका दाता, सुखदायक,
- **Translation**: 

---

