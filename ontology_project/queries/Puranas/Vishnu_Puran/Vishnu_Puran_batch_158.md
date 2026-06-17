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

### Verse 1 (Vishnu Puran 0.3141)
- **Original**: 7 योजनानां सहसं तु द्वीपो5य॑ दक्षिणोत्तरात्‌ । पूर्वे किराता यस्थान्ते पश्चिमे यबना: स्थिता:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3142)
- **Original**: 8 ब्राह्मणा: क्षत्रिया वैश्या मध्ये शूद्राक्ष भागशञ: । इज्यायुश्रवाणिज्याझ्रर्वर्तयन्तो व्यवस्थिता:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3143)
- **Original**: 9 शतवूच्नन्द्रभागाद्या.. हिमवत्पादनिर्गता: । बेदस्मृतिमुखाद्याश्ष पारियात्रोद्धधा मुने
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3144)
- **Original**: 10 नर्मदा सुरसाद्माश्च नद्यो विन्ध्याद्रिनिर्गता: । ऋक्षसम्भवा:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3145)
- **Original**: 11 गोदावरी भोमरथी कृष्णवेण्यादिकास्तथा । सह्यपादोद्धबा नहा: स्मृता: पापभयापहा:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3146)
- **Original**: 12 कृतमाला ताम्रपर्णीप्रमुखा मलयोद्धवाः । त्रिसामा चार्यकुल्याद्या महेन्द्रप्रभवा: स्पृता:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3147)
- **Original**: 13 ऋषिकुल्‍याकुमाराद्या: शुक्तिमत्पादसम्भवा: । आसां नहदुपनद्मभश्न सन्यन्याश्ष सहस्रशः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3148)
- **Original**: 14 श्रीपराशरजी बोले--हे मैत्रेय ! जो समुद्रके उत्तर तथा हिमालयके दक्षिणमें स्थित है वह देश भारतवर्ष कहल्लता है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3149)
- **Original**: ठसमें भरतकी सन्तान बसी हुई है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3150)
- **Original**: हे महासुने ! इसका विस्तार नौ हजार योजन है। यह स्वर्ग और अपवर्ग प्राप्त करनेबालॉकी कर्मभूमि है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3151)
- **Original**: इसमें महेन्द्र, मलय, सहाय, शुक्तिमान्‌, ऋक्ष, विन्ध्य और पारियात्र--ये स्रात कुलपर्वत हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3152)
- **Original**: हे मुने ! इसी देझामें मनुष्य ज्ुभकर्मोद्वारा स्वर्ग अथया मोक्ष प्राप्त कर सकते हैं और यहींसे [ पाप-कर्माँमें प्रकृत होनेपर ] वे नस्क अथवा तिर्यग्योनिमें पड़ते हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3153)
- **Original**: यहींसे [ कर्मानुसार ] स्वर्ग, मोक्ष, अन्तरिक्ष अथवा पाताल आदि ल्ोकॉक्) प्राप्त किया जा सकता है, पृथिवीमें यहाँके सिवा और कहीं भी मनुष्यक्रे लिये कर्मकी विधि नहीं है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3154)
- **Original**: इस भारतवर्षके नौ भाग हैं; उनके नाम ये हैं-- इन्द्रद्यीप, कसेरु, ताम्रपर्ण, गर्भास्तिमान्‌, नागद्वीप, सौम्य, गन्धर्व और नारुण तथा यह समुदसे घिरा हुआ द्वीप उनमें नवाँ है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3155)
- **Original**: यह द्रीप उत्तरसे दक्षिणतक सहस्र योजन है। इसके पूर्वीय भागमें किरात लोग और पश्चिमीयमें यवन बसे हुए हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3156)
- **Original**: तथा यज्ञ, युद्ध और व्यापार आदि अपने-अपने कर्मोंकी व्यवस्थाके अनुसार आचरण करते हुए ब्राह्मण, क्षत्रिय, वैश्य और शूद्रगण जर्णविभागानुसार मध्यमें रहते हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3157)
- **Original**: हे मुने ! इसकी शतद्ूू और चन्रभागा आदि नदियाँ हिमालयकी तलैटीसे खेद और स्मृति आदि पारियात्र पर्वतसे, नर्मदा और सुरसा आदि विन्ध्याचलसे तथा तापी, पयोष्णो और निर्विन्ध्या आदि ऋक्षगिरिसे निकली हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3158)
- **Original**: गोदावरी, भीमरथी और कृष्णवेणी आदि पापहारिणी नदियाँ सह्दपर्वतसे उत्पन्न हुई कही जाती हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3159)
- **Original**: कृतमाला और ताप्रपर्णी आदि मलयाचलसे, त्रिसामा और-आर्य- कुल्या आदि महेन्द्रगिरिसि तथा ऋषिकुल्‍या और कुमारी आदि नदियाँ शुक्तिमान्‌ पर्वतसे निकली हैं । इनकी और भी सहस्रों शास्ता नदियाँ और उपनदियाँ हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3160)
- **Original**: आ0 3 ] द्वितीय अंझ 113 तास्विमे कुरुपाश्ाला मध्यदेशादयो जना: । पूर्वदेशादिकाश्ैव. कामरूपनिवासिन:
- **Translation**: 

---

