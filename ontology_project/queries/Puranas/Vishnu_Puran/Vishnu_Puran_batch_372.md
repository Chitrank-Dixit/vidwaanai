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

### Verse 1 (Vishnu Puran 0.7421)
- **Original**: रम्भस्त्वनपत्यो35भवत्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7422)
- **Original**: क्षत्रवृद्धसुतः प्रतिक्षत्रो5भवत्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7423)
- **Original**: तत्पुत्र: सझ्जयस्तस्पापि जयस्तस्यापि विजयस्तस्माश्च जज्ञे कृत:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7424)
- **Original**: तस्य च हर्यधनो हर्यथनसुतस्सहदेबस्तस्माददीनस्तस्य जयस्सेनस्ततश्न संस्कृतिस्तत्पुत्र: क्षत्रधर्मा इत्येते क्षत्रवृद्धश्य वंइया:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7425)
- **Original**: ततो नहुषवंशं प्रवक्ष्यामि
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7426)
- **Original**: बुद्धिकों मोहित करनेवाले उस अभिचार-कर्मसे अभिभूत हो जानेके कारण रजि-पुत्र ब्राह्मण-विरोधी, धर्म-त्यागी और तलेट-खिसुस्त हो गये
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7427)
- **Original**: तब धर्माचारहीन हो जानेसे इन्द्रने उन्हें मार डाला
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7428)
- **Original**: और पुरोहितजीके झरा तेजोबुद्ध होकर स्वर्गपर अपना अधिकार जमा लिया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7429)
- **Original**: इस प्रकार इन्द्रके अपने पदसे गिरकर उस्रपर फिर आरूद़ होनेके इस प्रसक्गषको सुननेसे पुरुष अपने पदसे पतित नहीं होता और उसमें कभी दुष्टता नहीं आती
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7430)
- **Original**: [ कयुबत्र दूसरा पुत्र ] रम्भ सच्तानहींन हुआ
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7431)
- **Original**: क्षत्रवृद्धका पुत्र प्रतिक्षत्र हुआ, प्रतिक्षञका सक्षम, सञयका जय, जयका विजय, विजयका कृत; कृतका हर्यघन, जयल्सेनका संस्कृति और संस्कृतिका पुत्र क्षत्रधर्मा हुआ। ये सब क्षत्रवृद्धेध वंशज हुए
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7432)
- **Original**: 25--27
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7433)
- **Original**: अब मैं नहुषबंशका वर्णन करूँगा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7434)
- **Original**: >0__>»ण जद 00000--- इति श्रीविष्णुपुराणे चतुर्थ नबमो5ध्यायः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7435)
- **Original**: चनम औ चप+ दसवाँ अध्याय अयातिका चरित्र ... औपयदर उवाच श्रीपराहरजी 5744030 46 यति, सयाति, यतिययातिसंयात्यायातिवियातिकृतिसंज्ञा.
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7436)
- **Original**: संयाति, आयाति, वियाति और कृति नामक छ: नहुषस्य षट पुत्रा महाबलपराक्रमा बभूबु:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7437)
- **Original**: यतिस्तु राज्य नैच्छत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7438)
- **Original**: ययातिस्तु भूभदभवत्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7439)
- **Original**: उदशनसश्र दुहितर देवयानीं वार्षपर्वर्णी च्॒शार्मिष्ठामुपग्रेमे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7440)
- **Original**: अत्रानुवंशइलोको भवति
- **Translation**: 

---

