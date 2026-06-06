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

### Verse 1 (Vishnu Puran 0.5221)
- **Original**: 24 पुत्रद्रव्यकलत्रेषु _ त्यक्तत्लेहो नराधिप । चतुर्थमाश्रमस्थानं. गच्छेब्रिर्शूतमत्सर:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5222)
- **Original**: 25 वि पु 7-- भओोजन- प्रबन्ध नहीं होता और जो जहाँ सायंकाल हो जाता है वहीं ठहर जाते हैं, उन सबका आधार और मूल गृहस्थाश्रम ही है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5223)
- **Original**: है राजन ! ऐसे व्येग जब घर आयें तो उगका कुशल-प्रश्न और मधुर बचनोंसे स्वागत करे तथा शब्या, आसन और भोजनके द्वारा उनका यथाशक्ति सत्कार करे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5224)
- **Original**: जिसके घरसे अतिथि निराज्ञा होकर ल्तैट जाता है उसे अपने समस्त दुष्कर्म देकर बह (अतिथि) उसके पुण्यकर्मोंको स्यं ले जाता है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5225)
- **Original**: गृहस्थके लिये अतिथिके प्रति अपमान, अहड्भार और दम्भका आचरण करना, उसे देकर प्छताना, उसपर प्रहार करना अथवा उससे कटुभाषण करना उचित नहीं है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5226)
- **Original**: इस प्रकार जो गृहस्थ अपने परम धर्मका पूर्णतया पान करता है वह समस्त बन्धनोंसे मुक्त होकर अत्युत्तम स्योेकोंकों प्राप्त कर लेता है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5227)
- **Original**: हे राजन्‌ ! इस प्रकार गृहस्थोचित कार्य करते-कररते जिसकी अवस्था दल गयी हो उस गृहस्थको उचित है कि स्नीको पुत्रोंके प्रति सॉपकर अथवा अपने साथ लेकर बनको चला जाय
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5228)
- **Original**: वहाँ पत्र, मूल, फल आदिका आहार करता हुआ, लोभ, इमश्रु (दाढ़ो-मुँछ) और जटाओंको घारण कर पृथिवीपर झायन करे और मुनिदृत्तिका अवल्म्बन कर सब प्रकार अतिथिकी सेवा करें
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5229)
- **Original**: उसे चर्म, काश और कुशाओंसे अपना बिछौना तथा ओकनेका यस््र बनाना चाहिये । हे नरेशध्वर ! उस मुनिके लिये ब्रिकाल-स्नानका विधान है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5230)
- **Original**: इसो प्रकार देखपूजन, होम, सब अतिथियोंका सत्कार, भिक्षा और बलिशैप्टेल भी उसके विहित कर्म हैं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5231)
- **Original**: हे राजेन्द्र
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5232)
- **Original**: ! वन्य तैल्ादिको झ्वरीरमें मछना और शीतोष्णका सहन करते हुए तपस्यामें लगे रहना उसके ग्रशस्त कर्म हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5233)
- **Original**: जो वानप्रस्थ मुनि इन नियत कर्मॉंका आचरण करता है वह अपने समस्त दोषोंक्त्रे अग्रिके समान मस्म कर देता है और नित्य-लोकोंको प्राप्त कर खेता है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5234)
- **Original**: है नुप ! पण्डितगण जिस चतुर्थ आश्रमको भिक्षु- आश्रम कहते हैं अब मैं उसके स्वरूपका यर्णन करता हूँ, सावधान होकर सुनो
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5235)
- **Original**: हे नरेन्द्र ! तृतीय आश्रमके अनन्तर पुत्र, द्रव्य और स््री आदिके स्त्रेहको सर्वथा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5236)
- **Original**: 188 श्रीयिष्णुपुराण [( आन 10 तैवर्गिकांस्यजेत्सर्वानारम्भानवनीपते.. । मित्रादिषपु समो मैत्रस्समस्तेश्लेव जन्तुषु
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5237)
- **Original**: 26 जरायुजाप्डजादीनां वाड्डनःकायकर्मभि: । युक्त: कुर्बीत न द्रोहं सर्वसड्भांश्र वर्जयेत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5238)
- **Original**: 27 एकरान्नस्थिति््रामे पञ्नरात्रस्थिति: पुरे । तथा तिष्लेद्यथाप्रीतिददेषों वा नास्य जायते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5239)
- **Original**: 28 प्राणयात्रानिमित्त चर व्यड्वारे भुक्ततजने
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5240)
- **Original**: काले प्रशस्तवर्णानां भिक्षार्थ पर्यटेद गृहान्‌
- **Translation**: 

---

