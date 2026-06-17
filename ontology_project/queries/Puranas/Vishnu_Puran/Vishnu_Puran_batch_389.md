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

### Verse 1 (Vishnu Puran 0.7761)
- **Original**: तदलमनेन , जीवता घातयित्वैन॑ तन्महारत्रं स्यम्न्तकारूयं त्वया कि न गृह्मते वयमभ्युप- त्य्थामों यद्यच्युतस्तवोपरि.. वैरानुबन्ध करिष्यतीत्येवमुक्तस्तथेत्यसावप्याह
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7762)
- **Original**: जतुगृहदग्धानां -पाप्छुतनयानां. बिद्ित- परमाथोंडपि भगवान्‌ दुर्योधनप्रयत्रदौधिल्य- करणार्थ कुल्यकरणाय वारणाबतं गत:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7763)
- **Original**: तदनत्तर जाम्बबानने पुनः प्रणाम करके उन्हें प्रसन्न किया और घर॒पर आये हुए भगवान्‌के लिये अध्यस्थरूप अपनी जाम्बबती नामकी कन्या दे दी तथा उन्हें प्रणाम करके मणिरत्र स्यमत्तक भी दे दिया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7764)
- **Original**: भगवान्‌ अच्युतने भी उस अति बिनीतसे लेने योग्य न होनेपर भी अपने कलूडू-शोधनके किये वह मणि- रन ले ल्था और जाम्बनतीके - सहित द्वारकामें आये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7765)
- **Original**: उस समय भगवान्‌ कृष्णचद्धरके आगमनसे जिनके इर्षका वेग अत्यन्त बढ़ गया है उन द्वास्कावासियॉमेंसे बहूत ढली हुई अवस्थावाट्डॉमें भी उनके दर्शानके प्रभावसे तत्काल ही मानो नवयौवनका सझ्लार हो गया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7766)
- **Original**: तथा सम्पूर्ण चादवगण और उनकी स्त्रियाँ 'अहोभाग्य ! अहोभाग्य !!' ऐसा कहकर उनकत्र अभिवादन करने लगीं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7767)
- **Original**: भगवानने भी जो-जो बात जैसे-जैसे हुईं थी सह ज्यॉ-की-त्यों यादत-ससाजमें सुना दी और सत्राजितकों स्थमन्तकमणि देकर मिध्या कलडूसे छुटकारा पा ट्त्या। फिर जाम्बबतोको अपने अनन्तःपुरमें पहुँचा दिया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7768)
- **Original**: 69--63
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7769)
- **Original**: सन्नाजितने भी यह सोचकर कि मैंने ही कृष्णचन्द्रको मिथ्या कलड्डू लगाया था, डरते-डरते उन्हें पत्नीरूपसे अपनी कन्या सत्यभामा विवाह दी
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7770)
- **Original**: उस कन्याको अक्रूर, कृतवर्मा और शतधन्वा आदि यादवोंने पहले वरण किया था
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7771)
- **Original**: अतः श्रीकृष्णचन्द्रके साथ उसे विवाह देनेसे उन्होंने अपना अपमान समझकर सत्राजित्से चैर बाँध लिया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7772)
- **Original**: ! तदनन्तर अक्रूर और कृतबर्मा आदिने शतघन्वासे कहा--
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7773)
- **Original**: “यह सत्राजित्‌ बड़ा ही दुष्ट है, देशो, इसने हमारे और आपके माँगनेपर भी हमत्अ्रेगोंको कुछ भी न समझकर अपनी कन्या कृष्णचन्द्रकों दे दी
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7774)
- **Original**: अतः आप स्यमन्तक महार्माण क्यों नहीं ले लेते हैं ? पीछे, यदि अच्युत आपरो किसी फ्रकारका विरोध करेंगे तो हमत्मेग भी आपका साथ देंगे।' उनके ऐसा कहनेपर शतथन्याने कहा--' बहुत अच्छा, ऐसा ही करेंगे”
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7775)
- **Original**: इसी समय पाण्डबॉके ल्लाक्षागहमें जलनेपर, यथार्थ बातको जानते हुए भी भगवान्‌ कण्णचन्द्र दर्योधनके प्रयत्लको शिथिल करनेके उद्देश्यसे कुलोचित कर्म करनेके लिये तारणातत नगरको गये
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7776)
- **Original**: गते क् तस्मिन्‌ सुप्तमेव सत्राजितं शतधन्वा जघान मणिरल्रं चाददात्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7777)
- **Original**: पितृवधामर्ष- पूर्णा च सत्यभामा शीभ्र स्थन्दममारूढा वारणावते अगवते5ह॑ प्रतिपादितेत्यक्षान्तिमता जैलोक्यं॑ भविष्यत्ति
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7778)
- **Original**: तदियं त्वदीयाप- हासना तदालोच्य यदत्न युक्ते तत्क्रियतापिति कृष्णमाह
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7779)
- **Original**: तया चैवपुक्त: परितुष्टान्तःकरणो5पि कृष्ण: सत्यभामाममर्षताम्रनयनः प्राह
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7780)
- **Original**: सत्ये सत्यं ममैवैषधापहासना नाहमेतां तस्य दुरात्मनस्सहिष्ये
- **Translation**: 

---

