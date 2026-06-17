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

### Verse 1 (Vaivtpuran 55.5325)
- **Original**: दक्षता प्राप्त की थी। मैंने पहले पुष्करतीर्थमें * 3 क्लीं श्रीं कृष्णप्रियाये नम:।' यह मन्त्र मेरे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 55.5326)
- **Original**: सूर्यग्रहणके अवसरपर सनत्कुमारकों इस कवचका कण्ठकी रक्षा करे। '3» रां रासेश्व्य नम:।' यह मन्र
- **Translation**: 

---

### Verse 3 (Vaivtpuran 55.5327)
- **Original**: उपदेश दिया था। सनत्कुमारने मेरुपर्वतपर मेरे कंधेकी रक्षा करें। '3:7 र रासविलासिन्यै स्वाहा।'
- **Translation**: 

---

### Verse 4 (Vaivtpuran 55.5328)
- **Original**: सान्दीपनिको यह कवच प्रदान किया। सान्दीपनिने यह मन्त्र मेरे पृष्ठभागकी सदा रक्षा करें। “47
- **Translation**: 

---

### Verse 5 (Vaivtpuran 55.5329)
- **Original**: बलरामजीको और बलरामजीने दुर्योधनको इसका यृून्दावनविलासिन्य स्वाहा।' यह मन्त्र वक्ष:स्थलकी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 55.5330)
- **Original**: उपदेश दिया। इस कबचके प्रसादसे मनुष्य सदा रक्षा करे। ' 34 तुलसीवनबासिन्यै स्वाहा।' यह
- **Translation**: 

---

### Verse 7 (Vaivtpuran 55.5331)
- **Original**: जीवन्मुक्त हो सकता है।* *3> राधेति चतुर्थ्यन्त॑ बढ्निजायान्तमेव च । कृष्णेनोपासितो मन्त्र: कल्पवृक्षः शिरो5बतु
- **Translation**: 

---

### Verse 8 (Vaivtpuran 55.5332)
- **Original**: 35 हाँ श्रीं राधिका डेउन्तं बह्िजायान्तमेव च । कपाल॑ नेत्रयुग्म॑ च॒श्रोत्रयुग्म॑ सदाबतु
- **Translation**: 

---

### Verse 9 (Vaivtpuran 55.19164)
- **Original**: 8क्ड » संक्षिम ख्रह्मवैलवर्तपुराण « 22.20 0000 00000 00000 00000 00050 000 0000 00000 00000 00000 000 00000] 2! .. श्रीसक्चास्तोत्राणि 5 सं: हर 2 !
- **Translation**: 

---

### Verse 10 (Vaivtpuran 55.19165)
- **Original**: श्रीराधाया: परीहारस्तोत्रम्‌ त्वं देवी जगतां माता विष्णुमाया सनातनी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 55.19166)
- **Original**: कृष्णप्राणाधिदेवी चर कृष्णप्राणाधिका शुभा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 55.19167)
- **Original**: कृष्णप्रेममयी शक्ति: कृष्णसौभाग्यरूपिणी । कृष्णभक्तिप्रदे राधे. नमस्ते. मड्ूलप्रदे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 55.19168)
- **Original**: अद्य में सफल॑ जन्म जीवन॑ सार्थक॑ मम । पूजितासि मया सा च॒ या श्रीकृष्णेन पूजिता
- **Translation**: 

---

### Verse 14 (Vaivtpuran 55.19169)
- **Original**: कृष्णवक्षस या राधा सर्व॑सौभाग्यसंयुता । रासे रासेश्वरीरूपा बृन्दा युन्दायने बने
- **Translation**: 

---

### Verse 15 (Vaivtpuran 55.19170)
- **Original**: कृष्णप्रिया च गोलोके तुलसी कानने तु या
- **Translation**: 

---

### Verse 16 (Vaivtpuran 55.19171)
- **Original**: चम्पावती कृष्णसंगे क्रीडा चम्पककानने
- **Translation**: 

---

### Verse 17 (Vaivtpuran 55.19172)
- **Original**: चतल्रावली चद्रधवने शतश्ृज्ञे सतीति च। विरजादर्पहन्त्री च विरजातटकानने
- **Translation**: 

---

### Verse 18 (Vaivtpuran 55.19173)
- **Original**: पदावती पदावने कृष्णा कृष्णसरोबरे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 55.19174)
- **Original**: भद्रा कुझ्कुटीरे च काम्या च काम्यके बने
- **Translation**: 

---

### Verse 20 (Vaivtpuran 55.19175)
- **Original**: बैकुण्ठे च महालक्ष्मीर्वाणी नाराबणोरसि ।
- **Translation**: 

---

