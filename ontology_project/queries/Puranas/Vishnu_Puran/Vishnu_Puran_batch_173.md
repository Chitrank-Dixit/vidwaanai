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

### Verse 1 (Vishnu Puran 0.3441)
- **Original**: 3 तथा पूबबहः पापो बहिज्वालो हाध:झिरा: । सन्दंशः कालसूत्रश्न तमश्चावीचिरिव च
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3442)
- **Original**: डे श्वभोजनो5थाप्रतिष्ठक्षाप्रचिक्ष तथा पर: । इत्येबमादयश्रान्ये नरका भुझदारुणा:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3443)
- **Original**: 5 यमस्य विषये घोरा: दास्त्राअरभियदायिन: । पतत्ति येघषु पुरुषा: पापकर्मसतास्तु ये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3444)
- **Original**: 6 कूटसाक्षी तथाउसम्यक्पक्षपातेन यो बदेत्‌ । यश्चान्यदनृत वक्ति स नरो याति रौरवम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3445)
- **Original**: 7 भ्रूणहा पुरहन्ता च गोप्नश्च मुनिसत्तम । यान्ति ते नरक॑ रोध॑ यश्चोच्छुवासनिरोधक:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3446)
- **Original**: 8 श्रीपराह्रजी बोल्ले--हे विप्र ! तदनत्तर पृथिवी और जलके नीचे नरक हैं जिनमें पापी लोग गिराये जाते हैं। है महामुने ! उनका विवरण सुनो
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3447)
- **Original**: विदश्वसन, महाज्वाल, कृमीश, कृमिभोजन, असिफत्रवन, कृष्ण, स्मस्प्रभक्ष, दारुण, पूयवह, पाप, वहििज्बाल, अधः:शिरा, सन्देश, कालसूत्र, तमस्‌, आतवीचि, श्वभोजन, अप्रतिष्ठ और अप्रचि--ये सब तथा इनके सिच्रा और भी अनेकों महाभयड्भूर नरक हैं, जो यमराजके शञासनाधीन हैं और अति दारुण डास््र-भय तथा अग्रि-भय देनेवाले हैं और जिनमें जो पुरुष पापरत होते हैं वे ही गिरते हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3448)
- **Original**: जो पुरुष कूटसाक्षी (झूठा गवाह अर्थात्‌ जानकर भी न बतलानेबाल्मप्र या कुछ-का-कुछ कहनेवाल्त्र) होता है अथवा जो पक्षपातसे यथार्थ नहीं बोलता और जो मिथ्या-भाषण करता है बह रौरबनरकमें जाता है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3449)
- **Original**: है मुनिसत्तम ! भ्रूण (गर्भ) नष्ट करनेवाले ग्रामनाशक और गो-हत्यारे लोग रोघ नामक नसकमें जाते हैं जो
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3450)
- **Original**: आ0 6 ] सुरापो ब्रह्महा हर्ता सुवर्णस्य च सूकरे । अ्रयान्ति नरके यश्व तैः संसर्गमुपैति बै
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3451)
- **Original**: 9 राजन्यवैश्यहा ताले तथैय गुरुतल्पग: । तप्तकुण्डे स्वसृगामी हन्ति राजभटाँश्च यः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3452)
- **Original**: 10 साध्बीविक्रवकृद््धपाल:... केसरिविक्रयी । तप्तलोहे पतन्त्ेते यश्चव भक्त परित्यजेत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3453)
- **Original**: 119 खुषां सुतां च्रापि गत्वा महाज्वाले निपात्यते । अवमन्ता गुरूणां यो यश्चाक्रोष्टा नराधम:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3454)
- **Original**: 12 वेददूषयिता यश्न वेदक्क्रियिकक्ष यः। अगम्यगामी यश्च स्पात्ते यान्ति लवणं द्विज
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3455)
- **Original**: 13 चोरो विलोहे पतति मर्यादादूषकस्तथा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3456)
- **Original**: 14 देवद्विजपितृद्वेशा रत्रदूषषिता च यः। स याति कृमिभक्षे वै कृमीशे च दुरिष्टकृत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3457)
- **Original**: 15 पितृदेवातिर्थीसत्यक्तवा पर्यक्षाति नराधम: । ल्जलाभक्षे स यात्युग्रे झरकर्त्ता च वेधके
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3458)
- **Original**: 16 कग्रेति कर्णिनो यश्व यश्व खड़गादिकृन्नरः । प्रयान्येते विशसने नरके भुशदारुणे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3459)
- **Original**: 17 असत्मतिगृहीता तु नरके यात्यधोमुखे । अयाज्ययाजकश्चैव तथा नक्षत्रसूचक:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3460)
- **Original**: 18 बेगी पूथवहे चैको याति पिष्टान्नभुदनरः
- **Translation**: 

---

