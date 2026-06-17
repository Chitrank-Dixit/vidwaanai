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

### Verse 1 (Vishnu Puran 0.841)
- **Original**: वे सुनिजन तो और ही हैं; तुम समझो, मैं तो दुर्वासा हूँ न 2
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.842)
- **Original**: गौतमादि अन्य मुनिजनेनि व्यर्थ ही तुझे इतना मुंह छूगा लिया है; पर याद रख, मुझ दुर्वासाका सर्वस्त तो क्षमा न करता ही है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.843)
- **Original**: दयामूर्ति जसिष्ठ आदिके बढ़-बढ़कर स्तुति करनेसे तू इतना गर्वीत्ग हो गया कि आज मेरा भी अपमान करने चल्त्र है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.844)
- **Original**: अरे ! आज त्रिल्परेकीमें ऐसा कौन है जो मेरे प्रज्वल्तित जराकल्मप और टेढ़ी भुकुटिकों देस्ककर भयभीत न हो जाय 2
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.845)
- **Original**: रे झातक्रतों ! तू बारम्बार समनुनथ-विनय करनेका दढोंग क्‍यों करता है ? तेरे इस कहने सुननेसे वया होगा ? मैं क्षमा नहों कर सकता
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.846)
- **Original**: श्रीपराशरजी बोछे--हे ब्रह्मन्‌ ! इस प्रकार कह ये खिप्रवर वहाँसे चल दिये और इन्द्र भी ऐेराबतपर चढ़कर अमरावतीको चले गये
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.847)
- **Original**: हे मैत्रेय ! तभीसे इन्द्रके सहित तीनों लोक बुक्ष-छता आदिकेः क्षीण हो जानेसे श्रीहीन और नष्ट-भ्रष्ट होने लगे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.848)
- **Original**: तबसे यज्ञॉका होना बन्द हो गया, तपस्वियोंने तप करना छोड़ दिया तथा ल्तेगोंका दान आदि घ्मो्ें चित्त नहीं रहा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.849)
- **Original**: हे ट्विजोत्तम ! सम्पूर्ण स्लेक स्थ्रेभादिके वशीभूत हो जानेसे सत्वशुन्य (सामर्थ्यहीन) हो गये और तुच्छ बस्तुओंकि हिल्ये भी स्प्रस्भयित रहने रूगो
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.850)
- **Original**: जहाँ सत्त्व होता है वहीं लक्ष्मी रहती है और सत्त्व भी लक्ष्मीका ही साथी है। श्रीहीनोयें भव्म सत्त्व कहाँ? और बिना सत्त्वके गुण
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.851)
- **Original**: आश्9 ] 0 अथम अं डर बलझशौर्याद्यभावश्च॒पुरुषाणां गुणैर्विना । लडुनीय: समस्तस्य बलशौर्यविवर्जित:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.852)
- **Original**: 30 भवत्यपध्वस्तमतिर्ल्लित: प्रथित: पुमान्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.853)
- **Original**: 31 एवमत्यन्तनि:श्रीके त्रैल्म्रेक्ये सत्त्ववर्जिते । देवान्‌ प्रति बलोदोग चक्ु्दैतियदानवा:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.854)
- **Original**: 32 लोभाभिभूता निःश्रीका दैत्या: सत्त्वविवर्जिता: । श्रिया विहीनैर्नि:स्त्वैर्देबश्चकुस्ततो रणम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.855)
- **Original**: 33 बिजिताख्दक्ञा दैल्यैरिन्दराद्या: शरणं ययुः । पितामह॑ महाभाग॑ हुताशनपुरोगमाः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.856)
- **Original**: 34 यथावत्कथितो देबैब्रह्मा प्राह ततः सुरान्‌ । परावरेश॑ हारणं त्रजध्वमसुरार्दनम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.857)
- **Original**: 35 उत्पत्तिस्थितिनाशानामहेतुं. हेतुमीश्वरम्‌ । अजापतिपति विष्णुपनन्तमपराजितम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.858)
- **Original**: 36 अधानपुंसोरजयो: कारणं कार्यभूतयो: । प्रणतार्त्तिहरं विष्णुं स व: श्रेयो विधास्यति
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.859)
- **Original**: 37 श्रीएराज्र उवाच एवमुक्त्वा सुरान्सर्वान्‌ ब्रह्म ल्ोकपितामह: । क्षीरोटस्योत्तरं त्तीर॑ तैरैेव सहितो ययौ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.860)
- **Original**: 38 सर गत्या ब्रिदशै: सर्वे: समवेतः पितामहः
- **Translation**: 

---

