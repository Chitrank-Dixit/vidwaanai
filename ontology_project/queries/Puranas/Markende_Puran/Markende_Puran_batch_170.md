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

### Verse 1 (Markende Puran 0.3381)
- **Original**: सर्वस्थरूपे सर्वेशे सर्वशक्तिसमन्सिते। भवेभ्यस्वराहि नो देवि दुर्गे देवि नमोउस्तु ते
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3382)
- **Original**: एतत्ते बदन सौप्मे॑ लोचनप्रवभूषितप्‌। पातु न; सर्वभीतिभ्य: कांत्यायनि नमो5स्तु ते
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3383)
- **Original**: ज्यालाकरालमत्थुग्रमशेषासुरसूदनम्‌ । अव्ोग्रतिषाश्य भागा यब्रारमों दस्युखलाति यत्र। यंत्र. तथाब्धिमध्ये तत्र स्थिता व परिषाप्ति विश्वम्‌
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3384)
- **Original**: विश्लेश्रवि त्व॑ परिषासि विर्श्न विश्वात्मिका थरबयप्तीति विश्वम्‌। विश्वेशवन्या भवती भ्रसन्ति विश्वाभ्रया यें त्वयि भ्क्तिनग्रा:
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3385)
- **Original**: देवि प्रसीद परिपालय चोअरिभीते- तिंत्य॑ यशासुरवथादधुनैव सद्य:। पापानि सर्वजगत्तों प्रशम भयाशु उत्पातपाकजनिर्ताश्ष मंहोपसगनि
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3386)
- **Original**: प्रणतानां प्रसीद त्थ॑ देवि विश्वार्ति्वारिणि। रक्षांसि दावानलों जिशूलं पातु नो भीतेभभद्रकालि नमो5स्तु ते
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3387)
- **Original**: तैलोक्ययासिनाभीड्ये लोकानां बरदा भव #ष 25 4 हिनस्ति दैत्यतेजांसि स्वनेनापूर्य या जगत्‌। ऋषि कहते हैं--
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3388)
- **Original**: देवोंके द्वारा वहाँ सा घण्टा पातु नो देवि पापेभ्योउन: सुतानिव
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3389)
- **Original**: महादैत्यपति शुम्भके मारे जानेपर इन्द्र आदि असुणसग्वसापक्कूनर्त्नितस्ते करोज्म्खल:
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3390)
- **Original**: देवता आग्निकों आगे करके उने कात्यायनी शुभाव खड़गो भवनु चण्डिके त्यां नता वयम्‌
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3391)
- **Original**: देवोको स्तुति करते लगे। उस समय अभीष्टकी रोगानशेषानपरईंसि तुष्टा ऋष्टा' तु कामान्‌ सकलानभीष्टनू। ल्‍्वामाअतानों न विपकन्नशणणां ग्रान्नि होनेसे उनके मुख-कमल दमक उठे थे और
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3392)
- **Original**: उनके प्रकाशसे दिशाएँ भी जगपगा उलठी थीं
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3393)
- **Original**: देंबता बोले-शरणागतकों पीड़ा दूर करनेवाली त्वाभाश्रिता हाश्रयतां प्रमानिं
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3394)
- **Original**: देवि! हमपर प्रसन्न होओ। सम्पूर्ण जगत्‌की माता! बत्कदने त्वयाह्म धर्मद्विणां देचि महासुराणाम्‌। रूपैरनेकैर्यहुधा 5 उत्ममूर्ति एतल्कूर्त प्रसन्न हौओ। विश्रेश्वरि ! विश्वकों रक्षा करो। देवि! तुम्हीं चराचर जगत्‌कों अधोंभ्वरी हो
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3395)
- **Original**: तुप इस जगतका एकमात्र आधार हो, क्योंकि पृध्चीरूपमें कृत्याम्बिके तत्पकरोति कान्या
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3396)
- **Original**: तुम्हारी ही स्थिति है। देवि! तुम्हारा पराक्रम विद्यासु शास्त्रेष_ विवेकदीपे- ध्याप्ेपु वाक्येषु च का त्वदन्या
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3397)
- **Original**: ममत्वगतेंउतिमहान्थकारे विश्रामयत्येतदतीन 6. फ0-पूँ। 2. पा0-रात्रे। 2, पा*-मह्ापाने। गाठ हैं, जो इम्र प्रकार ईै-- अलड्डनीत हैं। मुम्हों जलरूपमें स्थित होकर सम्पूर्ण जगत॒कों तृम्त करती हो
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3398)
- **Original**: तुम अनन्त बलसम्फ्म जैप्णवी शक्ति हो। इस बिश्वकी कारणभृता विश्वम्‌
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3399)
- **Original**: परा माया हों। देवि! तुमे इस सपस्त जगवकों 4. शान्तनवी टौकाक्ारने यहाँ एक श्लोक अधिक पाठ +सर्वतःपाणिपादारों रुवंतो5क्षिशिरोमसे। भ्र्ततः भ्रवणप्राणे तशायणि तमौउस्तु ते
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3400)
- **Original**: 232 मोहित कर रखा है। तुम्हीं प्रसन्न होनेपर इस
- **Translation**: 

---

