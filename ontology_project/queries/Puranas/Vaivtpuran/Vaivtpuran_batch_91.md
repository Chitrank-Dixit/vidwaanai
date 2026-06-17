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

### Verse 1 (Vaivtpuran 7.9553)
- **Original**: भक्तानुरोधातू साकारो निराकारों. निरंकुशः । स्वेच्छामयश्च सर्वेश: सर्व: सर्वगुणाश्रय:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 7.9554)
- **Original**: सुखदो दुःखदो दुर्गों दुर्जानक एबं च। निर्व्यूहों निखिलाधारों निःशक्लो निरुषद्रव:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 7.9555)
- **Original**: निरुषाधिश्ष निर्लितों निरीहों.. निधनान्तक: । आत्माराम: पूर्णकामों निर्दोषो नित्य एबं च
- **Translation**: 

---

### Verse 4 (Vaivtpuran 7.9556)
- **Original**: सुभगो दुर्भगो वाग्मी दुराशध्यो दुरत्ययः । वेदहेतुश वेदाक्ष वेदाड्रो वेदबिद्‌ विभु:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 7.9557)
- **Original**: इत्येवमुक्त्वा देवाक्ष प्रणेमुश्ष॒ मुहु्मुहु: । ह्श्रुलोचना: सर्वे बबृषु: कुसुमानि च
- **Translation**: 

---

### Verse 6 (Vaivtpuran 7.9558)
- **Original**: द्विचत्वारिशप्तामानि प्रातरुत्धाया यः पदठेत्‌। दृढां भक्ति हरेदास्थं लभते बाज्छितं फलम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 7.9559)
- **Original**: (श्रीकृष्णजन्मखण्ड 7। 55-61)
- **Translation**: 

---

### Verse 8 (Vaivtpuran 7.9560)
- **Original**: * भ्रीकृष्णजन्मखण्ड * 431 कक 4 64555 %%%%:%# ########% 27 27]7]+4])0000 0
- **Translation**: 

---

### Verse 9 (Vaivtpuran 7.9561)
- **Original**: मकराकृति कुण्डल झलमला रहे थे। मुख मन्द
- **Translation**: 

---

### Verse 10 (Vaivtpuran 7.9562)
- **Original**: हाथ जोड़ भक्तिभावसे उनकी स्तुति कौ। जज दर बसुदेवजी बोले--भगवन्‌! आप श्रीमान्‌ (सहज शोभासे सम्पन्न), इन्द्रियातीत, अविनाशी, निर्गुण, सर्वव्यापी, ध्यानसे भी किसीके वशर्में
- **Translation**: 

---

### Verse 11 (Vaivtpuran 7.9563)
- **Original**: न होनेवाले, सबके ईश्वर और परमात्मा हैं। +7.
- **Translation**: 

---

### Verse 12 (Vaivtpuran 7.9564)
- **Original**: स्वेच्छामय, सर्वस्वरूप, स्वच्छन्द रूपधारी, अत्यन्त 922 निर्लिपत, परब्रह्म तथा सनातन बीजरूप हैं। आप
- **Translation**: 

---

### Verse 13 (Vaivtpuran 7.9565)
- **Original**: स्थूलसे भी अत्यन्त स्थूल सर्वत्र व्यापत, अतिशय कं ह।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 7.9566)
- **Original**: सूक्ष्म, दृष्टिपथमें न आनेवाले, समस्त शरीरोंमें 0004
- **Translation**: 

---

### Verse 15 (Vaivtpuran 7.9567)
- **Original**: साक्षीरूपसे स्थित तथा अदृश्य हैं। साकार, “ निराकार; सगुण, गुणोंके समूह; प्रकृति, प्रकृतिके हास्यकी छठटासे प्रसन्न जान पड़ता था। वे भक्तोंपर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 7.9568)
- **Original**: शासक तथा प्राकृत पदार्थोँमें व्याप्त होते हुए भी कृपा करनेके लिये कातर-से दिखायी पड़ते थे।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 7.9569)
- **Original**: प्रकृतिसे परे विद्यमान हैं। विभो! आप सर्वेश्वर, श्रेष्ठ मणि-रत्ञोंक सारतत्त्वसे निर्मित आभूषण
- **Translation**: 

---

### Verse 18 (Vaivtpuran 7.9570)
- **Original**: सर्वरूप, सर्वान्तक, अविनाशी, सर्वाधार, निराधार उनके शरीरकी शोभा बढ़ा रहे थे। पीताम्बस्से
- **Translation**: 

---

### Verse 19 (Vaivtpuran 7.9571)
- **Original**: और निर्व्यूह (तर्कके अविषय) हैं; मैं आपकी सुशोभित श्रीविग्रहकी कान्ति नूतन जलधरके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 7.9572)
- **Original**: क्या स्तुति करूँ? भगवान्‌ अनन्त (सहस्रो समान श्याम थी। चन्दन, अगुरु, कस्तूरी और
- **Translation**: 

---

