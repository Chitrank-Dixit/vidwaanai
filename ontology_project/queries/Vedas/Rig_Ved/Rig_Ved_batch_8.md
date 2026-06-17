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

### Verse 1 (Rig Ved 0.141)
- **Original**: छन्द- गायत्री
- **Translation**: 

---

### Verse 2 (Rig Ved 0.142)
- **Original**: ] 61. इन्द्रमिद्‌ गाथिनो बृहदिन्द्रमकेभिरकिंण:। इन्द्र वाणीरनूषत
- **Translation**: 

---

### Verse 3 (Rig Ved 0.143)
- **Original**: सामगान के साधकों ने गाये जाने योग्य वृहत्‌साम की स्तुतियों ( *गाथा ) से देवराज इद्ध को प्रसन्‍न किया है । इसी तरह याज्ञिकों ने भी मन्त्रोच्चारण के द्वारा इन्द्रदेव की प्रार्थना को है
- **Translation**: 

---

### Verse 4 (Rig Ved 0.144)
- **Original**: [* गाला शब्द गान या पद्म के आर्थ में आया हूँ इसे मंत्र या कक के स्तर का नहीं पाना जाता ।] 62. इन्द्र इद्धयों: सचा सम्मिशल आ वचोयुजा। इन्द्रो वज्री हिरण्यय:
- **Translation**: 

---

### Verse 5 (Rig Ved 0.145)
- **Original**: संयुक्त करने की क्षमता वाले, वज्रधारी, स्वर्ण-मण्डित इन्द्रदेव , बचन मात्र के इशारे से जुड़ जाने वाले अश्वों के साथी हैं
- **Translation**: 

---

### Verse 6 (Rig Ved 0.146)
- **Original**: ['वीय॑ वा अश्कः ' के अनुसार पराक्रम ही अश्व है। जो पराक्रमी समय पर संकेत मात्र से संगठित हो जायें, इच्ध देवता उनके साथी हैं, जो अहंकारवश बिखरे रहते हैं, वे इच्धदेव के प्रिय नहीं हैं। ] 63. इन्द्रो दीर्घाय चक्षस आ सूर्य रोहयद्‌ दिवि। वि गोभिरद्रिमैरयत्‌
- **Translation**: 

---

### Verse 7 (Rig Ved 0.147)
- **Original**: (देवशक्तियों के संगठक ) इन्द्रदेव ने विश्व को प्रकाशित करने के महान्‌ उद्देश्य से सूर्यदेव को उच्चाकाश में स्थापित किया, जिनने अपनी किरणों से पर्वत आदि समस्त विश्व को दर्शनार्थ प्रेरित क्रिया
- **Translation**: 

---

### Verse 8 (Rig Ved 0.148)
- **Original**: 64. इन्द्र वाजेषु नोडव सहस््प्रधनेषु च। उग्र उग्राभिरूतिभि:
- **Translation**: 

---

### Verse 9 (Rig Ved 0.149)
- **Original**: है वीर इन्द्रदेव ! आप सहसौ्रों प्रकार के धन - लाभ वाले छोटे-बड़े संग्रामों में वीरतापूर्वक हमारी रक्षा करें
- **Translation**: 

---

### Verse 10 (Rig Ved 0.150)
- **Original**: 65, इन्द्र बय॑ं महाधन इन्द्रमभें हवामहे। युर्ज वृत्रेषु वच्रिणम्‌
- **Translation**: 

---

### Verse 11 (Rig Ved 0.151)
- **Original**: हम छोटे - बड़े सभी (जीवन) संग्रामों में वृत्रासुर के संहारक, तज्पाणि इन्द्रदेव को सहायतार्थ बुलाते हैं
- **Translation**: 

---

### Verse 12 (Rig Ved 0.152)
- **Original**: 66. स नो वृषन्नमुं चरुं सत्रादावन्‍नपा वृधि। अस्मध्यमप्रतिष्कुत:
- **Translation**: 

---

### Verse 13 (Rig Ved 0.153)
- **Original**: सतत दानशील, सदैव अपराजित हे इद्धदेव ! आप हमारे लिये मेघ से जल की वृष्टि करें
- **Translation**: 

---

### Verse 14 (Rig Ved 0.154)
- **Original**: 67. तुझेतुज्जे य उत्तरे स्तोमा इन्द्रस्य वच्रिण:। न विन्धे अस्य सुष्टुतिम्‌
- **Translation**: 

---

### Verse 15 (Rig Ved 0.155)
- **Original**: प्रत्येक दान के समय , वज्ञधारी इद्धदेव के सदृश दान की (दानी की) उपम्ा कहीं अन्यत्र नहीं मिलती । इन्रदेब की इससे अधिक उत्तम स्तुति करते में हम समर्थ नहीं है
- **Translation**: 

---

### Verse 16 (Rig Ved 0.156)
- **Original**: 68. वृषा यूथेव वंसग: कृष्टीरियत्योजसा
- **Translation**: 

---

### Verse 17 (Rig Ved 0.157)
- **Original**: ईशानो अप्रतिष्कुत:
- **Translation**: 

---

### Verse 18 (Rig Ved 0.158)
- **Original**: सबके स्वामी, हमारे विरुद्ध कार्य न करते वाले, शक्तिमान्‌ इद्धदेव अपनों सामर्थ्य के अनुसार , अनुदान जाँटने के लिये मनुष्यों के पास उसी प्रकार जाते हैं, जैसे वृषभ गायों के समृह में जाता है
- **Translation**: 

---

### Verse 19 (Rig Ved 0.159)
- **Original**: 69. य एकश्चर्षणीनां वसूनामिरज्यति
- **Translation**: 

---

### Verse 20 (Rig Ved 0.160)
- **Original**: इन्द्र: पञ्च क्षितीनाम्‌
- **Translation**: 

---

