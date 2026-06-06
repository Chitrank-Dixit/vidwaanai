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

### Verse 1 (Vishnu Puran 0.3161)
- **Original**: 95 पुण्ड्रा: कलिड्जा मगधा दक्षिणाद्याश्न सर्वशः । तथापरान्ता: सौराष्ट्राः: शूराभीरास्तधार्बुदाः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3162)
- **Original**: 16 कारूषा मालवाश्ैव पारियात्रनिवासिन: । सौवीरा: सैशधवा हृणा: साल्वा: कोशलवासिन: । माद्रारामास्तथाम्बष्ठा: पारसीकादयस्तथा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3163)
- **Original**: 17 आसां पिबन्ति सलिलं बसन्ति सहिताः सदा । समीपतो महाभाग हष्टपुष्टजनाकुला:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3164)
- **Original**: 18 चत्वारि भारते वर्षे युगान्यत्र महामुने। कृत॑ त्रेता द्वापरक्ष कल्िआन्यत्र न क्रचित्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3165)
- **Original**: 19 तपस्तप्यन्ति मुनयो जुद्धते चात्र यज्विनः । द्वानानि चाजत्र दीयन्ते परलोकार्थमादरात्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3166)
- **Original**: 20 पुरुषर्यज्षपुरुषो. जम्बूद्वीपी. संदेज्यते । विष्णुरन्वद्वीपेषू. चान्यथा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3167)
- **Original**: 21 अत्रापि भारत॑ श्रेष्ठ जम्बूद्वीप॑ महामुने । यतो हि कर्मभूरेषा ह्तोउन्‍्या भोगभूमय:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3168)
- **Original**: 22 अत्र जन्मसहस्नाणां सहस्नैरपि सत्तम। कदाचिल्लभते जनन्‍्तुर्मानुष्यं पुण्यसझ्यात्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3169)
- **Original**: 23 । गायन्ति देवा: किल गीतकानि 5 अच्यास्तु ते भारत भूमिभागे। स्वर्गापबर्गास्पदमार्गभूते _ अबन्ति भूयः पुरुषा: सुरत्वात्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3170)
- **Original**: 24 कमण्यसड्डल्पिततत्फलानि ... संन्‍्यस्थ विष्णी परमात्मभूते। अवाष्य ता कर्ममहीमनन्ते..... .. तर्सिल्लय ये त्वमला: प्रयान्ति
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3171)
- **Original**: 25 "5 टे- रू + का धनन्‍्या: खल ते मनुष्या से करत मेस्ियविप्रीना:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3172)
- **Original**: 26 इन नदियोंके तटपर बुछू, पाकछाल और मध्यदेशादिके रहनेवाले, पूर्वदेश और क्ामरूपके निवासी, पुण्ड, कलिंग, मगध और दाक्षिणात्यल््रेग, अपसान्तदेशवासी, सौराष्ट्ररण तथा झूर, आभीर और अर्बुंदगण, कारूष, मालव और पारियात्रनिवासी, सौबीर, सैन्धव, हुण, सालथ और कोद्गनल देशवासी तथा माद्र, आम, अम्बष्ठ और पारसीगण रहते हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3173)
- **Original**: 15---17
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3174)
- **Original**: है महाभाग ! ले लोग सदा आपसमें मिलकर रहते है और इन्हींका जल्ड पान करते हैं । इसकी सन्निधिके कारण से यड़े इष्ट-पृष्ट रहते हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3175)
- **Original**: है मुने
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3176)
- **Original**: इस भारतवर्षमें ही सत्ययुग, त्रेता, द्वापर और कॉलि नामक चार युग हैं, अन्यत्र कहीं नहीं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3177)
- **Original**: इस देशामें परस्लेकके लिये मुनिजन तपस्या करते हैं, याज्िक लोग यज्ञानुष्ठान करते हैं और दानीजन आदरपूर्वक दान देते हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3178)
- **Original**: जम्बूद्वीपमें यज्ञमय यज्ञपुरुष भगवान्‌ लिष्णुका सदा यज्ञोंद्रारा यजन किया जाता है, इसके अतिरिक्त अन्य द्रीपॉर्में उनकी और-और अ्रकारसे उपासना होती है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3179)
- **Original**: हे महामुने ! इस जम्बद्वोपमें भो भारतरर्ण सर्वश्रेष्ठ है, क्योवि; यह फर्मभभुमि है इसके अतिरिक्त अन्यान्य देश भोग-भूमियाँ हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3180)
- **Original**: डे सत्तम ! जीवको सहस्तनों जन्मोके अनन्तर महान्‌ पुण्योंका उदय होनेपर ही कभी इस देझामें मनुष्य-जत्म प्राप्त होता है
- **Translation**: 

---

