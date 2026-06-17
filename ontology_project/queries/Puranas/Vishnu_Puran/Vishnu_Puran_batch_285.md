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

### Verse 1 (Vishnu Puran 0.5681)
- **Original**: बन्धू-जान्धवोंको चाहिये कि भली प्रकार स्तन करानेके अनन्तर पुष्प मास्प्रओऑसे विभूषित शावका गाँकके £ जग
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5682)
- **Original**: स्ण्ड श्रीविष्णुपुराण रे ड आआआआआआ ोविष्णुपुराण [अःरे3 [ आः 13 यत्र तत्र स्थितायैतदमुकायेति वादिनः। दक्षिणाभिमुखा ददघ्युर्बान्यवास्सल्लाझलीन्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5683)
- **Original**: 9 प्रविष्टाश्ष सर्म॑ गोभिग्राम नक्षत्रदर्शने । कटकर्म ततः कुर्युभूमो प्रस्तरशायिन:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5684)
- **Original**: 10 दातव्योडनुदिनं पिण्ड: प्रेताय भुवि पार्थिव । दिवा च भक्त भोक्तव्यममांसं मनुजर्षभ
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5685)
- **Original**: 19 दिनानि तानि चेच्छात: कर्तव्यं त्रिप्रभोजनम्‌ । ज्रेता यान्ति तथा तृप्ति बन्धुवगेंण भुक्लता
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5686)
- **Original**: 12 प्रथमेउद्मि तृतीये च सप्तमे नवमते तथा। सख्रत्यागबहिस्स्राने कृत्वा द्द्यात्तिकोदकम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5687)
- **Original**: 13 चतुर्थे<छ्लि च॒ कर्तव्यं तस्यास्थिचयनं नृप । तदृध्व॑मड्डसंस्पर्शस्सपिण्डानामपीष्यते._
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5688)
- **Original**: 14 योग्यास्सर्वक्रियाणां तु समानसलिलास्तथा । अनुल्लेपनपुष्पादिभोगादन्यत्र. पार्थिव
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5689)
- **Original**: 15 शाब्यासनोपभोगश्च॒ सपिण्डानामपीष्यते । भस्मास्थिचयनादूर्ध्व संयोगो न तु योषिताम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5690)
- **Original**: 16 बाले देशान्तरस्थे च पतिते तर पुनौ मृते । सद्यइञ्ौच तथेच्छातो जलाम्न्युद्नधनादिषु
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5691)
- **Original**: 97 मृतबन्धोर्दशाहानि कुलस्थान्न न भुज्यते । दान॑ प्रतिग्रहो होम: स्वाध्यायश्व निवर्तते
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5692)
- **Original**: 18 विष्रस्यैतद्‌ द्वादशाहं राजन्यस्याप्यशौचकम । बाहर दाह करें और फिर जल्ञ्रशयमें वस्क्सहित स्त्रान कर दक्षिण-मुख होकर “यत्र ततन्न स्थितायैतदमुकाय' * आदि वाक्यका उच्चारण करते हुए जलाझलि दें
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5693)
- **Original**: तदनत्षर, गोधूल्म्कि समय तारा-मष्डछके दीखने रूगनेपर आममें प्रवेश करें और कटकर्म (अज्ञौच कल्प) सम्पन्न करके पृथिवीपर दृणादिकी शय्यापर शयन करें.
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5694)
- **Original**: हे पृथिजीपते ! मृत पुरुषके लिये नित्यप्रति पृथिवीपर पिण्डदान करना चाहिये और हे पुरुषश्रेष्ठ ! केवल दिनके समय मौसहीन भात खाना चाहिये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5695)
- **Original**: अश्जौच काल्में, यदि ब्राह्मणोंकी इच्छा हो तो उन्हें भोजन कराना चाहिये, क्योंकि उस समय ब्राह्मण और बन्धुवर्गके भोजन करनेसे मृत्र जीवकी तृप्ति होती है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5696)
- **Original**: अजश्ौचके पहले, तीसरे, सातलें अथवा नवें दिन बस्तर स्यागकर और बहिर्देशमें स्नान करके तिस्म्रेदफ दे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5697)
- **Original**: है नृुप ! अशौचके चौथे दिन अस्थिचयन करना चाहिये; उसके अन्तर अपने सपिण्ड बन्धुजनॉक्त्र अंग स्पर्श किया जा सकता है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5698)
- **Original**: है राजन्‌ ! उस समयसे सम्तानोदक + पुरुष चन्दन और पुष्पधारण आदि क्रियाओंके सिवा [ पशुयज्ञादि ] और सब कर्म कर सकते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5699)
- **Original**: भस्म और अस्थिचयनके अनच्तर सपिण्ड पुरुषोंद्राया शय्या और आसनका उपयोग तो किया जा सकता है किन्तु स्वी-संसर्ग नहीं फिया जा सकता
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5700)
- **Original**: बालक, देशान्तरस्थित व्यक्ति, पतित और तपस्वीके मस्नेपर तथा जल, अग्नि और उद्धघन (फॉसी लगाने) आदिद्वारा आत्मघात करनेपर शीघ्र ही अच्ौचकी निवृत्ति हो जाती है +
- **Translation**: 

---

