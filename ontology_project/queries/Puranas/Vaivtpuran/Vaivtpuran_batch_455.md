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

### Verse 1 (Vaivtpuran 23.2062)
- **Original**: + प्रकृतिखण्ड + 5 5.38 5 9 2 3 5
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.2063)
- **Original**: 8 8 8 8 8 8
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.2064)
- **Original**: 5 3 3 3 3 5
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.2065)
- **Original**: 3 8 8 8 8
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.2066)
- **Original**: 5 2 8 2 3 थे। वह सदा उनके साथ रहती थी। श्रीकृष्णका
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.2067)
- **Original**: आधे वाम-अड्भजसे “कमला” का प्रादुर्भाव हुआ वक्ष:स्थल ही उसका स्थान था। सौ मन्वन्तरका
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.2068)
- **Original**: और दाहिनेसे 'राधिका' का। उसी समय श्रीकृष्ण समय व्यतीत हो जानेपर उसने एक सुवर्णके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.2069)
- **Original**: भी दो रूप हो गये। आधे दाहिने अद्गभसे स्वयं समान प्रकाशमान बालक उत्पन्न किया। उसमें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.2070)
- **Original**: “द्विभुज' विराजमान रहे और बायें अड्भसे 'चार विश्वको धारण करनेकी समुचित योग्यता थी,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.2071)
- **Original**: भुजावाले विष्णु' का आविर्भाव हो गया। तब किंतु उसे देखकर उस देवीका हृदय दुःखसे संतप्त
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.2072)
- **Original**: श्रीकृष्णे सरस्वतीसे कहा-“देवी! तुम इन हो उठा। उसने उस बालकको ब्रह्माण्ड-गोलकके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.2073)
- **Original**: विष्णुकी प्रिया बन जाओ। मानिनी राधा यहाँ अथाह जलमें छोड़ दिया। इसने बच्चेकों त्याग
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.2074)
- **Original**: रहेंगी। तुम्हारा परम कल्याण होगा। इसी प्रकार दिया--यह देखकर देवेश्वर श्रीकृष्णने तुरंत उस [संतुष्ट होकर श्रीकृष्णने लक्ष्मीको नारायणकी देवीसे कहा--अरी कोपशीले! तूने यह जो
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.2075)
- **Original**: सेवामें उपस्थित होनेकी आज्ञा प्रदान की। फिर बच्चेका त्याग कर दिया है, यह बड़ा घृणित कर्म तो जगतूकी व्यवस्थामें तत्पर रहनेबाले श्रीविष्णु है। इसके फलस्वरूप तू आजसे संतानहीना हो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.2076)
- **Original**: उन सरस्वती और लक्ष्मी देवियोंके साथ बैकुण्ठ द्क्कसुण्य -3 पधारे। मूल प्रकृतिरूपा राधाके अंशसे प्रकट 4“ होनेके कारण वे देवियाँ भी संतान प्रसव करनेमें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.2077)
- **Original**: असमर्थ रहां। फिर नारायणके अड्भसे चार 1),
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.2078)
- **Original**: भुजावाले अनेक पार्षद उत्पन्न हुए। सभी पार्षद 5 गुण, तेज, रूप और अबस्थामें श्रीहरिके समान » #
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.2079)
- **Original**: थे। लक्ष्मीके अड्गसे उन्हीं-जैसे लक्षणोंसे सम्पन्न 6-4
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.2080)
- **Original**: करोड़ों दासियाँ उत्पन्न हो गयीं। मुनिवर नारद! इसके बाद गोलोकेश्वर जा। यह बिलकुल निश्चित है। यही नहीं, किंतु
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.2081)
- **Original**: भगवान्‌ श्रीकृष्णके रोमकूपसे असंख्य गोप प्रकट तेरे अंशसे जो-जो दिव्य स्त्रियाँ उत्पन्न होंगी, वे ; सभी तेरे समान ही नूतन तारुण्यसे सम्पन्न रहनेपर
- **Translation**: 

---

