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

### Verse 1 (Vishnu Puran 0.61)
- **Original**: तथा मेरे प्रसादसे तुन्हारो निर्मल बुद्धि प्रवृत्ति और नियृत्ति (भोग और मोक्ष) के उत्पन्न करनेवाले क्मोंमें निःसन्देह हो जायगी
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.62)
- **Original**: [पुलर्यजीके इस तरह कहनेके आनन्तर
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.63)
- **Original**: फिर मेरे पितामह भगवान्‌ बसिष्ठजों बो़े “पुलस्त्यजोने जो कुछ कहा है, नह सभी सत्य होगा''
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.64)
- **Original**: हे पैत्रेय ! इस प्रकार पूर्वकालमें बुद्धिमान्‌ पसिप्ठजो और पुलस्तयजीने जो कुछ कहा था, जह सब तुम्हारे प्रशसे मुझे स्मरण हो आया है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.65)
- **Original**: अतः हे गैत्रेय ! तुग्हारे पूछनेसे में उस सम्पूर्ण पुराणसंहिताको तुम्हें सुनाता हूँ; तुम उसे भल्तो प्रकार ध्यान देकर खुनो
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.66)
- **Original**: यह जगत्‌ त्िष्णुसे उत्पन्न हुआ है, उन्हींमें स्थित है, के हो इसकी श्थिति और हूयके ऊत्ां हैं तथा यह जगत्‌ भी ये ही है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.67)
- **Original**: जभ-+ हऔ "प++5 इति श्रीविष्णुपुराणे प्रथमेंडदों प्रथमोड्ध्यायः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.68)
- **Original**: शा दूसरा अध्याय चौबीस तस्‍क्थोंके विचारके स्लाथ जगतक़े उत्पत्ति- क्रमका वर्णन और विष्णुकी महिमा श्रीपयाशर उतान अबिकाराय शुद्धाय नित्याय पसर्मात्मने सदैकरूपरूपाय विष्णवे सर्वजिष्णवे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.69)
- **Original**: 9 नमो हिरण्यगर्भाय हरये शद्भूराय च। वासुदेवाय ताराब सर्गस्थित्यन्तकारिणे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.70)
- **Original**: 2 एकानेकस्वरूपाय स्थूलसूक्ष्मात्मने नमः । अय्यक्तब्यक्तरूपाय बिष्णवे पुक्तिहेतवे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.71)
- **Original**: 43 सर्गस्थितिविनाशानां जगतो यो जगन्मयः । मूलभूतो नमस्तस्मैँ विष्णले परमात्मने
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.72)
- **Original**: डे ओऔपराहरजी ब्लोले--जो ब्रह्मा, विष्णु और शुँकररूपसे झगतूकी उत्पत्ति, स्थिति और संहास्क्े रण हैं तथा अपने भक्तोंको संसार-सागस्से ताश्नेगल्ले हैं, डन विकाररहित, शुद्ध, अब्नादी, परमात्मा, सर्वदा एकरस, सर्वविजयी भगवान्‌ छासूदेल विष्णुको नमस्कार है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.73)
- **Original**: जो एक होकर भी नाना रूपयाछे हैं, स्थूल- सूक्ष्ममय हैं, अव्मक्त (कारण) एबं व्यक्त (कार्य) रूप है तथा [अपने अनन्य भ्रक्तोंकी] मुक्तिके कारण हैं [उन श्रीथिण्णुभगलानको नमस्कार है)
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.74)
- **Original**: जो विशरूप प्रभु विश्वकी उत्पत्ति, स्थिति और सेहारके
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.75)
- **Original**: है] [ अ0 2 आधारभूत विश्वस्पाप्यणीयांसमणीयसाम्‌ । प्रणम्व॒ सर्वभूतस्थमच्युत॑ पुरुषोत्तमम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.76)
- **Original**: 5 ज्ञानस्वरूपमत्यन्तनिर्मलं परमार्थत: । तमेवार्थस्वरूपेण श्रान्तिदर्शनतः स्थितम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.77)
- **Original**: 6 विष्णु ग्रसिष्णुं विश्वस्य स्थितों से तथा प्रभुप्‌ प्रणम्य जगतामीशमजमक्षयमव्ययम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.78)
- **Original**: 7 कथ्चययामि यथापूर्व दक्षाहर्मुनिसत्तमै: । पृष्ट: प्रोब्राच भगवानब्जयोनि: पितामह:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.79)
- **Original**: 8 तैश्ोक्ते पुरुकृत्साय भूभुजे नर्मदातटे । सारस्वताय तेनापि महां सारस्क्‍तेन च
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.80)
- **Original**: 9 पर: पराणां परम: परमात्मात्मसंस्थित: । रूपवर्णादिनिर्देशविशेषणविवर्जित:
- **Translation**: 

---

