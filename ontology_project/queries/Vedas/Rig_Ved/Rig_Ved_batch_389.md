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

### Verse 1 (Rig Ved 0.7761)
- **Original**: 3382. उत दासस्य वर्चिनः सहस्नाणि शतावशी:
- **Translation**: 

---

### Verse 2 (Rig Ved 0.7762)
- **Original**: अधि पउ्च प्रधीरिव
- **Translation**: 

---

### Verse 3 (Rig Ved 0.7763)
- **Original**: हे इन्द्रदेव ! चक्र के अरों के समान नियोजित संगठित होकर रहने वाले वर्चस्व्री दास के रिपुओं के पाँच लाख सैनिकों को आपने विनष्ट कर दिया था
- **Translation**: 

---

### Verse 4 (Rig Ved 0.7764)
- **Original**: 3383. उत तय पुत्रमग्रुवः परावृक्त शतक्रतु:। उक्थेष्विन्द्र आभजतू
- **Translation**: 

---

### Verse 5 (Rig Ved 0.7765)
- **Original**: . सैकड़ों यज्ञ सम्पन्न करने वाले इन्द्रदेव ने 'अग्रु' के पुत्र 'परावृक्त' को स्तोत्र पाठ में भाग लेने योग्य बनाया
- **Translation**: 

---

### Verse 6 (Rig Ved 0.7766)
- **Original**: 3384. उत त्या तुर्वशायदू अस्नातारा शचीपति: । इन्द्रो विद्ां अपारयत्‌
- **Translation**: 

---

### Verse 7 (Rig Ved 0.7767)
- **Original**: ययाति के शाप से पतित, विख्यात शासक 'यदु' तथा “तुर्वश' को शची के पति ज्ञानी इन्द्रदेव ने अभिषेक के योग्य बनाया
- **Translation**: 

---

### Verse 8 (Rig Ved 0.7768)
- **Original**: 3385, उत त्या सद्य आर्या सरयोरिन्द्र पारत:
- **Translation**: 

---

### Verse 9 (Rig Ved 0.7769)
- **Original**: अर्णाचित्ररथावधी:
- **Translation**: 

---

### Verse 10 (Rig Ved 0.7770)
- **Original**: हे इन्द्रदेव ! सरयू नदी के किनारे निवास करने वाले “अर्ण' तथा 'चित्ररथ' नामक आर्य शासकों को आपने तत्काल मार दिया था
- **Translation**: 

---

### Verse 11 (Rig Ved 0.7771)
- **Original**: 3386. अनु द्वा जहिता नयो5न्थं श्रोणं च वृत्रहन्‌। न तत्ते सुम्नमष्टवे
- **Translation**: 

---

### Verse 12 (Rig Ved 0.7772)
- **Original**: मं0 4 सूक्त 31 51 हे वृत्रहन्ता इन्द्रदेव ! समाज के द्वारा परित्याग किये गये अन्धों तथा पंगुओं को आपने अनुकूल रास्ते पर चलाया था । आपके द्वारा प्रदान किये गये सुख को हटाने में कोई सक्षम नहीं हो सकता
- **Translation**: 

---

### Verse 13 (Rig Ved 0.7773)
- **Original**: 3387, शतमश्मन्मयीनां पुरामिन्द्रो व्यास्यत्‌। दिवोदासाय दाशुषे 20
- **Translation**: 

---

### Verse 14 (Rig Ved 0.7774)
- **Original**: रिपुओं के सैकड़ों पाषाण विनिर्मित नगयों को इन्द्रदेव ने हवि प्रदाता दिवोदास के लिए प्रदान किया
- **Translation**: 

---

### Verse 15 (Rig Ved 0.7775)
- **Original**: 3388, अस्वापयद्भीतये सहस्रा त्रिंशतं हथै:
- **Translation**: 

---

### Verse 16 (Rig Ved 0.7776)
- **Original**: दासानामिन्द्रो मायया
- **Translation**: 

---

### Verse 17 (Rig Ved 0.7777)
- **Original**: उन इन्द्रदेव ने 'दभीति' के कल्याण के लिए अपनी सामर्थ्य के द्वारा असुरों के तीस हजार वीरों को हथियारों से मारकर सुला दिया
- **Translation**: 

---

### Verse 18 (Rig Ved 0.7778)
- **Original**: 3389. स घेदुतासि वृत्रहन्त्समान इन्द्र गोपतिः । यस्ता विश्वानि चिच्युषे
- **Translation**: 

---

### Verse 19 (Rig Ved 0.7779)
- **Original**: हे इद्धदेव ! आप उन समस्त रिपुओं को हिला देते हैं । हे वृत्र का संहार करने वाले इन्द्रदेव ! आप गौओं के पालक हैं । आप समस्त याजकों के साथ समान व्यवहार करते हैं
- **Translation**: 

---

### Verse 20 (Rig Ved 0.7780)
- **Original**: 3390, उत नून॑ यदिन्द्रियं करिष्या इन्द्र पौस्यम्‌। अद्या नकिष्टदा मिनत्‌
- **Translation**: 

---

