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

### Verse 1 (Vishnu Puran 0.12321)
- **Original**: सबके प्राणस्वरूप उस वायुमें जब अम्निका प्रकाशक रूप लीन हो जाता है तो रूप-तन्मात्राके नष्ट हो जानेसे अभ्नि रूपहीन हो जाता है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12322)
- **Original**: उस समय संसारके प्रकाशहीन और तेजके बायुमें लीन हो जानेसे अप्नि शान्त हो जाता है और अति प्रचण्ड वायु चलने छगता है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12323)
- **Original**: तब अपने डद्भव- स्थान आकाशका आश्रय कर वह प्रचण्ड यायु ऊपर-नोचे तथा सब ओर दसों दिशाओंमें बड़े लेगसे चछने त्कगता है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12324)
- **Original**: तदनन्तर वायुके गुण स्पर्शको आकाश लीन कर लेता है; तब वायु झन्त हो जाता है और आकाश आवरणहीन हो जाता है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12325)
- **Original**: उस समय रूप, रस, स्पर्ती, गन्‍्ध तथा आक्यरसे रहित अत्यन्त महान्‌ एक आकाश ही सबको व्याप्त करके प्रकाशित होता है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12326)
- **Original**: आअ*ड ] परिमण्डलं च सुषिरमाकाशं शब्दलक्षणम्‌ । शब्दमात्र तदाकाशं सर्वमावृत्य तिध्ठति
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12327)
- **Original**: 26 ततइशब्दगुणं तस्थ भूतादिर्भसते पुनः । भूतेन्द्रियिष. युगपद्धृूतादौ संस्थितेषु वै। अभिमानात्मको ह्वोष भूतादिस्तामसस्स्मृत:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12328)
- **Original**: 27 भूतादि ग्रसते चापि महान्वै बुख्धिलक्षण:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12329)
- **Original**: 28 उर्वी महांश्व जगतः प्रान्तेडन्तर्बाह्मतस्तथा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12330)
- **Original**: 29 एवं सप्त महाबुद्धे क्रमात्मकृतयस्स्मृता: । प्रत्याहारे तु तास्सर्वा: प्रव्िद्न्ति परस्परम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12331)
- **Original**: 30 येनेदमावृतत सर्वमण्डमप्सु. प्रल्लीयते । सप्नद्वीपसमुद्रान्त॑ सप्तक्ोके सपर्वतम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12332)
- **Original**: 31 उदकावरणं यत्तु ज्योतिषा पीयते तु तत्‌। ज्योतिर्वायौ लय॑ याति यात्याकाशे समीरण:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12333)
- **Original**: 32 आकाझं चैब भूतादिय्रेसते त॑ तथा महान्‌। महान्तमेभिस्सहित प्रकृतिर्ग्रतते द्विज
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12334)
- **Original**: 33 गुणसाम्यमनुद्रिक्तमन्यूनं च महामुने । प्रोच्यते प्रकृतिहंतु: प्रधान कारण परम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12335)
- **Original**: 34 इत्येषा प्रकृतिस्सर्बा व्यक्ताव्यक्तस्वरूपिणी । व्यक्तस्वरूपमव्यक्ते तस्मान्मैत्रेय लीयते
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12336)
- **Original**: 35 एकइशुद्धोक्षरो नित्यस्सर्वव्यापी तथा पुमान्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12337)
- **Original**: सोउप्यंशस्सर्वभूतस्य॒मैत्रेय परमात्मन:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12338)
- **Original**: 36 न सन्ति यत्र सर्वेशे नामजात्यादिकल्पना: । सत्तामात्रात्मके ज्ञेये ज्ञानात्मन्यात्मनः परे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12339)
- **Original**: 37 तदूहा परम॑ धाम परमात्मा स चेश्वर: । स॒विष्णुस्सर्वमेवेदे यतो नावर्तते यति:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12340)
- **Original**: 38 प्रकृति मया55ख्याता व्यक्ताव्यक्तस्वरूपिणी । पुरुषश्चाप्युभावेती लीयेते परमात्मनि
- **Translation**: 

---

