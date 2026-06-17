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

### Verse 1 (Vishnu Puran 0.2221)
- **Original**: “ये जो हाथियोंके वजके समान कठोर दाँत टूटःगये हैं इसमें मेरा कोई बल नहीं है; यह तो श्रीजनार्दनभगवानके महाविपत्ति और क्रेशॉके नष्ट करतेबाले स्मरणका ही प्रभाव है”'
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2222)
- **Original**: हिरण्यकशिपु बोल्शा-- रे दिग्गजों ! तुम हट जाओ । दैत्यगण
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2223)
- **Original**: तुप अग्नि जलाओ, और हे वायु ! तुम अग्निकों प्रज्यलित करों जिससे इस पापीको जल्मम डाला जाय
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2224)
- **Original**: । श्रीपराझरजी ओले--तब अपने स्वामीकी आज्ञासे दानवगण काप्ठके एक बड़े केरमें स्थित उस असुर राजकुमास्को अप्रि प्रज्वल्लित करके जलाने लगे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2225)
- **Original**: प्रह्मादजी बोले--हे तात ! पवनसे प्रेरित हुआ भी यह अग्नि मुझे नहीं जर्मता। मुझको तो सभी दिदाएँ, ऐसी शीतल प्रतीत होती हैं मानो मेरे चारों ओर कमल बिछे हुए हो
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2226)
- **Original**: श्रीपराशरजी बोले--तदनन्तर, शुक्रजीके पुत्र जड़े वाग्मी मह्मत्मा [ षण्डामर्क आदि ] पुरोहितगण सामनीतिसे दैत्यराजकी बड़ाई करते हुए बोले
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2227)
- **Original**: पुरोहित बोस्ठै--हे राजन! अपने इस बालक पुत्रके प्रति अपना क्रोध शात्त कीजिये; आपको तो देवताऑपर ही क्रोध करना चाहिये, क्योंकि उसकी सफलता तो वहीं है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2228)
- **Original**: है राजन्‌ ! हम आपके इस बाल्कको ऐसी शिक्षा देंगे जिससे यह विपक्षके नाशका कारण होकर आपके प्रति अति विनीत हो जायगा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2229)
- **Original**: है दैत्यराज ! बाल्यावस्था तो सब अकारके दोषोंका आश्रय होती ही है, इसल्यि आपको इस बालकपर अत्यन्त क्रोधका प्रयोग नहीं करना चाहिये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2230)
- **Original**: यदि हमारे कहनेसे भी यह विष्णुका पक्ष नहीं छोड़ेगा तो हम इसको नष्ट करनेके लिये किसी प्रकार न टलनेवाली कृत्या उत्पन्न करेंगे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2231)
- **Original**: श्रीपराहास्जीने कहा--पुरोहितोंके इस प्रकार प्राथना करनेपर दैत्यराजने दैत्योँड्वाए प्रह्मादको अग्निसमूहसे बाहर निकलयाया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2232)
- **Original**: फिर प्रह्ादजी, गुरुजोके यहाँ रहते हुए उनके पढ़ा चुकनेपर अन्य अध्यापयामास मुहरुपदेशान्तते गुरोः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2233)
- **Original**: दानवकुमारोंको बार-बार उपदेश्ञ देने छगे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2234)
- **Original**: अह्वाद उवाच श्रूयतां परमार्थो मे दैतेया दितिजात्मजा: । न चान्यथैतन्मन्तव्यं नात्र छोभादिकारणम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2235)
- **Original**: 55 जन्प बाल्य॑ ततः सर्वो जन्तुः प्राप्नोति यौवनम्‌। अव्याहतैब भवति ततोउनुदिवर्स जरा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2236)
- **Original**: 56 ततश्च मृत्युमभ्येति जन्‍्तुददैत्येश्वरात्मजा: । प्रत्यक्ष दृश्यते चैतदस्माक भवता तथा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2237)
- **Original**: 57 मृतस्य च॒ पुनर्जन्म प्रवत्येतश् नान्यथा। आगसमो3यं तथा यश्व नोपादान॑ विनोद्धवः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2238)
- **Original**: 58 गर्भवासादि याखत्तु पुनर्जन्मोपपादनम्‌। समस्तावस्थक॑ तादहु:ग्मेबावगम्यताम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2239)
- **Original**: 59 क्षृत्ृष्णोपश्म॑ तद्वच्छीताह्युपशमं सुख्म्‌। मन्यते बालबुद्धित्वाहुःखमेब हि तत्पुन:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2240)
- **Original**: 60 क्व कान्तिशो भासन्दर्यरमणीयादयो गुणा:
- **Translation**: 

---

