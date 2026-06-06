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

### Verse 1 (Vaivtpuran 4.8867)
- **Original**: लगे हुए थे। उनके सारे अड्भ चन्दनसे चर्चित आश्रम हैं, जिनकी रचना उत्तम श्रेणीके रत्नोंद्वारा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8868)
- **Original**: थे और वे सभी रत्रमय आभूषणोंसे विभूषित हुई है। उनकी जो किंकरियाँ हैं, उनके लिये
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8869)
- **Original**: थे। देवेश्वरोने वहाँ उन सबके दर्शन किये। वे भी मणिरत्न आदिके द्वारा बड़े सुन्दर और मनोहर सभी श्रीहरिके श्रेष्ठ पार्षद थे। भवन बनाये गये हैं, जिनकी संख्या दस करोड़
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8870)
- **Original**: मुने! वहाँसे थोड़ी ही दूरपर उन्हें एक है। ये सभी दिव्य आश्रम और भवन वृन्दावनकी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8871)
- **Original**: मनोहर राजमार्ग दिखायी दिया, जिसके दोनों शोभाका विस्तार करते हैं। पार्श्वमें लाल मणियोंसे अद्भुत रचना की गयी थी। सैकड़ों जन्मोंकी तपस्याओंसे पवित्र हुए जो
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8872)
- **Original**: इन्द्रनील, पद्मराग, होरे और सुवर्णकी बनी हुई भक्तजन भारतवर्षकी भूमिपर श्रीहरिकी भक्तिमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8873)
- **Original**: वेदियाँ उस राजमार्गके उभय पार्श्रकों सुशोभित तत्पर रहते हैं, वे कर्मोके शान्त कर देनेवाले
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8874)
- **Original**: कर रही थीं। दोनों ओर रन्नमय विश्राम-मण्डप हैं--उनके कर्मबन्धन नष्ट हो जाते हैं। मुने! जो
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8875)
- **Original**: शोभा पाते थे। उस मार्गपर चन्दन, अगुरु, कस्तूरी सोते, जागते हर समय अपने मनको श्रीहरिके और कुंकुमके द्रवसे मिश्रित जलका छिड़काव ही ध्यानमें लगाये रहते हैं तथा दिन-रात
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8876)
- **Original**: किया गया था। पल्‍लब, लाजा, फल, पुष्प, दूर्वा *राधाकृष्ण', “श्रीकृष्ण” इत्यादि नामॉंका जप
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8877)
- **Original**: तथा सूक्ष्म सूत्रमें गुँथे हुए चन्दन-पल्लवोंकी किया करते हैं; उन श्रीकृष्ण-भक्तोंके लिये भी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8878)
- **Original**: बन्दनवारसे युक्त सहस््नों कदली-स्तम्भोंके समूह
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8879)
- **Original**: डण्8 + संक्षिप्त ब्रह्मवैवर्तपुराण « । ] )] घ ]])] ]घघ]घ]]7]])))))0]])
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8880)
- **Original**: । 3 8 8022802082242
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8881)
- **Original**: उस राजमार्गके तटप्रान्तकी शोभा बढ़ाते थे। उन,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8882)
- **Original**: हैं। बहुमूल्य र्नोंद्वारा निर्मित परकोटोंसे वह सबपर कुंकुम-केसर छिड़के गये थे। जगह-
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8883)
- **Original**: आश्रममण्डल घिरा हुआ है। उसमें सात दरवाजे जगह उत्तम रत्रोंके बने हुए मज़लघट स्थापित थे,
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8884)
- **Original**: हैं, जो सभी उत्तम रत्रोंकी बनी हुई वेदिकाओंसे उनमें फल और शाखाओंसहित पल्‍्लव शोभा पाते
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8885)
- **Original**: युक्त हैं। उन दरवाजोंमें विचित्र रत्न जड़े गये थे। सिन्दूर, कुंकुम, गन्‍्ध और चन्दनसे उनकी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8886)
- **Original**: हैं और नाना प्रकारके चित्र बने हैं। क्रमशः बने अर्चना की गयी थी। पुष्पमालाओंसे विभूषित हुए
- **Translation**: 

---

