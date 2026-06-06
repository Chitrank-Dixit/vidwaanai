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

### Verse 1 (Vishnu Puran 0.2941)
- **Original**: 8 मेधाम्रिबाहुपुत्रनास्तु त्रयों योगपरायणा:। जातिस्मरा महाभागा न राज्याय मनो दधुः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2942)
- **Original**: 9 ओपैश्रेयजी बोल्के--हे भगबन्‌ ! हे गुरो ! मैंने जगत्‌की सृष्टिके विषयमें आपसे जो कुछ पूछा था वह सब आपने मुझसे भली प्रकार कह दिया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2943)
- **Original**: हे मुनिश्रेष्ठ ! जगत्‌को सुष्टिसम्बन्धी आपने जो यह प्रथम अंडा बड़ा है, उसकी एक बात मैं और सुनना चाहता हूँ
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2944)
- **Original**: 2। स्वायम्पुतमनुके जो प्रियत्रत और उत्तानपाद दो पुत्र थे, उनमेंसे उत्तानपादके पुत्र धुकब्के बिषयमें तो आपने कहा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2945)
- **Original**: किंतु, हे द्विज ! आपने प्रियत्रतकी सत्तानके विषयर्मे कुछ भी नहीं कहा, अतः मैं उसका वर्णन सुनना चाहता हूँ, सो आप प्रसन्नतापूर्वक कहिये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2946)
- **Original**: श्रीपरादारजी बोले--प्रियज्रतने कर्दमजीकी पुत्रीसे विवाह किया था
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2947)
- **Original**: उससे उनके सप्राट्‌ और कुक्षि नामकी दो कन्याएँ तथा दस पुत्र हुए
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2948)
- **Original**: प्रियत्रतके पुज बड़े बुद्धिमान्‌, बलवान, विनयसम्पन्न और अपने माता- पिठाके अह्यत्त प्रिय कहे जाते हैं; उनके नाम सुनों--
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2949)
- **Original**: ये आग्रीध, अभिवाहु, बपुष्मान, झुतिमान, मेधा, मेधातिथि, भव्य, सबन और पुत्र थे तथा दसवाँ यथार्थनामा ज्योतिष्पान्‌ था। ये प्रियश्रतके पुत्र अपने बल-पराक्रमके कारण खिख्यात थे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2950)
- **Original**: उनमें महाभाग मेथा, अग्निबाहु और पुत्र--ये तीन योगपरायण तथा अपने पूर्वजन्पक्ता तृत्तान्त जाननेवाले थे। उन्होंने
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2951)
- **Original**: 106 निर्मछाः सर्वकालन्तु समस्तार्थेंषु तै मुने । चक्र: क्रियां यथान्यायमफलाकाद्विणो हि ते
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2952)
- **Original**: 10 फ्रियव्रतो ददौ तेषां सप्तानां सुनिसत्तम। सप्रद्वीपानि मैत्रेय विभज्य सुमहात्मनाम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2953)
- **Original**: 11 जम्बूद्वीप॑ महाभाग साम्रीध्राय ददौ पिता । प्रेधातिथेस्तथा प्रादात्म्क्षद्वीप तथापरम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2954)
- **Original**: 12 शाल्मले च वपुष्मन्तं नरेन्द्रमभिषिक्तवान। ज्योतिष्पन्त कुशद्वीपे राजानं कृतवाग्रभु:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2955)
- **Original**: 13 झुतिमन्त॑ च राजान॑ क्रौकद्वीपे समादिशत्‌। आाकद्दीपेश्वं चापि भव्यं चक्रे प्रियत्रतः । पुष्कराधिपति चक्रे सवन॑ चापि स प्रभु:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2956)
- **Original**: 14 जाबबूद्वीपेश्वरो यस्तु आम्मीध्रो मुनिसत्तम
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2957)
- **Original**: 15 तस्य पुत्रा बभूवुस्ते प्रजापतिसमा नव। नाभि: किम्पुरुषश्चैथ हरिवर्ष इलाबृत:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2958)
- **Original**: 16 रम्यो हिरण्वान्यप्ठश्न कुरुर्भद्राश् एव च। केतुपालस्तथैवान्य: साथुचेष्टो$भवन्नूप:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2959)
- **Original**: 17 जम्बूद्ीपविभागांश्न तेषां विप्र निशामय । पित्रा दत्त हिमाह्“ं तु वर्ष नाभेस्तु दक्षिणम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2960)
- **Original**: 18 हेमकूर्ट तथा वर्ष ददौ किम्पुरुषाय सः । तृतीय॑ नैषर्ध वर्ष हरिवर्षाय दत्तवान्‌
- **Translation**: 

---

