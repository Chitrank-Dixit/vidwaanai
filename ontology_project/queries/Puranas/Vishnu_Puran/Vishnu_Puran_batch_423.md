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

### Verse 1 (Vishnu Puran 0.8441)
- **Original**: बेदबादके विरुद्ध बचन बोलनेके कारण देवापिके पतित हो जानेसे, खड़े भाईके रहते हुए भी सम्पूर्ण धान्योंकी उत्पत्तिके लिये पर्जन्यदेव (मेघ) बरसने छगे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8442)
- **Original**: 24 बाह्लीकात्सोमदत्त:पुत्रो5भूत्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8443)
- **Original**: सोमदत्तस्थापि भूरिभूरिश्रवःहाल्यसंज्ञास्त्रय: पुत्रा बभूवु:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8444)
- **Original**: शान्तनोरप्यमरनद्मां जाह्नव्या- मुदारकीर्तिरशेषश्ञास्रार्थविद्धीष्पफ. पुत्रो3भूत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8445)
- **Original**: सत्यवत्यां च चित्राड्रदविचित्रवीयों डे पुत्रावुत्पादयामास झान्तनु:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8446)
- **Original**: चित्राड्रदस्तु बाल एब नचित्राडुदेनैव गन्धरवेणाहवे निहतः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8447)
- **Original**: विचित्रवीयोपि काशिराजतनये अम्बिकाम्बालिके उपयेमे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8448)
- **Original**: तदुपभोगाति खेदाध्य यक्ष्मणा गृहीतः स॒पश्ञत्वमगमत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8449)
- **Original**: सत्यवतीनियोगाश्च मत्पुत्र: कृष्ण- भुजिष्यायां विदुरं चोत्पादयामास
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8450)
- **Original**: धृतराष्ट्रोएपि गान्यार्याँ दुर्योधनदुशशासनप्रधान॑ पुत्रहतमुत्पादयामास
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8451)
- **Original**: मृगयायामृषिद्ञापोपहतप्रजाजननसामर्थ्यस्य धर्म- वाबुशक्रै्युधिष्ठिरभीमसेनार्जुना कुन्त्यां नकुलसहदेवों चाप्निभ्यां माद्रयां पञ्नपुत्रा- स्समुत्पादिता:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8452)
- **Original**: तेषां च॒ द्रौपद्यों पश्ैव पुत्रा बभूतु:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8453)
- **Original**: सुधिष्ठिराद्मतिविन्ध्य: नकुलाच्छुतकर्मा सहदेवात्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8454)
- **Original**: अन्ये च पाण्डवानामात्मजास्तद्यथा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8455)
- **Original**: यौधेयी युधिष्टिराहेबक॑ पुत्रमबाप
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8456)
- **Original**: हिडिम्बा घटोत्कचं भीमसेनात्पुत्रं छेमे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8457)
- **Original**: काशी च भीमसेनादेब सर्वगं सुतमवाप
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8458)
- **Original**: सहदेवाध बिजया सुहोत्र॑ पुत्रमवाप
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8459)
- **Original**: रेणुमत्यां च नकुलो5पि निरपित्रमजीजनत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8460)
- **Original**: अर्जुनस्पाप्युलृप्पंं नागकन्यायामिरावान्नाम पुत्रो5भवत्‌
- **Translation**: 

---

