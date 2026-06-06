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

### Verse 1 (Vishnu Puran 0.901)
- **Original**: जो शुद्धस्वरूप होकर भी उपचारसे परमेश्वर (परमा>महालक्ष्मी> ईश्वर-पति) अर्थात्‌ लक्ष्मीपति कहलाते हैं और जो समस्त देहधारियोंके आत्मा हैं वे श्रीविष्णुभगवान्‌ हमपर प्रसन्न हों
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.902)
- **Original**: जो कारण और कार्यरूप हैं तथा कारणके भी कारण और कार्यके भो कार्य हैं वे श्रीहरि हमपर प्रसन्न हों
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.903)
- **Original**: जो कार्य (महत्तत्त्व) के कार्य (अहंकार) का भी कार्य (तन्मात्रापद्धक) है उसके कार्य (भूतपञ्षक) का भी कार्य (ब्रह्माण्ड) जो स्वये है और जो उसके कार्य (वद्मा-दक्षादि) का भी कार्यघूत (अजापतियोंके पुत्र-पौत्रादि) है उसे हम प्रणाम करते हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.904)
- **Original**: तथा जो जगत्के कारण (ब्रह्मादि) का कारण (ब्रह्माण्ड) और उसके कारण (भूतपश्क) के कारण (पञ्ततन्मात्रा) के कारणों (अहँैकार-महत्तत्वादि) का भी हेतु (मूलप्रकति) है उस परसेश्वरक्रो हम प्रणाम करते हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.905)
- **Original**: जो भोक्ता और भोग्य, स्रष्टा और सृज्य तथा कर्त्ता और कार्यरूप स्वयं ही हैं उस परमपदक्ते हम प्रणाम करते हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.906)
- **Original**: जो विज्वुद बोधस्वकूप, नित्य, अजन्पा, अक्षय, अव्यय, अव्यक्त और अलिकारी है वही विष्णुका परमपद (परस्वरूप) है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.907)
- **Original**: जो न स्थूल है न सूक्ष्म और न किसी अन्य विशेषणका खिषय है वही भगवान्‌ विष्णुका नित्य-निर्मल परमपद है, हम उसको प्रणाम करते है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.908)
- **Original**: जिसके अयुतोश (दस हजारवें अंश) के अयुतांझमें यह विश्वरचनाकी ञ्क्ति स्थित है तथा जो परमअह्मस्वरूप है उस अव्ययको हम प्रणाम करते हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.909)
- **Original**: नित्य-युक्त योगिगण अपने पुण्य-पापादिका क्षय हो जानेपर 3*कारद्वारा चिन्तनोय जिस अबिनाझी पदक साक्षात्कार करते हैं बही भगवान्‌ विष्णुका पररपद है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.910)
- **Original**: जिसको देवगण, मुनिगण, झॉकर और मैं-- कोई भी नहीं जान सकते वही परमेश्वर श्रीविष्णुका परमपद है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.911)
- **Original**: जिस अभूतपूर्व देवकी ब्रह्मा, विष्णु और जझिवरूप दाक्तियाँ हैं कही भगवान्‌ विष्णुका परमफद है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.912)
- **Original**: हे सर्वेश्वर ! हे सर्वभूतात्मन्‌ ! हे सर्वरूष ! हे सर्वाधार : हे अच्युत ! हे बिष्णों ! हम भक्तॉपर प्रसन्न होकर हमें दर्शन दौजिये
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.913)
- **Original**: अीपराशरजी योले--अक्वाजीके इन उद्गारोक्तरे सुनकर देवगण भी प्रणाम करके बोले--'प्रभो ! हमपर प्रसन्न होकर हमें दर्शन दीजिये
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.914)
- **Original**: हे जगद्धाम
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.915)
- **Original**: आः्9 ] इत्यन्ते बचसस्तेषां देवानां ब्रह्मणस्तथा। ऊचुर्देवर्षयस्सर्वें बृहस्पतिपुरोगमा:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.916)
- **Original**: 60 आध्यो यज्ञपुमानील्ट: पूर्वेषां यश्च पूर्वज: । तन्नता: सम जगत्स्रष्ट: स्रष्टारमविशेषणम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.917)
- **Original**: 61 भ्रगवन्भूतभव्येश. यज्ञमूर््तिथराव्यय । असीद ग्रणतानां त्ब॑ सर्वेषां देहि दर्शनम
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.918)
- **Original**: 62 सर्वादित्यै: सम॑ पूषा पावको5यं सहाग्रिभि:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.919)
- **Original**: 63 अश्विनौ वसवश्चेमे सर्वे चैते मरुद्गणा:। साध्या विश्वे तथा देवा देवेन्रश्नायमीश्वर:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.920)
- **Original**: 6ड प्रणामप्रवणा नाथ दैत्यसैन्ये: पराजिता: । शरण त्वामनुप्राप्ता: समस्ता देवतागणा:
- **Translation**: 

---

