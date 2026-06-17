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

### Verse 1 (Vishnu Puran 0.261)
- **Original**: है सत्तम ! इफहतर चतुर्युगसे कुछ अधिक* कारूका एक मन्यन्तर तोता है । यही मनु और देवता आदिका काल-है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.262)
- **Original**: इस प्रकार दिव्य वर्ष-गणतासे एक मन्वन्तरमें- आठ लाख बावन हजार वर्ष बताये जाते हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.263)
- **Original**: तथा हे मडामुने ! मानवी वर्ष-गणनाके अनुसार मन्वन्तरकः परिमाण पूरे तीस करोड़ सरसठ लाख बीस हजार वर्ष है, इससे अधिक नहीं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.264)
- **Original**: इस क्काल्का चौदह गुना ब्रह्माका दिन होता है, इसके अनन्तर नैमित्तिक नामवाल्त्र ब्राह्म-प्रलुय होता है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.265)
- **Original**: उस समय भूर््भ्ेक, भुवरस्भ्ेक और स्वस्प्रेंक तोनों जलने लगते हैं और महलोंकमों रहनेजाले सिद्धणण अति सन्तप्त होकर जनलोकको चले जाते हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.266)
- **Original**: इस प्रकार त्रिल्मेकीके जल्मय हो जानेपर जनलोकजासी योगियोंद्वारा ध्यान किये जाते हुए नारायणरूप कमलयोनि ब्रह्माजी तिस्थेकीके गराससे तृप्त होकर दिनके बरायर ही परिमाणवाली उस रात्रिमें शोषशय्यापर झयन करते हैं और उसके बीत जानेपर पुनः संसास्की सृष्टि करते हैं। 24-25
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.267)
- **Original**: इसी प्रकार (पक्ष, मास आदि) गणनासे ब्रह्माका एक वर्ष और फिर सौ वर्ष होते हैं। त्रह्माके सौ वर्ष हो उस महात्मा (ब्रह्मा) को परमायु हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.268)
- **Original**: हे अनघ ! उन ब्रह्माजोका एक परार्द्ध बोत चुका है । उसके अत्तमें पाद्य नामसे विख्यात महाकल्प हुआ था
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.269)
- **Original**: हे ट्विज ! इस समय वर्तमान उनके दूसरे परार्द्धको यह वाराह नामक पहला कल्प कहा गया है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.270)
- **Original**: कत- औै --++- इति श्रीविष्णुपुराणे प्रथमेंडशो तृतीयोउध्यायः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.271)
- **Original**: व्च्स्च्पन ज सब चोथा अध्याय ब्रद्माजीकी उत्पत्ति वराहपभगवानड्वारा पृथ्िवीका उद्धार और तह्याजीकी व्लेक-रचना श्रोमैत्रेय उवात्त ब्रह्मा नारायणाख्योउसो कल्पादी भगवान्यथा । आमैश्नेय खोछे-- है. महायुने ! कल्पके आदिें नाययणाख्य भगजान्‌ बद्याजीने जिस प्रकार समस्त सर्बभूतानि तदाच्नक्ष्य महामुने
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.272)
- **Original**: भूतोंकी रचना की वह आप वर्णन कीजिये
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.273)
- **Original**: इकहत्तर चतुर्युगके हिसानसे चौदह पन्जन्तरोंमें 994 चतुर्युग होते हैं. और ब्रह्माके एक दिनमें एक हजार चतुर्युग झोते हैं, अत: छ: चतुर्यु! और बचे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.274)
- **Original**: 7ः चतुर्युगक््र चौदहवाँ भाग कुछ कम पाँच हजार एक सौ तीन दिव्य वर्ष होता है, इस प्रक्यरें एक मन्यन्तरमें इकहनर चतुर्यृगके अतिरिक्त इतने दिव्य वर्ष और अधिक होते हैं ।
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.275)
- **Original**: 366 विस्तारिताक्षियुगलो राजान्तःपुरयोषिताम्‌ । नागरस्त्रीसमूहश्न॒ ड्रछूं न विरराम तम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.276)
- **Original**: 53 सख्यः पश्यत कृष्णस्य मुखमत्यरुणेक्षणम्‌ । गजयुद्धकृतायासस्वेदाग्बुकणिकाचितम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.277)
- **Original**: 54 विकासिशर्दम्भोजमवश्यायजलोक्षितम्‌ । परिभूय स्थित जन्म सफल क्रियतां दृश:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.278)
- **Original**: 55 श्रीवत्साडु महद्धाम बालस्यैतद्विलोक्यताम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.279)
- **Original**: विपक्षक्षपणं वक्षों भुजयुग्मं च भामिनि
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.280)
- **Original**: 56 कि न पश्यसि दुग्धेन्दुमुणालधवल्लाकृतिम्‌ । बलभ्द्रमिमम नीलपरिधानमुपागतम्‌
- **Translation**: 

---

