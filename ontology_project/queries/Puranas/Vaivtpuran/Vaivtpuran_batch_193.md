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

### Verse 1 (Vaivtpuran 13.6590)
- **Original**: और पर्वतोंने पार्वतीसहित शंकरको प्रेरित किया, जलने कहा--प्रभो! कृत्तिकाओंने उस रोते
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.6591)
- **Original**: तब उन्होंने लाखों क्षेत्रपाल, भूत, बेताल, यक्ष, हुए शिशुको अपने घर लाकर और उसके भूखे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.6592)
- **Original**: कृष्माण्ड, ब्रह्मराक्षस, डाकिनी, योगिनी और होनेपर उसे अपने स्तनोंका दूध पिलाकर बढ़ाया।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.6593)
- **Original**: भैरवोंके साथ महान्‌ बल-पराक्रमसम्मन्न वीरभद्र, मया दत्त च तुभ्यं च यस्मै कस्मै न दास्यसि
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.6594)
- **Original**: पर॑ वर॑ सर्वपूज्य॑_ सर्वसंकटतारणम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.6595)
- **Original**: गुरुमभ्यर्ज विधिवत्‌ कबच धारयेतु. यः। कणष्ठे वा दक्षिणे जाहौँ सोउपि विष्णुर्न संशय:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.6596)
- **Original**: अश्रमेघसहलाणि शाजपेयशतानि च । ग्रहेन्द्र कबचस्थास्य कला नाहन्ति षोडशीम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.6597)
- **Original**: इ्द॑_ कव॒चमज्ञात्वा यो... भजेच्छ॑करात्मजम्‌ । शतलक्षप्रजप्रोषपि न॒ मन्त्र: सिद्धिदायक:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.6598)
- **Original**: (गणपतिखण्ड 13
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.6599)
- **Original**: 79-96)
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.6600)
- **Original**: 326 + संक्षिप्त ग्रह्मवैवर्तपुराण न्प %$%$%%$%%#%%%%%%%%%#%#####%% ## ##################### &############### ## ###&####### ## विशालाक्ष, शंकुकर्ण, कबन्ध, नन्दीश्वर, महाकाल,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.6601)
- **Original**: इन कृत्तिकाओंने तुम्हें पाया है। अब तुम अपने वज़दन्त, भगन्दर, गोधामुख, द्िमुख आदि
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.6602)
- **Original**: घर चलो। वहाँ तुम्हें सम्पूर्ण शस्त्रास्त्रोंकी प्राप्ति दूतोंको, जो धधकती हुई आगकी लपटके समान
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.6603)
- **Original**: होगी, विष्णु देवताओंको साथ लेकर तुम्हारा उद्दी्र हो रहे थे, भेजा। उन सभी शिव-दूतोंने, , अभिषेक करेंगे और तब तुम तारकासुरका वध जो नाना प्रकारके शस्त्रास्त्रोंसे सुसज्जित थे, शीघ्र
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.6604)
- **Original**: करोगे। तुम विश्वसंहर्ता शंकरके पुत्र हो, अतः ही जाकर कृत्तिकाओंके भवनको चारों ओरसे ये कृत्तिकाएँ तुम्हें उसी तरह नहीं छिपा सकतीं, घेर लिया। उन्हें देखकर सभी कृत्तिकाओंका मन
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.6605)
- **Original**: जैसे शुष्क वृक्ष अपने कोटरमें अग्निको गुप्त नहीं भयसे व्याकुल हो गया। तब वे ब्रह्मतेजसे उद्दी्त रख सकता। तुम तो विश्वमें दीप्तिमानू हो। इन होते हुए कार्तिकेयके पास जाकर कहने लगीं।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.6606)
- **Original**: कृत्तिकाओंके घरमें तुम्हारी उसी प्रकार शोभा नहीं कहा--बेटा कार्तिकिय ! असंख्यों हो रही है, जैसे महाकृपमें पड़े हुए चन्द्रमा कराल सेनाओंने भवनको चारों ओस्से घेर लिया
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.6607)
- **Original**: शोभित नहीं होते। जैसे सूर्य मनुष्यके हाथोंकी है और हमें पता भी नहीं है कि ये किसको हैं।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.6608)
- **Original**: ओटमें नहीं छिप सकते, उसी तरह तुम भी इनके तब कार्तिकेय बोले--माताओ
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.6609)
- **Original**: आपलोगोंका
- **Translation**: 

---

