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

### Verse 1 (Vishnu Puran 0.9201)
- **Original**: फिर यशोदाने भी छकड़ेमें रखे हुए फूटे भाण्डोंके टुकड़ोंकी और उस छकड़ेक दही, पुष्प, अक्षत और फल आदिसे पूजा को
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9202)
- **Original**: इसी ,समय वसुदेजजोके कहनेसे गर्गाचार्यने गोपोंसे छिपे-छिपे गोकुलमें आकर उन दोनों खाल्कोके [ द्विजोचित ] संस्कार किये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9203)
- **Original**: उन दोनोंके नामकरण-संस्कार करते हुए महामति गर्गजोने बड़ेका नाम राम और छोटेका कृष्ण- बतलाया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9204)
- **Original**: 3322 स्वल्पेनैब तु कालेन रिश्विणौ तो तदा ब्रजे । घृष्टजानुकराौ विप्र बभूवतुरुभावपि
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9205)
- **Original**: 10 करीषभस्मदिग्धाड्ौ भ्रममाणात्रितस्ततः । न निवारयितुं शेके यशोदा तौ न रोहिणी
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9206)
- **Original**: 19 गोबाठमध्ये क्रीडन्तो वत्सवार्ट गतो पुनः । तद्हर्जातगोवत्सपुच्छाकर्षणतत्परो
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9207)
- **Original**: 12 यदा यशोदा तौ बाल्शवेकस्थानचराबुभौ । शशाक नो वारवितुं क्रीडन्तावतिचञ्जललौ
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9208)
- **Original**: 13 दाप्ला मध्ये ततो बद्ध्वा बबन्ध तमुलूखले । कृष्णमक्लिप्टकर्माणमाह चेदममर्षिता
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9209)
- **Original**: 14 यदि शक़ोषि गच्छ त्वमतिचश्ललचेष्टित । इत्युकत्वाथ निज कर्म सा चकार कुदुम्बिनी
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9210)
- **Original**: 15 व्यग्रायामथ तस्यां स कर्षमाण उलूखलम्‌ । यमलार्जुनमध्येन. जगाम कमलेक्षण:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9211)
- **Original**: 16 कर्षता वृक्षयोर्मध्ये तिर्यमातमुलूखलम्‌। भम्नावुत्तुडुशाखाग्रौ तेन तो यमलार्जुनो
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9212)
- **Original**: 17 ततः. कटकटाशब्दसमाकर्णनतत्पर: । आजगाम ब्रजजनो ददर्श च महादुमो
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9213)
- **Original**: 18 नवोद्ठताल्पदन्तांशुसितहासं च बालकम्‌। तयोरमध्यगत॑ दाप्ना बद्धं गाढं तथोदरे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9214)
- **Original**: 19 ततश्न दामोदरतां स ययौ दामबन्धनात्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9215)
- **Original**: 20 गोपबृद्धास्ततः सर्वे ननन्‍्दगोपपुरोगम्ताः । मन्त्रयामासुरुद्दिमा महोत्यातातिभीरव:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9216)
- **Original**: 21 स्थानेनेह न नः कार्य ब्रजामोउन्यन्महावनम्‌ । उत्पाता बहवो हात्र दृश्यन्ते नाइहेतवः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9217)
- **Original**: 22 पूतनाया विनाशश्व शकटस्थ विपर्ययः । बिना वबातादिदोषेण ट्रमयो: पतन तथा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9218)
- **Original**: 23 बृन्दावनपित:ः स्थानात्तस्मादृच्छाम मा चिरम्‌। यावद्धौममह्नेत्पातदोषो नाभिभवेद्व्जम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9219)
- **Original**: 24 इति कृत्वा मति सर्वे गमने ते ब्रजौकस: । ऊतचुस्स्व॑ स्व कुलं शीघ्र गम्बतां मा बिलम्बथ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9220)
- **Original**: 25 अ्रीविष्णुपुराण [अ9 6 है विप्र ! वे दोनों बालक थोड़े ही दिनोंगें गौओकि गोष्ठमें रेंगते-रेंगते हाथ और सुटनॉके बल्ठ चलनेवारे हो गये
- **Translation**: 

---

