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

### Verse 1 (Markende Puran 0.3221)
- **Original**: उसे आते देख देवाने शह्ढु बजाबा और धनुषको प्रत्यज्लाका भी अत्यन्त दुस्सह शब्द किया
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3222)
- **Original**: साथ ही अपने घंटेके शब्दसे, जो समस्त दैत्य-सैविकरोकां तेज नष्ट करनेवाला था, सम्पूर्ण दिशाओंकों व्याप्त कर दिबा
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3223)
- **Original**: तदनत्तर सिंहने भी अपनी दहाड़से, जिसे सुनकर बड़े-बड़े गजराजोंकां महान्‌ मद दूर जो जाता था, आकाश, प्रृथ्वीं और दरों दिशाओंको गुँजा दिश.
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3224)
- **Original**: फिर कालीने आकाशमें उछलकर अपने दोनों हा्थोंसे पृथ्वीपर आघात क्िया। उससे ऐसा भंबंकर शब्द हुआ, झिससे पहलेके सभी शब्द शान्‍्त हो गये
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3225)
- **Original**: तत्पशथ्चात्‌ शिवदुतीने दैत्योँके लिये अमझ्ललजनक अट्टहास किया, इन शब्दोंकों सुनकर समस्त असुर थर्रा उठे; कितु शुम्भकों बड़ा क्रोध हुआ
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3226)
- **Original**: उस समय देवीने जन्म शुम्भकों लक्ष्य करके कहा--'जओ दुरात्मन्‌! खड़ा रह, खड़ा रह," तभी आकाशमें खड़े हुए देठता बोल उठे, “जय हो, जय हो'
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3227)
- **Original**: शुम्भने वहाँ आकर ज्व्वालाओंसे युक्त अत्वन्त भयानक शक्ति चलायी। अस्निपब पर्वतके समान आती हुई उस शक्तिको देवौने बड़े भारी लूके से दूर हटा दिया
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3228)
- **Original**: उस समझ शूुम्भक्के सिहनादसे तीनों लोक गूँज ठठे । गजन्‌ ! उसकी प्रतिध्वनिसे वच्भपातके समाग भ्यानक्त शब्द हुआ, जिसने अन्य सब्र शब्दोंक्रो जीत लिया
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3229)
- **Original**: शुम्भक्ते चलाये हुए बाणोंके देवोने और देवोके चलाबे हुए बाणोंके शुम्भने अपने भयंकर बार्णेद्वारा सैकड़ों और हजारों टुकड़े कर दिये
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3230)
- **Original**: तन क्रोधर्में भरी हुई चण्डिकराने शुम्भकों शुलसें मारा। डसके आछ्गतसे मूच्छित हो बह पृथ्वौपर #ए पड़ा
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3231)
- **Original**: 5. ण0-दोग्रदंड्रा0। 2. पा0-खण्डरूण्ड
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3232)
- **Original**: 225 हक कक ऋकऋ# फकछ प्रक्मध अमध्ाज मश् क # ह 75 हर 5 ततों निशुष्भ: स॒प्प्राष्य चेतनामाक्कार्मुक:। आजपघान शरैदेंबीं कालीं केसरिणं तथा
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3233)
- **Original**: पुनश्च॒कृत्वा बाहुनामचुर्त दनुजेश्वर:। अक्राबुधेन दित्तिजश्छादयाप्रास चणिडकामू
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3234)
- **Original**: ज़्ञतों भगवती क्कुद्धा दुर्गा दुर्गार्तिनाशिनी। चिच्छेद तानि चक्राणि स्वर्श/ सायकांख तानू
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3235)
- **Original**: ततो निशुम्भो वेगेन गदामादाय चण्डिकाम्‌। अभ्यधावत वै हन्तुं दैल्यसेनासमावृतः
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3236)
- **Original**: तस्यापतत एबाशु गदां चिच्छेद चण्डिका। खड्गेन शितथारेण स्॒ च॒ शूल समाददें
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3237)
- **Original**: शूलहस्त॑ समायान्त॑ निशुम्भमररार्दनम्‌
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3238)
- **Original**: हदि विव्याथ शूलेन सेगासिद्धेन त्ण्जिका
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3239)
- **Original**: भिन्नस्य तस्य शूलेन हृदयात्रि:सृतोऐऊपरः। प्रहाबलो महावीर्यस्तिछ्लेति पुरुषो बदन्‌
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3240)
- **Original**: तस्थ निष्क्रामतो देवी प्रहस्य स्वनशत्तत:। शिरश्निच्छेद स्वड्गेन त्ततोउस्रावपतद्धुत्रि
- **Translation**: 

---

