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

### Verse 1 (Vishnu Puran 0.8341)
- **Original**: तौ च् मृगया- मुप्यातइशात्तनुदृष्ठा कृपया जग्राह
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8342)
- **Original**: ततः कुमार: कृषः कन्या चाश्वत्थाम्नो जननी कृपी ड्रोणाचार्यस्य पल्‍्यभवत्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8343)
- **Original**: दिवोदासस्थ पुत्रों मित्रायु:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8344)
- **Original**: मित्रायोइच्यवनो नाम राजा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8345)
- **Original**: च्यबना- त्सुदासः सुदासात्सौंदासः सौदासात्सहदेवस्तस्यापि सोमक:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8346)
- **Original**: सोमकाज्न्तुः पुत्रशतज्येष्टो- 5भवत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8347)
- **Original**: तेषां यवीयान्‌ पृषतः पृषताद- ब्रुपदस्तस्माश् धूष्टय्युम्नस्ततो धृष्टकेतु:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8348)
- **Original**: चतुर्थ अंझ 291 द्विजमीढका पुत्र यवीनर था
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8349)
- **Original**: उसका धृतिमान्‌, धृतिमानका सल्यधृति, सत्यधृतिका दुढनेमि, दृढनेमिक्ा सुपार्श्व, सुपार्श्रक्ा सुमति, सुमतिका सन्नतिमान्‌ तथा सन्नतिसान्‌का पुत्र कृत हुआ जिसे हिरण्यनाभने योगविद्याकी शिक्षा दी थी तथा जिसने प्राच्य सामग श्रुतियोंकी चौबीस संहिताएँ रची थीं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8350)
- **Original**: 49--52
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8351)
- **Original**: कृतका पुत्र उग्रायुध था जिसने अनेकों नीपवैज्ञीय क्षत्रियोंकीा. नाइा किया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8352)
- **Original**: उद्पायुधके , क्षेम्यके सुधीर, सुधीरके रिपुक्रय और रिपुकयसे बहुरथने जन्प लिया। ये सब पुरुर्वशीय राजागण हुए
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8353)
- **Original**: अजमीढकी नल्थनीनाम्नी एक भार्या थी। उसके नील नामक एक पूत्र दुआ
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8354)
- **Original**: नीलके झान्ति, शान्तिके हर्यश्॒ नामक पुत्र हुआ
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8355)
- **Original**: हर्यश्चके मुद्गल, सुञ्ञय ,बृहदिपु, यवीनर और काम्पिल्थ नामक पाँच पूत्र हुए। पिताने कहा था कि मेरे ये पुत्र मेरे आश्रित पाँचों देशॉकी रक्षा करनेसें समर्थ हैं, इसलिये ये पाशाल कहलाये
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8356)
- **Original**: मुद्रलसे मौद्ल्य नामक क्षत्रोपेत ब्राह्मणोंकी उत्पत्ति हुई
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8357)
- **Original**: सुद्रलसे बृहद् और बृहदश्वसे दिवोदास नामक पुत्र एवं अहल्या नामकी एक कन्याक्रा जन्म हुआ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8358)
- **Original**: अहल्यासे महर्षि गौतमके द्वारा शतानन्दक्यय जन्म हुआ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8359)
- **Original**: झतानन्दसे धनुर्वेदका पारदर्शी सत्पधृति उत्पन्न हुआ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8360)
- **Original**: एक चार अप्प्राऑमें श्रेष्ठ उर्बवशीकों देखनेसे सत्यधृतिका वीर्य स्खलित होकर ऋारस्तम्ब (सरकण्डे) पर पड़ा
- **Translation**: 

---

