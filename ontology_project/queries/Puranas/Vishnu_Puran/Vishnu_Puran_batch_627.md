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

### Verse 1 (Vishnu Puran 0.12521)
- **Original**: उस अखिलभूतात्मामें समस्त भूतगण निवास करते हैं और बह स्वयं भी समस्त भूतोंमें विराजमान है, इसलिये वह अव्यय (परमात्मा) ही वकारका अर्थ है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12522)
- **Original**: # अ्रथण-इन्द्रियद्वारा शास््रका प्रहण होता है; इसलिये शास्त्रजन्य ज्ञान ही “इच्द्रियोद्धन' शब्दसे कहा गया है।
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12523)
- **Original**: डडर अ्रीविष्णुपुराण 4 आर 5 एवमेष महाउछब्दो मैत्रेय भगवानिति। परमन्रह्मभूतस्य वासुदेवस्थ नान्यग:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12524)
- **Original**: 76 तत्र. पूज्यपदार्थोक्तिपरिभाषासमन्वित: । शब्दो5्य॑ नोपचारेण त्वन्यत्र ह्युपचारत:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12525)
- **Original**: 77 उत्पत्ति प्रछ॒यं चैब भूतानामागर्ति गतिम्‌। केत्ति विद्यामबिद्यों चस वाच्यो भगवानिति
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12526)
- **Original**: 78 ज्ञानशक्तिबलैश्वर्यवीर्यतेजास्यशेषत: ..। अगबच्छव्दबाच्यानि विना हेयेगणादिभिः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12527)
- **Original**: 79 सर्वाणि तत्र भूतानि वसन्ति परमात्मनि। भूतेषु च स सर्वात्मा वासुदेवस्ततः स्मृतः 4
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12528)
- **Original**: 80 खाण्डिक्यजनकायाह पृष्ट: केशिध्बज: पुरा । जामव्याख्यामनन्तस्यथ वासुदेवस्थ तत्त्वतः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12529)
- **Original**: 89 भूतेषु वसते सो5न्तर्वसन्त्यत्र च तानि यत्‌ । धाता विधाता जगतां वासुदेवस्ततः प्रभु:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12530)
- **Original**: 82 स सर्वभूतप्रकृति विकारा- ..... ज्ञुणादिदोर्षाश्व घुने व्यतीतः। अतीतसर्वावरणोअखिलात्पमा . स्सस्ताधिताश्ेषजगछ्धितो यः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12531)
- **Original**: 84 तेजोबलैश्वयमहावक्लोध-.......... ..._ सुवीर्यक्षक्त्यादिगुणैकराशि: । परः पराणों सकला न यत्र हु परावरेशे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12532)
- **Original**: 85 स॒इंश्वरो व्यपष्रसमषश्टर्पो ॑ऋं:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12533)
- **Original**: मय परमेश्वराख्य:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12534)
- **Original**: 879 हे मैत्रेय ! इस प्रकार यह महान्‌ 'भगवान्‌' शब्द परबह्मस्वरूप श्रीवासुदेवका ही वाचक है, किसी औरका नहीं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12535)
- **Original**: पूज्य पदार्थोको सूचित करनेके लक्षणसे युक्त इस 'भगवान' झऋब्दका परमात्मामें मुख्य प्रयोग है तथा औरोंके लिये गौण
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12536)
- **Original**: क्योंकि जो समस्त च्राणियोंकि उत्पत्ति और नाश, आना और जाना तथा विद्या और अविद्याकों जानता है वही भगवान्‌ कहलानेयोम्य है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12537)
- **Original**: त्याग करनेयोग्य [ त्रिनिध ] गुण [ और उनके क्लेता ] आदिको छोड़कर ज्ञान, दाक्ति, बल्ह, ऐश्वर्य, वीर्य और तेज आदि सद्‌गुण ही 'भगलत्‌' शब्दके वाच्य हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12538)
- **Original**: 79 उन परमात्मामें ही समस्त भूत बसते हैं और वे स्वयं भी उन्हें जासुदेज भी कहते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12539)
- **Original**: पूर्वकाल्में स्ताण्डिक्य जनकके पूछनेपर केशिध्वजने उनसे भगवान्‌ अनन्तके “वासुदेव' नामकी यथार्थ व्याख्या इस प्रकार की थी
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12540)
- **Original**: “प्रभु समस्त धूतोंमें व्याप्त हैं और सम्पूर्ण भूत भी उन्‍्हींमें रहते हैं तथा ये ही संसास्के रचयिता और रक्ष्कक हैं; इसलिये वे 'वासुदेव' कहल्लाते है'
- **Translation**: 

---

