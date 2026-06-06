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

### Verse 1 (Markende Puran 0.541)
- **Original**: उपलक्ष्याण जणानीथ्रान्सुक्ताोां हरकादनु
- **Translation**: 

---

### Verse 2 (Markende Puran 0.542)
- **Original**: दया भृतेषु सदवाद; पस्लोकत्रतिक्रिया
- **Translation**: 

---

### Verse 3 (Markende Puran 0.543)
- **Original**: सत्व॑ भूतहितार्थोक्तिजेंदप्रामाष्वदर्शनार्‌ । गुरुटेबर्षिसिद्धर्षिपूजर साधुसड्भम+
- **Translation**: 

---

### Verse 4 (Markende Puran 0.544)
- **Original**: सत्क्रियाध्यसन पैजीमिति बुध्येत पर्डित॑: । आन्याति चैव सऊर्मक्रेसाभूताति यानि च
- **Translation**: 

---

### Verse 5 (Markende Puran 0.545)
- **Original**: स्वर्गच्युतानां. लिड्रानि. उध्षराणामपापिनाम्‌
- **Translation**: 

---

### Verse 6 (Markende Puran 0.546)
- **Original**: (30 15। 31--डेंड 5) [पुत्र डबाच है तत्तस्‍्तमग्रत: कृत्वा स॒राणा गनुपुद्यतः। तदश्व सर्वरत्कु्ट यातनास्थायिर्भिनृभि:
- **Translation**: 

---

### Verse 7 (Markende Puran 0.547)
- **Original**: प्रसाईं कुरु भूषेति तिष्ठ वायन्मुद्र्॑तकाय्‌ । त्वदज्ञसज्ञी पथनों भनो ह्रादयते हि न:
- **Translation**: 

---

### Verse 8 (Markende Puran 0.548)
- **Original**: परितापं च मात्रेश्यः पीडाबाधाथ कृत्स्नश:। अपहन्ति नःव्यात्र द्सा कुरु महीपत्ते
- **Translation**: 

---

### Verse 9 (Markende Puran 0.549)
- **Original**: एतच्छुत्वा यचस्तेधां त॑ यान्यपुरुष॑ नृष:। थप्च्छ कथनेतेषामाह्ादों मश्रि तिप्ति
- **Translation**: 

---

### Verse 10 (Markende Puran 0.550)
- **Original**: किं मा कर्म तत्‌ पुण्य॑ मर्त्थलोके महत्‌ कृतम्‌
- **Translation**: 

---

### Verse 11 (Markende Puran 0.551)
- **Original**: आउ्लार्ददायिती बू्टियेनेये. रुद्दुदीरप
- **Translation**: 

---

### Verse 12 (Markende Puran 0.552)
- **Original**: (अ> 15। 47--»59)
- **Translation**: 

---

### Verse 13 (Markende Puran 0.553)
- **Original**: 48 #मंक्षिप्त मार्कण्डेय पुराण * 222 2::0 774 # ## «8 8 # 464 5:5:::77:2 72:05 59% 74774 444 ##:%65:::::2:2 2:27 07 44 #& 6 #: अमदत्तते कहा--2/जन्‌! आपका चह शरोर , जिसका मठ सक्लूटमें पड़े हुए प्राणियोंकी रक्षा पितरों, देवताओं, अतिथियों और भ्रृत्तजनोंसे बचे
- **Translation**: 

---

### Verse 14 (Markende Puran 0.554)
- **Original**: करनेगें नहीं लगता, ठसके बज्ञ, दान और तप हुए अनज्नके सेजनसे पृष्ठ हुआ है तथा आपका मन
- **Translation**: 

---

### Verse 15 (Markende Puran 0.555)
- **Original**: इहलोक और परलोकमें भी कल्याणके साधन भी इन्हींक़ीं सेचार्मे संल
- **Translation**: 

---

### Verse 16 (Markende Puran 0.556)
- **Original**: रहा हैं। इसीलिये
- **Translation**: 

---

### Verse 17 (Markende Puran 0.557)
- **Original**: नहीं होते। जिसका हृदय बालक, वृद्ध तथा आपके श़रोरको छूकर बहनेवाली वायु आरन्ददायिनी
- **Translation**: 

---

### Verse 18 (Markende Puran 0.558)
- **Original**: आतुर प्राणियोंके प्रति कठोरता धारण करता जान पड़ती है और इसके लगनेसे इन पापियोंको
- **Translation**: 

---

### Verse 19 (Markende Puran 0.559)
- **Original**: है, मैं उसे मनुष्य नहों मायता: वह तो निरा नरककी णातता कष्ट नहीं पहुँचाती! आपने अंश्वमेध राक्षस है। माना, इनके निकट रहनेसे अग्निजनित आदि यन्ञॉका विधिपूर्वक अनुष्ठान किया हैं; अठ: संतापका कष्ट स्रहता होगा, नरककी भयात्क आपके दर्शनसे यमलोकके यन्त्र, शस्त्र, औन
- **Translation**: 

---

### Verse 20 (Markende Puran 0.560)
- **Original**: दुर्गन्धक्रा भोग करना पड़ेगा, भूख-प्यासका और कौए आदि पक्षी, जो पीड़न, छेदन और
- **Translation**: 

---

