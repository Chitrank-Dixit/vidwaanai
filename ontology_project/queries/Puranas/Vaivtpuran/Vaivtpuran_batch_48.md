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

### Verse 1 (Vaivtpuran 4.9007)
- **Original**: बढ़ी-चढ़ी तथा श्रीराधिकाकी प्रिया हैं। सुरम्य बढ़ाते थे। उनका रूप बड़ा ही मनोहर था।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.9008)
- **Original**: भूषणोंसे भूषित हुई उन गोपसुन्दरियोंके अज्ञॉमें चन्दन, अगुरु, कस्तूरी और कुंकुमसे उनका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.9009)
- **Original**: नूतन यौबनका अंकुर प्रकट हुआ है। श्रृज्ञार हुआ था। वे अपने कपोलोंके योग्य। इस प्रकार वे तीनों द्वार स्वप्नकालिक कानोमें उत्तम रत्रमय कुण्डल धारण करके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.9010)
- **Original**: अनुभवके समान अद्भुत, अश्रुत, अदृष्टपूर्व, प्रकाशित हो रहे थे। श्रेष्ठ रल्नोंद्वारा रचित विचित्र
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.9011)
- **Original**: अतिरमणीय और विद्वानोंके द्वारा भी अवर्णनीय मुकुट उनके मस्तककी शोभा बढ़ा रहा था।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.9012)
- **Original**: थे।उन सबको देखकर और उन-उन गोपाड्ुनाओंसे प्रफुल्ल मालती-पुष्पकी मालाओंसे उनके सारे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.9013)
- **Original**: बातचीत करके आश्चर्यचकित हुए बे तीनों देवेश्वर अद्भ विभूषित थे। करोड़ों गोपोंसे घिरे होनेके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.9014)
- **Original**: सोलहवें मनोहर द्वारपर गये, जो श्रीराधिकाके कारण राजाधिराजसे भी अधिक उनकी शोभा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.9015)
- **Original**: अन्त:पुरका द्वार था। वह सब द्वारोंमें प्रधान तथा होती थी। उनकी अनुमति ले देवतालोग प्रसन्नतापूर्वक
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.9016)
- **Original**: केवल गोपाड्भनागणोंद्वारा ही रक्षणीय था। श्रीराधाको बारहवें द्वारपर गये, जहाँ बहुमूल्य रत्नोंकी बनी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.9017)
- **Original**: जो तैंतीस समवयस्का सखियाँ थीं, वे ही इस
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.9018)
- **Original**: 412 * संक्षिप्त ब्रह्मवैयर्तपुराण ही] #%#%%%%$%ऊ%#$%##%#######&##&####$#%ऊ$%ऊ$%%ऋ$%ऊऋ$ऋक##%#%###&# ########## कक कक कक कक द्वास्का संरक्षण करती थीं। उन सबकी वेश-
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.9019)
- **Original**: भक्तिके उद्रेकसे उनकी आँखें भर आयी थीं। भूषा अवर्णनीय थी। वे नाना प्रकारके सदगुणोंसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.9020)
- **Original**: उनके मुख और कंधे कुछ-कुछ झुक गये थे। युक्त, रूप-यौवनसे सम्पन्न तथा रत्रमय अलंकारोंसे अब देबताओंने श्रीराधिकाके उस श्रेष्ठ विभूषित थीं। रत्ननिर्मित कड्डूण, केयूर तथा नूपुर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.9021)
- **Original**: अन्तःपुरको अत्यन्त निकटसे देखा। समस्त मन्दिरोंके धारण किये हुए थीं। उनके कटिय्रदेश श्रेष्ठ रत्नोंकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.9022)
- **Original**: मध्यभागमें एक मनोहर चतु:शाला थी, जिसकी बनी हुई श्षुद्र घण्टिकाओंसे अलंकृत थे।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.9023)
- **Original**: रचना बहुमूल्य रत्नोंक सारभागसे की गयी थी। रत्निर्मित युगल कुण्डलोंसे उनके गण्डस्थलोंकी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.9024)
- **Original**: भाँति-भाँतिके हीरक-जटित मणिमय स्तम्भ उसकी बड़ी शोभा हो रही थी। प्रफुल्ल मालतीकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.9025)
- **Original**: शोभा बढ़ा रहे थे। पारिजात-पुष्पोंकी मालाओंकी मालाओंसे उनके वक्ष:स्थलका मध्यभाग उद्धासित
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.9026)
- **Original**: झालरोंसे उसे सजाया गया था। मोती, माणिक्य, हो रहा था। उनके मुख-चन्द्र शरत्पूर्णिमाके
- **Translation**: 

---

