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

### Verse 1 (Vishnu Puran 0.10601)
- **Original**: 12 न तद्ले यादवानां विजितं यदनेकशः। तत्तु सन्निधिमाहात्म्य॑ विष्णोरंशस्प चक्रिण:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10602)
- **Original**: 13 मनुष्यधर्मशीलस्थ लीला सा जगतीपते: । अख्ाण्यनेकरूपाणि यदरातिषु मुख्तति
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10603)
- **Original**: 14 मनसैव जगत्सृष्टिं संहारं च करोति य: । तस्थारिपक्षक्षषणे. कियानुद्यमविस्तर:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10604)
- **Original**: 15 तथापि यो मनुष्याणां धर्मस्तमनुवर्तते । कुर्वन्बलवता सन्धि हीनैर्युद्ध॑ं करोत्यसौ
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10605)
- **Original**: 16 साम चोषपप्रदानं चर तथा भेद च दर्शयन्‌। करोति दण्डपा्त च क्चिदेव पलायनम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10606)
- **Original**: 17 मनुष्यदेहिनां चेष्टामित्येबमनुबर्तते । लीला जगत्पतेस्तस्यच्छन्दत: परिवर्तते
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10607)
- **Original**: 18 गया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10608)
- **Original**: इस शत्रकार अत्यन्त दुर्धर्ष मगधणज जरासखने राम और कृष्ण आदि यादवॉसे अद्जारह बार युद्ध किया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10609)
- **Original**: इन सभी यद्धोंमें अधिक सैन्यशाल्त जरास-थ थोड़ी-सी सेनावाले यदुर्वशियोंसे हारकर भाग गया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10610)
- **Original**: यादवॉकी थोड़ौ-सौं सेना भी जो [ठसकी अनेक बड़ी सेनाओंसे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10611)
- **Original**: पराजित न हुई, यह सब भगवान्‌ विष्णुके अंशावतार श्रीकृष्णयत्द्रकी सप्निधिका ही माहात्म्य था
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10612)
- **Original**: उन मानवर्धर्मशील जगत्पतिको यह लीला ही है जो कि ये अपने शब्रुऑपर नाना प्रकारके अख्न-शख्त्र छोड़ रहे हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10613)
- **Original**: जो केवल संकल्पमात्रसे ही संसारकी उत्पत्ति और संह्ार कर देते हैं उन्हें अपने जत्नुपक्षका नाश करनेके लिये भत्त उद्योग फैल्ानेकी कितनी आवश्यकता है ?
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10614)
- **Original**: तथापि ये बल्ूयानोंसे सम्धि और बलडहीनोंसे युद्ध कस्के मानव-धर्मोंका अनुवर्तन कर रहे थे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10615)
- **Original**: वे कहीं साम, कहीं दान और कहीं भेदनीतिका व्यवहार करते थे तथा कहीं दण्ड देते आऔर कहांसे स्वयं भाग भो जाते थे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10616)
- **Original**: इस प्रकार मानवदेहधारियोंकी चेष्टाऑंका अनुवर्तन करते हुए श्रीजगत्पतिकी अपनी इच्छानुसार लीस्प्रएँ होती रहती थीं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10617)
- **Original**: इति श्रीविष्णुपुराणे पञ्चमेंडशे द्वाविशोड्ध्याय:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10618)
- **Original**: >+++ कै तततत तेईसवाँ अध्याय द्वारका-दुर्गकी रचना, कालयवनका भस्म होना तथा मुचुकुन्दकृत भगवत्स्तुति औीपराशर उवाय गाग्य॑ गोष्ठ्या द्विजे श्यालष्पण्ड डइत्युक्तवान्द्विज । यदूनां सत्रिधौ सर्वे जहसुर्यादवास्तदा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10619)
- **Original**: 9 तसतः कोपपरीतात्मा दक्षिणापथमेत्य सः । लोहचूर्णपभक्षयत्‌ । ददौ यरं च तुष्टोउस्मै वर्षे तु द्वादशो हरः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10620)
- **Original**: 3 सन्‍्तोषयामास च ते यवनेशों ह्वानात्मजः । तद्योषित्सड्भमाश्चास्य पुत्रो$भूदलिसबन्निभ:ः
- **Translation**: 

---

