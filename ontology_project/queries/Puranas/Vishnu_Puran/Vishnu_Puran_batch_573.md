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

### Verse 1 (Vishnu Puran 0.11441)
- **Original**: निशबरिशासिगदाशूलशक्तिकार्मुकशालिना
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11442)
- **Original**: 19 क्षणेन शार्डनिर्मुक्तेदशरैररिविदारणै:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11443)
- **Original**: गदाचक्रनिपातैश् ॒ सूदयामास॒तद्ठलम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11444)
- **Original**: 20 काशिराजबलं चैबं क्षय नीत्वा जनार्दन: । उबाच पौण्डुक॑ मूढमात्मचिह्लोपलक्षितम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11445)
- **Original**: 21 श्रीभगवापुवाच पोण्ड्कोक्त त्वया यत्तु दूतवक्त्रेण मां प्रति । समुत्सुजेति चिह्नानि तत्ते सम्पादयराम्यहम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11446)
- **Original**: 22 चअक्रमेतत्समुत्सृष्टं गदेय॑ ते बिसर्जिता । गरुत्मानेष चोत्सृष्टस्समारोहतु ते ध्वजम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11447)
- **Original**: 23 अश्रीपराइर उवाच इत्युश्वार्य विमुक्तेन चक्रेणासो विदारितः । पातितो गदया भग्नो ध्वजश्नास्थ गरुत्मता
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11448)
- **Original**: 24 ततो हाहाकृते छोके काशिपुर्यधिपों बली । युयुथे वासुदेवेन मित्रस्थापचितों स्थित:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11449)
- **Original**: 25 ततदशार्डधनुर्मुक्तिशिछत््ता तस्य शिरइझरै: । काशिपुर्या स चिक्षेप कुर्बल्लोकस्थ विस्मयम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11450)
- **Original**: 26 हत्वा त॑ पौण्डुक॑ शौरि: काझिराज च सानुगम्‌ । पुनर्द्धारव्तों प्राप्तो रेमे स्वर्गगतो यथा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11451)
- **Original**: 27 तच्छिर: पतितं तत्र दृष्ठा काशिपते: पुरे। जन: किमेतदित्याहच्छिन्ने केनेति विस्मित:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11452)
- **Original**: 28 सेना ले उपस्थित हुआ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11453)
- **Original**: तदनन्तर अपनी महान्‌ सेनाके सहित काशीनरेशकी सेना लेकर पौण्ड्क यासुदेव श्रोकृष्णचन्द्रके सम्मुख आया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11454)
- **Original**: भगबानते दूस्से हो उसे हाथमें चक्र, गदा, झार्ड-धनुष और पद्म लिये एक उत्तम रथपर बैठे देखा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11455)
- **Original**: श्रीहरिने देखा कि उसके कण्ठमें वैजयन्तीमात्म है, शरीरमें पीताम्बर है, गरुडरचित ध्यजा है और वक्षःस्थलमें श्रोवत्सचिह्न हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11456)
- **Original**: उसे नाना प्रकासके रत्रोंसे सुसज्जित किरीट और कुण्डछ धारण किये देखकर श्रीगरडध्वज भगवान्‌ गम्भीर भावसे हँसने लें
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11457)
- **Original**: और हे द्विज ! उसकी हाथी-घोड़ोंसे बलि तथा निश्तरिश खड़, गदा, शूल, शक्ति और घनुष आदिसे सुसज्जित सेनासे युद्ध करने छूगे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11458)
- **Original**: श्रीभगवानते एक क्षणमें ही अपने शार्ज्र-धनुषसे छोड़े हुए ऋष्रुऑको चिदीर्ण करनेवाले तीक्षण वाणों तथा गदा और चक्रसे उसकी सम्पूर्ण सेनाको नष्ट कर डाला
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11459)
- **Original**: इसी प्रकार काहिराजकी सेनाकों भी नष्ट करके श्रोजनार्दनने अपने चिड्डोंसे युक्त मूढ़नति पौण्डुकसे कहा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11460)
- **Original**: श्रीभगवान्‌ बोले--हे पौण्डक ! मेरे प्रति तूने जो दूतके मुखसे यह कहल्तया था कि मेरे चिह्नोंको छोड़ दे सो मैं तेंर सम्मुख ठस आज्ञाकों सम्पन्न करता हूँ
- **Translation**: 

---

