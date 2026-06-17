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

### Verse 1 (Sama Ved 0.2061)
- **Original**: ! हम आपका आवाहन करते हैं
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2062)
- **Original**: 795,वरुण: प्राविता भुवन्मित्रो विश्वाभिरूतिभि:। करतां नः सुराधस:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2063)
- **Original**: सभी रक्षा साधनों से युवत होकर मित्रावरुण हमें आश्रय प्रदान करें और हमें परम पवित्र धन प्रदान करें
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2064)
- **Original**: 796.इन्द्रमिद्गाथिनों बृहदिन्द्रमकेभिरकिंण:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2065)
- **Original**: इन्द्र वाणीरनूषत
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2066)
- **Original**: *.. सामगान के साथकों ने गाये जाने योग्य बृहत्‌ साम की स्तुतियों से देवराज इन्द्र का स्तवन किया है ; इसी तरह कऋऋत्वजों ने भी मन्रोच्चारण के द्वारा इद्धदेव की प्रार्थना की है
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2067)
- **Original**: 797.इन्द्र इद्ध्यों: सचा सम्मिश्ल आ बचोयुजा । इन्द्रो वद्री हिरण्यय:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2068)
- **Original**: बद्रधारी (विध्मनाशक) स्वर्णाभूषणों (श्रेष्ठगुणों) से युक्त इन्द्रदेव, श्रेष्ठ घोड़ों (शक््तिशालो प्रवृत्तियों) को वाणी के साध प्रयुक्त करते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2069)
- **Original**: 798.इन्द्र बाजेषु नो5व सहस््रप्रधनेषु च। उग्र उग्राभिरूतिभि:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2070)
- **Original**: हे वीरेन्द्र ! हजारों प्रकार के ऐश्वर्य की प्राप्ति के लिए होने वाले युद्ध (जीवन समर) में आप अपने प्रवल रक्षा साधनों से युक्त होकर हमारे रक्षक बनें
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2071)
- **Original**: 799.इन्द्रो दीर्घाय चक्षस आ सूर्य रोहयद्दिवि। वि गोभिरद्रिमैरयत्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2072)
- **Original**: (देवशबितयों के संगठक) इन्द्रदेब ने विश्व को प्रकाशित करने के महान्‌ उद्देश्य से सूर्यदेव को उच्चाकाश में स्थापित किया । उसी प्रकार किरणों से बादलों को प्रेरित किया
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2073)
- **Original**: ह 800.इन्द्रे अग्ना नमो बृहत्सुवृक्तिमेरयामहे
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2074)
- **Original**: धिया धेना अवस्थव:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2075)
- **Original**: इन्द्र और अग्निदेवों के पास अपने संरक्षण की कामना से हम अन्न (आहुतियों के माध्यम से) पहुँचाते हैं 31; पर्ण मरायोग से उनकी प्रार्थना करते हैं
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2076)
- **Original**: 806.ता हि शश्वन्त ईडत इत्था विप्रास ऊतये। सबाधो बाजसातये
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2077)
- **Original**: आजादि पोषक पदार्थों के लिए जब (सामान्य जन) झगड़ते हैं, तब ज्ञानीजन, इन्द्र और ऑअग्निदेतों से ऐसी (यज्ञों भं की जाने वाली) प्रार्थनाएँ करते हैं
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2078)
- **Original**: 802.ता वां गीर्मिविंपन्यव: प्रयस्वन्तो हवामहे
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2079)
- **Original**: मेधसाता सनिष्यव:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2080)
- **Original**: हम याज्निक स्तोता, धन प्राप्ति की इव्छा से, हविष्यान्त आदि पदार्थों के साथ, आप टोनों (इन्द्र और अग्नि) को प्रार्थना द्वारा आवाहित करते हैं
- **Translation**: 

---

