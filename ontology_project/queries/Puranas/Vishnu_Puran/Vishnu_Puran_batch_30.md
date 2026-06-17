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

### Verse 1 (Vishnu Puran 0.581)
- **Original**: प्ठी च क्ममचारित्व॑ सप्तमी सिद्ेक्ययते
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.582)
- **Original**: अप्रमी च तथा प्रोक्ता. यत्रक्तचनवायिता # अर्थ--सल्ययुगमें रसका स्वय॑ ही उल्सास छोता भा । यही रसोल्ल्रस नामकी सिद्धि है, उसके प्रभावसे मनुष्य भूखको नष्ट कर देता है । उस समय प्रजा स्री आदि भोगोंकी अपेक्षाके बिना ही सदा तृप्त रहती घी, इसीवे मुगिश्रेष्ठोने 'तुत्नि नामक दूसरी सिद्धि कहा है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.583)
- **Original**: उनका जो उत्तम धर्म था वही उनब्गी तीसरी सिद्धि वर्ली जाती है । उस समय सप्पूर्ण प्रजाके रूप और आयु एक-से छे, यही उनकी चौथी सिद्धि थी। अल्की ऐक््रान्तिकों अधिकता--यह 'विश्येका' नामको पौयवों सिद्धि है। परसात्मपरायण रहते हुए; तप-ध्यानादिमें तत्पर रहना छठी सिद्धि है । स्वेच्छानुसार विचरना सातवीं स्द्धि कहो जाती है तथा जहाँ-तहां मनज्ये मौज पढ़ें रहना आठवीं सिद्धि कही गयी है। + पहाड़ या नदीके तरपर बसे हुए छोटे छोटे टोलोको 'स्पर्यट' कहते हैं।
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.584)
- **Original**: श्र अ्रीविष्णुपुराण (अ*ब्6 ब्रीहयस्सयवा माषा गोधूमाश्नाणवस्तिला: । इयाम्राकास्त्वथ नीवारा जर्तिला: सगवेधुका: । तथा बेणुयवा: प्रोक्तास्तथा मर्कटका मुने
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.585)
- **Original**: 257 ग्राष्यारण्या: स्पृता छोता ओवषध्यस्तु चतुर्दश । यज्ञनिष्पत्तये. यज़स्तथासा हेतुरुत्तमः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.586)
- **Original**: 26 एताञ्न सह यज्ञेन प्रजानों कारण परम्‌। परावरकिद: प्राज्ञास्ततो यज्ञान्वितन्वते
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.587)
- **Original**: 27 अहन्यहन्यनुष्ठान॑ यज्ञानां मुनिसत्तम । उपकारकरं पुंसां क्रियमाणाघशान्तिदम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.588)
- **Original**: 28 येषां तु कालसूछ्ोडसो पापबिन्दुर्महामुने । चेत:सु ववृधे चक्तुस्ते न यज्ञेषु मानसम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.589)
- **Original**: 29 येदवादांस्तथा वेदान्यज्ञकर्मादिक च्च यत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.590)
- **Original**: तत्सर्व॑ निन्दयामासुर्यज्ञव्यासेधकारिण:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.591)
- **Original**: 30 प्रवृत्तिमार्गव्युक्छित्तिकारिणो वेदनिन्दका: । दुरात्मानो दुराजारा बभूवु: कुटिलाशया:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.592)
- **Original**: 31 संसिद्धायां तुवातायां प्रजा: सृष्टा प्रजापति: । पर्यादा स्थापयामास यथास्थानं यथागुणम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.593)
- **Original**: 32 बर्णानामाश्रमाणां च धर्मान्धर्मभृतां बर
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.594)
- **Original**: लोकांश सर्ववर्णानां साम्यग्धर्मानुपालिनाम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.595)
- **Original**: 33 स्थानमैद्ध क्षत्रियाणां संग्रामेष्ननिवर्तिनाम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.596)
- **Original**: 34 खैह्यानां मारुत॑ स्थान स्वघर्ममनुवर्तिनाम्‌। गायशधर्व॑ झुद्रजातीनां परित्तयनुवर्तिनाम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.597)
- **Original**: 35 अष्टाशीतिसहर्लाणि मुनीनामूध्वरितसाम्‌ । स्मृतं तेषां तु यत्स्थानं तदेव गुरुतवासिनाम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.598)
- **Original**: 36 सप्रर्षीणां तु यत््थान॑ स्मृ्ते तहै बनौकसाम्‌ । प्राजापत्यं गृहस्थानां न्यासिनां ब्रह्मसंज्ञितम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.599)
- **Original**: 37 योगिनामपृतं स्थार्न स्वात्यसन्तोषकारिणाम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.600)
- **Original**: 38 एकान्तिनः सदा ब्रह्मध्याविनो योगिनश्व ये । तेषों तु परम स्थान यत्तत्पए्यन्ति सूरय:
- **Translation**: 

---

