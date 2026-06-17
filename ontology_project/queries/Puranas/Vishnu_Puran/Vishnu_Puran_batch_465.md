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

### Verse 1 (Vishnu Puran 0.9281)
- **Original**: वे दोनों कभी गौओंके साथ मनोहर गान और तान छेड़ते तथा कभी अत्यन्त ज्ञोतल वृक्षतल्का आश्रय लेते हुए बिचरते रहते थे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9282)
- **Original**: वे कमी तो कदम्ब-पुष्पोंके हारसे विचित्र वेष बना लेते, कभी मयूर- पिच्छकी माल्मसे सुझोभित होते और कर्भी नाना प्रकारकी पर्वतीय धातुओंसे अपने शरीरक्रो लिप्त कर केते
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9283)
- **Original**: कभी कुछ झपको लेनेकी एच्छासे पत्तोंकी दाय्यापर फेट जाते और कभी मेघके गज्नेपर 'हा हा' करके कोलाहल मचाने लगते
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9284)
- **Original**: कभी दूसरे गोपोदि: गानेपर आप दोनों उसकी प्रशसा करते और कभी ग्वाल्लेकी-सी बाँसुगी बजाते हुए मयूरकी बोलीका अनुकरण करने लगते
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9285)
- **Original**: इस प्रकार ये दोनों अत्यन्त प्रीतिके साथ नाना प्रकारके भावोंसे परस्पर खेलते हुए प्रसन्नचित्तसे उस वनमें खिचरने लगे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9286)
- **Original**: सायछूलके समय वे महाबल्मी बालक बनमें यथायोग्य विहार करनेफे अनन्तर गौ और ग्वाल्यालॉके साथ वजयें ल्लौट आते थे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9287)
- **Original**: इस तरह अपने समवयस्क गोपगणके साथ देवताओंके समान क्रीड़ा करते हुए वे महातेजस्वी राम और कृष्ण वहाँ रहने छरे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9288)
- **Original**: अन्‍न्‍ममन्‍_ नह उाला+-तऋ इति श्रीविष्णुपुराणे पश्चमें5ऐे पष्टोउध्यायः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9289)
- **Original**: आन औ “---
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9290)
- **Original**: आ 7] क्षय अंश आर शरव सातवाँ अध्याय कालिय-दमन औपराशर उवात्त श्रीपराशरजी खोके--एक दिन रामको बिना साथ एकदा तु बिना राम॑ कृष्णों वृन्दावन ययो ।..
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9291)
- **Original**: लिये कृष्ण अकेले ही वृल्दावनको गये और वहाँ वन्य विचचार वृतो गोपैर्वन्यपुष्पस्नरगुज्ज्वलः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9292)
- **Original**: पुष्पोंकी माल्मऑसे सुशोभित हो गोपगणसे घिरे हुए विचरने लगे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9293)
- **Original**: घूमते-घूमतें लें चआल तस्क्लोंसे 4 तीरसंलप्रफेनौचैहंसन्तीमिव काहिन्दी ललोलकस्त्पेलझालिनीम्‌ शोभित यमुनाके तटपर जा पहुँचे जो किनारोंपर फेनके तीरसंलप्रफेनोवैहसन्तीमिव सर्वतः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9294)
- **Original**: 2 इकट्ठे हो जानेसे मानों सब ओरसे हैंस रही थी
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9295)
- **Original**: तस्वाज्नातिमहाभीम॑ विधाभिशभ्रितवारिकम्‌ । यमुनाजोमें. उन्होंने विषाग्रिसे सन्‍्तम्त जलवाला हुदे. कालियनागस्यथ दर्दर्शातिविभीषणम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9296)
- **Original**: $3 विधाभिना प्रसरता दमग्धतीरमहीरुहम
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9297)
- **Original**: वाताहताम्बुविक्षेपस्पर्शदग्धविहड्जरमम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9298)
- **Original**: 4 तमतीव महारौद्र प्रृत्युवक्त्रसिवापरम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9299)
- **Original**: विलोक्य चिन्तयामास भगवान्मधुसूदन:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9300)
- **Original**: 5 अस्मिन्‍्बसति दुष्टात्मा कालियोउसौ विषायुध: । यो मया निर्जितस्त्थकत्वा वुष्टो नष्ट: पयोनिधिम
- **Translation**: 

---

