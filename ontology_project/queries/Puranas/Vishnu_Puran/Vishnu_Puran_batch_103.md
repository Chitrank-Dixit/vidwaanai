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

### Verse 1 (Vishnu Puran 0.2041)
- **Original**: >कमें इनके उत्पत्ति और निरोध निरन्तर हुआ करते हैं। ये यथा सूर्यस्थ मैत्रेय उदयास्तमनाविह। एवं देवनिकायास्ते सम्भवन्ति युगे युगे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2042)
- **Original**: 139 दित्या पुत्रद्दय॑ जज्ने कश्यपादिति नः श्रुतम्‌ हिरण्यकशिपुश्चैत॒ हिरण्याक्षश्न दुर्जय:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2043)
- **Original**: 940 सिंहिका चाभवत्कन्या तिप्रचित्ते: परिग्रह:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2044)
- **Original**: 141 हिरण्यकज्िपो: पुत्राश्रत्वार: प्रधितौजस: । अनुड्रादश ह्रादश प्रह्मादशैब बुद्धिमान्‌। संह्रादश्ष महावीर्या दैत्यतंशत्रिवर्द्धना:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2045)
- **Original**: 942 खाताय कपिस्ख
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2046)
- **Original**: एक हजार सुगके अनन्तर पुतः-पुनः उत्पन्न होते रहते है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2047)
- **Original**: 137-138
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2048)
- **Original**: हे मैत्रेय ! जिस प्रकार ल्वेकमें सूर्यके अस्त और उदय निरन्तर हुआ करते हैं उसी प्रकार ये देवगण भी युग-युगमें उत्पन्न होते रहते हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2049)
- **Original**: हमने सुना है दितिके कइ्यपजीके बीर्यसे परम दुर्जय हिरण्यकशिपु और हिरण्याक्ष नामक दो पुत्र तथा सिंहिका नाप्रकी एक कन्या हुई जो विप्रचित्तिको लिवाही गयी
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2050)
- **Original**: 140-141
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2051)
- **Original**: हिरण्यकशिपुके अति तेजस्वी और महापराक्रमी अनुद्गाद, ढ्वाद, वुद्धिमान्‌ प्रद्माद और संह्वाद नामक चार पुत्र हुए जो दैत्यवैशको बढ़ानेयाले थे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2052)
- **Original**: बिद्ुदातपायातिझ्रेहिता
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2053)
- **Original**: पीता वर्षाय विज्ञेया दुर्भिक्षाय सिता भवेत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2054)
- **Original**: अर्थात्‌ कपिल (भुरी) कर्णकी बिजली बायु त्मनेबाली, अत्यत्त ल्लेहित धूप निकालनेवालों, पीतवर्णा यृष्टि लानेवाली और सिता (श्वेत) दुर्भिक्षकौ सूचना देनेवात्मै होती है।
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2055)
- **Original**: अ 17 ] तेषां मध्ये महाभाग सर्वत्र समदृग्वशी । प्रह्वादः परमां भक्ति य उवाच जनार्दने
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2056)
- **Original**: 943 न ददाह च य॑ विप्र यासुदेवे हदि स्थिते
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2057)
- **Original**: 144 महार्णवान्तःसलिले स्थितस्य चलतो मही । चचाल सकला यस्य पाशबद्धस्थ धीमत:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2058)
- **Original**: 145 न भिन्न विविधै: दस्त्र्यस्य दैत्येनद्रपातितैः । आरीरमद्भिकठिनं. सर्वत्राच्युतल्ेतस:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2059)
- **Original**: 1946 विषानल्लोज्ज्वलमुखा यस्य दैत्यप्रचोदिता: । नान्ताय सर्पपतदो बभूवुरुरुतेजसः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2060)
- **Original**: 147 औैलैराक्रान्तदेहो5पि यः स्मरन्पुरुषोत्तमम्‌ तत्याज नात्मन: प्राणान्‌ विष्णुस्मरणदंशितः
- **Translation**: 

---

