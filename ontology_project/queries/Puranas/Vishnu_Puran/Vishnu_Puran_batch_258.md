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

### Verse 1 (Vishnu Puran 0.5141)
- **Original**: हे नृपश्रेष्ठ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5142)
- **Original**: शास्नोंमें जो-जो वर्णाश्रम-धर्म कहे हैं उन-उनका ही आचरण करके पुरुष विष्णुकी आराधना कर सकता है और किसी प्रकार नहीं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5143)
- **Original**: सगर खोले--हे द्विजश्रेष्त ! अब मैं सम्पूर्ण वर्णधर्म और आश्रमघर्मोको सुनना चाहता हूँ, कृपा करके वर्णन कीजिये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5144)
- **Original**: ओर्य ओले--जिनका मैं वर्णन करता हूँ, उन भ्रह्मण, क्षत्रिय, वैज््य और झूद्रेकि धर्मोक्मा तुम एकापथचित्त होकर क्रमत्ञाः श्रवण करों
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5145)
- **Original**: ब्राह्मणका कर्तव्य है कि दान दे, अज्ञोंद्रारा देवताओंका यजन करे, स्वाध्यायशील हो, नित्य ख्रान-तर्पण करे और अग्न्याधान आदि कर्म करता रहे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5146)
- **Original**: ब्राह्मणको उचित है कि वत्तिके लिये दूसरोंसे यज्ञ कराते, औरेंको पढ़ाये और न्यायोपार्जित शुद्ध ध्नपमेंसे न्‍्यायानुकूल द्रब्य-संगह् करे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5147)
- **Original**: ब्राह्मणको कभी किसोका अद्डित नहीं करना चाहिये और सर्वदा समस्त प्राणियोंके हितमें तत्पर रहना चाहिये। सम्पूर्ण प्राणियॉमें मैत्रो रखना हो ब्राद्मणका परम धन है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5148)
- **Original**: पत्थरमें और पराये रल्नमें ब्राह्मणको समान-बुद्धि रखनी चाहिये । हे यजन्‌ ! पत्नीके
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5149)
- **Original**: आः्8 ] दानानि द््वादिच्छातो द्विजेभ्यः क्षत्रियोषपि वा। यजेच्च विविधैर्यज्नरधीयीत च पार्थिव:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5150)
- **Original**: 26 शस्त्राजीयो महीरक्षा प्रवरा तस्य जीविका । तत्रापि प्रथम: कल्प: पृथिवीपरिपात्नम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5151)
- **Original**: 27 धरित्रीपालनेनेव कृतकृत्या नराधिपा: । भवन्ति नृपत्तेरेंशा यतो यज्ञादिकर्मणाम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5152)
- **Original**: 28 दृष्टानां शासनाद्राजा शिष्टानां परिपालनात्‌ । ्राप्नोत्यभिमताल्‍ीोकान्वर्णसंस्थां करोति य:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5153)
- **Original**: 29 पाशुपाल्यं च वाणिज्य कृषि च मनुजेश्वर । वैश्याय जीविकां ब्रह्मा ददौ ल्लेकपितामह:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5154)
- **Original**: 30 तस्थाप्यध्ययन यज्ञों दानं धर्मअ शस्यते। नित्यनैमित्तिकादीनामनुष्ठानं च कर्मणाम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5155)
- **Original**: 31 द्विजातिसंश्रितं कर्म तादर्थ्य तेन पोषणम्‌। क्रयविक्रयजैर्बापि धनै: कारूद्धवेन वा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5156)
- **Original**: 32 झूद्रस्प सन्नतिइशोौच्च सेवा स्वाभिन्यमायया । अमन्त्रयज्ञो ह्वास्तेयं सत्सज्रो विप्रसक्षणम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5157)
- **Original**: 33 दान चर द्याक्तुद्रोडपि पाकयज़ैर्यजेत च। पित्रयादिकं च तत्सव शुद्रः कुर्वीत तेन वै
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5158)
- **Original**: 34 भृत्यादिभरणार्थाय सर्वेषां न परिग्रह: । ऋतुकाले<भिगमन स्वदारेषु_ महीपते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5159)
- **Original**: 35 दया समस्तभूतेषु तितिक्षा नातिमानिता। सत्यं शौचमनायासो मड्ड्ल प्रियवादिता
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5160)
- **Original**: 36 पैत्यस्पृहा तथा तद्दकार्पण्य॑ नरेश्वर । अनसूया च सामान्यवर्णानां कथिता गुणा:
- **Translation**: 

---

