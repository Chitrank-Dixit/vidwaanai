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

### Verse 1 (Vishnu Puran 0.4221)
- **Original**: (ज़सेबकका गला काट डाला और अपने पार्षदोंसहित ततस्सौवीरराजस्य प्रयातस्थ मह्ात्मन: । उसका तीखा राधिर पान किया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4222)
- **Original**: 48---50 । विष्टिकर्ताथ मन्येत बिष्टियोग्योउयमित्यपि
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4223)
- **Original**: 59 कि 03003 दिन #2+5औ 0000. श्अ जा छ 5" । उस समय उनके समझा कि यह ते तादृ् महात्मानं भस्मच्छन्नमिवानलम्‌।
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4224)
- **Original**: ब्ेगारके हो योग्य है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4225)
- **Original**: राजाके सेवकोॉने भी भस्ममें क्षता सौवीरराजस्य विष्टियोग्यममम्यत
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4226)
- **Original**: 52 छिप हुए अभिके समान उन महात्माका रघ्ज-कड़ देखकर स राजा शिबिकारूढ़ो गन्तुं कृतमतिद्विज उन्हें बेगारके योग्य समझा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4227)
- **Original**: हे द्विज। उन पूछनेके लिये कि 'इस्र दुःख़मय संसारमें मनुष्योंका श्रेय श्रेयः किमन्न संसारे दुःखप्राये नृगामिति।
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4228)
- **Original**: किसमें है" शिविक्रापर चढ़कर इक्षमती नदीके किनारे उन प्रद्ठुं ते मोक्षथ्र्मज्ञ॑ं कपिलाख्य॑ महामुनिम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4229)
- **Original**: महर्षिके आश्रमपर जानेका विचार किया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4230)
- **Original**: . तब राजसेवकके कहनेसे भरत मुनि भी उसकी उबाह शिबिकां तस्य क्षत्तुबंचनचोदित । पालकीकों अन्य बेगारियोंके बीचमें छगकर वहन करने नृणां विष्टिगृहीतानामन्येषां सोडपि मध्यग:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4231)
- **Original**: 55 लगे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4232)
- **Original**: इस प्रकार बेगारमें फ्कड़े जाकर अपने शृहीतो विष्टिना विष्र: सर्वज्ञानेकभाजनः । पूर्वजन्मका स्मरण रखनेवाले, सम्पूर्ण बिज्ञानके एकमात्र जातिस्मरो सौ पापस्य क्षयंकाम उबाह ताम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4233)
- **Original**: परत जे विप्रवर अपने पापमय प्रारब्धका क्षय करनेके लिये उस्र शिब्रिकाको उठाकर चलने छगे।
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4234)
- **Original**: ये ययौ जडमतिः सो5थ युगप्रात्रावलोकनम्‌ । बुद्धिमानोंमें श्रेष्ठ द्विजबर तो चार हाथ भूमि देखते हुए कुर्वन्मतिमतां श्रेष्ठस्तवन्ये त्वरित ययु:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4235)
- **Original**: मन्द-गतिसे चलते थे, किन्तु उनके अन्य साथी जल्दी-
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4236)
- **Original**: अ* 13 ) बिल्लोक्य नृषतिः सो5थ विषमां शिव्षिकागतिम्‌ । क्रिमेतदित्याह सम॑ गम्यतां शिबिकावहाः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4237)
- **Original**: 58 पुनस्तधैव शिबिकां बिलोक्य विषमां हिस: । नृपः: किमेतदित्याह भवद्धिर्गम्यतेउन्यथा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4238)
- **Original**: 59 भूपतेर्यदतस्तस्य॒श्रुल्वेत्यं बहुशो बच:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4239)
- **Original**: शिबिकाबाहका:ः प्रोचुरयं यातीत्यसत्वरम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4240)
- **Original**: 60 ए्जोवाच कि श्रान्तोउस्यल्पमध्वान त्वयोढा शिश्रिका मम । 'किमायाससहो न त्व॑ं पीवानसि निरीक्ष्यसे
- **Translation**: 

---

