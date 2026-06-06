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

### Verse 1 (Markende Puran 0.3441)
- **Original**: देवता बोले--
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3442)
- **Original**: सर्वेश्वारें! तुम इसी प्रकार तोनों लोकंक्री समस्त चाधाओऔँकों शान्त करों और हमारे शत्रुओंका दाश करती रहों
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3443)
- **Original**: वेब्युवाच
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3444)
- **Original**: / चैवस्वते5न्तरे प्रामें अष्टाविशतिमे युगे। शुम्भों निशुम्भञ्षैवान्यावुत्पत्स्थेते महासुरी
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3445)
- **Original**: नन्दमोपगृहे” जाता यशोदागर्भसम्भया। ततस्ती नाशविष्यामि विन्य्याचलनियासिनी
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3446)
- **Original**: पुनरप्यतिरौद्रेण.. रूपेण. पृधिवीतले। अवत्तीर्य इनिष्यापि बैप्रचित्तांस्तु दानबान्‌ 4 43
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3447)
- **Original**: भक्षयन्ताश्ष तानुग्रात्‌ बैप्रचित्तान्सहासुरानू। रक्ता दन्ता भविष्यन्ति दाडिमीकुसुमोषमा:
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3448)
- **Original**: जतो मां देवता: स्वर्ग मत्पंलोके चर मानवा:। स्तुलन्तो व्याइरिध्यन्ति सतत॑ रक्तदन्तिकाम
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3449)
- **Original**: भूयंश्ष॒ शत्तार्थिक्यामनावृष्टसामनम्भंसि। मुनिभि: रूंस्तुता भूमौ संभविष्याप्ययोनिजा
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3450)
- **Original**: त्तः शत्तेन नेत्राप्यां निरीक्षिष्यामि यन्मुनीन्‌
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3451)
- **Original**: 'कॉलेबिष्वन्ति मनुजा: शताक्षीमिति भो तत:
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3452)
- **Original**: 477 उत्तोडहपखिलं_ लोकपात्मदेहसमुझ्धव:। भरिष्यामि सुरा: शाकैशबूष्टें: प्राणधारकै:
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3453)
- **Original**: शाकम्भसीति विख्यातिं तदा यास्थाम्यह भुवि। तप्रैस अर स्रथिप्यामि दुर्गभाझ्यं महासुरम्‌
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3454)
- **Original**: दुर्गा देवीति विख्यातं तन्मे नाम भविष्वति। पुनश्चाहे बदा भीम॑ रूप॑ कृत्वा हिमाचले
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3455)
- **Original**: रक्षांसि भक्षयिष्यामि'* मु्रीनां त्राणकारणात्‌। कद माँ मुनवः सर्वे स्तोप्यन्त्यानप्रमूर्तय:
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3456)
- **Original**: भीमा देवीति विख्यात॑ तन्मै नाम 'भव्रिष्यति। यदारुणाख्यस्तैलोक्ये मड़ायाथ्रां करिष्यति
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3457)
- **Original**: 52 फ् , तराहँ भ्रामं रूप कृत्वाउसंख्येघपट्ंपटय। जैलोक्यस्य हितार्धाय वशिष्याभि महासुर्म। घ 3 ध आमरीति त्ञ मां लोकास्तदा स्तोष्यन्ति सर्वतः
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3458)
- **Original**: इत्थं चंदा यदा बाधा दानवोत्था भविष्यति
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3459)
- **Original**: तदा तदावतीर्थाहे करिष्याम्यथरिंसक्षचम्‌
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3460)
- **Original**: देवी बॉली--
- **Translation**: 

---

